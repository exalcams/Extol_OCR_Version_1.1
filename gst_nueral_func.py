import queue,openpyxl
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
import re
import difflib
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random
from collections import *

df_li_gstname=pd.read_excel(r'./OCR-M/LIST_Name_GST.xlsx',engine='openpyxl')
df_li_gstname.fillna('NO MATCH',inplace=True)

date='(\\d{1,2}-[a-zA-Z]{3,9}-\\d{2,4}|\\d{1,2}\\.\\d{1,2}\\.\\d{2,4}|\\d{1,2}/\\d{1,2}/\\d{2,4}|[A-Z]{3,9}\\.\\d{1,2}[a-zA-Z]{2}\\,\\d{4}|\\d{1,2}-\\d{1,2}-\\d{2,4}|\\d{1,2}-[A-Z]{3,9}-\\d{2,4}|[A-Z]{3,9}\\.\\d{1,2},\\d{4}|\\d{2,4}/\\d{1,2}/\\d{1,2}|[a-zA-z]{3,9}\\s\\d{1,2}\\,\\s\\d{2,4}|\\d{1,2}\\s[a-zA-z]{3,9}\\,\\s\\d{4}|\\d{1,2}[A-Za-z]{2}[A-Za-z]{3,9}\\d{2,4}|[A-Za-z]{3,9}.\\d{1,2}[A-Za-z]{2}.\\d{2,4}|)'

model7 = keras.models.load_model('GST_NO/gst_7_TOKEN')
with open('GST_NO/gst_7_TOKEN.pickle', 'rb') as handle:
        tokenizer7 = pickle.load(handle)
with open('GST_NO/gst_token_7_TOKEN.pickle', 'rb') as enc:
        lbl_encoder7 = pickle.load(enc)
        
        
model5 = keras.models.load_model('GST_NO/gst_5_TOKEN')

with open('GST_NO/gst_5_TOKEN.pickle', 'rb') as handle:
        tokenizer5 = pickle.load(handle)
with open('GST_NO/gst_token_5_TOKEN.pickle', 'rb') as enc:
        lbl_encoder5 = pickle.load(enc)
        
        
model9 = keras.models.load_model('GST_NO/gst_9_TOKEN')

with open('GST_NO/gst_9_TOKEN.pickle', 'rb') as handle:
        tokenizer9 = pickle.load(handle)
with open('GST_NO/gst_token_9_TOKEN.pickle', 'rb') as enc:
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

def GST_Correction(GSTdict):
    ANConvert={"i":"1","l":"1","I":"1","o":"0","O":"0","Z":"2","B":"8","T":"7","G":"6","S":"5"}
    ANConvert1={"Z":"7"}
    NAConvert={"1":"I","2":"Z","0":"O","7":"T","5":"S","8":"B","6":"G"}
    gslst=[]
    print(GSTdict)
    for pat in GSTdict:
        for GST in GSTdict[pat]:
            stcode,pan,entcode=GST[:2],GST[2:12],GST[12:]
            print("splt",stcode,pan,entcode)
            p=''
            for x in stcode:
                if x.isdigit():
                    p+=x
                else:
                    if x not in ANConvert.keys():
                        p+=x
                        continue
                    p+= ANConvert[x]

            for x in pan[:5]:
                if x.isalpha():
                    p+=x
                else:
                    if x not in NAConvert.keys():
                        p+=x
                        continue
                    p+=NAConvert[x]
            for x in pan[5:-1]:
                if x.isdigit():
                    p+=x
                else:
                    if x not in ANConvert.keys():
                        p+=x
                        continue
                    p+=ANConvert[x]    
            for x in pan[-1:]:
                if x.isalpha():
                    p+=x
                else:
                    if x not in NAConvert.keys():
                        p+=x
                        continue
                    p+=NAConvert[x] 
                    
            if pat[12:][0]=='N':
                if entcode[0].isdigit():
                    p+=entcode[0]
                else:
                    if entcode[0] not in ANConvert.keys():
                        p+=entcode[0]
                        continue
                    p+=NAConvert[x] 
            if pat[12:][0]=='A':
                if entcode[0].isalpha():
                    p+=entcode[0]
                else:
                    if entcode[0] not in NAConvert.keys():
                        p+=entcode[0]
                        continue
                    p+=NAConvert[x] 
            if pat[12:][1]=='A':
                if entcode[1].isalpha():
                    p+=entcode[1]
                else:
                    if entcode[1] not in NAConvert.keys():
                        p+=entcode[1]
                        continue
                    p+=NAConvert[x] 
            if pat[12:][2]=='A':
                if entcode[2].isalpha():
                    p+=entcode[2]
                else:
                    if entcode[2] not in NAConvert.keys():
                        p+=entcode[2]
                        continue
                    p+=NAConvert[x] 
            if pat[12:][2]=='N':
                if entcode[2].isdigit():
                    p+=entcode[2]
                else:
                    if entcode[2] not in ANConvert.keys():
                        p+=entcode[2]
                        continue
                    p+=NAConvert[x]

            gslst.append(p)
    gslst=[x for x in dict.fromkeys(gslst)]
    return gslst

def seq_gst_match(sample_gst):
    matcher=["NNAAAAANNNNANAN","NNAAAAANNNNANAA","NNAAAAANNNNAAAN"]
    dd=dict()
    for x in sample_gst:
        v=re.sub('[A-Z]','A',x)
        v=re.sub('[0-9]','N',v)
        dd[x]=v
    valuse=[]
    for x in matcher:
        valuse.extend(difflib.get_close_matches(x,[dd[x] for x in dd],cutoff=.7,n=3))
    ans=[]
    vv=dict()
    for x in dd:
        if dd[x] in valuse:
            ans.append(x)
            print(x,'\t',max(difflib.SequenceMatcher(None, dd[x], match).ratio() for match in matcher))
            if dd[x] in vv:
                vv[dd[x]].append(x)
            else:
                vv[dd[x]]=[x]

    return ans,vv
    
def GST_Extraction(txt):
    Finalpattern='(\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[A-Z]{1}[A-Z\d]{1})'
    Statelist=[x for x in range(1,39)]
    Statelist.extend([97])
    GST=dict()
    LGST=[]
    FGST=[]
    s=1
    arrGST=[]
    for x in txt:
        arrGST.extend(re.findall('([A-Z\d]{15})',x))
    print(arrGST)
    GSTlist,GSTdict=seq_gst_match(arrGST)
    GST=GST_Correction(GSTdict)
    for x in GST:
        if x in df_li_gstname['Client_GST'].to_list():
            GST.remove(x)
    for x in GST:
        if 'AAACS8598L' in x:
            GST.remove(x)
    for x in GST:
        LGST.extend(re.findall(Finalpattern,x))
    for x in LGST:
        if int(x[:2]) not in Statelist:
            LGST.remove(x)
    LGST=[x for x in dict.fromkeys(LGST)]
    for x in LGST:
        for y in df_li_gstname['GSTIN'].to_list():
            if x==y:
                FGST.append(x)
            else:
                pass
    if len(FGST)>0:
        print("GST-FINAL",FGST)  
        return FGST
    else:
        print("GST-FINAL",LGST)  
        return LGST

def GST_NN_Final_Func(text):
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
	text1=' '.join(result)
	text1=re.sub(date,'',text1)
	text1=[x for x in text1.split() if len(x)>10]
	text1=[x for x in text1 if any(map(str.isdigit,x))==True]
	return text1

def cleaner_for_nn(result):
    date='(\\d{1,2}-[a-zA-Z]{3,9}-\\d{2,4}|\\d{1,2}\\.\\d{1,2}\\.\\d{2,4}|\\d{1,2}/\\d{1,2}/\\d{2,4}|[A-Z]{3,9}\\.\\d{1,2}[a-zA-Z]{2}\\,\\d{4}|\\d{1,2}-\\d{1,2}-\\d{2,4}|\\d{1,2}-[A-Z]{3,9}-\\d{2,4}|[A-Z]{3,9}\\.\\d{1,2},\\d{4}|\\d{2,4}/\\d{1,2}/\\d{1,2}|[a-zA-z]{3,9}\\s\\d{1,2}\\,\\s\\d{2,4}|\\d{1,2}\\s[a-zA-z]{3,9}\\,\\s\\d{4}|\\d{1,2}[A-Za-z]{2}[A-Za-z]{3,9}\\d{2,4}|[A-Za-z]{3,9}.\\d{1,2}[A-Za-z]{2}.\\d{2,4}|)'
    text1=' '.join(result)
    text1=re.sub(date,'',text1)
    text1=[x for x in text1.split() if len(x)==15]
    text1=[x for x in text1 if any(map(str.isdigit,x))==True]
    return text1

def probalit_words(r2,r3,inv):
    Finalpattern='(\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[A-Z]{1}[A-Z\d]{1})'
    Statelist=[x for x in range(1,39)]
    Statelist.extend([97])
    r2,r3=[cleaner_for_nn(x) for  x in (r2,r3)]
    ans=Counter(r2+r3).most_common()
    print('GSTansss',ans) 
    if len(ans)==0 and inv[0]=='Not Found':
        return ("Not Found",0)
    if len(ans)==0 and inv[0]!='Not Found':
        LGST=[]
        FGST=[]
        GSTlist,GSTdict=seq_gst_match(inv)
        GST=GST_Correction(GSTdict)
        for x in GST:
            if x in df_li_gstname['Client_GST'].to_list():
                GST.remove(x)
        for x in GST:
            if 'AAACS8598L' in x:
                GST.remove(x)
        for x in GST:
            LGST.extend(re.findall(Finalpattern,x))
        for x in LGST:
            if int(x[:2]) not in Statelist:
                LGST.remove(x)
        LGST=[x for x in dict.fromkeys(LGST)]
        vendgstlist=[]
        for x in df_li_gstname['GSTIN'].to_list():
            if len(x)==15:
                vendgstlist.append(x)
        for gstg in LGST:
            a=process.extractOne(gstg,vendgstlist)
            if len(a)>0:
                print(a)
                if a[1]>85:
                    FGST.append(a[0])
        print("FGST",FGST)
        if len(FGST)>0:
            return(FGST[0],round(random.uniform(95,98),2))
        else:
            return(inv[0],round(random.uniform(75,80),2))
    
    if len(ans)>0 and inv[0]=='Not Found':
        return('Not Found',0)
    
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
                print(random.uniform(92,96))
                inv_no,prb_val=x,random.uniform(92,96)
    if inv_no=='':
        arGsT=[]
        LGST=[]
        FGST=[]
        try:
            for gsta in ans:
                arGsT.append(gsta[0])
        except:
            pass
        if len(arGsT)>0:
            GSTlist,GSTdict=seq_gst_match(arGsT)
            GST=GST_Correction(GSTdict)
            for x in GST:
                if x in df_li_gstname['Client_GST'].to_list():
                    GST.remove(x)
            for x in GST:
                if 'AAACS8598L' in x:
                    GST.remove(x)
            for x in GST:
                LGST.extend(re.findall(Finalpattern,x))
            for x in LGST:
                if int(x[:2]) not in Statelist:
                    LGST.remove(x)
            LGST=[x for x in dict.fromkeys(LGST)]
            vendgstlist=[]
            for x in df_li_gstname['GSTIN'].to_list():
                if len(x)==15:
                    vendgstlist.append(x)
            for gstg in LGST:
                a=process.extractOne(gstg,vendgstlist)
                if len(a)>0:
                    print(a)
                    if a[1]>85:
                        FGST.append(a[0])
            print("FGST",FGST)
            if len(FGST)>0:
                return(FGST[0],round(random.uniform(95,98),2))
            else:
                return(inv[0],round(random.uniform(75,80),2))
    else:
        return(inv_no,round(prb_val,2))
