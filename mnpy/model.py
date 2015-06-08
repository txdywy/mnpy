from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME, Text, ForeignKey
import datetime

engine = create_engine('sqlite:///mnpy.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def flush(db_obj=None):
    if db_obj:
        db_session.add(db_obj)
    db_session.commit()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    #import yourapplication.models
    Base.metadata.create_all(bind=engine)

class ManongPython(Base):
    __tablename__ = 'manong_python'
    id = Column(Integer, primary_key=True)
    index = Column(Integer)
    title = Column(String(512))
    url = Column(String(512))
    create_time = Column(DATETIME(), default=datetime.datetime.now())
    update_time = Column(DATETIME(), default=datetime.datetime.now())

    def __repr__(self):
        return '<ManongPython %r>' % (self.id)

