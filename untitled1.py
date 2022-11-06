#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 14:26:52 2022

@author: umair
"""

import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import requests as rq
import numpy as np


def get_data(link):
    """
    this function get data from link in xlsx form and then store it in data variable  and return the  data
    """
    
    # url variable store url link
    url=link
    
    # get data from link and store in data list
    data =rq.get(url).content
    
    # read exel file and store in dataframe
    data = pd.read_excel(BytesIO(data))
    
    # return dataframe
    return data



def carbon_emission_avg(data):
    
    """
    this function take data  as parameter then calculate the average  of values and return the average
    """
    
    # calculating average of carbon emission
    sum_data = 0
    
    #for loop it will iterate and sum all values
    for t in data:
        sum_data = sum_data + t           

    # Avg variable is used to store average of data
    avg = sum_data / len(data)
    
    return avg


def data_normalization(data):
    """
    in this function the data normalization take place global variables are initilized here and data preprocessing take place here
    """
    
    # global variables declared to store data at global level so it can be accessed at global
    global uk_carbon_emission
    global maxico_carbon_emission
    global ukrine_carbon_emission
    global india_carbon_emission
    global year
    
    # getting data of five year  and storing in lists
    year_fifteen=data['2015 [YR2015]']
    year_sixteen=data['2016 [YR2016]']
    year_seventeen=data['2017 [YR2017]']
    year_eighteen=data['2018 [YR2018]']
    year_nineteen=data['2019 [YR2019]']
    
    # store specific countries data of five year
    uk_carbon_emission=[year_fifteen.iloc[180],year_sixteen.iloc[180],year_seventeen.iloc[180],year_eighteen.iloc[180],year_nineteen.iloc[180]]
    maxico_carbon_emission=[year_fifteen.iloc[111],year_sixteen.iloc[111],year_seventeen.iloc[111],year_eighteen.iloc[111],year_nineteen.iloc[111]]
    ukrine_carbon_emission=[year_fifteen.iloc[178],year_sixteen.iloc[178],year_seventeen.iloc[178],year_eighteen.iloc[178],year_nineteen.iloc[178]]
    india_carbon_emission=[year_fifteen.iloc[60],year_sixteen.iloc[60],year_seventeen.iloc[60],year_eighteen.iloc[60],year_nineteen.iloc[60]]
    
    # define years
    year=['2015','2016','2017','2018','2019']
    
def data_visualization(data,type):
    """
    in this function the visualization take place like pie chart , bar chart and multiline plot based on country carbon emission of five years
    """    

    # if used to selectdifferent graph
    if type=="multiline":
        
        # here we ploting data
        plt.plot(year, uk_carbon_emission,label=data['Country Name'].iloc[180])
        plt.plot(year, maxico_carbon_emission,label=data['Country Name'].iloc[111])
        plt.plot(year, ukrine_carbon_emission,label=data['Country Name'].iloc[178])
        plt.plot(year, india_carbon_emission,label=data['Country Name'].iloc[60])
        
    
        # we are defining the label
        plt.xlabel("Year")
        plt.ylabel("Carbon Emission")
        
    
        # we are adding lagend on upper right
        plt.legend(loc='upper right')
        
        # Dispay graph
        plt.show()
        
        
    elif type=="pie":
        
        # here we ploting pir chart graph
        plt.pie([carbon_emission_avg(uk_carbon_emission),carbon_emission_avg(maxico_carbon_emission),carbon_emission_avg(ukrine_carbon_emission),carbon_emission_avg(india_carbon_emission),],labels=["UK","Mexico","Ukrine","India"])
        
        # here we show pir graph
        plt.show()
        
        
    elif type=="bar":
        
        # here we get avg of countries and add in average list
       average = [carbon_emission_avg(uk_carbon_emission),carbon_emission_avg(maxico_carbon_emission),carbon_emission_avg(ukrine_carbon_emission),carbon_emission_avg(india_carbon_emission),]
       
       # here we define names of bars
       bars = ('UK', 'Mexico', 'Ukrine', 'India')
       x_pos = np.arange(len(bars))
 
       # Create bars and choose color
       plt.bar(x_pos, average, color = (0.5,0.1,0.5,0.2))
 
       # Add title and axis names
       plt.title('Carbon Emission Data For Last Five Year in Kilo Ton')
       plt.xlabel('Countries')
       plt.ylabel('Carbon Emission')
 
       # Create names on the x axis
       plt.xticks(x_pos, bars)
 
       # Show graph
       plt.show()
        
    


if __name__=="__main__":
    
    # empty list for to store global data
    uk_carbon_emission=[]
    maxico_carbon_emission=[]
    ukrine_carbon_emission=[]
    india_carbon_emission=[]
    year=[]
    
    # here we get data from link
    value=get_data("https://github.com/umairaziz999/Assignment1/blob/main/Data_Extract_From_World_Development_Indicators.xlsx?raw=true")
    
    # here we do preprocessinng of data
    data_normalization(value)
    
    # here we visuallize data with miltiline
    data_visualization(value,"multiline")
    
    # here we visuallize data with bar graph
    data_visualization(value,"bar")
    
    # here we visuallize data with pie graph
    data_visualization(value,"pie")
    