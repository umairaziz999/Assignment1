#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 14:26:52 2022

@author: umair
"""

import pandas as pd
import matplotlib.pyplot as plt

def fun():
    data = pd.read_excel("Data_Extract_From_World_Development_Indicators.xlsx",)

    year15=data['2015 [YR2015]']
    year16=data['2016 [YR2016]']
    year17=data['2017 [YR2017]']
    year18=data['2018 [YR2018]']
    year19=data['2019 [YR2019]']
    ukcarbon=[year15.iloc[180],year16.iloc[180],year17.iloc[180],year18.iloc[180],year19.iloc[180]]
    maxicocarbon=[year15.iloc[111],year16.iloc[111],year17.iloc[111],year18.iloc[111],year19.iloc[111]]
    ukrinecarbon=[year15.iloc[178],year16.iloc[178],year17.iloc[178],year18.iloc[178],year19.iloc[178]]
    indcarbon=[year15.iloc[60],year16.iloc[60],year17.iloc[60],year18.iloc[60],year19.iloc[60]]
    year=['2015','2016','2017','2018','2019']
    f=data[(data['Country Name']=="Mexico")]
    plt.plot(year, ukcarbon,label=data['Country Name'].iloc[180])
    plt.plot(year, maxicocarbon,label=data['Country Name'].iloc[111])
    plt.plot(year, ukrinecarbon,label=data['Country Name'].iloc[178])
    plt.plot(year, indcarbon,label=data['Country Name'].iloc[60])
    plt.xlabel("Year")
    plt.ylabel("Carbon Emission")
    plt.legend(loc='upper right')
    plt.show()


if __name__=="__main__":
    fun()