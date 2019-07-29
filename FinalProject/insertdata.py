
import sqlalchemy

from sqlalchemy import create_engine, func,inspect
import pandas as pd
from sqlalchemy import Column,INTEGER,String, DATE,DATETIME,FLOAT,TEXT
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# Base.metadata.create_all(mysql_engine)    
from datetime import date,datetime
from database_connection import create_session


class logininfo(Base):
    __tablename__ = 'logininfo'
    ID = Column(INTEGER, primary_key=True)
    SRC_SYS = Column(String)
    SUB_SYS = Column(String)
    SERVER_ID = Column(String)
    API_NAME = Column(String)
    METHOD_NAME = Column(String)
    MOBILE_NUMBER = Column(INTEGER)
    WIRELESS_BAN= Column(INTEGER)
    WIRELINE_BAN = Column(String)
    UVERSE_BAN = Column(INTEGER)
    DTV_BAN = Column(INTEGER)
    LOGINID = Column(String)
    TRX_DATE = Column(DATE)
    TRX_HOUR = Column(INTEGER)
    TRX_DATETIME = Column(DATETIME)
    SESSION_ID = Column(String)
    FAILED = Column(String)
    RESPONSE_TIME = Column(INTEGER)
    AGENT_ID = Column(String)

class paymentinfo(Base):
    __tablename__ = 'paymentinfo'
    ID = Column(INTEGER, primary_key=True)
    SRC_SYS = Column(String)
    SUB_SYS = Column(String)
    SERVER_ID = Column(String)
    API_NAME = Column(String)
    METHOD_NAME = Column(String)
    MOBILE_NUMBER = Column(INTEGER)
    WIRELESS_BAN= Column(INTEGER)
    WIRELINE_BAN = Column(String)
    UVERSE_BAN = Column(INTEGER)
    DTV_BAN = Column(INTEGER)
    LOGINID = Column(String)
    TRX_DATE = Column(DATE)
    TRX_HOUR = Column(INTEGER)
    TRX_DATETIME = Column(DATETIME)
    SESSION_ID = Column(String)
    FAILED = Column(String)
    RESPONSE_TIME = Column(INTEGER)
    AGENT_ID = Column(String)

class agentinfo(Base):
    __tablename__ = 'agentinfo'
    ID = Column(INTEGER, primary_key=True)
    SRC_SYS = Column(String)
    SUB_SYS = Column(String)
    SERVER_ID = Column(String)
    API_NAME = Column(String)
    METHOD_NAME = Column(String)
    MOBILE_NUMBER = Column(INTEGER)
    WIRELESS_BAN= Column(INTEGER)
    WIRELINE_BAN = Column(String)
    UVERSE_BAN = Column(INTEGER)
    DTV_BAN = Column(INTEGER)
    LOGINID = Column(String)
    TRX_DATE = Column(DATE)
    TRX_HOUR = Column(INTEGER)
    TRX_DATETIME = Column(DATETIME)
    SESSION_ID = Column(String)
    FAILED = Column(String)
    RESPONSE_TIME = Column(INTEGER)
    AGENT_ID = Column(String)


def create_clean_df(path):
    print("creating Dataframe...")
    df = pd.read_csv(path,low_memory=False)
    print("Cleaning Dataframe...")
    mod_df = df.drop(columns=['THREAD_ID','INTERNAL_ID','CHILD_SEQ_NUM','UD_ID','UVERSE_MEM_ID','BACKEND_TX_TIME','ERR_SRC','ERR_CODE','ERR_DESC','EXTRA_INFO1','EXTRA_INFO2','EXTRA_INFO3','SL_SVR_ID','GUID','FTN','WTN','WIRELINE_MEM_ID','WIRELINE_BILLING_ID','ORDER_NUMBER','DTVNOW_BAN','HTTP_SESSIONID','BACKEND_REF_ID'])
    mod_df = mod_df.drop_duplicates(subset='SESSION_CODE', keep='first')
    mod_df["MOBILE_NUMBER"].fillna(0, inplace = True) 
    mod_df["WIRELESS_BAN"].fillna("NULL", inplace = True) 
    mod_df["UVERSE_BAN"].fillna(0, inplace = True) 
    mod_df["CSR_ID"].fillna("NULL", inplace = True) 
    mod_df["SLID"].fillna("NULL", inplace = True) 
    mod_df["BTN"].fillna(0, inplace = True) 
    mod_df["DTV_BAN"].fillna(0, inplace = True)
    mod_df["TX_TIME"].fillna(0, inplace = True)
    print(mod_df.info())
    mod_df['TRX_HOUR'] = ""
    mod_df['TRX_DATE'] = ""    
    return mod_df

def remove_duplicates(df):
    df= df.drop_duplicates(subset='SESSION_CODE', keep='first')
    return df 



def time_microsec(timeformat):
    hr, m,s,n = timeformat.split('.')
    a=n.split(" ")
    b=int(a[0])/1000
    return hr+"."+m+"."+s+"."+str(int(b))+" "+a[1]


def insert_login_records(filepath):
    
    session = create_session()
    mod_df=create_clean_df(filepath)
    for index, row in mod_df.iterrows():
            print(index)
        # get restaurant type from df
            SRC_SYS = row['SRC_SYS']
            SUB_SYS = row['SUB_SYS']
            SERVER_ID = row['SERVER_ID']
            NAME = row['NAME']
            PARENT_NAME = row['PARENT_NAME']
            MOBILE_NUMBER = row['MOBILE_NUMBER']
            WIRELESS_BAN = row['WIRELESS_BAN']
            UVERSE_BAN = row['UVERSE_BAN']
            CSR_ID = row['CSR_ID']
            START_TIME = datetime.strptime(time_microsec(row['START_TIME']), "%d-%b-%y %H.%M.%S.%f %p")
            TX_TIME = row['TX_TIME']
            FAILED = row['FAILED']
            SESSION_CODE = row['SESSION_CODE']
            SLID = row['SLID']
            BTN = row['BTN']
            DTV_BAN = row['DTV_BAN']
            AGENT_ID=row['CSR_ID']
            DATE = START_TIME.date()
            HOUR =START_TIME.time().strftime('%H')
            mod_df.loc[index, 'TRX_HOUR'] = HOUR
            mod_df.loc[index, 'TRX_DATE'] = DATE



            login_info =logininfo(SRC_SYS=SRC_SYS,SUB_SYS=SUB_SYS,SERVER_ID=SERVER_ID,API_NAME=NAME,METHOD_NAME=PARENT_NAME,MOBILE_NUMBER=MOBILE_NUMBER,WIRELESS_BAN=WIRELESS_BAN,WIRELINE_BAN=BTN,UVERSE_BAN=UVERSE_BAN,DTV_BAN=DTV_BAN,LOGINID=SLID,TRX_DATE=DATE,TRX_HOUR=HOUR,TRX_DATETIME=START_TIME,SESSION_ID=SESSION_CODE,FAILED=FAILED,RESPONSE_TIME=TX_TIME,AGENT_ID=AGENT_ID)
            session.add(login_info)

    session.commit()


def insert_payment_records(filepath):
    
    session = create_session()
    mod_df=create_clean_df(filepath)
    for index, row in mod_df.iterrows():
            print(index)
        # get restaurant type from df
            SRC_SYS = row['SRC_SYS']
            SUB_SYS = row['SUB_SYS']
            SERVER_ID = row['SERVER_ID']
            NAME = row['NAME']
            PARENT_NAME = row['PARENT_NAME']
            MOBILE_NUMBER = row['MOBILE_NUMBER']
            WIRELESS_BAN = row['WIRELESS_BAN']
            UVERSE_BAN = row['UVERSE_BAN']
            CSR_ID = row['CSR_ID']
            START_TIME = datetime.strptime(time_microsec(row['START_TIME']), "%d-%b-%y %H.%M.%S.%f %p")
            TX_TIME = row['TX_TIME']
            FAILED = row['FAILED']
            SESSION_CODE = row['SESSION_CODE']
            SLID = row['SLID']
            BTN = row['BTN']
            DTV_BAN = row['DTV_BAN']
            AGENT_ID=row['CSR_ID']
            DATE = START_TIME.date()
            HOUR =START_TIME.time().strftime('%H')
            mod_df.loc[index, 'TRX_HOUR'] = HOUR
            mod_df.loc[index, 'TRX_DATE'] = DATE
            payment_info =paymentinfo(SRC_SYS=SRC_SYS,SUB_SYS=SUB_SYS,SERVER_ID=SERVER_ID,API_NAME=NAME,METHOD_NAME=PARENT_NAME,MOBILE_NUMBER=MOBILE_NUMBER,WIRELESS_BAN=WIRELESS_BAN,WIRELINE_BAN=BTN,UVERSE_BAN=UVERSE_BAN,DTV_BAN=DTV_BAN,LOGINID=SLID,TRX_DATE=DATE,TRX_HOUR=HOUR,TRX_DATETIME=START_TIME,SESSION_ID=SESSION_CODE,FAILED=FAILED,RESPONSE_TIME=TX_TIME,AGENT_ID=AGENT_ID)
            session.add(payment_info)

    session.commit()
    

def insert_agent_records(filepath):
    
    session = create_session()
    mod_df=create_clean_df(filepath)
    for index, row in mod_df.iterrows():
            print(index)
        # get restaurant type from df
            SRC_SYS = row['SRC_SYS']
            SUB_SYS = row['SUB_SYS']
            SERVER_ID = row['SERVER_ID']
            NAME = row['NAME']
            PARENT_NAME = row['PARENT_NAME']
            MOBILE_NUMBER = row['MOBILE_NUMBER']
            WIRELESS_BAN = row['WIRELESS_BAN']
            UVERSE_BAN = row['UVERSE_BAN']
            CSR_ID = row['CSR_ID']
            START_TIME = datetime.strptime(time_microsec(row['START_TIME']), "%d-%b-%y %H.%M.%S.%f %p")
            TX_TIME = row['TX_TIME']
            FAILED = row['FAILED']
            SESSION_CODE = row['SESSION_CODE']
            SLID = row['SLID']
            BTN = row['BTN']
            DTV_BAN = row['DTV_BAN']
            AGENT_ID=row['CSR_ID']
            DATE = START_TIME.date()
            HOUR =START_TIME.time().strftime('%H')
            mod_df.loc[index, 'TRX_HOUR'] = HOUR
            mod_df.loc[index, 'TRX_DATE'] = DATE
            agent_info =agentinfo(SRC_SYS=SRC_SYS,SUB_SYS=SUB_SYS,SERVER_ID=SERVER_ID,API_NAME=NAME,METHOD_NAME=PARENT_NAME,MOBILE_NUMBER=MOBILE_NUMBER,WIRELESS_BAN=WIRELESS_BAN,WIRELINE_BAN=BTN,UVERSE_BAN=UVERSE_BAN,DTV_BAN=DTV_BAN,LOGINID=SLID,TRX_DATE=DATE,TRX_HOUR=HOUR,TRX_DATETIME=START_TIME,SESSION_ID=SESSION_CODE,FAILED=FAILED,RESPONSE_TIME=TX_TIME,AGENT_ID=AGENT_ID)
            session.add(agent_info)

    session.commit()

insert_payment_records("C:\coding\LearnPython\FinalProject\export_make_payment_0718_ATL.csv")