
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# Base.metadata.create_all(mysql_engine)    
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

def createEngine():
    print("creating Engine...")
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/myinfo?charset=utf8")
    return engine

def create_session():
    print("creating session...")
    mysql_engine = createEngine()
    session = Session(bind=mysql_engine)
    return session 

def create_db_classes():
    Base1=automap_base()
    Base1.prepare(createEngine(),reflect=True)
    login_data=Base1.classes.logininfo
    payment_data=Base1.classes.paymentinfo
    agent_data=Base1.classes.agentinfo
    return [login_data,payment_data,agent_data]