from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.http import JsonResponse
import yfinance as yf
import time
import pandas as pd
import numpy as np
from datetime import datetime


#網頁畫面呼叫
def show(request):  
    return render(request, 'show.html', locals())

def screen_input(request):

    stock1 = request.POST['stock1']
    stock2 = request.POST['stock2']
    Start_date = request.POST['Start_date']
    End_date = request.POST['End_date']
    # print(stock1)
    # print(stock2)
    # print(Start_date)
    # print(End_date)


    df = yf.download(stock1, start = Start_date, end = End_date)
    Stock1_Price = df.Close


    stock1_index_list = []
    for x in range(len(df.index)):
        time_index = str(df.index[x])
        stock1_index_list.append(time_index[:10])
   
    Stock1_list = []
    for stock_index,price in zip ((stock1_index_list),list(Stock1_Price)):
        Stock1_list.append(list((stock_index,price)))

    stock1_response =[[int(time.mktime(datetime.strptime(
        ele[0], "%Y-%m-%d").timetuple()))*1000]+[ele[1] ]for ele in Stock1_list]
    # print(stock1_response)



    df = yf.download(stock2, start = Start_date, end = End_date)
    Stock2_Price = df.Close


    stock2_index_list = []
    for x in range(len(df.index)):
        time_index = str(df.index[x])
        stock2_index_list.append(time_index[:10])
   
    Stock2_list = []

    for stock_index,price in zip ((stock2_index_list),list(Stock2_Price)):
        Stock2_list.append(list((stock_index,price)))
    
    stock2_response =[[int(time.mktime(datetime.strptime(
        ele[0], "%Y-%m-%d").timetuple()))*1000]+[ele[1] ]for ele in Stock2_list]
    
    # correlation = np.corrcoef(Stock1_Price,Stock2_Price)
    # 'correlation':correlation

    response = {'stock1_response':stock1_response,'stock2_response':stock2_response,'stock1':stock1,'stock2':stock2,}
    return JsonResponse(response)


    