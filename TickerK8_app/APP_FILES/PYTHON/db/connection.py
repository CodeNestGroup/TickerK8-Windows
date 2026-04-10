# --- Import packages ---
import sqlite3
import pymysql
import json
import requests
import pathlib
from cryptography.fernet import Fernet

class database():
    def __init__(self):
        super().__init__()
        self.user_dict = {}
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        self.conn = self.Connect_offline_database()

# --- Offline database ---
    def Connect_offline_database(self):
        c = sqlite3.connect(
            database=self.main_path+'/CONFIG/GLOBAL/tickerk8_offline.db'
        )
        return c

    def GetCountries(self):
        r = self.conn.execute('SELECT name FROM country;')
        return [x[0] for x in r.fetchall()]

    def GetPhonePrefix(self):
        r = self.conn.execute('SELECT prefix FROM phone_prefix;')
        return [x[0] for x in r.fetchall()]
    
# --- Online database ---
    def ConnectData(self) -> dict:
        try:
            conf = json.load(open(f'{self.main_path}/PYTHON/db/conf.json', 'r', encoding='utf-8'))
            payload = {
                "token":conf['token'],
                "name":'u_app'
            }
            response = requests.post(conf['url'], json=payload)
            response.raise_for_status()
            cipher = Fernet(conf['key'].encode())
            return json.loads(cipher.decrypt(response.text.encode()))
        except:
            pass

# --- Connection --- 
    def Connection(self):
        try:
            login_data = self.user_dict['u_app']
        except:
            self.user_dict['u_app'] = self.ConnectData()
            login_data = self.user_dict['u_app']
        conn = pymysql.connect(
            host=login_data['host'],
            user=login_data['username'],
            password=login_data['password'],
            database=login_data['database'],
            port=login_data['port'],
            ssl={'ca':f'{self.main_path}/PYTHON/db/rds-combined-ca-bundle.pem'}
        )
        return conn

    def LoginByName(self, u_name:str):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL login_by_name(%s);', (u_name,))
            result = curs.fetchone()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None
    
    def GetUserConfig(self, i):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL get_user_config(%s);', (i))
            result = curs.fetchone()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

    def GetUserData(self, i):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL get_user_data(%s);', (i))
            result = curs.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

    def UpdateLastLogin(self, u_id:str):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL update_last_login(%s);', (u_id))
            result = curs.fetchone()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

    def RegisterUser(self, u_data:tuple):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute("SET @p_errors = NULL;")
            curs.execute(
                "CALL register_user(%s, %s, %s, %s, %s, %s, @p_errors);",
                u_data
            )
            curs.execute("SELECT @p_errors;")
            errors_json = curs.fetchone()[0]
            if errors_json:
                errors = json.loads(errors_json)
                conn.rollback()
                return errors
            conn.commit()
            return None

        except pymysql.err.OperationalError as e:
            if conn:
                conn.rollback()
                raise 
        except Exception as e:
            if conn:
                conn.rollback()
                raise
        finally:
            if curs:
                curs.close()
                curs = None
            if conn:
                conn.close()
                conn = None

    def LoginConfiguration(self, i:str):
        c = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r', encoding='utf-8'))
        t = json.load(open(self.main_path+'/PYTHON/login_config/j_list_translate.json', 'r', encoding='utf-8'))
        l = c['language'] 
        n = t[l]

        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute(
                "CALL user_config_configuration(%s, %s, %s, %s, %s, %s, %s);",
                    (
                    i,
                    json.dumps(c),
                    n[0],
                    n[1],
                    n[2],
                    n[3],
                    c['subscription']
                    )
                )
            conn.commit()
            return None
        except pymysql.err.OperationalError as e:
            if conn:
                conn.rollback()
                raise 
        except Exception as e:
            if conn:
                conn.rollback()
                raise
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

#   --- Get data ---
    def GetNewsList(self, t, i, l):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL get_news_list(%s, %s, %s);', (t, json.dumps(i), l))
            result = curs.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None
    
    def GetNewsById(self, i, l):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL get_news_by_id(%s, %s);', (i, l))
            result = curs.fetchall()
            return result
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None
    
    def UpdateNewsPopularity(self, i):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL update_news_popularity(%s);', (i,))
            conn.commit()
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

    def AddObjectToList(self, N):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL add_object_to_list(%s, %s, %s, %s, %s, %s);', (N['UserId'], N['TableName'], N['SectionName'], N['NewObjectPlace'], N['NewObjectType'], N['NewObjectId']))
            conn.commit()
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None
    def DeleteObjectFromList(self, D):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL delete_object_from_list(%s, %s, %s, %s);', (D['UserId'], D['listname'], D['sectionname'], D['objectplace']))
            conn.commit()
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None

    def SaveSettings(self, i, t, l):
        conn = self.Connection()
        curs = conn.cursor()
        try:
            curs.execute('CALL save_settings(%s, %s, %s);', (i, t, l))
            conn.commit()
        finally:
            curs.close()
            curs = None
            conn.close()
            conn = None