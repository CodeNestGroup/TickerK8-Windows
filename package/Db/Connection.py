# --- Import ---
import sqlite3
import pymysql
import json
import requests
from cryptography.fernet import Fernet


#   --- Class Databse ---

class Database():
    def __init__(self, parent):
        super().__init__()
#           --- Get data from parent [ core ] ---
        self.Path = parent.Path
        self.LoggedUserId = parent.LoggedUserId
#           --- Set Class varaibles ---
        self.UserDict = {}
        self.Conn = self.ConnectOfflineDatabase()

#       --- Offline database ---
    def ConnectOfflineDatabase(self):
        c = sqlite3.connect(
            database=self.Path+'/assets/DB/Tickerk8Offline.db'
        )
        return c

    def GetCountries(self):
        r = self.Conn.execute('SELECT name FROM country;')
        return [x[0] for x in r.fetchall()]

    def GetPhonePrefix(self):
        r = self.Conn.execute('SELECT prefix FROM phone_prefix;')
        return [x[0] for x in r.fetchall()]
    
# --- Online database ---
    def ConnectData(self) -> dict:
        try:
            Conf = json.load(open(f'{self.Path}/assets/JSON/DatabaseOnlineConf.json', 'r', encoding='utf-8'))
            Payload = {
                "token":Conf['token'],
                "name":'u_app'
            }
            Response = requests.post(Conf['url'], json=Payload)
            Response.raise_for_status()
            Cipher = Fernet(Conf['key'].encode())
            return json.loads(Cipher.decrypt(Response.text.encode()))
        except:
            pass

# --- Connection --- 
    def Connection(self):
        try:
            LoginData = self.UserDict['u_app']
        except:
            self.UserDict['u_app'] = self.ConnectData()
            LoginData = self.UserDict['u_app']
        Conn = pymysql.connect(
            host=LoginData['host'],
            user=LoginData['username'],
            password=LoginData['password'],
            database=LoginData['database'],
            port=LoginData['port'],
            ssl={'ca':f'{self.Path}/assets/SSL/rds-combined-ca-bundle.pem'}
        )
        return Conn

    def LoginByName(self, UserName:str):
        Conn = self.Connection()
        Curs = Conn.cursor()
        try:
            Curs.execute('CALL login_by_name(%s);', (UserName,))
            Result = Curs.fetchone()
            return Result
        finally:
            Curs.close()
            Curs = None
            Conn.close()
            Conn = None
    
    def GetUserConfig(self, UserId):
        Conn = self.Connection()
        Curs = Conn.cursor()
        try:
            Curs.execute('CALL get_user_config(%s);', (UserId,))
            Result = Curs.fetchone()
            return Result
        finally:
            Curs.close()
            Curs = None
            Conn.close()
            Conn = None

    def GetUserData(self, UserId):
        Conn = self.Connection()
        Curs = Conn.cursor()
        try:
            Curs.execute('CALL get_user_data(%s);', (UserId))
            Result = Curs.fetchall()
            return Result
        finally:
            Curs.close()
            Curs = None
            Conn.close()
            Conn = None

    def UpdateLastLogin(self, UserId:str):
        Conn = self.Connection()
        Curs = Conn.cursor()
        try:
            Curs.execute('CALL update_last_login(%s);', (UserId))
            Result = Curs.fetchone()
            return Result
        finally:
            Curs.close()
            Curs = None
            Conn.close()
            Conn = None

    def RegisterUser(self, UserData:tuple):
        Conn = self.Connection()
        Curs = Conn.cursor()
        try:
            Curs.execute("SET @p_errors = NULL;")
            Curs.execute(
                "CALL register_user(%s, %s, %s, %s, %s, %s, @p_errors);",
                UserData
            )
            Curs.execute("SELECT @p_errors;")
            ErrorsJson = Curs.fetchone()[0]
            if ErrorsJson:
                Errors = json.loads(ErrorsJson)
                Conn.rollback()
                return Errors
            Conn.commit()
            return None

        except pymysql.err.OperationalError as e:
            if Conn:
                Conn.rollback()
                raise 
        except Exception as e:
            if Conn:
                Conn.rollback()
                raise
        finally:
            if Curs:
                Curs.close()
                Curs = None
            if Conn:
                Conn.close()
                Conn = None

    def LoginConfiguration(self):
        c = json.load(open(self.Path+'/assets/JSON/LoginConfigurationConfig.json', 'r', encoding='utf-8'))
        t = json.load(open(self.Path+'/assets/JSON/LoginConfigurationListConfTranslate.json', 'r', encoding='utf-8'))
        l = c['language'] 
        n = t[l]
        Conn = self.Connection()
        Curs = Conn.cursor()
        try:
            Curs.execute(
                "CALL user_config_configuration(%s, %s, %s, %s, %s, %s, %s);",
                    (
                    self.LoggedUserId,
                    json.dumps(c),
                    n[0],
                    n[1],
                    n[2],
                    n[3],
                    c['subscription']
                    )
                )
            Conn.commit()
            return None
        except pymysql.err.OperationalError as e:
            if Conn:
                Conn.rollback()
                raise 
        except Exception as e:
            if Conn:
                Conn.rollback()
                raise
        finally:
            Curs.close()
            Curs = None
            Conn.close()
            Conn = None

#   --- Get data ---
    def GetNewsList(self, t, i, l):
        Conn = self.Connection()
        Curs = Conn.cursor()
        try:
            Curs.execute('CALL get_news_list(%s, %s, %s);', (t, json.dumps(i), l))
            Result = Curs.fetchall()
            return Result
        finally:
            Curs.close()
            Curs = None
            Conn.close()
            Conn = None
    
    def GetNewsById(self, NewsId, Language):
        Conn = self.Connection()
        Curs = Conn.cursor()
        try:
            Curs.execute('CALL get_news_by_id(%s, %s);', (NewsId, Language))
            Result = Curs.fetchall()
            return Result
        finally:
            Curs.close()
            Curs = None
            Conn.close()
            Conn = None
    
    def UpdateNewsPopularity(self, NewsId):
        Conn = self.Connection()
        Curs = Conn.cursor()
        try:
            Curs.execute('CALL update_news_popularity(%s);', (NewsId,))
            Conn.commit()
        finally:
            Curs.close()
            Curs = None
            Conn.close()
            Conn = None

    def AddObjectToList(self, N):
        Conn = self.Connection()
        Curs = Conn.cursor()
        try:
            Curs.execute('CALL add_object_to_list(%s, %s, %s, %s, %s, %s);', (N['UserId'], N['TableName'], N['SectionName'], N['NewObjectPlace'], N['NewObjectType'], N['NewObjectId']))
            Conn.commit()
        finally:
            Curs.close()
            Curs = None
            Conn.close()
            Conn = None

    def DeleteObjectFromList(self, D):
        Conn = self.Connection()
        Curs = Conn.cursor()
        try:
            Curs.execute('CALL delete_object_from_list(%s, %s, %s, %s);', (D['UserId'], D['listname'], D['sectionname'], D['objectplace']))
            Conn.commit()
        finally:
            Curs.close()
            Curs = None
            Conn.close()
            Conn = None

    def SaveSettings(self, i, t, l):
        Conn = self.Connection()
        Curs = Conn.cursor()
        try:
            Curs.execute('CALL save_settings(%s, %s, %s);', (i, t, l))
            Conn.commit()
        finally:
            Curs.close()
            Curs = None
            Conn.close()
            Conn = None
