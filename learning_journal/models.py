from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    DateTime,
    )

import sqlalchemy as sa

from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )


from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable = True)
    created = Column(DateTime, default=datetime.utcnow())
    edited = Column(DateTime, default=datetime.utcnow())

    @classmethod
    def all(cls, session=None):
        if session is None:
            session = DBSession
        return session.query(cls).order_by(sa.desc(cls.created)).all()

    @classmethod
    def by_id(cls, id, session=None):
        if session is None:
            session = DBSession
        return DBSession.query(cls).filter(cls.id==id).first()
 
       
Index('entries_index', Entry.title, unique=True, mysql_length=255)
