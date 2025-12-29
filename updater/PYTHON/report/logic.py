""" Import packages """
import mysql.connector
import datetime
#______________________________________________________________________________________________________________________

""" send report """
def send_report(self):
    m = self.textfield_textarea.toPlainText()
    connect = mysql.connector.connect( 
                    host='localhost', 
                    user='launcherclient', 
                    password='qwerty', 
                    database='TickerK8' 
                    )
    cursor = connect.cursor()
    cursor.execute(f'INSERT INTO report (date, message) VALUES ("{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}", "{m}");')
    connect.commit()
    connect.close()
    self.textfield_textarea.setText('')
#______________________________________________________________________________________________________________________
