import databases
import sqlalchemy

DATABASE_URL ="sqlite:///./book.sqlite3"



engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread":False})

metadata = sqlalchemy.MetaData()

booklist = sqlalchemy.Table(
    "BookList",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column("title",sqlalchemy.String),
    sqlalchemy.Column("author", sqlalchemy.String),
    sqlalchemy.Column("price",sqlalchemy.Integer)
)

metadata.create_all(engine)

async def get_db():
    db = databases.Database(DATABASE_URL)
    await db.connect()
    yield db


