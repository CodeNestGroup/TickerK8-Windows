#   --- Import ---\
import sqlite3

def Setup(self, Table, ItemId):
    conn = sqlite3.connect(f'{self.Path}/assets/DB/Tickerk8Offline.db')
    cur = conn.cursor()
    cur.execute(f'SELECT icon, ticker, name FROM "{Table}" WHERE id=?;', (int(ItemId),))
    r = cur.fetchone()
    conn.close()
    
    #self.IconL.setPixmap(QPixmap(r[0]))
    self.TickerL.setText(r[1])
    self.InfoNameValueL.setText(r[2])
    self.InfoTickerValueL.setText(r[1])