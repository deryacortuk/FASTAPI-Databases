import sqlite3



def init_db():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    qry = "SELECT count(name) FROM sqlite_master WHERE type='table' and name='Books'"
    cur.execute(qry)
    if cur.fetchone()[0]==0:
        qry = "CREATE TABLE IF NOT EXISTS Books( id INTEGER(10) PRIMARY KEY, \
            title STRING(50), author STRING(20), price INTEGER(10), publisher STRING(20))"
        cur.execute(qry)
    conn.close()
    
def get_cursor():
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    yield (conn, cur)
    
    
