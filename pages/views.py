from codeop import CommandCompiler
from django.shortcuts import render
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#from .utils import get_plot
# Create your views here.


def index(request):
    df=pd.read_csv('data.csv')
    df1=df['Sales Method'].unique().tolist()
    df2=df['Sales Method'].value_counts(ascending=True).tolist()

    Product=df['Product'].count()
    Total=df['Total Sales'].count()

    return render(request,'index.html',{'df1':df1 ,'df2':df2 ,'Product':Product ,'Total':Total})





'''
def index(request):
    df=pd.read_csv('supermarket_sales.csv.csv')
    df1=df['City'].nunique()
    df2=df['cogs'].nunique()
    total=df['Total']
    gross=df['gross income'].count()
    branch=df['Branch'].nunique()
    gender=df['Gender'].nunique()
    #ptt=plt.plot(df['Total'] , df['gross income'])
    #context={'df1':df1}
    return render(request,'index.html',{'df1':df1,'df2':df2, 'total':total,'gross':gross ,
                                        'branch':branch,'gender':gender})
'''



'''
def index(request):
    df=pd.read_csv('supermarket_sales.csv.csv')
    #df1=df['City'].nunique()
    #df2=df['cogs'].count()
    #ptt=plt.plot(df['Total'] , df['gross income'])
    x=df['Total']
    y=df['gross income']
    plt.xlabel('one')
    plt.ylabel('Two')
    chart=get_plot(x,y)
    #context={'ptt':ptt}
    return render(request,'index.html',{'chart':chart})
'''
'''
def qqq(request):
    df=pd.read_csv('supermarket_sales.csv.csv')
    x=df['cogs']
    y=df['Rating']
    chart2=get_plot(x,y)
    plt.xlabel('eeeee')
    plt.ylabel('qqqq')
    return render(request,'index.html',{'chart':chart2})
''' 
