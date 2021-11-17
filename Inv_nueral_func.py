import queue
from threading import Thread
import json 
import numpy as np,pandas as pd
import tensorflow as tf,pickle,re
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

date='(\\d{1,2}-[a-zA-Z]{3,9}-\\d{2,4}|\\d{1,2}\\.\\d{1,2}\\.\\d{2,4}|\\d{1,2}/\\d{1,2}/\\d{2,4}|[A-Z]{3,9}\\.\\d{1,2}[a-zA-Z]{2}\\,\\d{4}|\\d{1,2}-\\d{1,2}-\\d{2,4}|\\d{1,2}-[A-Z]{3,9}-\\d{2,4}|[A-Z]{3,9}\\.\\d{1,2},\\d{4}|\\d{2,4}/\\d{1,2}/\\d{1,2}|[a-zA-z]{3,9}\\s\\d{1,2}\\,\\s\\d{2,4}|\\d{1,2}\\s[a-zA-z]{3,9}\\,\\s\\d{4}|\\d{1,2}[A-Za-z]{2}[A-Za-z]{3,9}\\d{2,4}|[A-Za-z]{3,9}.\\d{1,2}[A-Za-z]{2}.\\d{2,4}|)'

model7 = keras.models.load_model('model/invoice_7_TOKEN')
with open('model/inv_7_TOKEN.pickle', 'rb') as handle:
        tokenizer7 = pickle.load(handle)
with open('model/inv_token_7_TOKEN.pickle', 'rb') as enc:
        lbl_encoder7 = pickle.load(enc)
        
        
model5 = keras.models.load_model('model/invoice_5_TOKEN')

with open('model/inv_5_TOKEN.pickle', 'rb') as handle:
        tokenizer5 = pickle.load(handle)
with open('model/inv_token_5_TOKEN.pickle', 'rb') as enc:
        lbl_encoder5 = pickle.load(enc)
        
        
model9 = keras.models.load_model('model/invoice_9_TOKEN')

with open('model/inv_9_TOKEN.pickle', 'rb') as handle:
        tokenizer9 = pickle.load(handle)
with open('model/inv_token_9_TOKEN.pickle', 'rb') as enc:
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
    text=re.sub('''([0-9\)\?+#%&>(/*.,;:'"\]\[,])''','',text)
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

def detail_extract(text,tok):
    text=text.lower()
    final_ans=[]
    indlist=[tok[1].index(x) for x in tok[0]]
    
    end=[]
    for x in tok[0]:
        ind=tok[1].index(x)
        stind=ind
        end=''
        if ind-1 in indlist:
            continue
        Flag=True
        while Flag:
            ind+=1
            if ind in indlist:
                continue
            endind=ind
            Flag=False
        s_token=tok[1][stind].split()        
        
        end_text=tok[1][endind].split()[-1]
        f_token,sec_token=s_token[0],s_token[1]
        
        if text.find(f_token)==-1:
            f_token,sec_token=s_token[1],s_token[2]
        if text.find(sec_token)==-1:
            sec_token=s_token[2]
        if f_token==sec_token:
            sec_token=s_token[s_token.index(sec_token)+1]
        if text.find(end_text)==-1:
            end_text=tok[1][endind].split()[-2]
        if end_text==s_token:
            end_text=tok[1][endind+1].split()[-1]
            if text.find(end_text)==-1:
                end_text=tok[1][endind+2].split()[-1]
                
        f1,f2,e1=[],[],[]
        for x in re.finditer(f_token,text):    
            f1.append(x.start())
        for x in re.finditer(sec_token,text):
            f2.append(x.start())
        for y in re.finditer(end_text,text):    
            e1.append(y.start())    
        v=[x for x in f1 for y in f2 if x<y]
        v=list(dict.fromkeys(v))
        cors=[(x,y) for x in v for y in e1 if x<y]
        dd=[text[x[0]:x[1]] for x in cors]   
        j=[y for x in dd for y in dd if (x!=y and x in y)]
        ans=[x for x in dd if x not in j ]
        final_ans.extend(ans)
    return final_ans


def INV_NN_Final_Func(text):
    text1=text.lower()
    # text1= replace_gst(text)
    # text1= replace_pan(text1)
    # text1= replace_date(text1)
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