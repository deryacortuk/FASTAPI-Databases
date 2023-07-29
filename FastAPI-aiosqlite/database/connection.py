import aiosqlite


async def init_db():
    conn = await aiosqlite.connect("data.sqlite3")
    cur = await conn.cursor()
    qry = "SELECT count(name) FROM sqlite_master WHERE type='table' and name='Books'"
    await cur.execute(qry)
    result = await cur.fetchone()  
    if result[0] == 0:  
        qry = "CREATE TABLE IF NOT EXISTS Books( id INTEGER(10) PRIMARY KEY, \
            title STRING(50), author STRING(20), price INTEGER(10), publisher STRING(20))"
        await cur.execute(qry)
    await conn.close()
async def get_cursor():
    conn = await aiosqlite.connect("data.sqlite3")
    conn.row_factory = aiosqlite.Row
    cursor = await conn.cursor()
    yield(conn, cursor)
    