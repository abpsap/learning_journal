# Run this within the virtualenv, after activating the virtualenv
# This script runs sql queries on the 'Entry' table

from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from learning_journal.models import Entry

config = 'development.ini'
settings = get_appsettings(config)
engine = engine_from_config(settings, 'sqlalchemy.')
Session = sessionmaker(bind=engine)
session = Session()
#session.query(Entry).all()

""" This method creates rows in the Entry table """
def createNewEntryRows():
    entryObjList = []
    for subject, desc in [('A Beautiful Mind', 'Russell Crowe plays the scientist'), ('Dead Poets society', 'Robin Williams did a class act, went above and beyond his duties'), ('The Theory of Everything', 'grand quest of Albert Einstein')]:
        entryObjList.append(Entry(title=subject, body=desc))
    
    session.add_all(entryObjList)
    session.new
    session.commit()

""" This method uses session query method to query the Entry Table """
def sessionQueryTableById(id_val):
    print "Querying rows by ID [" + str(id_val) + "]"
    print "********"
    for obj in session.query(Entry).filter(Entry.id == id_val):
        print "Title Column [" + obj.title + "]", " body Column [" + obj.body + "]"
    print "********"

""" This method uses session query method to query the Entry Table """
def sessionQueryTableAndOrder():
    print "Querying all rows  and order by"
    print "********"
    for obj in session.query(Entry).order_by(Entry.created):
        print "Tite Column [" + obj.title +"]", "body Column [" + obj.body + "]"
    print "********"

""" This method uses the Table object directly to query the Entry Table """
def queryTable():
    tableObj = Entry()
    print tableObj.__tablename__
    session.query(tableObj).by_id(1)



#createNewEntryRows()
sessionQueryTableById(2)
sessionQueryTableById(3)
sessionQueryTableAndOrder()
queryTable()




