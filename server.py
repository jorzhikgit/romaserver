from flask import Flask
from flask import jsonify
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import random
from pandas_datareader import data as pdr
import talib
from talib import abstract
from catboost import CatBoostClassifier


app = Flask(__name__)
def getSignal(val):
    if val<0:
        return "UP"
    if val>0:
        return "DOWN"
    
def getsignet(val):
    if val==True:
        return "BUY"
    else:
        return "SELL"
        
@app.route('/candle')
def getPatterns():
    patterndata=[]
    tickerhistory = yf.Ticker('BTC-USD')
    data=tickerhistory.history(period='5d',interval='60m')
    
    data.rename(columns={'Open':'open','High':'high','Low':'low','Close':'close'},inplace=True)
    
    
    # In[3]:
    patternslist={}
    
    #CDL2CROWS - Two Crows
    patt={}
    patt['pattern']='2CROWS - Two Crows'
    gs = abstract.CDL2CROWS(data)
    data['CDL2CROWS']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDL2CROWS"]].copy()
    data2crows['Signal'] = data2crows['CDL2CROWS'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDL2CROWS'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDL2CROWS']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[4]:
    
    
    #CDL3BLACKCROWS - Three Black Crows
    patt={}
    patt['pattern']='3BLACKCROWS - Three Black Crows'
    gs = abstract.CDL3BLACKCROWS(data)
    data['CDL3BLACKCROWS']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDL3BLACKCROWS"]].copy()
    data2crows['Signal'] = data2crows['CDL3BLACKCROWS'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDL3BLACKCROWS'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDL3BLACKCROWS']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[5]:
    
    
    #CDL3INSIDE - Three Inside Up/Down
    patt={}
    patt['pattern']='3INSIDE - Three Inside Up/Down'
    gs = abstract.CDL3INSIDE(data)
    data['CDL3INSIDE']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDL3INSIDE"]].copy()
    data2crows['Signal'] = data2crows['CDL3INSIDE'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDL3INSIDE'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDL3INSIDE']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    # In[6]:
    
    
    #CDL3LINESTRIKE - Three-Line Strike
    patt={}
    patt['pattern']='3LINESTRIKE - Three-Line Strike'
    gs = abstract.CDL3LINESTRIKE(data)
    data['CDL3LINESTRIKE']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    
    data2crows=data2crows[["index","Datetime","CDL3LINESTRIKE"]].copy()
    data2crows['Signal'] = data2crows['CDL3LINESTRIKE'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDL3LINESTRIKE'] != 0]
        dataarr=data2crows.to_dict('records')
   # patternslist['CDL3LINESTRIKE']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    #CDL3OUTSIDE - Three Outside Up/Down
    patt={}
    patt['pattern']='3OUTSIDE - Three Outside Up/Down'
    gs = abstract.CDL3OUTSIDE(data)
    data['CDL3OUTSIDE']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDL3OUTSIDE"]].copy()
    data2crows['Signal'] = data2crows['CDL3OUTSIDE'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDL3OUTSIDE'] != 0]
        dataarr=data2crows.to_dict('records')
    #patternslist['CDL3OUTSIDE']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    
    # In[8]:
    
    
    #CDL3STARSINSOUTH - Three Stars In The South
    patt={}
    patt['pattern']='3STARSINSOUTH - Three Stars In The South'
    gs = abstract.CDL3STARSINSOUTH(data)
    data['CDL3STARSINSOUTH']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDL3STARSINSOUTH"]].copy()
    data2crows['Signal'] = data2crows['CDL3STARSINSOUTH'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDL3STARSINSOUTH'] != 0]
        dataarr=data2crows.to_dict('records')
   # patternslist['CDL3STARSINSOUTH']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[9]:
    
    
    #CDL3WHITESOLDIERS - Three Advancing White Soldiers
    patt={}
    patt['pattern']='3WHITESOLDIERS - Three Advancing White Soldiers'
    gs = abstract.CDL3WHITESOLDIERS(data)
    data['CDL3WHITESOLDIERS']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDL3WHITESOLDIERS"]].copy()
    data2crows['Signal'] = data2crows['CDL3WHITESOLDIERS'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDL3WHITESOLDIERS'] != 0]
        dataarr=data2crows.to_dict('records')
    #patternslist['CDL3WHITESOLDIERS']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[10]:
    
    
    #CDLABANDONEDBABY - Abandoned Baby
    patt={}
    patt['pattern']='ABANDONEDBABY - Abandoned Baby'
    gs = abstract.CDLABANDONEDBABY(data)
    data['CDLABANDONEDBABY']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    
    data2crows=data2crows[["index","Datetime","CDLABANDONEDBABY"]].copy()
    data2crows['Signal'] = data2crows['CDLABANDONEDBABY'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLABANDONEDBABY'] != 0]
        dataarr=data2crows.to_dict('records')
        
   # patternslist['CDLABANDONEDBABY']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    
    # In[11]:
    
    
    #CDLADVANCEBLOCK - Advance Block
    patt={}
    patt['pattern']='ADVANCEBLOCK - Advance Block'
    gs = abstract.CDLADVANCEBLOCK(data)
    data['CDLADVANCEBLOCK']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    
    data2crows=data2crows[["index","Datetime","CDLADVANCEBLOCK"]].copy()
    data2crows['Signal'] = data2crows['CDLADVANCEBLOCK'].map(getSignal)
    
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        
        data2crows=data2crows.loc[data2crows['CDLADVANCEBLOCK'] != 0]
        print(data2crows)
        dataarr=data2crows.to_dict('records')
   # patternslist['CDLADVANCEBLOCK']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[12]:
    
    
    #CDLBELTHOLD - Belt-hold
    patt={}
    patt['pattern']='BELTHOLD - Belt-hold'
    gs = abstract.CDLBELTHOLD(data)
    data['CDLBELTHOLD']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLBELTHOLD"]].copy()
    data2crows['Signal'] = data2crows['CDLBELTHOLD'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLBELTHOLD'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLBELTHOLD']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[13]:
    
    
    #CDLBREAKAWAY - Breakaway
    patt={}
    patt['pattern']='BREAKAWAY - Breakaway'
    gs = abstract.CDLBREAKAWAY(data)
    data['CDLBREAKAWAY']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLBREAKAWAY"]].copy()
    data2crows['Signal'] = data2crows['CDLBREAKAWAY'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLBREAKAWAY'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLBREAKAWAY']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[14]:
    
    
    #CDLCLOSINGMARUBOZU - Closing Marubozu
    patt={}
    patt['pattern']='CLOSINGMARUBOZU - Closing Marubozu'
    gs = abstract.CDLCLOSINGMARUBOZU(data)
    data['CDLCLOSINGMARUBOZU']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLCLOSINGMARUBOZU"]].copy()
    data2crows['Signal'] = data2crows['CDLCLOSINGMARUBOZU'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLCLOSINGMARUBOZU'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLCLOSINGMARUBOZU']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[15]:
    
    
    #CDLCONCEALBABYSWALL - Concealing Baby Swallow
    patt={}
    patt['pattern']='CONCEALBABYSWALL - Concealing Baby Swallow'
    gs = abstract.CDLCONCEALBABYSWALL(data)
    data['CDLCONCEALBABYSWALL']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLCONCEALBABYSWALL"]].copy()
    data2crows['Signal'] = data2crows['CDLCONCEALBABYSWALL'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLCONCEALBABYSWALL'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLCONCEALBABYSWALL']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[16]:
    
    
    #CDLCOUNTERATTACK - Counterattack
    patt={}
    patt['pattern']='COUNTERATTACK - Counterattack'
    gs = abstract.CDLCOUNTERATTACK(data)
    data['CDLCOUNTERATTACK']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLCOUNTERATTACK"]].copy()
    data2crows['Signal'] = data2crows['CDLCOUNTERATTACK'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLCOUNTERATTACK'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLCOUNTERATTACK']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[17]:
    
    
    #CDLDARKCLOUDCOVER - Dark Cloud Cover
    patt={}
    patt['pattern']='DARKCLOUDCOVER - Dark Cloud Cover'
    gs = abstract.CDLDARKCLOUDCOVER(data)
    data['CDLDARKCLOUDCOVER']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLDARKCLOUDCOVER"]].copy()
    data2crows['Signal'] = data2crows['CDLDARKCLOUDCOVER'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLDARKCLOUDCOVER'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLDARKCLOUDCOVER']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[18]:
    
    
    #CDLDOJI - Doji
    patt={}
    patt['pattern']='DOJI - Doji'
    gs = abstract.CDLDOJI(data)
    data['CDLDOJI']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLDOJI"]].copy()
    data2crows['Signal'] = data2crows['CDLDOJI'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLDOJI'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLDOJI']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[19]:
    
    
    #CDLDOJISTAR - Doji Star
    patt={}
    patt['pattern']='DOJISTAR - Doji Star'
    gs = abstract.CDLDOJISTAR(data)
    data['CDLDOJISTAR']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLDOJISTAR"]].copy()
    data2crows['Signal'] = data2crows['CDLDOJISTAR'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLDOJISTAR'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLDOJISTAR']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[20]:
    
    
    #CDLDRAGONFLYDOJI - Dragonfly Doji
    patt={}
    patt['pattern']='DRAGONFLYDOJI - Dragonfly Doji'
    gs = abstract.CDLDRAGONFLYDOJI(data)
    data['CDLDRAGONFLYDOJI']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLDRAGONFLYDOJI"]].copy()
    data2crows['Signal'] = data2crows['CDLDRAGONFLYDOJI'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLDRAGONFLYDOJI'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLDRAGONFLYDOJI']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[21]:
    
    
    #CDLENGULFING - Engulfing Pattern
    patt={}
    patt['pattern']='ENGULFING - Engulfing Pattern'
    gs = abstract.CDLENGULFING(data)
    data['CDLENGULFING']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLENGULFING"]].copy()
    data2crows['Signal'] = data2crows['CDLENGULFING'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLENGULFING'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLENGULFING']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[22]:
    
    
    #CDLEVENINGDOJISTAR - Evening Doji Star
    patt={}
    patt['pattern']='EVENINGDOJISTAR - Evening Doji Star'
    gs = abstract.CDLEVENINGDOJISTAR(data)
    data['CDLEVENINGDOJISTAR']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLEVENINGDOJISTAR"]].copy()
    data2crows['Signal'] = data2crows['CDLEVENINGDOJISTAR'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLEVENINGDOJISTAR'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLEVENINGDOJISTAR']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[23]:
    
    
    #CDLEVENINGSTAR - Evening Star
    patt={}
    patt['pattern']='EVENINGSTAR - Evening Star'
    gs = abstract.CDLEVENINGSTAR(data)
    data['CDLEVENINGSTAR']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLEVENINGSTAR"]].copy()
    data2crows['Signal'] = data2crows['CDLEVENINGSTAR'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLEVENINGSTAR'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLEVENINGSTAR']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[24]:
    
    
    #CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines
    patt={}
    patt['pattern']='GAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines'
    gs = abstract.CDLGAPSIDESIDEWHITE(data)
    data['CDLGAPSIDESIDEWHITE']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLGAPSIDESIDEWHITE"]].copy()
    data2crows['Signal'] = data2crows['CDLGAPSIDESIDEWHITE'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLGAPSIDESIDEWHITE'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLGAPSIDESIDEWHITE']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[25]:
    
    
    #CDLGRAVESTONEDOJI - Gravestone Doji
    patt={}
    patt['pattern']='GRAVESTONEDOJI - Gravestone Doji'
    gs = abstract.CDLGRAVESTONEDOJI(data)
    data['CDLGRAVESTONEDOJI']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLGRAVESTONEDOJI"]].copy()
    data2crows['Signal'] = data2crows['CDLGRAVESTONEDOJI'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLGRAVESTONEDOJI'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLGRAVESTONEDOJI']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[26]:
    
    
    #CDLHAMMER - Hammer
    patt={}
    patt['pattern']='HAMMER - Hammer'
    gs = abstract.CDLHAMMER(data)
    data['CDLHAMMER']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLHAMMER"]].copy()
    data2crows['Signal'] = data2crows['CDLHAMMER'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLHAMMER'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLHAMMER']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[27]:
    
    
    #CDLHANGINGMAN - Hanging Man
    patt={}
    patt['pattern']='HANGINGMAN - Hanging Man'
    gs = abstract.CDLHANGINGMAN(data)
    data['CDLHANGINGMAN']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLHANGINGMAN"]].copy()
    data2crows['Signal'] = data2crows['CDLHANGINGMAN'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLHANGINGMAN'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLHANGINGMAN']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[28]:
    
    
    #CDLHARAMI - Harami Pattern
    patt={}
    patt['pattern']='HARAMI - Harami Pattern'
    gs = abstract.CDLHARAMI(data)
    data['CDLHARAMI']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLHARAMI"]].copy()
    data2crows['Signal'] = data2crows['CDLHARAMI'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLHARAMI'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLHARAMI']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[29]:
    
    
    #CDLHARAMICROSS - Harami Cross Pattern
    patt={}
    patt['pattern']='HARAMICROSS - Harami Cross Pattern'
    gs = abstract.CDLHARAMICROSS(data)
    data['CDLHARAMICROSS']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLHARAMICROSS"]].copy()
    data2crows['Signal'] = data2crows['CDLHARAMICROSS'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLHARAMICROSS'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLHARAMICROSS']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[30]:
    
    
    #CDLHIGHWAVE - High-Wave Candle
    patt={}
    patt['pattern']='HIGHWAVE - High-Wave Candle'
    gs = abstract.CDLHIGHWAVE(data)
    data['CDLHIGHWAVE']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLHIGHWAVE"]].copy()
    data2crows['Signal'] = data2crows['CDLHIGHWAVE'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLHIGHWAVE'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLHIGHWAVE']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[31]:
    
    
    #CDLHIKKAKE - Hikkake Pattern
    patt={}
    patt['pattern']='HIKKAKE - Hikkake Pattern'
    gs = abstract.CDLHIKKAKE(data)
    data['CDLHIKKAKE']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLHIKKAKE"]].copy()
    data2crows['Signal'] = data2crows['CDLHIKKAKE'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLHIKKAKE'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLHIKKAKE']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[32]:
    
    
    #CDLHIKKAKEMOD - Modified Hikkake Pattern
    patt={}
    patt['pattern']='HIKKAKEMOD - Modified Hikkake Pattern'
    gs = abstract.CDLHIKKAKEMOD(data)
    data['CDLHIKKAKEMOD']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLHIKKAKEMOD"]].copy()
    data2crows['Signal'] = data2crows['CDLHIKKAKEMOD'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLHIKKAKEMOD'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLHIKKAKEMOD']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[33]:
    
    
    #CDLHOMINGPIGEON - Homing Pigeon
    patt={}
    patt['pattern']='HOMINGPIGEON - Homing Pigeon'
    gs = abstract.CDLHOMINGPIGEON(data)
    data['CDLHOMINGPIGEON']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLHOMINGPIGEON"]].copy()
    data2crows['Signal'] = data2crows['CDLHOMINGPIGEON'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLHOMINGPIGEON'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLHOMINGPIGEON']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[34]:
    
    
    #CDLIDENTICAL3CROWS - Identical Three Crows
    patt={}
    patt['pattern']='IDENTICAL3CROWS - Identical Three Crows'
    gs = abstract.CDLIDENTICAL3CROWS(data)
    data['CDLIDENTICAL3CROWS']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLIDENTICAL3CROWS"]].copy()
    data2crows['Signal'] = data2crows['CDLIDENTICAL3CROWS'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLIDENTICAL3CROWS'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLIDENTICAL3CROWS']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[35]:
    
    
    #CDLINNECK - In-Neck Pattern
    patt={}
    patt['pattern']='INNECK - In-Neck Pattern'
    gs = abstract.CDLINNECK(data)
    data['CDLINNECK']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLINNECK"]].copy()
    data2crows['Signal'] = data2crows['CDLINNECK'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLINNECK'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLINNECK']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[36]:
    
    
    #CDLINVERTEDHAMMER - Inverted Hammer
    patt={}
    patt['pattern']='INVERTEDHAMMER - Inverted Hammer'
    gs = abstract.CDLINVERTEDHAMMER(data)
    data['CDLINVERTEDHAMMER']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLINVERTEDHAMMER"]].copy()
    data2crows['Signal'] = data2crows['CDLINVERTEDHAMMER'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLINVERTEDHAMMER'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLINVERTEDHAMMER']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[37]:
    
    
    #CDLKICKING - Kicking
    patt={}
    patt['pattern']='KICKING - Kicking'
    gs = abstract.CDLKICKING(data)
    data['CDLKICKING']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLKICKING"]].copy()
    data2crows['Signal'] = data2crows['CDLKICKING'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLKICKING'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLKICKING']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[38]:
    
    
    #CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu
    patt={}
    patt['pattern']='KICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu'
    gs = abstract.CDLKICKINGBYLENGTH(data)
    data['CDLKICKINGBYLENGTH']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLKICKINGBYLENGTH"]].copy()
    data2crows['Signal'] = data2crows['CDLKICKINGBYLENGTH'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLKICKINGBYLENGTH'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLKICKINGBYLENGTH']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[39]:
    
    
    #CDLLADDERBOTTOM - Ladder Bottom
    patt={}
    patt['pattern']='LADDERBOTTOM - Ladder Bottom'
    gs = abstract.CDLLADDERBOTTOM(data)
    data['CDLLADDERBOTTOM']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLLADDERBOTTOM"]].copy()
    data2crows['Signal'] = data2crows['CDLLADDERBOTTOM'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLLADDERBOTTOM'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLLADDERBOTTOM']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[40]:
    
    
    #CDLLONGLEGGEDDOJI - Long Legged Doji
    patt={}
    patt['pattern']='LONGLEGGEDDOJI - Long Legged Doji'
    gs = abstract.CDLLONGLEGGEDDOJI(data)
    data['CDLLONGLEGGEDDOJI']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLLONGLEGGEDDOJI"]].copy()
    data2crows['Signal'] = data2crows['CDLLONGLEGGEDDOJI'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLLONGLEGGEDDOJI'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLLONGLEGGEDDOJI']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[41]:
    
    
    #CDLLONGLINE - Long Line Candle
    patt={}
    patt['pattern']='LONGLINE - Long Line Candle'
    gs = abstract.CDLLONGLINE(data)
    data['CDLLONGLINE']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLLONGLINE"]].copy()
    data2crows['Signal'] = data2crows['CDLLONGLINE'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLLONGLINE'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLLONGLINE']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[42]:
    
    
    #CDLMARUBOZU - Marubozu
    patt={}
    patt['pattern']='MARUBOZU - Marubozu'
    gs = abstract.CDLMARUBOZU(data)
    data['CDLMARUBOZU']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLMARUBOZU"]].copy()
    data2crows['Signal'] = data2crows['CDLMARUBOZU'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLMARUBOZU'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLMARUBOZU']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[43]:
    
    
    #CDLMATCHINGLOW - Matching Low
    patt={}
    patt['pattern']='MATCHINGLOW - Matching Low'
    gs = abstract.CDLMATCHINGLOW(data)
    data['CDLMATCHINGLOW']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLMATCHINGLOW"]].copy()
    data2crows['Signal'] = data2crows['CDLMATCHINGLOW'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLMATCHINGLOW'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLMATCHINGLOW']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[44]:
    
    
    #CDLMATHOLD - Mat Hold
    patt={}
    patt['pattern']='MATHOLD - Mat Hold'
    gs = abstract.CDLMATHOLD(data)
    data['CDLMATHOLD']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLMATHOLD"]].copy()
    data2crows['Signal'] = data2crows['CDLMATHOLD'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLMATHOLD'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLMATHOLD']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[45]:
    
    
    #CDLMORNINGDOJISTAR - Morning Doji Star
    patt={}
    patt['pattern']='MORNINGDOJISTAR - Morning Doji Star'
    gs = abstract.CDLMORNINGDOJISTAR(data)
    data['CDLMORNINGDOJISTAR']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLMORNINGDOJISTAR"]].copy()
    data2crows['Signal'] = data2crows['CDLMORNINGDOJISTAR'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLMORNINGDOJISTAR'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLMORNINGDOJISTAR']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[46]:
    
    
    #CDLMORNINGSTAR - Morning Star
    patt={}
    patt['pattern']='MORNINGSTAR - Morning Star'
    gs = abstract.CDLMORNINGSTAR(data)
    data['CDLMORNINGSTAR']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLMORNINGSTAR"]].copy()
    data2crows['Signal'] = data2crows['CDLMORNINGSTAR'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLMORNINGSTAR'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLMORNINGSTAR']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[47]:
    
    
    #CDLONNECK - On-Neck Pattern
    patt={}
    patt['pattern']='ONNECK - On-Neck Pattern'
    gs = abstract.CDLONNECK(data)
    data['CDLONNECK']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLONNECK"]].copy()
    data2crows['Signal'] = data2crows['CDLONNECK'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLONNECK'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLONNECK']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[48]:
    
    
    #CDLPIERCING - Piercing Pattern
    patt={}
    patt['pattern']='PIERCING - Piercing Pattern'
    gs = abstract.CDLPIERCING(data)
    data['CDLPIERCING']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLPIERCING"]].copy()
    data2crows['Signal'] = data2crows['CDLPIERCING'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLPIERCING'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLPIERCING']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[49]:
    
    
    #CDLRICKSHAWMAN - Rickshaw Man
    patt={}
    patt['pattern']='RICKSHAWMAN - Rickshaw Man'
    gs = abstract.CDLRICKSHAWMAN(data)
    data['CDLRICKSHAWMAN']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLRICKSHAWMAN"]].copy()
    data2crows['Signal'] = data2crows['CDLRICKSHAWMAN'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLRICKSHAWMAN'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLRICKSHAWMAN']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[50]:
    
    
    #CDLRISEFALL3METHODS - Rising/Falling Three Methods
    patt={}
    patt['pattern']='RISEFALL3METHODS - Rising/Falling Three Methods'
    gs = abstract.CDLRISEFALL3METHODS(data)
    data['CDLRISEFALL3METHODS']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLRISEFALL3METHODS"]].copy()
    data2crows['Signal'] = data2crows['CDLRISEFALL3METHODS'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLRISEFALL3METHODS'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLRISEFALL3METHODS']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[51]:
    
    
    #CDLSEPARATINGLINES - Separating Lines
    patt={}
    patt['pattern']='SEPARATINGLINES - Separating Lines'
    gs = abstract.CDLSEPARATINGLINES(data)
    data['CDLSEPARATINGLINES']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLSEPARATINGLINES"]].copy()
    data2crows['Signal'] = data2crows['CDLSEPARATINGLINES'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLSEPARATINGLINES'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLSEPARATINGLINES']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[52]:
    
    
    #CDLSHOOTINGSTAR - Shooting Star
    patt={}
    patt['pattern']='SHOOTINGSTAR - Shooting Star'
    gs = abstract.CDLSHOOTINGSTAR(data)
    data['CDLSHOOTINGSTAR']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLSHOOTINGSTAR"]].copy()
    data2crows['Signal'] = data2crows['CDLSHOOTINGSTAR'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLSHOOTINGSTAR'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLSHOOTINGSTAR']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[53]:
    
    
    #CDLSHORTLINE - Short Line Candle
    patt={}
    patt['pattern']='SHORTLINE - Short Line Candle'
    gs = abstract.CDLSHORTLINE(data)
    data['CDLSHORTLINE']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLSHORTLINE"]].copy()
    data2crows['Signal'] = data2crows['CDLSHORTLINE'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLSHORTLINE'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLSHORTLINE']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[54]:
    
    
    #CDLSPINNINGTOP - Spinning Top
    patt={}
    patt['pattern']='SPINNINGTOP - Spinning Top'
    gs = abstract.CDLSPINNINGTOP(data)
    data['CDLSPINNINGTOP']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLSPINNINGTOP"]].copy()
    data2crows['Signal'] = data2crows['CDLSPINNINGTOP'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLSPINNINGTOP'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLSPINNINGTOP']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[55]:
    
    
    #CDLSTALLEDPATTERN - Stalled Pattern
    patt={}
    patt['pattern']='STALLEDPATTERN - Stalled Pattern'
    gs = abstract.CDLSTALLEDPATTERN(data)
    data['CDLSTALLEDPATTERN']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLSTALLEDPATTERN"]].copy()
    data2crows['Signal'] = data2crows['CDLSTALLEDPATTERN'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLSTALLEDPATTERN'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLSTALLEDPATTERN']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[56]:
    
    
    #CDLSTICKSANDWICH - Stick Sandwich
    patt={}
    patt['pattern']='STICKSANDWICH - Stick Sandwich'
    gs = abstract.CDLSTICKSANDWICH(data)
    data['CDLSTICKSANDWICH']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLSTICKSANDWICH"]].copy()
    data2crows['Signal'] = data2crows['CDLSTICKSANDWICH'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLSTICKSANDWICH'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLSTICKSANDWICH']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[57]:
    
    
    #CDLTAKURI - Takuri (Dragonfly Doji with very long lower shadow)
    patt={}
    patt['pattern']='TAKURI - Takuri (Dragonfly Doji with very long lower shadow)'
    gs = abstract.CDLTAKURI(data)
    data['CDLTAKURI']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLTAKURI"]].copy()
    data2crows['Signal'] = data2crows['CDLTAKURI'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLTAKURI'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLTAKURI']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[58]:
    
    
    #CDLTASUKIGAP - Tasuki Gap
    patt={}
    patt['pattern']='TASUKIGAP - Tasuki Gap'
    gs = abstract.CDLTASUKIGAP(data)
    data['CDLTASUKIGAP']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLTASUKIGAP"]].copy()
    data2crows['Signal'] = data2crows['CDLTASUKIGAP'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLTASUKIGAP'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLTASUKIGAP']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[59]:
    
    
    #CDLTHRUSTING - Thrusting Pattern
    patt={}
    patt['pattern']='THRUSTING - Thrusting Pattern'
    gs = abstract.CDLTHRUSTING(data)
    data['CDLTHRUSTING']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLTHRUSTING"]].copy()
    data2crows['Signal'] = data2crows['CDLTHRUSTING'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLTHRUSTING'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLTHRUSTING']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[60]:
    
    
    #CDLTRISTAR - Tristar Pattern
    patt={}
    patt['pattern']='TRISTAR - Tristar Pattern'
    gs = abstract.CDLTRISTAR(data)
    data['CDLTRISTAR']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLTRISTAR"]].copy()
    data2crows['Signal'] = data2crows['CDLTRISTAR'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLTRISTAR'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLTRISTAR']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[61]:
    
    
    #CDLUNIQUE3RIVER - Unique 3 River
    patt={}
    patt['pattern']='UNIQUE3RIVER - Unique 3 River'
    gs = abstract.CDLUNIQUE3RIVER(data)
    data['CDLUNIQUE3RIVER']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLUNIQUE3RIVER"]].copy()
    data2crows['Signal'] = data2crows['CDLUNIQUE3RIVER'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLUNIQUE3RIVER'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLUNIQUE3RIVER']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[62]:
    
    
    #CDLUPSIDEGAP2CROWS - Upside Gap Two Crows
    patt={}
    patt['pattern']='UPSIDEGAP2CROWS - Upside Gap Two Crows'
    gs = abstract.CDLUPSIDEGAP2CROWS(data)
    data['CDLUPSIDEGAP2CROWS']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLUPSIDEGAP2CROWS"]].copy()
    data2crows['Signal'] = data2crows['CDLUPSIDEGAP2CROWS'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLUPSIDEGAP2CROWS'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLUPSIDEGAP2CROWS']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[63]:
    
    
    #CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods
    patt={}
    patt['pattern']='XSIDEGAP3METHODS - Upside/Downside Gap Three Methods'
    gs = abstract.CDLXSIDEGAP3METHODS(data)
    data['CDLXSIDEGAP3METHODS']=gs
    data2crows=data.copy()
    data2crows.reset_index(inplace= True )
    data2crows.reset_index(inplace= True )
    data2crows.applymap(str)
    data2crows=data2crows[["index","Datetime","CDLXSIDEGAP3METHODS"]].copy()
    data2crows['Signal'] = data2crows['CDLXSIDEGAP3METHODS'].map(getSignal)
    gm=gs[gs !=0]
    dataarr=[]
    if len(gm)>0:
        data2crows=data2crows.loc[data2crows['CDLXSIDEGAP3METHODS'] != 0]
        dataarr=data2crows.to_dict('records')
    patternslist['CDLXSIDEGAP3METHODS']=dataarr
    patt['data']=dataarr
    patterndata.append(patt)
    
    
    # In[68]:
    
    
    result = jsonify(patterndata)
    return result

@app.route('/netpredict')
def netpredict():
    MA_PERIOD = 15
    tickerhistory = yf.Ticker('BTC-USD')
    data=tickerhistory.history(period='10y',interval='1d')
    data.rename(columns={'Open':'open','High':'high','Low':'low','Close':'close'},inplace=True)
    prices = pd.DataFrame(data,columns=['time', 'close']).set_index('time')
    prices.index = pd.to_datetime(prices.index, unit='s')
    prices = prices.dropna()
    ratesM = prices.rolling(MA_PERIOD).mean()
    ratesD = prices - ratesM
    for i in range(15):
            prices[str(i)] = ratesD.shift(i)
    prices=prices.dropna()
    labels = []
    dataset=prices
   
    for i in range(dataset.shape[0]-15):
        rand = random.randint(10, 15)
        if dataset['close'][i] >= (dataset['close'][i + rand]):
            labels.append(1.0)
        elif dataset['close'][i] <= (dataset['close'][i + rand]):
            labels.append(0.0)              
        else:
            labels.append(0.0)
    dataset = dataset.iloc[:len(labels)].copy()
    dataset['labels'] = labels
    dataset = dataset.dropna()
    pr=dataset
    X = pr[pr.columns[1:-1]]
    model = CatBoostClassifier()
    model.load_model("catboost_model")
    p = model.predict_proba(X)
    print(p)
    p2 = [x[0]<0.5 for x in p]
    netsig={}
    netsig["signal"]=getsignet(p2[len(p2)-1])
    result = jsonify(netsig)
    return result

if __name__ == "__main__":
    app.run()