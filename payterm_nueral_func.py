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
model7 = keras.models.load_model('pay_term/pay_term_7_TOKEN')
with open('pay_term/pay_term_7_TOKEN.pickle', 'rb') as handle:
        tokenizer7 = pickle.load(handle)
with open('pay_term/pay_term_token_7_TOKEN.pickle', 'rb') as enc:
        lbl_encoder7 = pickle.load(enc)
        
        
model5 = keras.models.load_model('pay_term/pay_term_5_TOKEN')

with open('pay_term/pay_term_5_TOKEN.pickle', 'rb') as handle:
        tokenizer5 = pickle.load(handle)
with open('pay_term/pay_term_token_5_TOKEN.pickle', 'rb') as enc:
        lbl_encoder5 = pickle.load(enc)
        
        
model9 = keras.models.load_model('pay_term/pay_term_9_TOKEN')

with open('pay_term/pay_term_9_TOKEN.pickle', 'rb') as handle:
        tokenizer9 = pickle.load(handle)
with open('pay_term/pay_term_token_9_TOKEN.pickle', 'rb') as enc:
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
    ans=tok7[0]
    dt=tok7[1]
    result=[]
    ans=[]
    for x in tok7[0]:
        z1=tok7[1].index(x)+1
        next_token=tok7[1][z1].split()
        token=x.split()
        v=[]
        v_end=[]
        v1=[]
      
        if tt.find(token[-1])!=-1:
            v.extend([x.start() for x in re.finditer(token[-1],tt)])
            v_end.extend([x.end() for x in re.finditer(token[-1],tt)])
        elif tt.find(token[-2])!=-1:
            v.extend([x.start() for x in re.finditer(token[-2],tt)])
        else:
            v.extend([x.start() for x in re.finditer(token[-3],tt)])

        if tt.find(next_token[-1])!=-1:
            v1.extend([x.end() for x in re.finditer(next_token[-1],tt)])
        elif tok7[1][z1+1].split()[-1]!=-1:
            v1.extend([x.end() for x in re.finditer(tok7[1][z1+1].split()[-1],tt)])
        elif tok7[1][z1+2].split()!=-1:
            v1.extend([x.end() for x in re.finditer(tok7[1][z1+1].split()[-1],tt)])   
        pairs=min([(x,y) for x in v for y in v1 if x<y])
        ans.append(tt[pairs[0]:pairs[1]])
    return ans


def PAYTM_NN_Final_Func(text):
    text1= replace_gst(text)
    text1= replace_pan(text1)
    text1= replace_date(text1)
    text1=' '.join([x for x in text1.split() if any(map(str.isdigit,x))==False])
    text1= filter(text1)
    threads=[]
    que1 = queue.Queue()
    que2 = queue.Queue()
    threads_list1 = list()
    threads_list2 = list()
    t1= Thread(target=lambda q, arg2: q.put(model_7_predict(arg2)), args=(que1, text1))
    t2= Thread(target=lambda q, arg3: q.put(model_9_predict(arg3)), args=(que2, text1))
    t1.start()
    t2.start()

    threads_list1.append(t1)
    threads_list2.append(t2)

    for t in threads_list1:
        t.join()
    for t in threads_list2:
        t.join()
        
    while not que1.empty():
        Seven_Token = que1.get()

    while not que2.empty():
        Nine_Token = que2.get()

    tok7=[x for x in Seven_Token]
    tok9=[x for x in Nine_Token]
    r2= detail_extract(text,tok7)
    r3= detail_extract(text,tok9)

    if r2==None:
        r2=[]
    if r3==None:
        r3=[]
    return r2,r3



def cleaner_for_nn(result):
    text1='\t'.join(result)
    text1=text1.split('\t')
    text2=[x for x in  text1 if 'day' in x.lower()]    
    return text2

def probalit_words(r2,r3,inv):
    r2,r3=[cleaner_for_nn(x) for  x in (r2,r3)]
    ans=Counter(r2+r3).most_common()
    print('ansss',ans)
    if len(ans)==0 and len(inv)==0:
        return ("Not Found",0)
    if len(ans)==0 and len(inv)>0:
        return (inv[0],random.uniform(75,80))
    l=[x[1] for x in ans]
    k=[x[0] for x in ans]
    inv_no,prb_val='',''
    for x in inv:
        if x in k:
            v=k.index(x)
            print(x,v)

            if l[v]==2 or l[v]>2:
                print('two times')
                print(random.uniform(97,99))
                inv_no,prb_val=x,random.uniform(97,99)
            if l[v]==1:
                print('one times')
                print(random.uniform(92,95))
                inv_no,prb_val=x,random.uniform(92,95)
    if inv_no=='':
        inv_no=ans[0][0]
        v=ans[0][1]
        if v==2 or v>2:
            prb_val=random.uniform(92,95)
        if v==1:
            prb_val=random.uniform(85,90)

    return inv_no,round(prb_val,2)
