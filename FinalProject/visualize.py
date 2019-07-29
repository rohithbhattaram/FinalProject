
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import plotly.offline as po

def payment_failure_viz():
    x=0
    fail_df=pd.read_csv("C:\\coding\\LearnPython\\FinalProject\\static\\resources\\data\\flow_failure_data.csv")
    suc_df=pd.read_csv("C:\\coding\\LearnPython\\FinalProject\\static\\resources\\data\\flow_success_data.csv")
    result_df = pd.concat([fail_df, suc_df], axis=1, sort=False)
    fig = px.scatter(result_df, x="LoginVolume", y="PaymentVolume", color="PaymentVolume",
                 size='PaymentVolume', hover_data=['Day_of_Month'])
    po.plot(fig, filename = 'C:\\coding\\LearnPython\\FinalProject\\static\\resources\\fail_viz_pay.html', auto_open=False)
    return x

def prfupdate_failure_viz():
    x=0
    fail_df=pd.read_csv("C:\\coding\\LearnPython\\FinalProject\\static\\resources\\data\\flow_failure_data.csv")
    suc_df=pd.read_csv("C:\\coding\\LearnPython\\FinalProject\\static\\resources\\data\\flow_success_data.csv")
    result_df = pd.concat([fail_df, suc_df], axis=1, sort=False)
    fig = px.scatter(result_df, x="LoginVolume", y="ProfileUpdate_Volume", color="ProfileUpdate_Volume",
                 size='ProfileUpdate_Volume', hover_data=['Day_of_Month'])
    po.plot(fig, filename = 'C:\\coding\\LearnPython\\FinalProject\\static\\resources\\fail_viz_prfu.html', auto_open=False)
    return x

def plan_failure_viz():
    x=0
    fail_df=pd.read_csv("C:\\coding\\LearnPython\\FinalProject\\static\\resources\\data\\flow_failure_data.csv")
    suc_df=pd.read_csv("C:\\coding\\LearnPython\\FinalProject\\static\\resources\\data\\flow_success_data.csv")
    result_df = pd.concat([fail_df, suc_df], axis=1, sort=False)
    fig = px.scatter(result_df, x="LoginVolume", y="ChnagePlan_FeatureVolume", color="ChnagePlan_FeatureVolume",
                 size='ChnagePlan_FeatureVolume', hover_data=['Day_of_Month'])
    po.plot(fig, filename = 'C:\\coding\\LearnPython\\FinalProject\\static\\resources\\fail_viz_cp.html', auto_open=False)
    return x
#--------------------------------------