
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import ElasticNet

def mlr_model_scores(path):
    df2 = pd.read_csv(path)
    X = df2[["Day","Login_Failures","Payment_Failures","Campaign_Clicks"]]
    y = df2["UnAuth_Payment_Volume"].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    training_score =round(model.score(X_train, y_train),4)
    testing_score = round(model.score(X_test, y_test),4)
#     predicted = model.predict(X_test)
#     mse=mean_squared_error(y_test,predcited)
#     r2=r2_score(y_test,predcited)
#     print(mse)
    return [training_score,testing_score]

def residual_plot(path):
    df1 = pd.read_csv(path)
    X = df1[["Day","Login_Failures","Payment_Failures","Campaign_Clicks"]]
    y = df1["UnAuth_Payment_Volume"].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    plt.clf()
    plt.scatter(model.predict(X_train), model.predict(X_train) - y_train, c="blue", label="Training Data")
    plt.scatter(model.predict(X_test), model.predict(X_test) - y_test, c="orange", label="Testing Data")
    plt.legend()
    plt.hlines(y=0, xmin=y.min(), xmax=y.max())
    plt.title("Residual Plot")
    plt.savefig("C:\\coding\\LearnPython\\FinalProject\\static\\resources\\assets\\residual.png")


def linear_plot_scatter(path):
    df = pd.read_csv(path)
    X = df[["Campaign_Clicks"]]
    y = df["UnAuth_Payment_Volume"].values.reshape(-1, 1)
    plt.clf()
    print("logic worked for linear_plot_scatter")
    plt.scatter(X,y)
    plt.xlabel("Login Failures")
    plt.ylabel("Unauth Payment Volumes")
    plt.savefig("C:\\coding\\LearnPython\\FinalProject\\static\\resources\\assets\\linear.png")
    

def linear_info(path):
    df3 = pd.read_csv(path)
    X = df3[["Campaign_Clicks"]]
    y = df3["UnAuth_Payment_Volume"].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)
    model = LinearRegression()
    model.fit(X_train_scaled, y_train_scaled)
    predictions = model.predict(X_test_scaled)
    MSE = round(mean_squared_error(y_test_scaled, predictions),4)
    r2 = round(model.score(X_test_scaled, y_test_scaled),4)
    return [MSE,r2]

def lasso_model(path):
    lasso_df = pd.read_csv(path)
    X = lasso_df[["Day","Login_Failures","Payment_Failures","Campaign_Clicks"]]
    y = lasso_df["UnAuth_Payment_Volume"].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)
    lasso = Lasso(alpha=.01).fit(X_train_scaled, y_train_scaled)
    predictions = lasso.predict(X_test_scaled)
    MSE = round(mean_squared_error(y_test_scaled, predictions),4)
    r2 = round(lasso.score(X_test_scaled, y_test_scaled),4)
    return [MSE,r2]

def ridge_model(path):
    ridge_df = pd.read_csv(path)
    X = ridge_df[["Day","Login_Failures","Payment_Failures","Campaign_Clicks"]]
    y = ridge_df["UnAuth_Payment_Volume"].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)
    ridge = Ridge(alpha=.01).fit(X_train_scaled, y_train_scaled)
    predictions = ridge.predict(X_test_scaled)
    error = round(mean_squared_error(y_test_scaled, predictions),4)
    rr = round(ridge.score(X_test_scaled, y_test_scaled),4)
    return [error,rr]




def multi_lr_agent(path):
    df1 = pd.read_csv(path)
    X = df1[["Login_Volume","Payment_Volume","ChnagePlan_FeatureVolume","PaymentPlan_Update_Volumes","ProfileUpdate_Volume"]]
    y = df1["Agent_Volume"].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)
    model = LinearRegression()
    model.fit(X_train_scaled, y_train_scaled)
    predictions = model.predict(X_test_scaled)
    training_score =round(model.score(X_train_scaled, y_train_scaled),4)
    MSE = round(mean_squared_error(y_test_scaled, predictions),4)
    r2 = round(model.score(X_test_scaled, y_test_scaled),4)
    return [MSE,r2]

def ridge_model_agent(path):
    ridge_df = pd.read_csv(path)
    X = ridge_df[["Login_Volume","Payment_Volume","ChnagePlan_FeatureVolume","PaymentPlan_Update_Volumes","ProfileUpdate_Volume"]]
    y = ridge_df["Agent_Volume"].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)
    ridge = Ridge(alpha=.01).fit(X_train_scaled, y_train_scaled)
    predictions = ridge.predict(X_test_scaled)
    error = round(mean_squared_error(y_test_scaled, predictions),4)
    rr = round(ridge.score(X_test_scaled, y_test_scaled),4)
    return [error,rr]

def lasso_model_agent(path):
    lasso_df = pd.read_csv(path)
    X = lasso_df[["Login_Volume","Payment_Volume","ChnagePlan_FeatureVolume","PaymentPlan_Update_Volumes","ProfileUpdate_Volume"]]
    y = lasso_df["Agent_Volume"].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)
    lasso = Lasso(alpha=.01).fit(X_train_scaled, y_train_scaled)
    predictions = lasso.predict(X_test_scaled)
    MSE = round(mean_squared_error(y_test_scaled, predictions),4)
    r2 = round(lasso.score(X_test_scaled, y_test_scaled),4)
    return [MSE,r2]


def elastic_net_agent(path):
    elastic_df = pd.read_csv(path)
    X = elastic_df[["Login_Volume","Payment_Volume","ChnagePlan_FeatureVolume","PaymentPlan_Update_Volumes","ProfileUpdate_Volume"]]
    y = elastic_df["Agent_Volume"].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)
    elasticnet = ElasticNet(alpha=.01).fit(X_train_scaled, y_train_scaled)
    predictions = elasticnet.predict(X_test_scaled)
    MSE = round(mean_squared_error(y_test_scaled, predictions),4)
    r2 = round(elasticnet.score(X_test_scaled, y_test_scaled),4)
    return [MSE,r2]




def linear_scatter_agent_lgn(path):
    df = pd.read_csv(path)
    X = df[["Login_Volume"]]
    y = df["Agent_Volume"].values.reshape(-1, 1)
    plt.clf()
    print("logic worked for linear_scatter_agent_lgn")
    plt.scatter(X,y)
    plt.xlabel("Login Failures")
    plt.ylabel("Agent Activity")
    plt.savefig("C:\\coding\\LearnPython\\FinalProject\\static\\resources\\assets\\LR_lgn_agt.png")


def linear_scatter_agent_cp(path):
    df = pd.read_csv(path)
    X = df[["ChnagePlan_FeatureVolume"]]
    y = df["Agent_Volume"].values.reshape(-1, 1)
    plt.clf()
    print("logic worked for linear_scatter_agent_cp")
    plt.scatter(X,y)
    plt.xlabel("ChnagePlan and Feature Failures")
    plt.ylabel("Agent Activity")
    plt.savefig("C:\\coding\\LearnPython\\FinalProject\\static\\resources\\assets\\LR_cp_agt.png")


def linear_scatter_agent_pu(path):
    df = pd.read_csv(path)
    X = df[["ProfileUpdate_Volume"]]
    y = df["Agent_Volume"].values.reshape(-1, 1)
    plt.clf()
    print("logic worked for linear_scatter_agent_pu")
    plt.scatter(X,y)
    plt.xlabel("Profile Update Failures")
    plt.ylabel("Agent Activity")
    plt.savefig("C:\\coding\\LearnPython\\FinalProject\\static\\resources\\assets\\LR_pu_agt.png")

def linear_scatter_agent_pf(path):
    df = pd.read_csv(path)
    X = df[["PaymentPlan_Update_Volumes"]]
    y = df["Agent_Volume"].values.reshape(-1, 1)
    plt.clf()
    print("logic worked for linear_scatter_agent_pf")
    plt.scatter(X,y)
    plt.xlabel("Payment plan update Failures")
    plt.ylabel("Agent Activity")
    plt.savefig("C:\\coding\\LearnPython\\FinalProject\\static\\resources\\assets\\LR_pay_agt.png")