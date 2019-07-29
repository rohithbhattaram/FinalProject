import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy
from database_connection import create_session,create_db_classes,createEngine

from sqlalchemy import create_engine, func,inspect
from regression_modeling import * 
from visualize import * 
from nlp_aws import * 
import time

app = Flask(__name__)



apath="https://smubootcamprohith.s3.us-east-2.amazonaws.com/android_app_ratings_updated1.csv"
ipath="https://smubootcamprohith.s3.us-east-2.amazonaws.com/ios_app_ratings_updated1.csv"
afname="android_app_ratings_updated1.csv"
ifname="ios_app_ratings1.csv"

#-------------------------------------------------------------------------------------------------------
@app.route("/static/resources/v1/native/nlp")
def nlp_natives():
    x=main_invoke(apath,afname)
    time.sleep(60)
    y=main_invoke(ipath,ifname)
    lists = [x,y]
    return  jsonify(results = lists)

#------------------------------------------------------------------------------------------------------
@app.route("/static/resources/v1/failure/visualization")
def fail_viz():
    x=payment_failure_viz()
    y=prfupdate_failure_viz()
    z=plan_failure_viz()
    lists = [x,y,z]
    return  jsonify(results = lists)
#-------------------------------------------------------------------------------------------------------

@app.route("/static/resources/v1/agent/mlr")
def agent_trx_mlr():
    try:
        path="C:\\coding\\LearnPython\\FinalProject\\static\\resources\\data\\flow_failure_data.csv"
        a=multi_lr_agent(path)
        b=lasso_model_agent(path)
        c=ridge_model_agent(path)
        d=elastic_net_agent(path)
        linear_scatter_agent_lgn(path)
        linear_scatter_agent_cp(path)
        linear_scatter_agent_pu(path)
        linear_scatter_agent_pf(path)
        lists = [a,b,c,d]
    except (ValueError, ImportError, AttributeError):
          print("Some sort exception occured")
    return  jsonify(results = lists)

#------------------------------------------------------------------------------------------------------
@app.route("/static/resources/v1/unauthpayment/mlr")
def unauth_payment_mlr():
    path="C:\\coding\\LearnPython\\FinalProject\\static\\resources\\data\\unauth_payment_regression.csv"
    linear_plot_scatter(path)
    residual_plot(path)
    a=mlr_model_scores(path)
    b=linear_info(path)
    c=lasso_model(path)
    d=ridge_model(path)
    lists = [a,b,c,d]
    return  jsonify(results = lists)

#-------------------------------------------------------------------------------------------------------
@app.route("/static/resources/v1/data/failure")
def failure_data_info():
    session = create_session()
    x=create_db_classes()[0]
    success_results_web = session.query(x.TRX_DATETIME, x.API_NAME,x.RESPONSE_TIME,x.SRC_SYS,x.LOGINID,x.SERVER_ID).\
            filter(x.FAILED=="Y").\
            order_by(x.TRX_DATETIME).limit(400).\
            all()

    df = pd.DataFrame.from_records(success_results_web, columns =["TIMESTAMP","API_NAME","RESPONSE_TIME","SRC_SYS","LOGINID","SERVER_ID"])
    lists=df.to_dict('records')

    return jsonify(results = lists)
#-------------------------------------------------------------------------------------------------------

@app.route("/static/resources/v1/agent/web")
def agent_web_info():
    session = create_session()
    x=create_db_classes()[2]
  
    success_results_web = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
          filter(x.FAILED=="N").\
          filter(x.SRC_SYS=="OLAM").\
          group_by(x.TRX_HOUR).all()
                                       
    failure_results_web = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
        filter(x.FAILED=="Y").\
        filter(x.SRC_SYS=="OLAM").\
        group_by(x.TRX_HOUR).all()

    # Create lists from the query results
    hours_web = [result[0] for result in success_results_web]
    suc_count_web = [int(result[1]) for result in success_results_web]
    hours1_web = [result[0] for result in failure_results_web]
    fail_count_web = [int(result[1]) for result in failure_results_web]


    # Generate the plot trace
    trace1 = {
        "x": hours_web,
        "y": suc_count_web,
        "type": "bar",
        "name" : "SUCCESS"
    }
    trace2 = {
        "x": hours1_web,
        "y": fail_count_web,
        "type": "bar",
        "name" : "FAILURE"
    }                                  
    lists=[trace1,trace2]      

    return jsonify(results = lists)


#-------------------------------------------------------------------------------------------------------
@app.route("/static/resources/v1/agent/mobile")
def agent_mob_info():
    session = create_session()
    x=create_db_classes()[2]
    success_results_mob = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
          filter(x.FAILED=="N").\
          filter(x.SRC_SYS=="COLDAPP").\
          group_by(x.TRX_HOUR).all()
                                       
    # Create lists from the query results
    hours_mob = [result[0] for result in success_results_mob]
    suc_count_mob = [int(result[1]) for result in success_results_mob]

    # Generate the plot trace
    trace1 = {
        "x": hours_mob,
        "y": suc_count_mob,
        'mode': 'markers'
    }
       
    lists=[trace1]      

    return jsonify(results = lists)
#------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

@app.route("/static/resources/v1/agent/searchinfo")
def agent_search_info():
    session = create_session()
    x=create_db_classes()[2]
    success_results = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
          filter(x.FAILED=="N").\
          group_by(x.TRX_HOUR).all()
                                       
    # Create lists from the query results
    hours = [result[0] for result in success_results]
    suc_count = [int(result[1]) for result in success_results]


    # Generate the plot trace
    trace1 = {
        "y": hours,
        "x": suc_count,
        'type': 'bar',
         "orientation": "h"
    }
                   
                                    
    lists=[trace1]      

    return jsonify(results = lists)

#-------------------------------------------------------------------------------------------------------


@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

#-------------------------------------------------------------------------------------------------------
@app.route("/static/resources/v1/paymentinfo")
def payment_info():
    session = create_session()
    x=create_db_classes()[1]
    results = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
        group_by(x.TRX_HOUR).all()
                                       
    mob_results = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
        filter(x.SRC_SYS=="COLDAPP").\
        group_by(x.TRX_HOUR).all()
    web_results = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
        filter(x.SRC_SYS=="OLAM").\
        group_by(x.TRX_HOUR).all()

    # Create lists from the query results
    hours = [result[0] for result in results]
    count = [int(result[1]) for result in results]
    hours1 = [result[0] for result in mob_results]
    count1 = [int(result[1]) for result in mob_results]
    hours2 = [result[0] for result in web_results]
    count2 = [int(result[1]) for result in web_results]


    # Generate the plot trace
    trace1 = {
        "x": hours,
        "y": count,
        "type": "scatter",
        "mode": "lines+markers",
        "name" : "OVERALL",
        "line": {"color" :"#17BECF"}
    }
    trace2 = {
        "x": hours1,
        "y": count1,
        "type": "bar",
        "name" : "MOBILE",
        "mode":'lines+markers'
    }   
    trace3 = {
        "x": hours2,
        "y": count2,
        "type": "bar",
        "name" :"DESKTOP",
        "mode":'lines+markers'
    }                                        
                                    
    lists=[trace1,trace2,trace3]      

    return jsonify(results = lists)





#-------------------------------------------------------------------------------------------------------

@app.route("/v1/logininfo/web")
def login_web_info():
    session = create_session()
    x=create_db_classes()[0]
    success_results_web = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
          filter(x.FAILED=="N").\
          filter(x.SRC_SYS=="OLAM").\
          group_by(x.TRX_HOUR).all()
                                       
    failure_results_web = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
        filter(x.FAILED=="Y").\
        filter(x.SRC_SYS=="OLAM").\
        group_by(x.TRX_HOUR).all()

    # Create lists from the query results
    hours_web = [result[0] for result in success_results_web]
    suc_count_web = [int(result[1]) for result in success_results_web]
    hours1_web = [result[0] for result in failure_results_web]
    fail_count_web = [int(result[1]) for result in failure_results_web]


    # Generate the plot trace
    trace1 = {
        "x": hours_web,
        "y": suc_count_web,
        "type": "bar",
        "name" : "SUCCESS"
    }
    trace2 = {
        "x": hours1_web,
        "y": fail_count_web,
        "type": "bar",
        "name" : "FAILURE"
    }                                  
    lists=[trace1,trace2]      

    return jsonify(results = lists)


#-------------------------------------------------------------------------------------------------------
@app.route("/v1/logininfo/mobile")
def login_mob_info():
    session = create_session()
    x=create_db_classes()[0]
    success_results_mob = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
          filter(x.FAILED=="N").\
          filter(x.SRC_SYS=="COLDAPP").\
          group_by(x.TRX_HOUR).all()
                                       
    failure_results_mob = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
        filter(x.FAILED=="Y").\
        filter(x.SRC_SYS=="COLDAPP").\
        group_by(x.TRX_HOUR).all()

    # Create lists from the query results
    hours_mob = [result[0] for result in success_results_mob]
    suc_count_mob = [int(result[1]) for result in success_results_mob]
    hours1_mob = [result[0] for result in failure_results_mob]
    fail_count_mob = [int(result[1]) for result in failure_results_mob]
    # Generate the plot trace
    trace1 = {
        "x": hours_mob,
        "y": suc_count_mob,
        "type": "bar",
        "name" : "SUCCESS"
    }
    trace2 = {
        "x": hours1_mob,
        "y": fail_count_mob,
        "type": "bar",
        "name" : "FAILURE"
    }                                  
                                    
    lists=[trace1,trace2]      

    return jsonify(results = lists)

#-------------------------------------------------------------------------------------------------------
@app.route("/v1/logininfo")
def login_info():
    session = create_session()
    x=create_db_classes()[0]
    results = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
        group_by(x.TRX_HOUR).all()
                                       
    mob_results = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
        filter(x.SRC_SYS=="COLDAPP").\
        group_by(x.TRX_HOUR).all()
    web_results = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
        filter(x.SRC_SYS=="OLAM").\
        group_by(x.TRX_HOUR).all()

    # Create lists from the query results
    hours = [result[0] for result in results]
    count = [int(result[1]) for result in results]
    hours1 = [result[0] for result in mob_results]
    count1 = [int(result[1]) for result in mob_results]
    hours2 = [result[0] for result in web_results]
    count2 = [int(result[1]) for result in web_results]


    # Generate the plot trace
    trace1 = {
        "x": hours,
        "y": count,
        "type": "scatter",
        "mode": "lines+markers",
        "name" : "OVERALL",
        "line": {"color" :"#17BECF"}
    }
    trace2 = {
        "x": hours1,
        "y": count1,
        "type": "bar",
        "name" : "MOBILE",
        "mode":'lines+markers'
    }   
    trace3 = {
        "x": hours2,
        "y": count2,
        "type": "bar",
        "name" :"DESKTOP",
        "mode":'lines+markers'
    }                                        
                                    
    lists=[trace1,trace2,trace3]      

    return jsonify(results = lists)


#-------------------------------------------------------------------------------------------------------


@app.route("/static/resources/v1/paymentinfo/mobile")
def payment_mob_info():
    session = create_session()
    x=create_db_classes()[1]
    success_results_mob = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
          filter(x.FAILED=="N").\
          filter(x.SRC_SYS=="COLDAPP").\
          group_by(x.TRX_HOUR).all()
    print(success_results_mob)                                  
    failure_results_mob = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
        filter(x.FAILED=="Y").\
        filter(x.SRC_SYS=="COLDAPP").\
        group_by(x.TRX_HOUR).all()
    print(failure_results_mob)   
    # Create lists from the query results
    hours_mob = [result[0] for result in success_results_mob]
    suc_count_mob = [int(result[1]) for result in success_results_mob]
    hours1_mob = [result[0] for result in failure_results_mob]
    fail_count_mob = [int(result[1]) for result in failure_results_mob]
    # Generate the plot trace
    trace1 = {
        "x": hours_mob,
        "y": suc_count_mob,
        "type": "bar",
        "name" : "SUCCESS"
    }
    trace2 = {
        "x": hours1_mob,
        "y": fail_count_mob,
        "type": "bar",
        "name" : "FAILURE"
    }                                  
                                    
    lists=[trace1,trace2]      

    return jsonify(results = lists)



  #-------------------------------------------------------------------------------------------------------



@app.route("/static/resources/v1/paymentinfo/web")
def payment_web_info():
    session = create_session()
    x=create_db_classes()[1]
    success_results_web = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
          filter(x.FAILED=="N").\
          filter(x.SRC_SYS=="OLAM").\
          group_by(x.TRX_HOUR).all()
    print(success_results_web)                                 
    failure_results_web = session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).\
        filter(x.FAILED=="Y").\
        filter(x.SRC_SYS=="OLAM").\
        group_by(x.TRX_HOUR).all()
    print(failure_results_web)   
    # Create lists from the query results
    hours_web = [result[0] for result in success_results_web]
    suc_count_web = [int(result[1]) for result in success_results_web]
    hours1_web = [result[0] for result in failure_results_web]
    fail_count_web = [int(result[1]) for result in failure_results_web]


    # Generate the plot trace
    trace1 = {
        "x": hours_web,
        "y": suc_count_web,
        "type": "bar",
        "name" : "SUCCESS"
    }
    trace2 = {
        "x": hours1_web,
        "y": fail_count_web,
        "type": "bar",
        "name" : "FAILURE"
    }                                  
                                 
    lists=[trace1,trace2]      

    return jsonify(results = lists)


#-------------------------------------------------------------------------------------------------------

@app.route("/v1/loginandpayment")
def login_payment_info():
    session = create_session()
    a=create_db_classes()
    x=a[0]
    y=a[1]                             
    login_results =session.query(x.TRX_HOUR, func.count(x.TRX_HOUR)).filter(x.FAILED=="N").group_by(x.TRX_HOUR).all()
    payment_results=session.query(y.TRX_HOUR, func.count(y.TRX_HOUR)).filter(y.FAILED=="N").group_by(y.TRX_HOUR).all()
    # Create lists from the query results
    hours = [result[0] for result in login_results]
    lgn_count = [int(result[1]) for result in login_results]
    hours1 = [result[0] for result in payment_results]
    pay_count = [int(result[1]) for result in payment_results]

    # Generate the plot trace
    trace1 = {
        "x": hours,
        "y": lgn_count,
        "type": "scatter"
    }
    trace2 = {
        "x": hours1,
        "y": pay_count,
        "type": "scatter"
    }                                  
                                    
    lists=[trace1,trace2]      

    return jsonify(results = lists)


if __name__ == '__main__':
    app.run(debug=True)
