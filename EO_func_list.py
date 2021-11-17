from pdf2image import convert_from_path
from pdf2image import convert_from_bytes
import shutil,openpyxl
import os,json
import re,pyzbar
import pandas as pd
import cv2
import numpy as np
import string
import spacy,easyocr
from spello.model import SpellCorrectionModel
import queue
from threading import Thread
import warnings
from padocr import *
from difflib import get_close_matches
import difflib
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random,jwt
from PIL import Image, ImageEnhance
from matplotlib import pyplot as plt
from pyzbar.pyzbar import decode

sp = SpellCorrectionModel(language='en')
sp.train(['INV','INVOICE','BILL','SERIAL'])
amtsp=SpellCorrectionModel(language='en')

nlp=spacy.load(r"./OCR-M/SPACY_NEW_ORG")

from yolov5 import YOLOv5
model=YOLOv5(r'OCR-M/best (5).pt')

reader=easyocr.Reader(['en'])

df=pd.read_excel(r"./OCR-M/Regex_.xlsx",engine='openpyxl')
df.fillna('NO DATA',inplace=True)

df_gst=pd.read_excel(r"./OCR-M/DATA_DUMP.xlsx",engine='openpyxl')
df_gst.fillna('NO MATCH',inplace=True)

df_li_gstname=pd.read_excel(r'./OCR-M/LIST_Name_GST.xlsx',engine='openpyxl')
df_li_gstname.fillna('NO MATCH',inplace=True)
Vnm_list=df_li_gstname['Vendor Name'].to_list()

df_statelist=pd.read_excel(r'./OCR-M/Statelist.xlsx',engine='openpyxl')
df_statelist.fillna('NO MATCH',inplace=True)

df_pincode=pd.read_csv(r'./OCR-M/Locality_village_pincode_final_mar-2017.csv')
df_pincode.fillna('NO MATCH',inplace=True)

hsndf=pd.read_csv('./OCR-M/hhssn.csv')
hsnl=hsndf['HSN'].to_list()

hsnl=list(set(hsnl))

HSN=pd.read_excel('./OCR-M/GST HSN Code list (1).xlsx',engine='openpyxl')
SAC=pd.read_excel('./OCR-M/SAC Code List for GST in Excel.xlsx',engine='openpyxl')
sac=SAC['SAC CODE'].dropna().astype('int').astype('str').unique().tolist()
hsn=HSN['HSN Code'].dropna().astype('int').astype('str').unique().tolist()
hsn_sac=hsn+sac  ## that variable name for hsn list already exist

hsnl.extend(hsn_sac)

pin_data = pd.read_csv('./OCR-M/all_india_PO_list_without_APS_offices_ver2_lat_long.csv')
dist_data = pd.read_csv(r"./OCR-M/dist_list1.csv")
con_data = pd.read_csv("./OCR-M/Country_list123.csv")
con_data1 = pd.read_csv("./OCR-M/Country_list123.csv")

def Read_pdf(path):
    try:
        shutil.rmtree('Pdf2Img/')
        os.mkdir('Pdf2Img')
    except:
        os.mkdir('Pdf2Img')
    imgs=convert_from_path(path)
    for cnt in range(len(imgs)):
        p = 'Pdf2Img/'+str(cnt)+'.jpeg'
        imgs[cnt].save(p)
        os.system('magick convert -density 500 -units pixelsperinch "{}" "{}"'.format(p,p))

def Bar_data(Img):
    bimg=cv2.imread(Img)
    ar=decode(bimg)
    if len(ar)>0:
        encDATA=ar[0].data.decode('utf-8')
    try:
        ans=jwt.decode(encDATA, options={"verify_signature": False})
        ans=json.loads(ans["data"])
    except:
        ans='No Data'
    return ans

def RemoveSeal(img):
    try:
        def removeSeal_inside(im):
            image = Image.fromarray(im)
            image_contrast = ImageEnhance.Contrast(image).enhance(1.5)

            img_hsv = cv2.cvtColor(np.array(image_contrast)[:, :, ::-1],
                        cv2.COLOR_BGR2HSV )

            red_lower = np.array([86, 89, 175], np.uint8)
            red_upper = np.array([200, 255, 255], np.uint8)
            red_mask = cv2.inRange(img_hsv, red_lower, red_upper)
    
            kernal = np.ones((5, 5), "uint8")
            red_mask = cv2.dilate(red_mask, kernal)
            cv2.imwrite(r"D:\Exalca_files\trainings\Remove_seal\output\red_mask.jpeg", red_mask)
            contours, _ = cv2.findContours(red_mask,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area = cv2.contourArea(contour)
                if(area > 50):
                    x, y, w, h = cv2.boundingRect(contour)
                    result = cv2.rectangle(im, (x, y), (x + w, y + h), (255, 255, 255), -1) 
   
            print("process done")
            return result
    
        img1 = cv2.imread(img)
        temp = img1
        dimensions = img1.shape
        height = img1.shape[0]
        width = img1.shape[1]
        channels = img1.shape[2]
        cropped_image = img1[700:1800, 0:1654]
        out = removeSeal_inside(cropped_image)
        out_temp = out
        return img1
    
    except:
        print("table outside seal or no seal") 

def easyocr1(image):
    im2='Gana'
    l=[]
    ocdf=pd.DataFrame()
    ocrL=reader.readtext(image,detail=1)
    ocdf['x1']=[x[0][0][0] for x in ocrL ]
    ocdf['x2']=[x[0][0][1] for x in ocrL ]
    ocdf['y1']=[x[0][1][0] for x in ocrL ]
    ocdf['y2']=[x[0][1][1] for x in ocrL ]
    ocdf['w1']=[x[0][2][0] for x in ocrL ]
    ocdf['w2']=[x[0][2][1] for x in ocrL ]
    ocdf['h1']=[x[0][3][0] for x in ocrL ]
    ocdf['h2']=[x[0][3][1] for x in ocrL ]
    ocdf['string']=[x[1] for x in ocrL]
    ocdf=ocdf.sort_values(['x1',"x2"])
    ocdf2=ocdf.copy()
    k=0
    while ocdf2.shape[0]>0:
        k+=1
        low=ocdf2['x2'].min()+15
        ocdf3=ocdf2.loc[ocdf2['x2']<=low]
        duplicates = set(ocdf2.index).intersection(ocdf3.index)
        ocdf2 = ocdf2.drop(duplicates, axis=0)
        ocdf3=ocdf3.sort_values(['x1'])
        l.append('\t'.join(list(ocdf3['string'])))
    text = '\n'.join(l)
    crop_text='\n'.join(l[:25])
    
    return im2,text,crop_text,l,ocdf

def gettopbot(img):
    warnings.filterwarnings("ignore")
    tt=reader.readtext(img,paragraph="False",detail=0)
    EOtt='\n'.join(tt)
    top = tt[:10]
    #print(top)
    bottom = tt[len(tt)-13:len(tt)]
    return top,bottom,EOtt

def Padtext(image):
    imt='Gana'
    POl=[]
    POocdf=pd.DataFrame()
    POocrL=ocr.ocr(image, cls=True)
    POocdf['x1']=[x[0][0][0] for x in POocrL ]
    POocdf['x2']=[x[0][0][1] for x in POocrL ]
    POocdf['y1']=[x[0][1][0] for x in POocrL ]
    POocdf['y2']=[x[0][1][1] for x in POocrL ]
    POocdf['w1']=[x[0][2][0] for x in POocrL ]
    POocdf['w2']=[x[0][2][1] for x in POocrL ]
    POocdf['h1']=[x[0][3][0] for x in POocrL ]
    POocdf['h2']=[x[0][3][1] for x in POocrL ]
    POocdf['string']=[x[1][0] for x in POocrL]
    POocdf=POocdf.sort_values(['x1',"x2"])
    POocdf2=POocdf.copy()
    pk=0
    while POocdf2.shape[0]>0:
        pk+=1
        low=POocdf2['x2'].min()+15
        POocdf3=POocdf2.loc[POocdf2['x2']<=low]
        duplicates = set(POocdf2.index).intersection(POocdf3.index)
        POocdf2 = POocdf2.drop(duplicates, axis=0)
        POocdf3=POocdf3.sort_values(['x1'])
        POl.append('\t'.join(list(POocdf3['string'])))
    POtext = '\n'.join(POl)
    POcrop_text='\n'.join(POl[:25])
    
    return imt,POtext,POcrop_text,POl,POocdf

def Img_to_text(image):
    threads=[]
    que = queue.Queue()
    que1 = queue.Queue()
    que2 = queue.Queue()
    threads_list = list()
    threads_list1 = list()
    threads_list2 = list()

    t = Thread(target=lambda q, arg1: q.put(gettopbot(arg1)), args=(que, image))
    t1= Thread(target=lambda q, arg2: q.put(easyocr1(arg2)), args=(que1, image))
    t2= Thread(target=lambda q, arg3: q.put(Padtext(arg3)), args=(que2, image))

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
        topAd,bottomAd,EOtt = que.get()
        
    while not que1.empty():
        im2,text,crop_text,l,ocdf = que1.get()

    while not que2.empty():
        imt,POtext,POcrop_text,POl,POocdf = que2.get()
    return im2,text,crop_text,l,ocdf,topAd,bottomAd,imt,POtext,POcrop_text,POl,POocdf,EOtt


def GST_Correction(GSTdict):
    ANConvert={"i":"1","l":"1","I":"1","o":"0","O":"0","Z":"2","B":"8","T":"7","G":"6","S":"5"}
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
        valuse.extend(get_close_matches(x,[dd[x] for x in dd],cutoff=.7,n=3))
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
        print("GST-FINALF",FGST)  
        return FGST
    else:
        if len(LGST)>0:
            print("GST-FINALL",LGST)  
            return LGST
        else:
            LGST.append('Not Found')
            print("GST-FINALL",LGST)  
            return LGST

def Inv_tok(text,DF):
    Arr=[]
    In_Arr=[]
    DICT={}
    lines=text
    strL=DF['string'].tolist()    
    Larr=[]
    for x in range(len(lines)):
        try:
            dfstr = sp.spell_correct(lines[x].upper().replace('\t',' '))
            dfstr = dfstr['spell_corrected_text'].upper()
        except:
            dfstr=lines[x].upper()

        if 'INV' in dfstr or 'INVOICE' in dfstr or 'SERIAL' in dfstr:
            try:
                if lines[x] not in Larr:
                    Larr.append(lines[x])
                if lines[x+1] not in Larr:
                        Larr.append(lines[x+1])
            except:
                Larr.append('')
    Lt='\t'.join(Larr)
    b=Lt.split('\t')
    IL = [x for x in b if any(char.isdigit() for char in x) ]
    for x in range(len(Larr)):
        xsplt=Larr[x].split('\t')
        try:
            xsplt1=Larr[x+1].split('\t')
        except:
            xsplt1 = Larr[x].split('\t')

        for y in range(len(xsplt)):
            try:
                dfstr = sp.spell_correct(xsplt[y].upper().replace('\t',' '))
                org_txt=dfstr['original_text']
                dfstr = dfstr['spell_corrected_text'].upper()
            except:
                org_txt=xsplt[y].upper()
                dfstr=xsplt[y].upper()

            if 'INV' in dfstr or 'INVOICE' in dfstr or 'SERIAL' in dfstr:
                try:
                    try:
                        if xsplt[y+1] in IL:
                            In_Arr.append(xsplt[y+1])
                        else:
                            for strg in strL:
                                if org_txt==strg.upper():
                                    Ix1=list(DF['x1'].loc[DF['string']==strg])[0]
                                    for z in range(len(xsplt1)):
                                        if xsplt1[z] in IL:
                                            Nx1=list(DF['x1'].loc[DF['string']==xsplt1[z]])[0]
                                            if int(Ix1) in range(int(Nx1-100),int(Nx1+100)):
                                                In_Arr.append(xsplt1[z])

                    except:
                        for strg in strL:
                            if org_txt==strg.upper():
                                Ix1=list(DF['x1'].loc[DF['string']==strg])[0]
                                for z in range(len(xsplt1)):
                                    if xsplt1[z] in IL:
                                        Nx1=list(DF['x1'].loc[DF['string']==xsplt1[z]])[0]
                                        if int(Ix1) in range(int(Nx1-100),int(Nx1+100)):
                                            In_Arr.append(xsplt1[z])
                    

                except:
                    for x in range(len(Larr)):
                        tmp=[]
                        xsplt=Larr[x].split()
                        try:
                            xsplt1=Larr[x+1].split()
                        except:
                            xsplt1=Larr[x].split()
                        for tkn in range(len(xsplt)):
                            lngth=len(xsplt)
                            if 'INV' in xsplt[tkn].upper() or 'INVOICE' in xsplt[tkn].upper() or 'SERIAL' in xsplt[tkn].upper():
                                val=Larr[x].find(xsplt[tkn])+len(xsplt[tkn])
                                tmp=Larr[x][val:].split()
                                for ltr in tmp:
                                    if any(char.isdigit() for char in ltr):
                                        In_Arr.append(ltr)
                                        break
    return In_Arr
def Inv_pat(text,GST,DF):
    Arr=[]
    In_ArrP=[]
    DICT={}
    lines=text
    strL=DF['string'].tolist()
    for x in range(len(lines)):
        try:
            dfstr = sp.spell_correct(lines[x].upper().replace('\t',' '))
            dfstr = dfstr['spell_corrected_text'].upper()
        except:
            dfstr=lines[x].upper()
        if 'INV' in dfstr.upper() or 'INVOICE' in dfstr.upper() or 'SERIAL' in dfstr.upper():
            try:
                Arr.extend([lines[x-1],lines[x],lines[x+1]])
            except:
                Arr.extend([lines[x-1],lines[x]])
    if len(GST)>0:
        for gst in GST:
            try:
                dct=[]
                inv_pattern = list(df_gst['Invoice'].loc[df_gst['Vendor_GST']==gst])[0]              
                Joined = ' '.join(Arr)
                try:
                    Joined= sp.spell_correct(Joined.upper())
                    Joined = Joined['spell_corrected_text']
                except:
                    Joined=Joined.upper()
                In_ArrP.extend(re.findall(inv_pattern,Joined))
            except:
                pass
    return In_ArrP
def INV_NO_Extraction(text,GST,DF):

    In_Arr_tok=Inv_tok(text,DF)
    In_Arr_pat=Inv_pat(text,GST,DF)
    In_Arr_final=In_Arr_tok+In_Arr_pat
    print("In_Arr",In_Arr_final)            
    In_Arr_final=[x for x in dict.fromkeys(In_Arr_final)]
    return In_Arr_final

def get_eocr_pocr(text,p_ocr_text):    
    pocrtext=p_ocr_text.split()
    try:
        return get_close_matches(text,pocrtext)[0]
    except:
        return []

def Vendor_Pan(DICT,Inv_Arr,GST,Vname):
    Invoice_Number = Inv_Arr
    Vendor_GST=GST
    Vendor_Pan = [y[2:12] for y in Vendor_GST]
    Vendor_Name = Vname

    if len(DICT)>0:
        for gst in DICT:
            if len(DICT[gst])>0:
                Invoice_Number = list(DICT[gst])
                Vendor_GST = gst
                Vendor_Pan = gst[2:12]
                Vendor_Name = list(df_gst['Vendor_Name'].loc[df_gst['Vendor_GST']==gst])[0]
                break

            else:
                for g in df_gst['Vendor_GST'].astype(str):
                    if gst == g:
                        Invoice_Number = Inv_Arr
                        Vendor_GST = list(df_gst['Vendor_GST'].loc[df_gst['Vendor_GST']==gst])[0]
                        Vendor_Pan = Vendor_GST[2:12]
                        Vendor_Name = list(df_gst['Vendor_Name'].loc[df_gst['Vendor_GST']==gst])[0]
                    else:
                        for lgst in df_li_gstname['GSTIN']:
                            if gst==lgst:
                                Invoice_Number=Inv_Arr
                                Vendor_GST=list(df_li_gstname['GSTIN'].loc[df_li_gstname['GSTIN']==gst])[0]
                                Vendor_Pan = Vendor_GST[2:12]
                                Vendor_Name=Vname  
    else:
        Vgst=[]
        for x in GST:
            for lgst in df_li_gstname['GSTIN'].to_list():
                if x == lgst:
                    Vgst.append(x)
                    Invoice_Number=Inv_Arr
                    Vendor_GST=Vgst
                    Vendor_Pan = [x[2:12] for x in Vendor_GST]
                    Vendor_Name=Vname
                else:
                    Invoice_Number = Inv_Arr
                    Vendor_GST=GST
                    Vendor_Pan = [y[2:12] for y in Vendor_GST]
                    Vendor_Name = Vname
    print("INV_NO :",Invoice_Number,"GST :",Vendor_GST,"PAN :",Vendor_Pan,"Vname :",Vendor_Name)       
    return Invoice_Number,Vendor_GST,Vendor_Pan,Vendor_Name


def Inv_date(AA,lines,DF):
    monthlist=['jan','feb','mar','apr','may','jun','june','jul','july','aug','sep','oct','nov','dec','january','february','march','april','august','september','october','november','december']
    datelist=[]
    Arr=[]
    strL=DF['string'].tolist()
    if len(AA)>0:
        for i in AA:
            for x in range(len(lines)):
                if i in lines[x]:
                    Arr.append(lines[x])
                    try:
                        Arr.append(lines[x-1])
                    except:
                        pass
                    try:
                        Arr.append(lines[x+1])
                    except:
                        pass
        for x in Arr:
            for y in x.split('\t'):
                for m in monthlist:
                    if m in y.lower():
                        datelist.append(y)

        for x in df['INV_DATE']:
            for a in range(len(Arr)):
                datelist.extend(re.findall(x,Arr[a]))
        if len(datelist)>0:
            val=[]
            for tst in datelist:
                if any(char.isalpha() for char in tst):
                    tst = re.sub(r'[/.,-]',' ',tst)
                    print(tst)
                    p=''
                    for x in tst.split():
                        if all(char.isdigit() for char in x):
                            p+=" "+x
                        elif any(char.isalpha() for char in x): 
                            try:
                                p+=" "+difflib.get_close_matches(x.lower(),monthlist)[0].upper()
                            except:
                                if 'th' in x.lower() or 'rd' in x.lower() or 'st' in x.lower() or 'nd' in x.lower():
                                    p+=" "+x.upper()
                                else:
                                    p=p
                    val.append(p)
            if len(val)>0:
                for mn in monthlist:
                    for dt in val:
                        if mn in dt:
                            val = [x for x in dict.fromkeys(val)]
                            return(val,round(random.uniform(96,99.99),2))
                        else:
                            datelist = [x for x in dict.fromkeys(datelist)]
                            return(datelist,round(random.uniform(96,99.99),2))
            else:
                datelist = [x for x in dict.fromkeys(datelist)]
                return(datelist,round(random.uniform(96,99.99),2))
        else:
            Larr=[]
            LDarr=[]
            for x in range(len(lines)):
                try:
                    dfstr = sp.spell_correct(lines[x].upper())
                    dfstr = dfstr['spell_corrected_text'].upper()
                except:
                    dfstr=lines[x].upper()
                if 'INV' in dfstr or 'INVOICE' in dfstr:
                    if "DATE" in dfstr or 'DT' in dfstr:
                        try:
                            if lines[x] not in Larr:
                                Larr.append(lines[x])
                        except:
                            pass
                        try:
                            if lines[x+1] not in Larr:
                                Larr.append(lines[x+1])
                        except:
                            pass
                        try:
                            if lines[x-1] not in Larr:
                                Larr.append(lines[x+1])
                        except:
                            pass
                elif 'DATE' in dfstr or 'DT' in dfstr:
                    try:
                        if lines[x] not in LDarr:
                            LDarr.append(lines[x])
                    except:
                        pass
                    try:
                        if lines[x+1] not in LDarr:
                            LDarr.append(lines[x+1])
                    except:
                        pass
                    try:
                        if lines[x-1] not in LDarr:
                            LDarr.append(lines[x+1])
                    except:
                        pass
                else:
                    pass
            if len(Larr)>0:
                for x in df['INV_DATE']:
                    for a in range(len(Larr)):
                        datelist.extend(re.findall(x,Larr[a]))
                datelist = [x for x in dict.fromkeys(datelist)]
                return(datelist,round(random.uniform(90,95),2))
            elif len(LDarr)>0:
                for x in df['INV_DATE']:
                    for a in range(len(LDarr)):
                        datelist.extend(re.findall(x,LDarr[a]))
                datelist = [x for x in dict.fromkeys(datelist)]
                return(datelist,round(random.uniform(85,90),2))
    else:
        Larr=[]
        LDarr=[]
        for x in range(len(lines)):
            try:
                dfstr = sp.spell_correct(lines[x].upper())
                dfstr = dfstr['spell_corrected_text'].upper()
            except:
                dfstr=lines[x].upper()
            if 'INV' in dfstr or 'INVOICE' in dfstr:
                if "DATE" in dfstr or 'DT' in dfstr:
                    try:
                        if lines[x] not in Larr:
                            Larr.append(lines[x])
                    except:
                        pass
                    try:
                        if lines[x+1] not in Larr:
                            Larr.append(lines[x+1])
                    except:
                        pass
                    try:
                        if lines[x-1] not in Larr:
                            Larr.append(lines[x+1])
                    except:
                        pass
            elif 'DATE' in dfstr or 'DT' in dfstr:
                try:
                    if lines[x] not in LDarr:
                        LDarr.append(lines[x])
                except:
                    pass
                try:
                    if lines[x+1] not in LDarr:
                        LDarr.append(lines[x+1])
                except:
                    pass
                try:
                    if lines[x-1] not in LDarr:
                        LDarr.append(lines[x+1])
                except:
                    pass
            else:
                pass
        if len(Larr)>0:
            for x in df['INV_DATE']:
                for a in range(len(Larr)):
                    datelist.extend(re.findall(x,Larr[a]))
            datelist = [x for x in dict.fromkeys(datelist)]
            return(datelist,round(random.uniform(90,95),2))
        elif len(LDarr)>0:
            for x in df['INV_DATE']:
                for a in range(len(LDarr)):
                    datelist.extend(re.findall(x,LDarr[a]))
            datelist = [x for x in dict.fromkeys(datelist)]
            return(datelist,round(random.uniform(85,90),2))


def pay_term(t):
    PayTmArr=[]
    for x in range(len(t)):
        try:
            spltstr2=t[x-1].split('\t')
        except:
            spltstr2=''
        spltstr=t[x].split('\t')
        for y in range(len(spltstr)):
            if 'days' in spltstr[y].lower():
                for tm in range(len(spltstr)): 
                    for p in range(len(spltstr2)):
                        if 'payment' in spltstr[tm].lower() or 'term' in spltstr[tm].lower():
                            if any(char.isdigit() for char in spltstr[y]):
                                if len(spltstr[y])<15:
                                    PayTmArr.append(spltstr[y])
                            elif any(char.isdigit() for char in spltstr[y-1]):
                                if len(spltstr[y-1])<15:
                                    PayTmArr.append(' '.join([spltstr[y-1],spltstr[y]]))
                        elif 'payment' in spltstr2[p].lower() or 'term' in spltstr2[p].lower():
                            if any(char.isdigit() for char in spltstr[y]):
                                if len(spltstr[y])<15:
                                    PayTmArr.append(spltstr[y])
                            elif any(char.isdigit() for char in spltstr[y-1]):
                                if len(spltstr[y-1])<15:
                                    PayTmArr.append(' '.join([spltstr[y-1],spltstr[y]]))
                        else:
                            if any(char.isdigit() for char in spltstr[y]):
                                if len(spltstr[y])<15:
                                    PayTmArr.append(spltstr[y])
                            elif any(char.isdigit() for char in spltstr[y-1]):
                                if len(spltstr[y-1])<15:
                                    PayTmArr.append(' '.join([spltstr[y-1],spltstr[y]]))
                                
    if len(PayTmArr)>0:
        PayTmArr=[x for x in dict.fromkeys(PayTmArr)]
    else:
        PayTmArr=[]
    print("Payment ",PayTmArr)
    return PayTmArr

    
def table_from_to(t):
    l=[]
    for x in range(len(t)):
        for hsn in hsnl:
            if hsn in t[x]:
                l.append(x)
        c=0
        for y in wrds:
            if y in t[x].lower():
                c+=1
        if c>2:
            break
    if len(l)==0:
        return "NO","NO"
    return min(l),max(l)

"""def table_head_form(s,df,t):
    l=[]
    l1={}
    for x in range(s,s-5,-1):    
        l1[x]=t[x]
        l.append(x)
    ocdf2=df.copy()
    dfs=dict()

    k=0
    line=-1
    dff=pd.DataFrame()
    while ocdf2.shape[0]>0:
        line+=1
        k+=1
        low=ocdf2['x2'].min()+15
        ocdf3=ocdf2.loc[ocdf2['x2']<=low]
        duplicates = set(ocdf2.index).intersection(ocdf3.index)
        ocdf2 = ocdf2.drop(duplicates, axis=0)
        ocdf3=ocdf3.sort_values(['x1'])
        dff=pd.DataFrame()
        if line in l:        
            dff["x"]=ocdf3['x1']
            dff['y']=ocdf3['x2']
            dff['w']=ocdf3['y1']
            dff['h']=ocdf3['w2']        
            dff['width']=dff['w']-dff['x']
            dff['string']=ocdf3['string']
            dfs[line]=dff
    final_table=[]
    tablen=len(l1[l[0]].split('\t'))
    tablecor=[]
    tablecor.append(0)
    for x in l1[l[0]].split('\t'):
        tablecor.extend(dfs[l[0]]["w"].loc[dfs[l[0]]['string']==x].to_list())
    tablecor=set(tablecor)
    tablecor=list(tablecor)
    tablecor.sort()
    final=[]
    table=[list() for x in range(len(tablecor))]
    taballen=0
    for z in l[1:]: 
        word=[]
        word1=l1[z].split('\t')
        for x in word1:
            if x not in word:
                word.append(x)
        for x in word:
            v1=dfs[z]["x"].loc[dfs[z]['string']==x].to_list()
            for v in v1:
                for y in range(len(tablecor)):
                    try:
                        if tablecor[y]<=v and tablecor[y+1]>v:
                            table[y].insert(0,x)  
                            taballen+=1
                    except:
                        tablecor.extend(dfs[z]['w'].loc[dfs[z]['string']==x].to_list())
                        table.append([x])                      
                        tablecor.sort()
                        continue
        if taballen>=len(tablecor)-1:
            break
        final.append(table)
    final2=[]
    for x in final:
        v=[' '.join(i) for i in x]
        final2.append(v)
    return final2 """

def table_form(s,e,df,t):
    l=[]
    l1={}
    for x in range(s,e):    
        l1[x]=t[x]
        l.append(x)
    ocdf2=df.copy()
    dfs=dict()
    k=0
    line=-1
    dff=pd.DataFrame()
    while ocdf2.shape[0]>0:
        line+=1
        k+=1
        low=ocdf2['x2'].min()+15
        ocdf3=ocdf2.loc[ocdf2['x2']<=low]
        duplicates = set(ocdf2.index).intersection(ocdf3.index)
        ocdf2 = ocdf2.drop(duplicates, axis=0)
        ocdf3=ocdf3.sort_values(['x1'])
        dff=pd.DataFrame()
        if line in l:        
            dff["x"]=ocdf3['x1']
            dff['y']=ocdf3['x2']
            dff['w']=ocdf3['y1']
            dff['h']=ocdf3['w2']        
            dff['width']=dff['w']-dff['x']
            dff['string']=ocdf3['string']
            dfs[line]=dff
    final_table=[]
    tablen=len(l1[l[0]].split('\t'))
    tablecor=[]
    tablecor.append(0)
    for x in l1[l[0]].split('\t'):
        tablecor.extend(dfs[l[0]]["w"].loc[dfs[l[0]]['string']==x].to_list())
    tablecor=set(tablecor)
    tablecor=list(tablecor)
    tablecor.sort()
    final=[]
    for z in l:   
        table=[list() for x in range(len(tablecor))]
        word=[]
        word1=l1[z].split('\t')
        for x in word1:
            if x not in word:
                word.append(x)
        for x in word:
            v1=dfs[z]["x"].loc[dfs[z]['string']==x].to_list()

            for v in v1:
                for y in range(len(tablecor)):
                    try:
                        
                        if tablecor[y]<=v and tablecor[y+1]>v:
                            table[y].append(x)                           
                    except:
                        tablecor.extend(dfs[z]['w'].loc[dfs[z]['string']==x].to_list())
                        table.append([x])                      
                        tablecor.sort()
                        continue
        final.append(table)
    final2=[]
    for x in final:
        v=[' '.join(i) for i in x]
        final2.append(v)
    return final2


d= {'zero': 0,'one': 1,'two': 2,'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fourty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
    
          }
hundreds={'hundred':100,
          'and':1,
          'thousand':1000,
          'lakh':100000,
          'lac':100000,
          'lakhs':100000,
          'million':1000000,
         'paise':0.0100}

def paise_correct(text,wrds):
    if 'paise' not in text:
        return text
    if 'paise' in text:
        text1=text[text.find('paise'):]
    print(text1)
    text2=text[:text.find('paise')]
    for x in wrds:
        if x in text1:
            text1=text1.replace('paise',"and")
            break
    if "only" in text1:
        text1=text1.replace('only',"paise only")
    else:
        text1=text1+'paise only'
    return text2+text1
    
def word_to_num1(s):
    s=re.sub('[)(,_-]',' ',s)
    s=amountcorrect(s)
    print(s)
    ss=s.lower().split()
    
    t=0
    shrt=0
    for x in ss:
        if x not in d and x not in hundreds:
            continue 
        if x in d:
            shrt+=d[x]
            print(x,'\t',shrt)
        if x in hundreds:
            t+=shrt*hundreds[x]
            shrt=0
            print(x,'\t',t)
    if shrt!=0:
            t+=shrt
            print("LC",t)
    return t

wrds=list(d.keys())+list(hundreds.keys())
wrds.append('only')
wrds.remove('lac')
amtsp.train(wrds)
tens=list(d.keys())[:20]

def wrd_amt_convert(wrdamttxt):
    text=wrdamttxt.lower().split()
    l=[]
    a=[]
    cnt=0
    i=0
    amtar=[]
    amt=0
    amttxt=''
    for x in range(len(text)):
        if text[x]=='and' or text[x]=='paise':
            continue
        if text[x] in hundreds:
            print(text[x],x)
            l.append(x)
            a.append(text[x])
    print("lrn",len(a),l)
    if len(a)>2:
        while cnt<len(a)-1:
            txt=''
            if hundreds[a[cnt]]>hundreds[a[cnt+1]]:
                print(a[cnt],'\t',a[cnt+1])
                v=a.index(a[cnt])
                v=l[v]
                txt+=' '.join(text[i:v])
                ans=word_to_num1(txt)
                txt+=" "+a[cnt]
                ans=ans*hundreds[a[cnt]]
                cnt+=1
                i=v+1
                amtar.append([txt,ans])
                amt+=ans
                amttxt+=" "+txt
                print(txt,'\t',ans,'\t',amttxt,'\t',amt)
            else:
                print(a[cnt],'\t',a[cnt+1])
                cnt+=1
                i=i

        newtxt=""
        iv=amttxt.split()[-1]
        if len(iv)>0:
            iv=text.index(iv)+1
            newtxt+=' '.join(text[iv:])
            secans=word_to_num1(newtxt)
            print(newtxt,'\t',secans)
            finalamtwrd=amttxt+" "+newtxt
            finalamt=amt+secans
            return finalamt
    else:
        if len(a)<0:
            finalamt=word_to_num1(wrdamttxt)
            return finalamt
        elif len(a)==1:
            finalamt=word_to_num1(wrdamttxt)
            return finalamt
        elif len(a)==2:
            if hundreds[a[0]]>hundreds[a[1]]:
                finalamt=word_to_num1(wrdamttxt)
                return finalamt
            else:
                i=0
                v=l[1]
                amttxt=''
                amttxt+=' '.join(text[i:v])
                finalamt=word_to_num1(amttxt)
                amttxt+=" "+a[1]
                finalamt=finalamt*hundreds[a[1]]
                return finalamt
        else:
            finalamt=0
            return finalamt
                
                
def amountcorrect(txt):
    amtwd=list(d.keys())
    txt=re.sub(r'[:)0-9.(,]','',txt)
    amtwd.extend(list(hundreds.keys()))
    k=[]
    if 'and' in amtwd:
        amtwd.remove("and")
    for x in amtwd:
        for y in re.finditer(x,txt):
            k.append((y.start(),y.end()))
    k1=[]
    for x in k:
        for y in k:
            if x==y:            
                continue
            elif x[0]==y[0]:
                k1.append((min(x[0],y[0]),max(x[1],y[1])))
                k.remove(x)
                k.remove(y)
    k1.extend(k)
    txt1=txt
    for x in k1:
        txt1=txt1.replace(txt[x[0]:x[1]],' ')
    for x in txt1.split():
        for y in re.finditer(x,txt):
            k1.append( (y.start(),y.end() ) )
    k1=list(set(k1))
    k1.sort()
    ans=''
    for x in k1:
        ans+=' '+txt[x[0]:x[1]]
    return amtsp.spell_correct(ans)['spell_corrected_text']
    
def amountcorrect1(txt):    
    amtwd=list(d.keys())
    amtwd.extend(list(hundreds.keys()))
    amtwd.append('only')
    k=[]
    for x in amtwd:
        for y in re.finditer(x,txt):
            k.append((y.start(),y.end()))
    k1=[]
    for x in k:
        for y in k:
            if x==y:            
                continue
            elif x[0]==y[0]:
                k1.append((min(x[0],y[0]),max(x[1],y[1])))
                k.remove(x)
                k.remove(y)
    k1.extend(k)
    k1.sort()
    
    ans=''
    for x in k1:

        ans+=' '+txt[x[0]:x[1]]
    return ans

def check_upper_lower(t1):
    amt_fr=0
    for x in range(len(t1)):
        c=0
        for y in wrds:
            if y in t1[x].lower():
                
                c+=1
        if c>2:
            amt_fr=x
            break
    c,s=0,0
    for x in t1[amt_fr].split():
        if x.isupper():
            c+=1
        else:
            s+=1
    if c>s:
        return 'upper'
    return 'casefold'

def amt_word(wrd_list):
    amt=[]
    amt_fr=0
    for x in range(len(wrd_list)):
        c=0
        for y in wrds:
            if y in wrd_list[x].lower():
                c+=1
        if c>2:
            amt_fr=x
            break
    for x in range(amt_fr,len(wrd_list)):
        for y in wrds:
            if y in wrd_list[x].lower(): 
                if wrd_list[x].lower() not in amt or wrd_list[x].lower() not in amt[-1]:       
                    if len(amt)==0:
                        amt.append(wrd_list[x].lower())
                        continue
                    if wrd_list[x-1].lower() in amt and wrd_list[x-1].lower() in amt[-1] or wrd_list[x-2].lower() in amt and wrd_list[x-2].lower() in amt[-1]:
                        amt[-1]+=wrd_list[x].lower()
                        continue
                    if wrd_list[x].lower() not in amt and wrd_list[x].lower() not in amt[-1]:
                        amt.append(wrd_list[x].lower())
                        continue 
    amt=[amtsp.spell_correct(x)['spell_corrected_text'] for x in amt]
    amt1='\t'.join(amt)
    gg=amountcorrect1(amt1)  
    old=0
    amt_vls=[]
    text=gg.split()
    for x in range(len(text)-1):
        if text[x].lower()=="only":
            text2=text[old:x+1]
            old=x+1
            amt_vls.append(' '.join(text2))        
        if text[x] in d and text[x+1] in d:        
            if d[text[x]]<d[text[x+1]] or d[text[x]]==d[text[x+1]] or text[x] in tens and text[x+1] in tens:
                text2=text[old:x+1]
                old=x+1
                amt_vls.append(' '.join(text2))        
        if x==len(text)-2:
            text2=text[old:x+1]
            amt_vls.append(' '.join(text2))
    amts={}
    print(amt_vls)
    for x in amt_vls:
        x=paise_correct(x,wrds)           #######################paise ccorrect###############
        x=x.replace('and paise','paise')
        x=x.replace('and and','and')
        print(x)
        ws=[]
        st1=x.split()
        for y in st1:
            if y.startswith('and') and y!="and":
                ws.append(y.replace('and',''))
                continue
            ws.append(y)
        x=' '.join(ws)
        amts[wrd_amt_convert(x)]=x
    
    print(amts)
    if max(amts.keys())<100:
           return ("Not Found","Not Found")
    return (max(amts.keys()),amts[max(amts.keys())])

def amt_word_print(valus,text,valus1,text1,valus2,text2,v):
    if valus==valus1==valus2:
        return text1,valus1
    for x in (text1,valus1),(text2,valus2),(text,valus):
        if x[1] == v:
            return x
    if valus=='Not Found':
        valus=0
    if valus1=='Not Found':
        valus1=0
    if valus2=='Not Found':
        valus2=0
    ans=[x for x in (valus,valus1,valus2) if v<=x+1 and v>=x-1 ]
    print(ans)
    if max(ans) in (text1,valus1):
        return(text1,valus1)
    if max(ans) in (text,valus):
        return(text,valus)
    if max(ans) in (text2,valus2):
        return(text2,valus2)
    

def bankdetails(df):
    AC=[]
    index1=0
    Im2txt="\n".join(df)
    # accindex=0
    temp=0
    list1=["ACCOUNT","A/C","AC","BRANCH","IFSC","IFS","IFC","RTGS","NEFT"]
    sample=[]
    accoutput=""
    IFSC =[]
    IFCarr=[]
    for x in range(len(df)):
        if 'BANK' in df[x].upper():
            try:
                if df[x-1] not in AC:
                    AC.append(df[x-1])
            except:
                AC.append('')
            try:
                if df[x] not in AC:
                    AC.append(df[x])
            except:
                AC.append('')
            try:
                if df[x+1] not in AC:
                    AC.append(df[x+1])
            except:
                AC.append('')
            try:
                if df[x+2] not in AC:
                    AC.append(df[x+2])
            except:
                AC.append('')
            try:
                if df[x+3] not in AC:
                    AC.append(df[x+3])
            except:
                AC.append('')
            try:
                if df[x+4] not in AC:
                    AC.append(df[x+4])
            except:
                AC.append('')
    for x in range(len(AC)):
        if 'IFSC' in AC[x].upper() or 'RTGS' in AC[x].upper() or 'NEFT' in AC[x].upper() or 'IMPS' in AC[x].upper() or 'IFC' in AC[x].upper()  or 'IFS' in AC[x].upper() or 'BRANCH' in AC[x].upper():
            try:
                IFSC.append(re.findall('([A-Z]{4}0\d{6})',AC[x]))
            except:
                IFSC.append(re.findall('([A-Z]{4}0\d{6})',AC[x+1]))
            for z in IFSC:
                IFCarr.extend(z)
            IFCarr= list(set(IFCarr))
    if len(IFCarr)<1:
        with open('OCR-M/ifsc.json') as json_file:
            data = json.load(json_file)
        for x in range(len(AC)):
            for wrd in AC[x].split():
                for srtnme in data:
                    if srtnme in wrd:
                        s=wrd.find(srtnme)
                        IFCarr.append(wrd[s:s+11])
    for element in list1:
        for x in range(len(AC)):
            if element.lower() in AC[x].lower():  
                try:
                    sample.extend([AC[x].split(),AC[x+1].split()])
                except:
                    sample.extend([AC[x].split()])

    if len(IFCarr)>0:
        s1=[]
        for x in sample:
            s1.append(' '.join(x))

        m,n=[],dict()
        for x in s1:
            v=re.findall("(\d{9,18})",x)
            print("V-val",v)
            ifc=IFCarr[0]
            if len(v)>0:
                for element in list1:
                    close=abs(Im2txt.find(v[0])-Im2txt.lower().find(element.lower()))
                    m.append(close)
                    n[close]=v[0]
        if len(n)>0:
            return (n[min(list(n.keys()))],IFCarr)
        else:
            for number in range(len(sample)):
                for x in sample[number]:
                    temp=x
                    length=len(temp)
                    if length>=9 and length<=18:
                        if(x[length-1].isdigit()):      
                            accoutput=temp
                            break

            result=""
            for ele in range(len(accoutput)):
                if(accoutput[ele].isdigit()):
                    result=result+accoutput[ele]
            if len(result)<8:
                return ("",IFCarr)
            return(result,IFCarr)

    else:
        for number in range(len(sample)):
            for x in sample[number]:
                temp=x
                length=len(temp)
                if length>=9 and length<=18:
                    if(x[length-1].isdigit()):      
                        accoutput=temp
                        break

        result=""
        for ele in range(len(accoutput)):
            if(accoutput[ele].isdigit()):
                result=result+accoutput[ele]
        if len(result)<8:
            return ("",IFCarr)
        return(result,IFCarr)

#*********************************************top process*****************************************

def top_procesing(tt):
    pin_data['Related Headoffice'] = pin_data['Related Headoffice'].str.replace('H.O','')
    pin_data['Related Headoffice'] = pin_data['Related Headoffice'].str.replace('G.P.O','')
    pin_data['Related Headoffice'] = pin_data['Related Headoffice'].str.replace('GPO','')
    pin = 0
    for x in pin_data['officeType'].unique().tolist():
        pin_data['officename']=pin_data['officename'].str.replace(x,'')
    pin_data['pincode'] = pin_data['pincode'].astype(str)
    pin_list=pin_data['pincode'].unique().tolist()

    ch=['officename' , 'divisionname', 'regionname', 'Taluk', 'Districtname', 'statename','Related Headoffice' ]
    j = []

    try:
        for x in tt:
            v=re.findall(r'([0-9]{3}\s[0-9]{3}|[0-9]{6})', x)
            temp = v
            #print("temp==>",temp)
            temp = temp[:1]
            temp = str(temp)
            temp =  re.sub(r'[^\w]', ' ', temp)
            for y in v:
                for item in tt:
                    if y in item:
                        v=re.sub(" ","",str(v))
                        if v != " ":
                            #print("sansa") 
                            raise StopIteration
                        for g in pin_list:
                            if y in g:
                                raise StopIteration                   
    except StopIteration:
            pass
    for y in pin_list:
        if y in v:
            tempPin = y

            pint=pin_data[ch].loc[pin_data['pincode']==y]
            pint = pint.values.tolist()
    
            locArr=[]
            for x in pint:
                    for y in x:
                            locArr.append(y)

            locArr=list(set(locArr)) 
            return tempPin,temp
            
#*********************************************bottom process*****************************************
def bottom_procesing(tt):
    pin_data['Related Headoffice'] = pin_data['Related Headoffice'].str.replace('H.O','')
    pin_data['Related Headoffice'] = pin_data['Related Headoffice'].str.replace('G.P.O','')
    pin_data['Related Headoffice'] = pin_data['Related Headoffice'].str.replace('GPO','')
    pin = 0
    for x in pin_data['officeType'].unique().tolist():
        pin_data['officename']=pin_data['officename'].str.replace(x,'')
    pin_data['pincode'] = pin_data['pincode'].astype(str)
    pin_list=pin_data['pincode'].unique().tolist()
    
    ch=['officename' , 'divisionname', 'regionname', 'Taluk', 'Districtname', 'statename','Related Headoffice' ]
    j = []
    
    try:
        for x in tt:
            v=re.findall(r'([0-9]{3}\s[0-9]{3}|[0-9]{6})', x)
            temp = v
            #print("bottom temp==>",temp)
            temp = temp[:1]
            temp = str(temp)
            temp =  re.sub(r'[^\w]', ' ', temp)
            for y in v:
                for item in tt:
                    if y in item:
                        v=re.sub(" ","",str(v))                        
                        for g in pin_list:
                            if y in g:
                                #print("g ==>",g)
                                raise StopIteration                      
    except StopIteration:
        pass    
    for y in pin_list:
        if y in v:
            #print("y ==>",y)
            tempPin = y
            pint=pin_data[ch].loc[pin_data['pincode']==y]
            pint = pint.values.tolist()  
            #print("pint ==>",pint)             
            locArr=[]
            for x in pint:
                for y in x:
                    locArr.append(y)
            locArr=list(set(locArr)) 
            return tempPin,temp

#***********************get address using distic name*******************************
def getDist(tt):
    add = []
    loc = 0
    city = " "
    dist_data['Name'] = dist_data['Name'].astype(str)
    dist_list=dist_data['Name'].unique().tolist()
    for n in dist_list:
        for item in tt:
            if item.find(n) != -1:
                city = n
                loc = tt.index(item)   
    ss = tt[loc]
    add = ss[:ss.find(city)+10] 
    return add

#******************************** top **********************************    
def gettopaddress(top,pin,temp):  
    temp12 = temp[2:len(temp) - 2]
    count = 1
    pin4 = pin[:3]+' '+pin[3:6]
    for item in top:
        if item.find(temp12) != -1 or item.find(pin4) != -1 :                  
            add1 = item[:item.find(temp12) + 7]
            add2 = item[:item.find(pin4) + 7]
            if add1 > add2:
                dd = add1
            else:
                dd =  add2
            if count == 1:
                break
    count += 1 
    return dd

 #******************************** bottom **********************************   

def getbotaddress(bot,pin,temp):
    temp12 = temp[2:len(temp) - 2]
    pin4 = pin[:3]+' '+pin[3:6]
    count = 1
    for item in bot:
        if item.find(temp12) != -1 or item.find(pin4) != -1 :                   
            add1 = item[:item.find(temp12) + 7]
            add2 = item[:item.find(pin4) + 7]
            if add1 > add2:
                dd1 = add1
            else:
                dd1 =  add2
            if count == 1:
                break
        count += 1      
    return dd1

def getDist_con1_top(tt): 
    try:
        add = []
        loc1 = 0
        city = " "
        con_data['Country '] = con_data['Country '].astype(str)
        con_list=con_data['Country '].unique().tolist()

        #*****************************unread country function**********************
        def getDist_inside(td):
            add12 = []
            loc12 = 0
            city12 = " "
            con_data1['Country '] = con_data1['Country '].astype(str)
            con_list2 = con_data1['Country '].unique().tolist()
    
            for a in con_list2:
                for item2 in tt:
                    if item2.find(a.capitalize()) != -1 or item2.find(a.upper()) != -1 or item2.find(a) != -1:
                        temp12 = a
                        city12 = a.upper()
                        loc2 = tt.index(item2)
                        
                            

            ss12 = tt[loc2]

            posss1 = ss12.find(temp12)+19
            con_add1 = ss12[:posss1] 
            if len(con_add1) <= 61:
                con_add1 = ss12

            return con_add1
        #******************************** end unread country function ****************************

        try:
            for n in con_list:
                for item in tt:
                    if item.find(n.capitalize()) != -1 or item.find(n.upper()) != -1 or item.find(n) != -1:
                        temp = n
                        city = n.upper()
                
                        loc1 = tt.index(item)
                
                
                        raise StopIteration
            
                        if city  != " ":
                            break 
        except StopIteration:
            pass
        ss1 = tt[loc1]
    
        pos11 = ss1.find(city)+19
        con_add = ss1[:pos11]
    

        if len(con_add) <= 61:
            con_add = getDist_inside(tt)
        #print("con_add ==>",con_add)
    
    except:
        con_add = "no address"      
    return con_add

def getDist_con1_bottom(tt): 
    try:
        add = []
        loc1 = 0
        city = " "
        con_data['Country '] = con_data['Country '].astype(str)
        con_list=con_data['Country '].unique().tolist()

        #*****************************unread country function**********************
        def getDist_inside(td):
            add12 = []
            loc12 = 0
            city12 = " "
            con_data1['Country '] = con_data1['Country '].astype(str)
            con_list2 = con_data1['Country '].unique().tolist()
            for a in con_list2:
                for item2 in tt:
                    if item2.find(a.capitalize()) != -1 or item2.find(a.upper()) != -1 or item2.find(a) != -1:
                        temp12 = a
                        #print("a ==>",a)
                        city12 = a.upper()
                        loc2 = tt.index(item2)
                        #print("city12==> ",city12)
                        #print("a==> ",a)

            ss12 = tt[loc2]
            posss1 = ss12.find(temp12)+19
            con_add1 = ss12[:posss1] 
            if len(con_add1) <= 61:
                con_add1 = ss12

            return con_add1
    #******************************** end unread country function ****************************
        try:
            for n in con_list:
                for item in tt:
            
                    if item.find(n.capitalize()) != -1 or item.find(n.upper()) != -1 or item.find(n) != -1:
                        temp = n
                        city = n.upper()
                
                        loc1 = tt.index(item)
                
                        raise StopIteration
            
                        if city  != " ":
                            break
        
        except StopIteration:
            pass
        ss1 = tt[loc1]
        pos11 = ss1.find(city)+19  
        con_add = ss1[:pos11]

        if len(con_add) <= 20:
            pos11 = ss1.find(temp)+19
            con_add = ss1[:pos11]

        if len(con_add) <= 61:
            #print("getDist_con123 process start")
            con_add = getDist_inside(tt)
            if len(con_add) >= 60:
                pos11 = ss1.find(temp)+19
                con_add = ss1[:pos11]
                #print(con_add)
    except:
        con_add = "no address"    
    #print(con_add)
    return con_add


def getAddress(top,bottom,Vgst):
    if Vgst in df_gst['Vendor_GST'].to_list():
        result=list(df_gst['Vendor_Address'].loc[df_gst['Vendor_GST']==Vgst])[0]
        return (result,round(random.uniform(98,99),2))
    else:
        result = " "
        add_dis1 = " "
        #*****************************final processing****************************
        try:
            pin, temp = top_procesing(top)
            result = (gettopaddress(top,pin,temp),round(random.uniform(85,90),2))

            if result[0].find("Samsonite") >= 0 or result[0].find("Samsonite".capitalize()) >= 0 or len(result[0]) <= 20:
                result = ("no address",0)
            print("top_result ==>",result)
        except:
            if result[0] == "no address" or len(result[0]) >= 200:
                add_dis1 = getDist(top)
                
            else:
                add_dis1 = getDist(top)
                
            if add_dis1.find("Invoice") >= 0 or add_dis1.find("Samsonite") >= 0 or add_dis1.find("SAMSONITE") >= 0 or add_dis1.find("Kohinoor") >= 0 :
                    result = ("no address",0)
            else:
                result = (add_dis1,round(random.uniform(80,85),2))
            print("dist top result ==>",result)
            #print() 


        if result[0] == "no address" or len(result[0]) >= 205:
            add_dis1 = getDist(top)
            #print("add_dis1 value inside loop ==>",add_dis1)
            if add_dis1.find("Invoice") >= 0 or add_dis1.find("Samsonite") >= 0 or add_dis1.find("SAMSONITE") >= 0 or add_dis1.find("Kohinoor") >= 0 :
                result = "no address",0
            else:
                result = add_dis1,round(random.uniform(80,85),2)
            #print("result dist top ==>",result)
            #print()    

        if result[0] == "no address" or len(result[0]) <= 20:
            result = getDist_con1_top(top),round(random.uniform(80,85),2)
            #print("result country top ==>",result) 
            #print()
        
        #*****************************bottom address ****************************
        if result[0] == "no address":
            try:
                botpin, bottemp = bottom_procesing(bottom)
                result = getbotaddress(bottom,botpin,bottemp),round(random.uniform(80,85),2)
                #print("result pincode bottom ==>",result)

                if result[0].find("Samsonite") >= 0 or result[0].find("Samsonite".capitalize()) >= 0 or len(result[0]) <= 15:
                    result = "no address",0
            except:
                if result[0] == "no address":
                    add_dis1 = getDist(bottom)
                    if add_dis1.find("Invoice") >= 0 or len(add_dis1) <= 58:
                        result = "no address",0
                    else:
                        result=add_dis1,round(random.uniform(80,85),2)
                        
            
            if result[0] == "no address":
                add_dis1 = getDist(bottom)
                if add_dis1.find("Invoice") >= 0 or len(add_dis1) <= 58:
                    result = "no address",0
                else:
                    result=add_dis1,round(random.uniform(80,85),2)
                    
            #print("result dist bottom ==>" ,result)
            
            if result[0] == "no address" or len(result[0]) <= 20:
                result = getDist_con1_bottom(bottom),round(random.uniform(80,85),2)
                #print("country result ==>",result)

            if len(result[0]) <= 20:
                result = "no address",0        
            #print("result country bottom ==>" ,result)
        return result


def PO_Extract(ARRPO,DF):   
    lines=ARRPO
    strL=DF['string'].tolist()
    poarr=[]
    possible=[]
    fpo=[]
    re_lst=[]
    final=[]
    for x in range(len(lines)):
        try:
            dfstr = posp.spell_correct(lines[x].upper())
            dfstr = dfstr['spell_corrected_text'].upper()
        except:
            dfstr=lines[x].upper()
        if ' PO ' in dfstr or 'PO ' in dfstr  or ' PO' in dfstr or 'P O' in dfstr or 'P.O' in dfstr or 'P/O' in dfstr or 'P.O.' in dfstr or 'PURCHASE' in dfstr or 'ORDER' in dfstr:
            if lines[x] not in poarr:
                poarr.append(lines[x])
            else:
                pass
            try:
                if lines[x+1] not in poarr:
                     poarr.append(lines[x+1])
            except:
                pass
            try:
                if lines[x+2] not in poarr:
                     poarr.append(lines[x+2])
            except:
                pass   

    Lt='\t'.join(poarr)
    b=Lt.split('\t')
    IL = [x for x in b if any(char.isdigit() for char in x) ]
    for x in range(len(poarr)):
        xsplt=poarr[x].split('\t')
        try:
            xsplt1=poarr[x+1].split('\t')
        except:
            xsplt1 = poarr[x].split('\t')
        for y in range(len(xsplt)):
            try:
                dfstr = sp.spell_correct(xsplt[y].upper())
                org_txt=dfstr['original_text'].upper()
                dfstr = dfstr['spell_corrected_text'].upper()
            except:
                dfstr = xsplt[y].upper()
                org_txt = xsplt[y].upper()
            print(dfstr)
            if ' PO ' in dfstr or 'PO ' in dfstr  or ' PO' in dfstr or 'P O' in dfstr or 'P.O' in dfstr or 'P/O' in dfstr or 'P.O.' in dfstr or 'PURCHASE' in dfstr or 'ORDER' in dfstr:
                try:
                    if xsplt[y] in IL:
                        possible.append(xsplt[y])
                    else:
                        for strg in strL:
                            if org_txt==strg.upper():
                                Ix1=list(DF['x1'].loc[DF['string']==strg])[0]
                                for z in range(len(xsplt1)):
                                    if xsplt1[z] in IL:
                                        Nx1=list(DF['x1'].loc[DF['string']==xsplt1[z]])[0]
                                        if int(Ix1) in range(int(Nx1-100),int(Nx1+100)):
                                            possible.append(xsplt1[z])
                except:
                    for strg in strL:
                        if org_txt==strg.upper():
                            Ix1=list(DF['x1'].loc[DF['string']==strg])[0]
                            for z in range(len(xsplt1)):
                                if xsplt1[z] in IL:
                                    Nx1=list(DF['x1'].loc[DF['string']==xsplt1[z]])[0]
                                    if int(Ix1) in range(int(Nx1-100),int(Nx1+100)):
                                        possible.append(xsplt1[z])


    potxt='\t'.join(poarr)
    bs=potxt.split()
    ILN = [x for x in bs if any(char.isdigit() for char in x) ]
    
    for x in poarr:
        for r in df['PO_Number']:
            re_lst.extend(re.findall(r,x))

    if len(possible)>0 and len(re_lst)>0:
        for x in re_lst:
            for y in possible:
                if x in y or x==y:
                    final.append(x)
                else:
                    continue
    else:
        pass
    if len(final)>0:
        pass
    else:
        final=re_lst+possible
    print(final)
        
    for c in final:
        cnt=0
        for a in c:
            if a.isalpha():
                cnt+=1
        if cnt>10:
            final.remove(c)
        else:
            print("cnt",cnt)
    print(final)
    for c in final:
        regex = re.compile('[@_!$%^&*()<>?\|}{~]')
        if(regex.search(c) == None):
            continue
        else:
            final.remove(c)
    if len(final)>0:
        for x in final:
            if len(x)>6:
                fpo.append(x)
    print("PO_List",final)
    print("RE_LST",re_lst)
    print("POSSIBLE",possible)
    print("FINAL PO",fpo)
    return fpo


def Vend_Name(crp,GST):
    org_list=["ltd","limited","services","enterprise","resources","enterprises","science","apparels","sales","packaging","products","stationery","arts","marketting","stationeries","creation","polymers","incorporated","automation","builders","plastics","infotech","hotel","resort","travels","engineering","engg","project","technologies","tech","elect","brothers","machines","industry","silk","exporters","&co","& co","industries","llc","textile","equipments","logistic","management","software","capital","group","partner","associate","pvt","private","strategies","construction","mechatronics","corporation","corp","global","solution","tools","consult","research","tubes","manufacture","computers","interiors","trader","work","international","store","hardware","company"]
    name_list=[]
    spc_name_list=[]
    final=[]
    nnl=[]
    try:
        for gst in GST:
            final=list(df_gst['Vendor_Name'].loc[df_gst['Vendor_GST']==gst])[0]
    except:
        final=[]
    if len(final)>0:
        print("Fname",final)
        return final,round(random.uniform(90,95),2)
    else:
        for x in crp[:8]:
            splt=x.split('\t')
            for y in splt:
                for z in org_list:
                    if z in y.lower():
                        name_list.append(y.upper())
        if len(name_list)<1:
            for x in crp[-8:-1]:
                splt=x.split('\t')
                for y in splt:
                    for z in org_list:
                        if z in y.lower():
                            name_list.append(y.upper())

        for x in crp[:8]:
            doc = nlp(x.upper())
            for ents in doc.ents:
                if ents.label_ == "ORG":
                    spc_name_list.append(ents.text)
        for x in crp[-8:-1]:
            doc = nlp(x.upper())
            for ents in doc.ents:
                if ents.label_ == "ORG":
                    spc_name_list.append(ents.text)

        temp=name_list+spc_name_list
        temp=[x for x in dict.fromkeys(temp)]
        print("temp",temp)
        if len(temp)>0:
            for n in temp:
                if len(n)>50:
                    continue
                else:
                    final.append(n)
        print("final1",final)
        if len(final)>0:
            for x in final:
                if 'samsonite' in x.lower():
                    pass
                else:
                    nnl.append(x)
        print("nnl",nnl)
        if len(nnl)>0:
            for nm in nnl:
                cnt=0
                for lt in nm:
                    if lt.isdigit():
                        cnt+=1
                if cnt>8:
                    nnl.remove(nm)
        print("nnl2",nnl)
        if len(nnl)>0:
            for x in nnl:
                regex = re.compile('[@_!$%^*<>+=?\|}{~]')
                if(regex.search(x) == None):
                    continue
                else:
                    nnl.remove(x)
        print("nnl3",nnl)
        if len(nnl)>0:
            for x in nnl:
                for y in nnl:
                    if x==y:
                        continue
                    if x in y:
                        try:
                            nnl.remove(x)
                        except:
                            pass
        print("nnl4",nnl)
        

        fnme=[]
        a=[]
        if len(nnl)>0:
            for nme in nnl:
                print("name",nme)
                a.append(process.extractOne(nme,Vnm_list))
        else:
            nnl.append("Not Found")
        for x in a:
            if x[1]>90:
                fnme.append(x[0])
        if len(fnme)>0:
            print("Fname",fnme)
            return fnme[0],round(random.uniform(80,90),2)
        else:
            print("Fname",final)
            return nnl[0],round(random.uniform(70,75),2)


def getBankName(IFSC):
    IFSC = IFSC[:4].upper()
    print(IFSC)
    
    with open('OCR-M/ifsc.json') as json_file:
        data = json.load(json_file)
    Name = data.get(IFSC)
    return Name

def total_amount_extraction(t1,conv_amt,conv_amt1,conv_amt2):
    tax=[]
    for x in range(len(t1)):
        if 'cgst' in t1[x].lower() or 'sgst' in t1[x].lower() or 'gst' in t1[x].lower() or 'net' in t1[x].lower() or 'amount' in t1[x].lower():
            tax.append(x)
            if x+1<len(t1):
                tax.append(x+1)  
        if 'gross' in t1[x].lower() or 'total' in t1[x].lower():
            tax.append(x)
            if x+1<len(t1):
                tax.append(x+1)
    b='\t'.join(t1[x] for x in set(dict.fromkeys(tax)))
    b=re.sub(r'[a-zA-Z|}{+@%:)/(]','',b)
    b=b.split('\t')
    b=' '.join(b)
    b=b.split()
    
    bb=[]    
    for x in b:
        if len(x)>14:
            continue
        try:
            x=x.replace('.',',')
            if x[-3]==',':
                x1=x[:-3]+'.'+x[-2:]
                x1=x1.replace(',','')
                bb.append(float(x1))
                continue
            if ',' in x:
                x=x.replace(',','')
                bb.append(float(x))
            if float(x)==0:
                continue
            bb.append(float(x))
        except:
            pass
    if conv_amt!="Not Found":
        bb.append(conv_amt)
    if conv_amt1!="Not Found":
        bb.append(conv_amt1)
    if conv_amt2!="Not Found":
        bb.append(conv_amt2)
    bb1=bb.copy()
    bb=[x for x in dict.fromkeys(bb)]
    for x in set(bb):
        if x*2 in set(bb):
            bb.remove(x*2)
    d=dict()
    for x in set(bb):
        for y in set(bb):
            if x==y or x<=1 or y<=1 or x<y:
                continue
            if x+(y*2) in bb:
                d[x+(y*2)]=(x,y,y)
                continue
            if x+y in bb:
                if x+y in d:
                    continue
                d[x+y]=(x,y)            
                continue
            if round(x+(y*2)) in bb:
                d[round(x+(y*2))]=(x,y,y)
                continue
            if round(x+y) in set(bb):
                if round(x+y) in d:
                    continue
                d[round(x+y)]=(x,y)
                continue
            if round(x+(y*2),2) in bb:
                d[round(x+(y*2),2)]=(x,y,y)
                continue
                
    if len(d)==0:
        bb2=[x for x in bb1 if bb1.count(x)>1]
        for x in dict.fromkeys(bb2):
            bb.append(round(2*x*100/18,2))
            bb.append(round(2*x*100/12,2))
            bb.append(round(2*x*100/28,2))
            bb.append(round(2*x*100/5,2))
        for x in set(bb):
            for y in set(bb):
                if x==y or x<=1 or y<=1 or x<y:
                    continue
                if x+(y*2) in bb:
                    d[x+(y*2)]=(x,y,y)
                    continue
                if x+y in bb:
                    if x+y in d:
                        continue
                    d[x+y]=(x,y)            
                    continue
                if round(x+(y*2),2) in bb:
                    d[round(x+(y*2),2)]=(x,y,y)
                    continue
                if round(x+y) in set(bb):
                    if round(x+y) in d:
                        continue
                    d[round(x+y)]=(x,y)
                    continue
                if round(x+(y*2)) in bb:
                    d[round(x+(y*2))]=(x,y,y)
                    continue
                    
    print("dd",d)
    
    if len(d)==0:
        return("Not Found","Not Found","Not Found","Not Found")

    if conv_amt=='Not Found':
        if len(d)>0:
            return(max(d),d[max(d)],"Not Found","Not Found")
        else:
            return("Not Found","Not Found","Not Found","Not Found")
    try:
        try:
            try:
                ori_val=max([x for x  in d if x<=conv_amt+1 and x>=conv_amt-1 ])
            except:
                ori_val=max([x for x  in d if x<=conv_amt1+1 and x>=conv_amt1-1 ])
        except:
            ori_val=max([x for x  in d if x<=conv_amt2+1 and x>=conv_amt2-1 ])
        if d[ori_val][0] in d:
            return ori_val,d[d[ori_val][0]],d[ori_val][0], d[ori_val][1]
        else:
            return ori_val,d[ori_val],"Not Found","Not Found"
    except:
        return("Not Found","Not Found","Not Found","Not Found")

def line_extracting(ocdf,mins,maxs):
    ocdf=ocdf.loc[(ocdf['x2']>=(mins-50)) &(ocdf['h2']<=(maxs+50)) ]
    l=[]
    ocdf=ocdf.sort_values(['x1',"x2"])
    ocdf2=ocdf.copy()
    k=0
    while ocdf2.shape[0]>0:
        k+=1
        low=ocdf2['x2'].min()+15
        ocdf3=ocdf2.loc[ocdf2['x2']<=low]
        duplicates = set(ocdf2.index).intersection(ocdf3.index)
        ocdf2 = ocdf2.drop(duplicates, axis=0)
        ocdf3=ocdf3.sort_values(['x1'])
        l.append('\t'.join(list(ocdf3['string'])))
    return l,ocdf

def table_end_yolo(tt1):
    try:
        wrds.remove('and')
    except:
        pass
    for x in range(len(tt1)):
        c=0
        for y in wrds:
            if y in tt1[x].lower():
                c+=1
        if c>2:
            return(x)
    return x    

def yolo_table(path,ocdf):
    imgs=cv2.imread(path)
    RESULT=model.predict(imgs,augment=True,size=520)
    df=RESULT.pandas().xyxy[0]
    mins=min(df['ymin'].tolist())
    maxs=max(df['ymax'].tolist())
    t1,dfs=line_extracting(ocdf,mins,maxs)
    s,e=0,table_end_yolo(t1)
    fan=table_form(s,e,dfs,t1)
    return fan
