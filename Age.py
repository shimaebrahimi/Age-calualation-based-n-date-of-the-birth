#!/usr/bin/env python
# coding: utf-8

# In[3]:


import datetime
import math
def datee(x,y,z):
    now=datetime.datetime.now()
    year=now.year
    month=now.month
    day=now.day
    hour=now.hour
    min=now.minute
    sec=now.second
    if (x>year) or (x==year and y>month) or (x==year and y==month and z>day):
        print("wrong date")
    else:
        if month<y:
            ye=year-x-1
            mo=math.fabs(month-y)
            da=math.fabs(day-z)
        else:
            ye=year-x
            mo=month-y
            da=math.fabs(day-z)
        if day<z:
            if month==y:
                mo=math.fabs(month-y)
                da=30-(math.fabs(day-z))
            else:
                mo=math.fabs(month-y)-1
                da=30-(math.fabs(day-z))
        yee=ye
        moo=(yee*12)+mo
        daa=(yee*12*30)+da
        houu=(yee*12*30*24)+hour
        miin=(yee*12*30*24*60)+min
        secc=(yee*12*30*24*60*60)+sec
        print(year,month,day)
        print(f"shoma{ye} sal,{mo} mah,{da} ruz,{hour} saat,{min} daghighe,{sec} sanie zendegi kardeid")
        print(f"shoma{yee} sal,{moo} mah,{daa} ruz,{houu} saat,{miin} daghighe,{secc} sanie zendegi kardeid")


# In[4]:


datee(1987,10,20)


# In[ ]:




