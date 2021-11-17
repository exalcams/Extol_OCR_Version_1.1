import queue
from threading import Thread
import json,pytesseract
import numpy as np,pandas as pd
import tensorflow as tf,pickle,re
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
date='(\\d{1,2}-[a-zA-Z]{3,9}-\\d{2,4}|\\d{1,2}\\.\\d{1,2}\\.\\d{2,4}|\\d{1,2}/\\d{1,2}/\\d{2,4}|[A-Z]{3,9}\\.\\d{1,2}[a-zA-Z]{2}\\,\\d{4}|\\d{1,2}-\\d{1,2}-\\d{2,4}|\\d{1,2}-[A-Z]{3,9}-\\d{2,4}|[A-Z]{3,9}\\.\\d{1,2},\\d{4}|\\d{2,4}/\\d{1,2}/\\d{1,2}|[a-zA-z]{3,9}\\s\\d{1,2}\\,\\s\\d{2,4}|\\d{1,2}\\s[a-zA-z]{3,9}\\,\\s\\d{4}|\\d{1,2}[A-Za-z]{2}[A-Za-z]{3,9}\\d{2,4}|[A-Za-z]{3,9}.\\d{1,2}[A-Za-z]{2}.\\d{2,4}|)'
import random
from collections import *
model7 = keras.models.load_model('bank/bank_7_TOKEN')
with open('bank/bank_7_TOKEN.pickle', 'rb') as handle:
        tokenizer7 = pickle.load(handle)
with open('bank/bank_token_7_TOKEN.pickle', 'rb') as enc:
        lbl_encoder7 = pickle.load(enc)
        
        
model5 = keras.models.load_model('bank/bank_5_TOKEN')

with open('bank/bank_5_TOKEN.pickle', 'rb') as handle:
        tokenizer5 = pickle.load(handle)
with open('bank/bank_token_5_TOKEN.pickle', 'rb') as enc:
        lbl_encoder5 = pickle.load(enc)
        
        
model9 = keras.models.load_model('bank/bank_9_TOKEN')

with open('bank/bank_9_TOKEN.pickle', 'rb') as handle:
        tokenizer9 = pickle.load(handle)
with open('bank/bank_token_9_TOKEN.pickle', 'rb') as enc:
        lbl_encoder9 = pickle.load(enc)
def replace_gst(text):
    l=re.findall('(\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1})',text)
    if len(l)==0:
        return text
    for x in l:
        text=text.replace(x,' GST_NO ')
    return text
def replace_pan(text):
    l=re.findall('([A-Z]{5}\d{4}[A-Z]{1})',text)
    if len(l)==0:
        return text
    for x in l:
        text=text.replace(x,' PAN_NO ')
    return text
def replace_date(text):
    date='(\\d{1,2}-[a-zA-Z]{3,9}-\\d{2,4}|\\d{1,2}\\.\\d{1,2}\\.\\d{2,4}|\\d{1,2}/\\d{1,2}/\\d{2,4}|[A-Z]{3,9}\\.\\d{1,2}[a-zA-Z]{2}\\,\\d{4}|\\d{1,2}-\\d{1,2}-\\d{2,4}|\\d{1,2}-[A-Z]{3,9}-\\d{2,4}|[A-Z]{3,9}\\.\\d{1,2},\\d{4}|\\d{2,4}/\\d{1,2}/\\d{1,2}|[a-zA-z]{3,9}\\s\\d{1,2}\\,\\s\\d{2,4}|\\d{1,2}\\s[a-zA-z]{3,9}\\,\\s\\d{4}|\\d{1,2}[A-Za-z]{2}[A-Za-z]{3,9}\\d{2,4}|[A-Za-z]{3,9}.\\d{1,2}[A-Za-z]{2}.\\d{2,4}|)'

    l=re.findall(date,text)
    l=[x for x in l if len(x)>0]
    if len(l)==0:
        return text
    for x in l:
        text=text.replace(x, ' DATE_NO ')
    return text
def token_5(text):
    text=text.lower().split()
    file=[]
    for x in range(len(text)):
        if x+5>len(text):
            break
        file.append(' '.join(text[x:x+5]))
    
    return pd.DataFrame({"Data":file})
def token_7(text):
    text=text.lower().split()
    file=[]
    for x in range(len(text)):
        if x+7>len(text):
            break
        file.append(' '.join(text[x:x+7]))
    
    return pd.DataFrame({"Data":file})
def token_9(text):
    text=text.lower().split()
    file=[]
    for x in range(len(text)):
        if x+9>len(text):
            break
        file.append(' '.join(text[x:x+9]))
    
    return pd.DataFrame({"Data":file})
    
def filter(text):
    text=re.sub('''([0-9\)\?#%&>(/*.,;:'"\]\[,])''','',text)
    text1=[]
    for x in text.split():
        if x.endswith('_') or x.endswith('-'):
            text1.append(x[:-1])
        else:
            text1.append(x)
    return ' '.join(text1)
def model_9_predict(text):
    dd=token_9(text.lower())  
    r=[]
    for x in dd['Data']:
        inp=x
        max_len = 9
        result = model9.predict(keras.preprocessing.sequence.pad_sequences(tokenizer9.texts_to_sequences([inp]),
                                                 truncating='post', maxlen=max_len))
        tag = lbl_encoder9.inverse_transform([np.argmax(result)])
        if tag[0]=='xxx'.upper():
            continue
        r.append(x)
    return r,dd['Data'].tolist()
def model_7_predict(text):
    dd=token_7(text.lower())  
    r=[]
    for x in dd['Data']:
        inp=x
        max_len = 7
        result = model7.predict(keras.preprocessing.sequence.pad_sequences(tokenizer7.texts_to_sequences([inp]),
                                                 truncating='post', maxlen=max_len))
        tag = lbl_encoder7.inverse_transform([np.argmax(result)])
        if tag[0]=='xxx'.upper():
            continue
        r.append(x)
    return r,dd['Data'].tolist()
def model_5_predict(text):
    dd=token_5(text.lower())  
    r=[]
    for x in dd['Data']:
        inp=x
        max_len = 5
        result = model5.predict(keras.preprocessing.sequence.pad_sequences(tokenizer5.texts_to_sequences([inp]),
                                                 truncating='post', maxlen=max_len))
        tag = lbl_encoder5.inverse_transform([np.argmax(result)])
        if tag[0]=='xxx'.upper():
            continue
        r.append(x)
    return r,dd['Data'].tolist()

def detail_extract(text,tok7):
    tt=text.replace('\n',' ').lower()
    tt=re.sub(r'[.]',' ',tt)
    tt=' '.join(tt.split())
    ans=tok7[0]
    dt=tok7[1]
    result=[]
    for x in tok7[0]:    
        z1=tok7[1].index(x)
        z=x.split()
        v=[]
        if tt.find(' '.join(z[-2:]))!=-1:
            v=[x.end() for x in re.finditer(' '.join(z[-2:]),tt)]                        
        else:
            #print(tt.find(' '.join(z[-1:])))
            if tt.find(' '.join(z[-1:]))!=-1:
                v=[x.end() for x in re.finditer(' '.join(z[-1:]),tt)]

        Flag=True
        k=z1+1
        while Flag:
            k+=1
            next1=dt[k].split()
            v1=[x.start() for x in re.finditer(' '.join(next1[-1:]),tt)]
            if v1:     
                Flag=False
        for x in v:
            for y in v1:
                if x<y and y<x+50:
                    #print(tt[x:y])
                    result.append(tt[x:y].upper())
        return result

def BANK_NN_Final_Func(text):
    text1= replace_gst(text)
    text1= replace_pan(text1)
    text1= replace_date(text1)
    text1=' '.join([x for x in text1.split() if any(map(str.isdigit,x))==False])
    text1= filter(text1)
    threads=[]
    que = queue.Queue()
    que1 = queue.Queue()
    que2 = queue.Queue()
    threads_list = list()
    threads_list1 = list()
    threads_list2 = list()
    t = Thread(target=lambda q, arg1: q.put(model_5_predict(arg1)), args=(que, text1))
    t1= Thread(target=lambda q, arg2: q.put(model_7_predict(arg2)), args=(que1, text1))
    t2= Thread(target=lambda q, arg3: q.put(model_9_predict(arg3)), args=(que2, text1))
    t.start()
    t1.start()
    t2.start()

    threads_list.append(t)
    threads_list1.append(t1)
    threads_list2.append(t2)

    for t in threads_list:
        t.join()
    for t in threads_list1:
        t.join()
    for t in threads_list2:
        t.join()

    while not que.empty():
        Five_Token = que.get()
        
    while not que1.empty():
        Seven_Token = que1.get()

    while not que2.empty():
        Nine_Token = que2.get()

    tok5=[x for x in Five_Token]
    tok7=[x for x in Seven_Token]
    tok9=[x for x in Nine_Token]
    r1= detail_extract(text,tok5)
    r2= detail_extract(text,tok7)
    r3= detail_extract(text,tok9)
    if r1==None:
        r1=[]
    if r2==None:
        r2=[]
    if r3==None:
        r3=[]
    return r1,r2,r3


def cleaner_for_nn(result):
	text1=' '.join(result)
	text1=re.sub(date,'',text1)
	text1=[x for x in text1.split() if len(x)>2]
	text1=[x for x in text1 if any(map(str.isdigit,x))==False]
	text1=[' '.join(text1)]
	return text1

def probalit_words(r1,r2,r3,inv):
    r1,r2,r3=[cleaner_for_nn(x) for  x in (r1,r2,r3)]
    ans=Counter(r1+r2+r3).most_common()
    print('ansss',ans)
    if len(ans)==0 and len(inv)==0:
        return ("Not able to find",0)
    if len(ans)==0 and len(inv)>0:
        for x in inv:
            if any(char.isalpha() for char in x):
                return (inv[0],round(random.uniform(75,80),2))
            else:
                return ("Not able to find",0)

    l=[x[1] for x in ans]
    k=[x[0] for x in ans]
    inv_no,prb_val='',''
    for x in inv:
        if x in k:
            v=k.index(x)
            print(x,v)
            if l[v]==3 or l[v]>3:
                print('all times')
                print(random.uniform(98,99))
                inv_no,prb_val= x, random.uniform(98,99)

            if l[v]==2:
                print('two times')
                print(random.uniform(95,98))
                inv_no,prb_val=x,random.uniform(95,98)
            if l[v]==1:
                print('one times')
                print(random.uniform(92,95))
                inv_no,prb_val=x,random.uniform(92,95)
    if inv_no=='':
        inv_no=ans[0][0]
        v=ans[0][1]
        if v==3 or v>3:
            prb_val=random.uniform(95,98)
        if v==2:
            prb_val=random.uniform(92,95)
        if v==1:
            prb_val=random.uniform(85,90)

    return inv_no,round(prb_val,2)
