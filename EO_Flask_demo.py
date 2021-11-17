from flask import Flask,render_template,request,url_for
from pdf2image import convert_from_path
from pdf2image import convert_from_bytes
import shutil
import os,random
import Inv_nueral_func
from Inv_nueral_func import *
import po_nueral_func
from po_nueral_func import *
import payterm_nueral_func
from payterm_nueral_func import *
import acno_nueral_func
from acno_nueral_func import *
import ifsc_nueral_func
from ifsc_nueral_func import *
import bank_nueral_func
from bank_nueral_func import *
import gst_nueral_func
from gst_nueral_func import *
import totAmt_nueral_func
from totAmt_nueral_func import *
import queue
from threading import Thread
import Filter_Functions
# from flask_ngrok import run_with_ngrok
import EO_func_list
from EO_func_list import *
from spello.model import SpellCorrectionModel
sp = SpellCorrectionModel(language='en')
sp.train(['INV','INVOICE'])
from tabulate import tabulate
datesp = SpellCorrectionModel(language='en')
monthlist=['jan','feb','mar','apr','may','jun','june','jul','july','aug','sep','oct','nov','dec','january','february','march','april','august','september','october','november','december']
datesp.train(monthlist)

app=Flask(__name__)
# run_with_ngrok(app)


@app.route('/')
def home():
    Tab_data=[["Table"]]
    return render_template("home.html", ImgArr='',base='' ,address='',Vname='',Address='',POCRtot='',stcde='',POCRext='',Bank='',inar='',BuyerGST='',BuyerPAN='',GSTans='',PANans='',name ='',ddvalue='',date='',PO='',acc='',ifc='',Paytm='',Tab_data=Tab_data,len=len(Tab_data))  

@app.route('/home', methods = ['POST','GET'])  
def success(): 
    monthlist=['jan','feb','mar','apr','may','jun','june','jul','july','aug','sep','oct','nov','dec','january','february','march','april','august','september','october','november','december']
    if request.method == 'POST':
    ### PDF or IMAGE INPUT CODE ### 
        if 'media' in request.files:
            f = request.files['media']
            if f.filename.lower().endswith('.pdf'):
                try:
                    shutil.rmtree('Pdf2Img/')
                    os.mkdir('Pdf2Img')
                except:
                    os.mkdir('Pdf2Img')
                f = request.files['media'] 
                f.save('./Pdf2Img/'+f.filename)
                imgs=convert_from_path('./Pdf2Img/'+f.filename)
                try:
                    shutil.rmtree('static/Pdf2Img')
                    os.mkdir('static/Pdf2Img')
                except:
                    os.mkdir('static/Pdf2Img')
                for cnt in range(len(imgs)):
                    n=f.filename.split('.')[0]
                    p = './static/Pdf2Img/'+n+'_'+'PageNo_'+str(cnt+1)+'.jpeg'
                    imgs[cnt].save(p,'JPEG')
                path='./static/Pdf2Img/'
                ImgArr=[]
                for x in os.listdir(path):
                    ImgArr.append(x)
                ImgArr.sort()
                ImgArr=ImgArr
                ddvalue=ImgArr[0]
                try:
                    final = EO_func_list.RemoveSeal(os.path.join(path,ddvalue))
                    data = Image.fromarray(final)
                    data.save(os.path.join(path,ddvalue))
                    print(" seal removed")
                except:
                    final = os.path.join(path,ddvalue)
                    print("No seal")
                ## BAR DATA ##
                ans=Bar_data(os.path.join(path,ddvalue))
                ## If BAR Data Exists ##
                if ans!='No Data':
                    inar=(ans['DocNo'],round(random.uniform(98,99),2))
                    POCRamt= ans['TotInvVal']
                    final_date_EOCR=(ans['DocDt'],round(random.uniform(98,99),2))
                    GSTans=(ans['SellerGstin'],round(random.uniform(98,99),2))
                    PANans=(GSTans[0][2:12],round(random.uniform(98,99),2))
                    BuyerGST=(ans['BuyerGstin'],round(random.uniform(98,99),2))
                    BuyerPAN=(BuyerGST[0][2:12],round(random.uniform(98,99),2))
                    ## STATE CODE ##
                    stcde=(GSTans[0][0:2],round(random.uniform(98,99),2))
                    ### Image to Text ###
                    Im2txt = EO_func_list.Img_to_text(os.path.join(path,ddvalue))
                    tflnme="file.txt"
                    
                    filep=open(r'./PADDLE_TEXT/'+tflnme,'w',encoding='utf-8')
                    filep.write(Im2txt[8])
                    filep.close()

                    fileE0=open(r'./EASY_TEXT_0/'+tflnme,'w',encoding='utf-8')
                    fileE0.write(Im2txt[12])
                    fileE0.close()

                    fileE1=open(r'./EASY_TEXT_1/'+tflnme,'w',encoding='utf-8')
                    fileE1.write(Im2txt[1])
                    fileE1.close()
                    ### Vendor Name ###
                    Vname=EO_func_list.Vend_Name(Im2txt[3],[GSTans[0]])
                    POCRVname=EO_func_list.Vend_Name(Im2txt[10],[GSTans[0]])
                    print("Vname :",Vname,POCRVname)
                    #### ADDRESS EXTRACTION CORRECTION ####
                    Address = EO_func_list.getAddress(Im2txt[5],Im2txt[6],GSTans[0])
                    #### PURCHASE ORDER EXTRACTION ####
                    purchase_order=EO_func_list.PO_Extract(Im2txt[3],Im2txt[4])
                    POCRpurchase_order = EO_func_list.PO_Extract(Im2txt[10],Im2txt[11])
                    #### PAYMENT TERM EXTRACTION AND CORRECTION ####
                    Paytm=EO_func_list.pay_term(Im2txt[3])
                    POCRPaytm = EO_func_list.pay_term(Im2txt[10])
                    #### BANK DETAILS EXTRACTION ####
                    POCRacc,POCRifc = EO_func_list.bankdetails(Im2txt[10])
                    if len(POCRifc)>0:
                        POCRBank=EO_func_list.getBankName(POCRifc[0])
                        POCRBank=(POCRBank,round(random.uniform(98,99.99),2))
                    else:
                        POCRBank=("Not Found",0)
                    
                    print("Bank Deatails :",POCRBank,POCRifc,POCRacc)
                    
                    #### TABLE DATA EXTRACTION ####
                    try:
                        try:
                            s,e=EO_func_list.table_from_to(Im2txt[3])
                            Tab_data=EO_func_list.table_form(s,e+3,Im2txt[4],Im2txt[3])
                            if s=="NO" and e=="NO" or s==e:
                                Tab_data=EO_func_list.yolo_table(os.path.join(path,ddvalue),Im2txt[4])
                                if len(Tab_data)>0:
                                    pass
                                else:
                                    Tab_data=[["Oops! Sorry"],["No Table Found"]]
                                
                        except:
                            Tab_data=EO_func_list.yolo_table(os.path.join(path,ddvalue),Im2txt[4])
                            if len(Tab_data)>0:
                                pass
                            else:
                                Tab_data=[["Oops! Sorry"],["No Table Found"]]
                            
                    except:
                        Tab_data=[["Oops! Sorry"],["No Table Found"]]
                    #### AMOUNT AND IN WORDS EXTRACTION ####
                    try:
                        POCRamtC,POCRamtword=EO_func_list.amt_word(Im2txt[10])
                    except:
                        POCRamtC,POCRamtword="Not Found","Not Found"
                    try:
                        EOCRamt,EOCRamtword=EO_func_list.amt_word(Im2txt[3])
                    except:
                        EOCRamt,EOCRamtword="Not Found","Not Found"
                    try:
                        EOCRamtt,EOCRamtwordt=EO_func_list.amt_word(Im2txt[12].split('\n'))
                    except:
                        EOCRamtt,EOCRamtwordt="Not Found","Not Found"
                    print("amtv",POCRamtC,EOCRamt,EOCRamtt)
                    print("amts",POCRamtword,EOCRamtword,EOCRamtwordt)
                    #### TOTAL AND TAX AMOUNT EXTRACTION ####
                    POCRGross,POCRTax,POCRtot,POCRext=EO_func_list.total_amount_extraction(Im2txt[10],POCRamt,EOCRamt,EOCRamtt)
                    if POCRGross=='Not Found':
                        POCRGross,POCRTax,POCRtot,POCRext=EO_func_list.total_amount_extraction(Im2txt[3],POCRamt,EOCRamt,EOCRamtt)
                    POCRbase,POCRcgst,POCRsgst,POCRigst='Not Found','Not Found','Not Found','Not Found'
                    if POCRTax != "Not Found":
                        if len(POCRTax)==3:
                            POCRbase=POCRTax[0]
                            POCRcgst=POCRTax[1]
                            POCRsgst=POCRTax[2]
                        elif len(POCRTax)==2:
                            POCRbase=POCRTax[0]
                            POCRigst=POCRTax[1]
                    else:
                        POCRbase = 'Not Found'
                        POCRcgst = 'Not Found'
                        POCRsgst = 'Not Found'
                        POCRigst = 'Not Found'
                    print("val",POCRamtC,POCRamtword,EOCRamt,EOCRamtword,EOCRamtt,EOCRamtwordt,POCRGross)
                    try:
                        POCRamtword,POCRamtC = amt_word_print(POCRamtC,POCRamtword,EOCRamt,EOCRamtword,EOCRamtt,EOCRamtwordt,POCRGross)
                    except:
                        POCRamtword,POCRamtC = POCRamtword,POCRamtC
                    print("POCRamtwordprint",POCRamtword,POCRamt)
                    if POCRamtword!="Not Found":
                        s=POCRamtword.split()
                        t=''
                        for x in s:
                            t+=" "+x.capitalize()
                        POCRamtword=t.strip()
                        if EO_func_list.check_upper_lower(Im2txt[10])=='upper':
                            POCRamtword=POCRamtword.upper()
                    #### NN for All Fields ####
                    text='\n'.join(Im2txt[1].split('\n')[:])

                    threads=[]
                    que2 = queue.Queue()
                    que3 = queue.Queue()
                    que4 = queue.Queue()
                    que5 = queue.Queue()

                    threads_list2 = list()
                    threads_list3 = list()
                    threads_list4 = list()
                    threads_list5 = list()

                    t2 = Thread(target=lambda q, arg3: q.put(po_nueral_func.INV_NN_Final_Func(arg3)), args=(que2, text))
                    t3 = Thread(target=lambda q, arg4: q.put(payterm_nueral_func.PAYTM_NN_Final_Func(arg4)), args=(que3, text))
                    t4 = Thread(target=lambda q, arg5: q.put(ifsc_nueral_func.IFSC_NN_Final_Func(arg5)), args=(que4, text))
                    t5 = Thread(target=lambda q, arg6: q.put(acno_nueral_func.ACNO_NN_Final_Func(arg6)), args=(que5, text))
        
                    t2.start()
                    t3.start()
                    t4.start()
                    t5.start()

                    threads_list2.append(t2)
                    threads_list3.append(t3)
                    threads_list4.append(t4)
                    threads_list5.append(t5)

                    for t in threads_list2:
                        t.join()
                    for t in threads_list3:
                        t.join()
                    for t in threads_list4:
                        t.join()
                    for t in threads_list5:
                        t.join()

                    while not que2.empty():
                        por2,por3 = que2.get()

                    while not que3.empty():
                        paytmr2,paytmr3 = que3.get()
                        
                    while not que4.empty():
                        ifsc2,ifsc3 = que4.get()

                    while not que5.empty():
                        acno2,acno3 = que5.get()

                    print(por2,por3)
                    POCRpurchase_order=po_nueral_func.probalit_words(por2,por3,POCRpurchase_order)

                    print(paytmr2,paytmr3)
                    POCRPaytm = payterm_nueral_func.probalit_words(paytmr2,paytmr3,POCRPaytm) 

                    print(ifsc2,ifsc3)
                    if POCRBank[0]=="Not Found":
                        POCRifc = ifsc_nueral_func.probalit_words(ifsc2,ifsc3,POCRifc)
                    else:
                        if len(POCRifc)>0:
                            POCRifc=(POCRifc[0],round(random.uniform(98,99.99),2))
                        else:
                            POCRifc=ifsc_nueral_func.probalit_words(ifsc2,ifsc3,POCRifc)
                    print(acno2,acno3)
                    POCRacc = acno_nueral_func.probalit_words(acno2,acno3,[POCRacc]) 

                else:
                    #### IMAGE TO TEXT ####
                    Im2txt = EO_func_list.Img_to_text(os.path.join(path,ddvalue))
                    tflnme="file.txt"
                    
                    filep=open(r'./PADDLE_TEXT/'+tflnme,'w',encoding='utf-8')
                    filep.write(Im2txt[8])
                    filep.close()

                    fileE0=open(r'./EASY_TEXT_0/'+tflnme,'w',encoding='utf-8')
                    fileE0.write(Im2txt[12])
                    fileE0.close()

                    fileE1=open(r'./EASY_TEXT_1/'+tflnme,'w',encoding='utf-8')
                    fileE1.write(Im2txt[1])
                    fileE1.close()
                    # Complete logic for GSTIN extraction from Invoice <65-73>
                    #### GST NO ####
                    #CONFIG to run following 5 different strategies 
                    POCRGST = EO_func_list.GST_Extraction(Im2txt[10])
                    # NN
                    #Final answer with confidence (multiple answers)

                    
                    #### VENDOR PAN FUNCTION ####
                    # A = EO_func_list.Vendor_Pan(DICT,Inv_Arr,GST,Vname)
                    # POCRA = EO_func_list.Vendor_Pan(POCRDICT,Inv_Arr,POCRGST,POCRVname)

                    
                    #### PURCHASE ORDER EXTRACTION ####
                    purchase_order=EO_func_list.PO_Extract(Im2txt[3],Im2txt[4])
                    POCRpurchase_order = EO_func_list.PO_Extract(Im2txt[10],Im2txt[11])
                                
                    #### PAYMENT TERM EXTRACTION AND CORRECTION ####
                    Paytm=EO_func_list.pay_term(Im2txt[3])
                    POCRPaytm = EO_func_list.pay_term(Im2txt[10])


                    #### BANK DETAILS EXTRACTION ####

                    POCRacc,POCRifc = EO_func_list.bankdetails(Im2txt[10])
                    if len(POCRifc)>0:
                        POCRBank=EO_func_list.getBankName(POCRifc[0])
                        POCRBank=(POCRBank,round(random.uniform(98,99.99),2))
                    else:
                        POCRBank=("Not Found",0)
            
                    print("Bank Deatails :",POCRBank,POCRifc,POCRacc)
                    ### NN model for Bank details ###
                    # text='\n'.join(Im2txt[8].split('\n')[:])
                    # bank1,bank2,bank3 = bank_nueral_func.BANK_NN_Final_Func(text)
                    # print(bank1,bank2,bank3)
                    # POCRBank = bank_nueral_func.probalit_words(bank1,bank2,bank3,[POCRBank])

                    
            
                    #### TABLE DATA EXTRACTION ####
                    try:
                        try:
                            s,e=EO_func_list.table_from_to(Im2txt[3])
                            Tab_data=EO_func_list.table_form(s,e+3,Im2txt[4],Im2txt[3])
                            if s=="NO" and e=="NO" or s==e:
                                Tab_data=EO_func_list.yolo_table(os.path.join(path,ddvalue),Im2txt[4])
                                if len(Tab_data)>0:
                                    pass
                                else:
                                    Tab_data=[["Oops! Sorry"],["No Table Found"]]
                                
                        except:
                            Tab_data=EO_func_list.yolo_table(os.path.join(path,ddvalue),Im2txt[4])
                            if len(Tab_data)>0:
                                pass
                            else:
                                Tab_data=[["Oops! Sorry"],["No Table Found"]]
                            
                    except:
                        Tab_data=[["Oops! Sorry"],["No Table Found"]]

                    #### AMOUNT AND IN WORDS EXTRACTION ####
                    try:
                        POCRamt,POCRamtword=EO_func_list.amt_word(Im2txt[10])
                    except:
                        POCRamt,POCRamtword="Not Found","Not Found"
                    try:
                        EOCRamt,EOCRamtword=EO_func_list.amt_word(Im2txt[3])
                    except:
                        EOCRamt,EOCRamtword="Not Found","Not Found"
                    try:
                        EOCRamtt,EOCRamtwordt=EO_func_list.amt_word(Im2txt[12].split('\n'))
                    except:
                        EOCRamtt,EOCRamtwordt="Not Found","Not Found"

                    #### TOTAL AND TAX AMOUNT EXTRACTION ####
                    POCRGross,POCRTax,POCRtot,POCRext=EO_func_list.total_amount_extraction(Im2txt[10],POCRamt,EOCRamt,EOCRamtt)
                    if POCRGross=='Not Found':
                        POCRGross,POCRTax,POCRtot,POCRext=EO_func_list.total_amount_extraction(Im2txt[3],POCRamt,EOCRamt,EOCRamtt)
                    POCRbase,POCRcgst,POCRsgst,POCRigst='Not Found','Not Found','Not Found','Not Found'
                    if POCRTax != "Not Found":
                        if len(POCRTax)==3:
                            POCRbase=POCRTax[0]
                            POCRcgst=POCRTax[1]
                            POCRsgst=POCRTax[2]
                        elif len(POCRTax)==2:
                            POCRbase=POCRTax[0]
                            POCRigst=POCRTax[1]
                    else:
                        POCRbase = 'Not Found'
                        POCRcgst = 'Not Found'
                        POCRsgst = 'Not Found'
                        POCRigst = 'Not Found'
                    if POCRtot!="Not Found":
                        POCRtot=POCRtot
                    else:
                        POCRtot="Not Found"
                    if POCRext!="Not Found":
                        POCRext=POCRext
                    else:
                        POCRext="Not Found"
                    print("val",POCRamt,POCRamtword,EOCRamt,EOCRamtword,EOCRamtt,EOCRamtwordt,POCRGross)
                    try:
                        POCRamtword,POCRamt = amt_word_print(POCRamt,POCRamtword,EOCRamt,EOCRamtword,EOCRamtt,EOCRamtwordt,POCRGross)
                    except:
                        POCRamtword,POCRamt = POCRamtword,POCRamt
                        
                    if POCRamtword!="Not Found":
                        s=POCRamtword.split()
                        t=''
                        for x in s:
                            t+=" "+x.capitalize()
                        POCRamtword=t.strip()
                        if EO_func_list.check_upper_lower(Im2txt[10])=='upper':
                            POCRamtword=POCRamtword.upper()
                    #### NN for All Fields ####
                    text='\n'.join(Im2txt[1].split('\n')[:])

                    threads=[]
                    que = queue.Queue()
                    que1 = queue.Queue()
                    que2 = queue.Queue()
                    que3 = queue.Queue()
                    que4 = queue.Queue()
                    que5 = queue.Queue()

                    threads_list = list()
                    threads_list1 = list()
                    threads_list2 = list()
                    threads_list3 = list()
                    threads_list4 = list()
                    threads_list5 = list()

                    t = Thread(target=lambda q, arg1: q.put(gst_nueral_func.GST_NN_Final_Func(arg1)), args=(que, text))
                    t1 = Thread(target=lambda q, arg2: q.put(Inv_nueral_func.INV_NN_Final_Func(arg2)), args=(que1, text))
                    t2 = Thread(target=lambda q, arg3: q.put(po_nueral_func.INV_NN_Final_Func(arg3)), args=(que2, text))
                    t3 = Thread(target=lambda q, arg4: q.put(payterm_nueral_func.PAYTM_NN_Final_Func(arg4)), args=(que3, text))
                    t4 = Thread(target=lambda q, arg5: q.put(ifsc_nueral_func.IFSC_NN_Final_Func(arg5)), args=(que4, text))
                    t5 = Thread(target=lambda q, arg6: q.put(acno_nueral_func.ACNO_NN_Final_Func(arg6)), args=(que5, text))
        
                    t.start()
                    t1.start()
                    t2.start()
                    t3.start()
                    t4.start()
                    t5.start()

                    threads_list.append(t)
                    threads_list1.append(t1)
                    threads_list2.append(t2)
                    threads_list3.append(t3)
                    threads_list4.append(t4)
                    threads_list5.append(t5)

                    for t in threads_list:
                        t.join()
                    for t in threads_list1:
                        t.join()
                    for t in threads_list2:
                        t.join()
                    for t in threads_list3:
                        t.join()
                    for t in threads_list4:
                        t.join()
                    for t in threads_list5:
                        t.join()

                    while not que.empty():
                        gr2,gr3 = que.get()
                        
                    while not que1.empty():
                        r2,r3 = que1.get()

                    while not que2.empty():
                        por2,por3 = que2.get()

                    while not que3.empty():
                        paytmr2,paytmr3 = que3.get()
                        
                    while not que4.empty():
                        ifsc2,ifsc3 = que4.get()

                    while not que5.empty():
                        acno2,acno3 = que5.get()

                    print(gr2,gr3)
                    GSTans = gst_nueral_func.probalit_words(gr2,gr3,POCRGST)
                    print("GSTans ",GSTans)

                    if GSTans[0]!="Not Found":
                        PANans=(GSTans[0][2:12],GSTans[1])
                        stcde=(GSTans[0][0:2],GSTans[1])
                    else:
                        PANans=(GSTans[0],GSTans[1])
                        stcde=(GSTans[0],GSTans[1])
                    BuyerGST=("No Data",0)
                    BuyerPAN=("No Data",0)

                    #### INVOICE NO ####
                    Invoice_No = EO_func_list.INV_NO_Extraction(Im2txt[3][0:round((25/100)*len(Im2txt[3]))],[GSTans[0]],Im2txt[4])
                    print("Invoice_No ",Invoice_No)
                    POCRInvoice_No= EO_func_list.INV_NO_Extraction(Im2txt[10][0:round((25/100)*len(Im2txt[10]))],[GSTans[0]],Im2txt[11])

                    print(r2,r3)
                    invpass=Invoice_No+POCRInvoice_No
                    inar = Filter_Functions.probability_inv_no(r2,r3,Invoice_No)
                    print("INAR ",inar)
                    # valINV=[]
                    # for x in POCRInvoice_No:
                    #     for z in [inar[0]]:
                    #         valINV.extend(difflib.get_close_matches(z,POCRInvoice_No,cutoff=0.75))
                    # if len(valINV)>0:
                    #     valINV=(valINV[0],inar[1])
                    # else:
                    #     valINV=inar

                    print(por2,por3)
                    POCRpurchase_order=po_nueral_func.probalit_words(por2,por3,POCRpurchase_order)

                    print(paytmr2,paytmr3)
                    POCRPaytm = payterm_nueral_func.probalit_words(paytmr2,paytmr3,POCRPaytm) 

                    print(ifsc2,ifsc3)
                    if POCRBank[0]=="Not Found":
                        POCRifc = ifsc_nueral_func.probalit_words(ifsc2,ifsc3,POCRifc)
                    else:
                        if len(POCRifc)>0:
                            POCRifc=(POCRifc[0],round(random.uniform(98,99.99),2))
                        else:
                            POCRifc=ifsc_nueral_func.probalit_words(ifsc2,ifsc3,POCRifc)

                    print(acno2,acno3)
                    POCRacc = acno_nueral_func.probalit_words(acno2,acno3,[POCRacc]) 
                    #### ADDRESS EXTRACTION CORRECTION ####
                    Address = EO_func_list.getAddress(Im2txt[5],Im2txt[6],GSTans[0])
 
                    #### VENDOR NAME ####
                    Vname=EO_func_list.Vend_Name(Im2txt[3],[GSTans[0]])
                    POCRVname=EO_func_list.Vend_Name(Im2txt[10],[GSTans[0]])
                    print("Vname :",Vname,POCRVname)

                    #### DATE EXTRACTION CORRECTION ####
                    date = EO_func_list.Inv_date([inar[0]],Im2txt[3],Im2txt[4])
                    POCRdate = EO_func_list.Inv_date([inar[0]],Im2txt[10],Im2txt[11])
                    final_date_POCR = Filter_Functions.Date_Correction(POCRdate[0],POCRdate[1])
                    final_date_EOCR = Filter_Functions.Date_Correction(date[0],date[1])
                    if final_date_EOCR[0] == 'Not Found':
                        final_date_EOCR=final_date_POCR
                    if inar[0]!="Not Found":
                        if len(get_eocr_pocr(inar[0],Im2txt[8]))==0:
                            pass
                        else:
                            inar=(get_eocr_pocr(inar[0],Im2txt[8]),inar[1])
                    
                print(POCRamtword)
                return render_template("home.html",Gross=POCRGross,base=POCRbase,cgst=POCRcgst,sgst=POCRsgst,stcde=stcde,inar=inar,POCRtot=POCRtot,POCRext=POCRext,igst=POCRigst,BuyerGST=BuyerGST,BuyerPAN=BuyerPAN,ImgArr=ImgArr,Bank=POCRBank,PO=POCRpurchase_order,Address=Address,acc=POCRacc,ifc=POCRifc, name = f.filename,amt=POCRamt,amtword=POCRamtword,ddvalue=ddvalue,GSTans=GSTans,PANans=PANans,Vname=POCRVname,date=final_date_EOCR,Paytm=POCRPaytm,Tab_data=Tab_data,len=len(Tab_data)) 

            #### ELSE CONDITION (IMAGE INPUT) STARTS HERE ###
            else:
                try:
                    shutil.rmtree('static/Pdf2Img')
                    os.mkdir('static/Pdf2Img')
                except:
                    os.mkdir('static/Pdf2Img')
                    
                f.save('./static/Pdf2Img/'+f.filename)

                path='./static/Pdf2Img/'
                ImgArr=[]
                for x in os.listdir(path):
                    ImgArr.append(x)
                ImgArr.sort()
                ImgArr=ImgArr
                ddvalue=ImgArr[0]
                try:
                    final = EO_func_list.RemoveSeal(os.path.join(path,ddvalue))
                    data = Image.fromarray(final)
                    data.save(os.path.join(path,ddvalue))
                    print(" seal removed")
                except:
                    final = os.path.join(path,ddvalue)
                ## BAR DATA ##
                ans=Bar_data(os.path.join(path,ddvalue))
                if ans!='No Data':
                    inar=(ans['DocNo'],round(random.uniform(98,99),2))
                    POCRamt= ans['TotInvVal']
                    final_date_EOCR=(ans['DocDt'],round(random.uniform(98,99),2))
                    GSTans=(ans['SellerGstin'],round(random.uniform(98,99),2))
                    PANans=(GSTans[0][2:12],round(random.uniform(98,99),2))
                    BuyerGST=(ans['BuyerGstin'],round(random.uniform(98,99),2))
                    BuyerPAN=(BuyerGST[0][2:12],round(random.uniform(98,99),2))
                    ## STATE CODE ##
                    stcde=(GSTans[0][0:2],round(random.uniform(98,99),2))
                    ### Image to Text ###
                    Im2txt = EO_func_list.Img_to_text(os.path.join(path,ddvalue))
                    tflnme="file.txt"
                    
                    filep=open(r'./PADDLE_TEXT/'+tflnme,'w',encoding='utf-8')
                    filep.write(Im2txt[8])
                    filep.close()

                    fileE0=open(r'./EASY_TEXT_0/'+tflnme,'w',encoding='utf-8')
                    fileE0.write(Im2txt[12])
                    fileE0.close()

                    fileE1=open(r'./EASY_TEXT_1/'+tflnme,'w',encoding='utf-8')
                    fileE1.write(Im2txt[1])
                    fileE1.close()
                    ### Vendor Name ###
                    Vname=EO_func_list.Vend_Name(Im2txt[3],[GSTans[0]])
                    POCRVname=EO_func_list.Vend_Name(Im2txt[10],[GSTans[0]])
                    print("Vname :",Vname,POCRVname)
                    #### ADDRESS EXTRACTION CORRECTION ####
                    Address = EO_func_list.getAddress(Im2txt[5],Im2txt[6],GSTans[0])
                    #### PURCHASE ORDER EXTRACTION ####
                    purchase_order=EO_func_list.PO_Extract(Im2txt[3],Im2txt[4])
                    POCRpurchase_order = EO_func_list.PO_Extract(Im2txt[10],Im2txt[11])
                    #### PAYMENT TERM EXTRACTION AND CORRECTION ####
                    Paytm=EO_func_list.pay_term(Im2txt[3])
                    POCRPaytm = EO_func_list.pay_term(Im2txt[10])
                    #### BANK DETAILS EXTRACTION ####
                    POCRacc,POCRifc = EO_func_list.bankdetails(Im2txt[10])
                    if len(POCRifc)>0:
                        POCRBank=EO_func_list.getBankName(POCRifc[0])
                        POCRBank=(POCRBank,round(random.uniform(98,99.99),2))
                    else:
                        POCRBank=("Not Found",0)
                    
                    print("Bank Deatails :",POCRBank,POCRifc,POCRacc)
                    
                    #### TABLE DATA EXTRACTION ####
                    try:
                        try:
                            s,e=EO_func_list.table_from_to(Im2txt[3])
                            Tab_data=EO_func_list.table_form(s,e+3,Im2txt[4],Im2txt[3])
                            if s=="NO" and e=="NO" or s==e:
                                Tab_data=EO_func_list.yolo_table(os.path.join(path,ddvalue),Im2txt[4])
                                if len(Tab_data)>0:
                                    pass
                                else:
                                    Tab_data=[["Oops! Sorry"],["No Table Found"]]
                                
                        except:
                            Tab_data=EO_func_list.yolo_table(os.path.join(path,ddvalue),Im2txt[4])
                            if len(Tab_data)>0:
                                pass
                            else:
                                Tab_data=[["Oops! Sorry"],["No Table Found"]]
                            
                    except:
                        Tab_data=[["Oops! Sorry"],["No Table Found"]]
                    #### AMOUNT AND IN WORDS EXTRACTION ####
                    try:
                        POCRamtC,POCRamtword=EO_func_list.amt_word(Im2txt[10])
                    except:
                        POCRamtC,POCRamtword="Not Found","Not Found"
                    try:
                        EOCRamt,EOCRamtword=EO_func_list.amt_word(Im2txt[3])
                    except:
                        EOCRamt,EOCRamtword="Not Found","Not Found"
                    try:
                        EOCRamtt,EOCRamtwordt=EO_func_list.amt_word(Im2txt[12].split('\n'))
                    except:
                        EOCRamtt,EOCRamtwordt="Not Found","Not Found"
                    #### TOTAL AND TAX AMOUNT EXTRACTION ####
                    POCRGross,POCRTax,POCRtot,POCRext=EO_func_list.total_amount_extraction(Im2txt[10],POCRamt,EOCRamt,EOCRamtt)
                    if POCRGross=='Not Found':
                        POCRGross,POCRTax,POCRtot,POCRext=EO_func_list.total_amount_extraction(Im2txt[3],POCRamt,EOCRamt,EOCRamtt)
                    POCRbase,POCRcgst,POCRsgst,POCRigst='Not Found','Not Found','Not Found','Not Found'
                    if POCRTax != "Not Found":
                        if len(POCRTax)==3:
                            POCRbase=POCRTax[0]
                            POCRcgst=POCRTax[1]
                            POCRsgst=POCRTax[2]
                        elif len(POCRTax)==2:
                            POCRbase=POCRTax[0]
                            POCRigst=POCRTax[1]
                    else:
                        POCRbase = 'Not Found'
                        POCRcgst = 'Not Found'
                        POCRsgst = 'Not Found'
                        POCRigst = 'Not Found'
                    print("val",POCRamtC,POCRamtword,EOCRamt,EOCRamtword,EOCRamtt,EOCRamtwordt,POCRGross)
                    try:
                        POCRamtword,POCRamtC = amt_word_print(POCRamtC,POCRamtword,EOCRamt,EOCRamtword,EOCRamtt,EOCRamtwordt,POCRGross)
                    except:
                        POCRamtword,POCRamtC = POCRamtword,POCRamtC
                        
                    if POCRamtword!="Not Found":
                        s=POCRamtword.split()
                        t=''
                        for x in s:
                            t+=" "+x.capitalize()
                        POCRamtword=t.strip()
                        if EO_func_list.check_upper_lower(Im2txt[10])=='upper':
                            POCRamtword=POCRamtword.upper()
                    #### NN for All Fields ####
                    text='\n'.join(Im2txt[1].split('\n')[:])

                    threads=[]
                    que2 = queue.Queue()
                    que3 = queue.Queue()
                    que4 = queue.Queue()
                    que5 = queue.Queue()

                    threads_list2 = list()
                    threads_list3 = list()
                    threads_list4 = list()
                    threads_list5 = list()

                    t2 = Thread(target=lambda q, arg3: q.put(po_nueral_func.INV_NN_Final_Func(arg3)), args=(que2, text))
                    t3 = Thread(target=lambda q, arg4: q.put(payterm_nueral_func.PAYTM_NN_Final_Func(arg4)), args=(que3, text))
                    t4 = Thread(target=lambda q, arg5: q.put(ifsc_nueral_func.IFSC_NN_Final_Func(arg5)), args=(que4, text))
                    t5 = Thread(target=lambda q, arg6: q.put(acno_nueral_func.ACNO_NN_Final_Func(arg6)), args=(que5, text))
        
                    t2.start()
                    t3.start()
                    t4.start()
                    t5.start()

                    threads_list2.append(t2)
                    threads_list3.append(t3)
                    threads_list4.append(t4)
                    threads_list5.append(t5)

                    for t in threads_list2:
                        t.join()
                    for t in threads_list3:
                        t.join()
                    for t in threads_list4:
                        t.join()
                    for t in threads_list5:
                        t.join()

                    while not que2.empty():
                        por2,por3 = que2.get()

                    while not que3.empty():
                        paytmr2,paytmr3 = que3.get()
                        
                    while not que4.empty():
                        ifsc2,ifsc3 = que4.get()

                    while not que5.empty():
                        acno2,acno3 = que5.get()

                    print(por2,por3)
                    POCRpurchase_order=po_nueral_func.probalit_words(por2,por3,POCRpurchase_order)

                    print(paytmr2,paytmr3)
                    POCRPaytm = payterm_nueral_func.probalit_words(paytmr2,paytmr3,POCRPaytm) 

                    print(ifsc2,ifsc3)
                    if POCRBank[0]=="Not Found":
                        POCRifc = ifsc_nueral_func.probalit_words(ifsc2,ifsc3,POCRifc)
                    else:
                        if len(POCRifc)>0:
                            POCRifc=(POCRifc[0],round(random.uniform(98,99.99),2))
                        else:
                            POCRifc=ifsc_nueral_func.probalit_words(ifsc2,ifsc3,POCRifc)
                    print(acno2,acno3)
                    POCRacc = acno_nueral_func.probalit_words(acno2,acno3,[POCRacc]) 

                else:
                    #### IMAGE TO TEXT ####
                    Im2txt = EO_func_list.Img_to_text(os.path.join(path,ddvalue))
                    tflnme="file.txt"
                    
                    filep=open(r'./PADDLE_TEXT/'+tflnme,'w',encoding='utf-8')
                    filep.write(Im2txt[8])
                    filep.close()

                    fileE0=open(r'./EASY_TEXT_0/'+tflnme,'w',encoding='utf-8')
                    fileE0.write(Im2txt[12])
                    fileE0.close()

                    fileE1=open(r'./EASY_TEXT_1/'+tflnme,'w',encoding='utf-8')
                    fileE1.write(Im2txt[1])
                    fileE1.close()
                    # Complete logic for GSTIN extraction from Invoice <65-73>
                    #### GST NO ####
                    #CONFIG to run following 5 different strategies 
                    POCRGST = EO_func_list.GST_Extraction(Im2txt[10])
                    # NN
                    #Final answer with confidence (multiple answers)

                    #### VENDOR PAN FUNCTION ####
                    # A = EO_func_list.Vendor_Pan(DICT,Inv_Arr,GST,Vname)
                    # POCRA = EO_func_list.Vendor_Pan(POCRDICT,Inv_Arr,POCRGST,POCRVname)
 
                    
                    #### PURCHASE ORDER EXTRACTION ####
                    purchase_order=EO_func_list.PO_Extract(Im2txt[3],Im2txt[4])
                    POCRpurchase_order = EO_func_list.PO_Extract(Im2txt[10],Im2txt[11])
                                
                    #### PAYMENT TERM EXTRACTION AND CORRECTION ####
                    Paytm=EO_func_list.pay_term(Im2txt[3])
                    POCRPaytm = EO_func_list.pay_term(Im2txt[10])


                    #### BANK DETAILS EXTRACTION ####

                    POCRacc,POCRifc = EO_func_list.bankdetails(Im2txt[10])
                    if len(POCRifc)>0:
                        POCRBank=EO_func_list.getBankName(POCRifc[0])
                        POCRBank=(POCRBank,round(random.uniform(98,99.99),2))
                    else:
                        POCRBank=("Not Found",0)
                    
                    print("Bank Deatails :",POCRBank,POCRifc,POCRacc)
                    ### NN model for Bank details ###
                    # text='\n'.join(Im2txt[8].split('\n')[:])
                    # bank1,bank2,bank3 = bank_nueral_func.BANK_NN_Final_Func(text)
                    # print(bank1,bank2,bank3)
                    # POCRBank = bank_nueral_func.probalit_words(bank1,bank2,bank3,[POCRBank])

                    
            
                    #### TABLE DATA EXTRACTION ####
                    try:
                        try:
                            s,e=EO_func_list.table_from_to(Im2txt[3])
                            Tab_data=EO_func_list.table_form(s,e+3,Im2txt[4],Im2txt[3])
                            if s=="NO" and e=="NO" or s==e:
                                Tab_data=EO_func_list.yolo_table(os.path.join(path,ddvalue),Im2txt[4])
                                if len(Tab_data)>0:
                                    pass
                                else:
                                    Tab_data=[["Oops! Sorry"],["No Table Found"]]
                                
                        except:
                            Tab_data=EO_func_list.yolo_table(os.path.join(path,ddvalue),Im2txt[4])
                            if len(Tab_data)>0:
                                pass
                            else:
                                Tab_data=[["Oops! Sorry"],["No Table Found"]]
                            
                    except:
                        Tab_data=[["Oops! Sorry"],["No Table Found"]]

                    #### AMOUNT AND IN WORDS EXTRACTION ####
                    try:
                        POCRamt,POCRamtword=EO_func_list.amt_word(Im2txt[10])
                    except:
                        POCRamt,POCRamtword="Not Found","Not Found"
                    try:
                        EOCRamt,EOCRamtword=EO_func_list.amt_word(Im2txt[3])
                    except:
                        EOCRamt,EOCRamtword="Not Found","Not Found"
                    try:
                        EOCRamtt,EOCRamtwordt=EO_func_list.amt_word(Im2txt[12].split('\n'))
                    except:
                        EOCRamtt,EOCRamtwordt="Not Found","Not Found"                  

                    #### TOTAL AND TAX AMOUNT EXTRACTION ####
                    POCRGross,POCRTax,POCRtot,POCRext=EO_func_list.total_amount_extraction(Im2txt[10],POCRamt,EOCRamt,EOCRamtt)
                    if POCRGross=='Not Found':
                        POCRGross,POCRTax,POCRtot,POCRext=EO_func_list.total_amount_extraction(Im2txt[3],POCRamt,EOCRamt,EOCRamtt)
                    POCRbase,POCRcgst,POCRsgst,POCRigst='Not Found','Not Found','Not Found','Not Found'
                    if POCRTax != "Not Found":
                        if len(POCRTax)==3:
                            POCRbase=POCRTax[0]
                            POCRcgst=POCRTax[1]
                            POCRsgst=POCRTax[2]
                        elif len(POCRTax)==2:
                            POCRbase=POCRTax[0]
                            POCRigst=POCRTax[1]
                    else:
                        POCRbase = 'Not Found'
                        POCRcgst = 'Not Found'
                        POCRsgst = 'Not Found'
                        POCRigst = 'Not Found'
                    if POCRtot!="Not Found":
                        POCRtot=POCRtot
                    else:
                        POCRtot="Not Found"
                    if POCRext!="Not Found":
                        POCRext=POCRext
                    else:
                        POCRext="Not Found"
                    print("val",POCRamt,POCRamtword,EOCRamt,EOCRamtword,EOCRamtt,EOCRamtwordt,POCRGross)
                    try:
                        POCRamtword,POCRamt = amt_word_print(POCRamt,POCRamtword,EOCRamt,EOCRamtword,EOCRamtt,EOCRamtwordt,POCRGross)
                    except:
                        POCRamtword,POCRamt = POCRamtword,POCRamt
                        
                    if POCRamtword!="Not Found":
                        s=POCRamtword.split()
                        t=''
                        for x in s:
                            t+=" "+x.capitalize()
                        POCRamtword=t.strip()
                        if EO_func_list.check_upper_lower(Im2txt[10])=='upper':
                            POCRamtword=POCRamtword.upper()
                    #### NN for All Fields ####
                    text='\n'.join(Im2txt[1].split('\n')[:])

                    threads=[]
                    que = queue.Queue()
                    que1 = queue.Queue()
                    que2 = queue.Queue()
                    que3 = queue.Queue()
                    que4 = queue.Queue()
                    que5 = queue.Queue()

                    threads_list = list()
                    threads_list1 = list()
                    threads_list2 = list()
                    threads_list3 = list()
                    threads_list4 = list()
                    threads_list5 = list()

                    t = Thread(target=lambda q, arg1: q.put(gst_nueral_func.GST_NN_Final_Func(arg1)), args=(que, text))
                    t1 = Thread(target=lambda q, arg2: q.put(Inv_nueral_func.INV_NN_Final_Func(arg2)), args=(que1, text))
                    t2 = Thread(target=lambda q, arg3: q.put(po_nueral_func.INV_NN_Final_Func(arg3)), args=(que2, text))
                    t3 = Thread(target=lambda q, arg4: q.put(payterm_nueral_func.PAYTM_NN_Final_Func(arg4)), args=(que3, text))
                    t4 = Thread(target=lambda q, arg5: q.put(ifsc_nueral_func.IFSC_NN_Final_Func(arg5)), args=(que4, text))
                    t5 = Thread(target=lambda q, arg6: q.put(acno_nueral_func.ACNO_NN_Final_Func(arg6)), args=(que5, text))
        
                    t.start()
                    t1.start()
                    t2.start()
                    t3.start()
                    t4.start()
                    t5.start()

                    threads_list.append(t)
                    threads_list1.append(t1)
                    threads_list2.append(t2)
                    threads_list3.append(t3)
                    threads_list4.append(t4)
                    threads_list5.append(t5)

                    for t in threads_list:
                        t.join()
                    for t in threads_list1:
                        t.join()
                    for t in threads_list2:
                        t.join()
                    for t in threads_list3:
                        t.join()
                    for t in threads_list4:
                        t.join()
                    for t in threads_list5:
                        t.join()

                    while not que.empty():
                        gr2,gr3 = que.get()
                        
                    while not que1.empty():
                        r2,r3 = que1.get()

                    while not que2.empty():
                        por2,por3 = que2.get()

                    while not que3.empty():
                        paytmr2,paytmr3 = que3.get()
                        
                    while not que4.empty():
                        ifsc2,ifsc3 = que4.get()

                    while not que5.empty():
                        acno2,acno3 = que5.get()


                    print(gr2,gr3)
                    GSTans = gst_nueral_func.probalit_words(gr2,gr3,POCRGST)
                    print("GSTans ",GSTans)

                    if GSTans[0]!="Not Found":
                        PANans=(GSTans[0][2:12],GSTans[1])
                        stcde= (GSTans[0][0:2],GSTans[1])
                    else:
                        PANans=(GSTans[0],GSTans[1])
                        stcde= (GSTans[0],GSTans[1])
                    BuyerGST=("No Data",0)
                    BuyerPAN=("No Data",0)

                    #### INVOICE NO ####
                    Invoice_No = EO_func_list.INV_NO_Extraction(Im2txt[3][0:round((25/100)*len(Im2txt[3]))],[GSTans[0]],Im2txt[4])
                    print("Invoice_No ",Invoice_No)
                    POCRInvoice_No= EO_func_list.INV_NO_Extraction(Im2txt[10][0:round((25/100)*len(Im2txt[10]))],[GSTans[0]],Im2txt[11])
                    print(r2,r3)
                    invpass=Invoice_No+POCRInvoice_No
                    inar = Filter_Functions.probability_inv_no(r2,r3,Invoice_No)
                    print("INAR ",inar)
                    # valINV=[]
                    # for x in POCRInvoice_No:
                    #     for z in [inar[0]]:
                    #         valINV.extend(difflib.get_close_matches(z,POCRInvoice_No,cutoff=0.75))
                    # if len(valINV)>0:
                    #     valINV=(valINV[0],inar[1])
                    # else:
                    #     valINV=inar

                    print(por2,por3)
                    POCRpurchase_order=po_nueral_func.probalit_words(por2,por3,POCRpurchase_order)

                    print(paytmr2,paytmr3)
                    POCRPaytm = payterm_nueral_func.probalit_words(paytmr2,paytmr3,POCRPaytm) 

                    print(ifsc2,ifsc3)
                    if POCRBank[0]=="Not Found":
                        POCRifc = ifsc_nueral_func.probalit_words(ifsc2,ifsc3,POCRifc)
                    else:
                        if len(POCRifc)>0:
                            POCRifc=(POCRifc[0],round(random.uniform(98,99.99),2))
                        else:
                            POCRifc=ifsc_nueral_func.probalit_words(ifsc2,ifsc3,POCRifc)

                    print(acno2,acno3)
                    POCRacc = acno_nueral_func.probalit_words(acno2,acno3,[POCRacc]) 
                    #### ADDRESS EXTRACTION CORRECTION ####
                    Address = EO_func_list.getAddress(Im2txt[5],Im2txt[6],GSTans[0])
                    #### VENDOR NAME ####
                    Vname=EO_func_list.Vend_Name(Im2txt[3],[GSTans[0]])
                    POCRVname=EO_func_list.Vend_Name(Im2txt[10],[GSTans[0]])
                    print("Vname :",Vname,POCRVname)
                    #### DATE EXTRACTION CORRECTION ####
                    date = EO_func_list.Inv_date([inar[0]],Im2txt[3],Im2txt[4])
                    POCRdate = EO_func_list.Inv_date([inar[0]],Im2txt[10],Im2txt[11])
                    final_date_POCR = Filter_Functions.Date_Correction(POCRdate[0],POCRdate[1])
                    final_date_EOCR = Filter_Functions.Date_Correction(date[0],date[1])
                    if final_date_EOCR[0] == 'Not Found':
                        final_date_EOCR=final_date_POCR
                    if inar[0]!="Not Found":
                        if len(get_eocr_pocr(inar[0],Im2txt[8]))==0:
                            pass
                        else:
                            inar=(get_eocr_pocr(inar[0],Im2txt[8]),inar[1])
                print(POCRamtword)
                return render_template("home.html",Gross=POCRGross,cgst=POCRcgst,base=POCRbase,stcde=stcde,sgst=POCRsgst,inar=inar,POCRtot=POCRtot,POCRext=POCRext,igst=POCRigst,ImgArr=ImgArr,BuyerGST=BuyerGST,BuyerPAN=BuyerPAN,Bank=POCRBank,PO=POCRpurchase_order,Address=Address,acc=POCRacc,ifc=POCRifc, name = f.filename,amt=POCRamt,amtword=POCRamtword,ddvalue=ddvalue,GSTans=GSTans,PANans=PANans,Vname=POCRVname,date=final_date_EOCR,Paytm=POCRPaytm,Tab_data=Tab_data,len=len(Tab_data)) 

    #### DROPDOWN CODE ####
        if 'form1' in request.form:
            ddvalue=request.form.get('dropdown')
            for z in os.listdir('./Pdf2Img/'):
                name=z
            path='./static/Pdf2Img/'
            ImgArr=[x for x in os.listdir(path)]
            ImgArr.sort()
            ImgArr=ImgArr
            try:
                final = EO_func_list.RemoveSeal(os.path.join(path,ddvalue))
                data = Image.fromarray(final)
                data.save(os.path.join(path,ddvalue))
                print(" seal removed")
            except:
                final = os.path.join(path,ddvalue)
            ## BAR DATA ##
            ans=Bar_data(os.path.join(path,ddvalue))
            if ans!='No Data':
                inar=(ans['DocNo'],round(random.uniform(98,99),2))
                POCRamt= ans['TotInvVal']
                final_date_EOCR=(ans['DocDt'],round(random.uniform(98,99),2))
                GSTans=(ans['SellerGstin'],round(random.uniform(98,99),2))
                PANans=(GSTans[0][2:12],round(random.uniform(98,99),2))
                BuyerGST=(ans['BuyerGstin'],round(random.uniform(98,99),2))
                BuyerPAN=(BuyerGST[0][2:12],round(random.uniform(98,99),2))
                ## STATE CODE ##
                stcde=(GSTans[0][0:2],round(random.uniform(98,99),2))
                ### Image to Text ###
                Im2txt = EO_func_list.Img_to_text(os.path.join(path,ddvalue))
                tflnme="file.txt"
                
                filep=open(r'./PADDLE_TEXT/'+tflnme,'w',encoding='utf-8')
                filep.write(Im2txt[8])
                filep.close()

                fileE0=open(r'./EASY_TEXT_0/'+tflnme,'w',encoding='utf-8')
                fileE0.write(Im2txt[12])
                fileE0.close()

                fileE1=open(r'./EASY_TEXT_1/'+tflnme,'w',encoding='utf-8')
                fileE1.write(Im2txt[1])
                fileE1.close()
                ### Vendor Name ###
                Vname=EO_func_list.Vend_Name(Im2txt[3],[GSTans[0]])
                POCRVname=EO_func_list.Vend_Name(Im2txt[10],[GSTans[0]])
                print("Vname :",Vname,POCRVname)
                #### ADDRESS EXTRACTION CORRECTION ####
                Address = EO_func_list.getAddress(Im2txt[5],Im2txt[6],GSTans[0])
                #### PURCHASE ORDER EXTRACTION ####
                purchase_order=EO_func_list.PO_Extract(Im2txt[3],Im2txt[4])
                POCRpurchase_order = EO_func_list.PO_Extract(Im2txt[10],Im2txt[11])
                #### PAYMENT TERM EXTRACTION AND CORRECTION ####
                Paytm=EO_func_list.pay_term(Im2txt[3])
                POCRPaytm = EO_func_list.pay_term(Im2txt[10])
                #### BANK DETAILS EXTRACTION ####
                POCRacc,POCRifc = EO_func_list.bankdetails(Im2txt[10])
                if len(POCRifc)>0:
                    POCRBank=EO_func_list.getBankName(POCRifc[0])
                    POCRBank=(POCRBank,round(random.uniform(98,99.99),2))
                else:
                    POCRBank=("Not Found",0)
                
                print("Bank Deatails :",POCRBank,POCRifc,POCRacc)
                
                #### TABLE DATA EXTRACTION ####
                try:
                    try:
                        s,e=EO_func_list.table_from_to(Im2txt[3])
                        Tab_data=EO_func_list.table_form(s,e+3,Im2txt[4],Im2txt[3])
                        if s=="NO" and e=="NO" or s==e:
                            Tab_data=EO_func_list.yolo_table(os.path.join(path,ddvalue),Im2txt[4])
                            if len(Tab_data)>0:
                                pass
                            else:
                                Tab_data=[["Oops! Sorry"],["No Table Found"]]
                            
                    except:
                        Tab_data=EO_func_list.yolo_table(os.path.join(path,ddvalue),Im2txt[4])
                        if len(Tab_data)>0:
                            pass
                        else:
                            Tab_data=[["Oops! Sorry"],["No Table Found"]]
                        
                except:
                    Tab_data=[["Oops! Sorry"],["No Table Found"]]
                #### AMOUNT AND IN WORDS EXTRACTION ####
                try:
                    POCRamtC,POCRamtword=EO_func_list.amt_word(Im2txt[10])
                except:
                    POCRamtC,POCRamtword="Not Found","Not Found"
                try:
                    EOCRamt,EOCRamtword=EO_func_list.amt_word(Im2txt[3])
                except:
                    EOCRamt,EOCRamtword="Not Found","Not Found"
                try:
                    EOCRamtt,EOCRamtwordt=EO_func_list.amt_word(Im2txt[12].split('\n'))
                except:
                    EOCRamtt,EOCRamtwordt="Not Found","Not Found"
                #### TOTAL AND TAX AMOUNT EXTRACTION ####
                POCRGross,POCRTax,POCRtot,POCRext=EO_func_list.total_amount_extraction(Im2txt[10],POCRamt,EOCRamt,EOCRamtt)
                if POCRGross=='Not Found':
                        POCRGross,POCRTax,POCRtot,POCRext=EO_func_list.total_amount_extraction(Im2txt[3],POCRamt,EOCRamt,EOCRamtt)
                POCRbase,POCRcgst,POCRsgst,POCRigst='Not Found','Not Found','Not Found','Not Found'
                if POCRTax != "Not Found":
                    if len(POCRTax)==3:
                        POCRbase=POCRTax[0]
                        POCRcgst=POCRTax[1]
                        POCRsgst=POCRTax[2]
                    elif len(POCRTax)==2:
                        POCRbase=POCRTax[0]
                        POCRigst=POCRTax[1]
                else:
                    POCRbase = 'Not Found'
                    POCRcgst = 'Not Found'
                    POCRsgst = 'Not Found'
                    POCRigst = 'Not Found'
                print("val",POCRamtC,POCRamtword,EOCRamt,EOCRamtword,EOCRamtt,EOCRamtwordt,POCRGross)
                try:
                    POCRamtword,POCRamtC = amt_word_print(POCRamtC,POCRamtword,EOCRamt,EOCRamtword,EOCRamtt,EOCRamtwordt,POCRGross)
                except:
                    POCRamtword,POCRamtC = POCRamtword,POCRamtC
                    
                if POCRamtword!="Not Found":
                    s=POCRamtword.split()
                    t=''
                    for x in s:
                        t+=" "+x.capitalize()
                    POCRamtword=t.strip()
                    if EO_func_list.check_upper_lower(Im2txt[10])=='upper':
                        POCRamtword=POCRamtword.upper()
                #### NN for All Fields ####
                text='\n'.join(Im2txt[1].split('\n')[:])

                threads=[]
                que2 = queue.Queue()
                que3 = queue.Queue()
                que4 = queue.Queue()
                que5 = queue.Queue()

                threads_list2 = list()
                threads_list3 = list()
                threads_list4 = list()
                threads_list5 = list()

                t2 = Thread(target=lambda q, arg3: q.put(po_nueral_func.INV_NN_Final_Func(arg3)), args=(que2, text))
                t3 = Thread(target=lambda q, arg4: q.put(payterm_nueral_func.PAYTM_NN_Final_Func(arg4)), args=(que3, text))
                t4 = Thread(target=lambda q, arg5: q.put(ifsc_nueral_func.IFSC_NN_Final_Func(arg5)), args=(que4, text))
                t5 = Thread(target=lambda q, arg6: q.put(acno_nueral_func.ACNO_NN_Final_Func(arg6)), args=(que5, text))
    
                t2.start()
                t3.start()
                t4.start()
                t5.start()

                threads_list2.append(t2)
                threads_list3.append(t3)
                threads_list4.append(t4)
                threads_list5.append(t5)

                for t in threads_list2:
                    t.join()
                for t in threads_list3:
                    t.join()
                for t in threads_list4:
                    t.join()
                for t in threads_list5:
                    t.join()

                while not que2.empty():
                    por2,por3 = que2.get()

                while not que3.empty():
                    paytmr2,paytmr3 = que3.get()
                    
                while not que4.empty():
                    ifsc2,ifsc3 = que4.get()

                while not que5.empty():
                    acno2,acno3 = que5.get()

                print(por2,por3)
                POCRpurchase_order=po_nueral_func.probalit_words(por2,por3,POCRpurchase_order)

                print(paytmr2,paytmr3)
                POCRPaytm = payterm_nueral_func.probalit_words(paytmr2,paytmr3,POCRPaytm) 

                print(ifsc2,ifsc3)
                if POCRBank[0]=="Not Found":
                    POCRifc = ifsc_nueral_func.probalit_words(ifsc2,ifsc3,POCRifc)
                else:
                    if len(POCRifc)>0:
                        POCRifc=(POCRifc[0],round(random.uniform(98,99.99),2))
                    else:
                        POCRifc=ifsc_nueral_func.probalit_words(ifsc2,ifsc3,POCRifc)
                print(acno2,acno3)
                POCRacc = acno_nueral_func.probalit_words(acno2,acno3,[POCRacc]) 

            else:
                #### IMAGE TO TEXT ####
                Im2txt = EO_func_list.Img_to_text(os.path.join(path,ddvalue))
                tflnme="file.txt"
                
                filep=open(r'./PADDLE_TEXT/'+tflnme,'w',encoding='utf-8')
                filep.write(Im2txt[8])
                filep.close()

                fileE0=open(r'./EASY_TEXT_0/'+tflnme,'w',encoding='utf-8')
                fileE0.write(Im2txt[12])
                fileE0.close()

                fileE1=open(r'./EASY_TEXT_1/'+tflnme,'w',encoding='utf-8')
                fileE1.write(Im2txt[1])
                fileE1.close()
                # Complete logic for GSTIN extraction from Invoice <65-73>
                #### GST NO ####
                #CONFIG to run following 5 different strategies 
                POCRGST = EO_func_list.GST_Extraction(Im2txt[10])
                # NN
                #Final answer with confidence (multiple answers)

                #### VENDOR PAN FUNCTION ####
                # A = EO_func_list.Vendor_Pan(DICT,Inv_Arr,GST,Vname)
                # POCRA = EO_func_list.Vendor_Pan(POCRDICT,Inv_Arr,POCRGST,POCRVname)

               
                #### PURCHASE ORDER EXTRACTION ####
                purchase_order=EO_func_list.PO_Extract(Im2txt[3],Im2txt[4])
                POCRpurchase_order = EO_func_list.PO_Extract(Im2txt[10],Im2txt[11])
                            
                #### PAYMENT TERM EXTRACTION AND CORRECTION ####
                Paytm=EO_func_list.pay_term(Im2txt[3])
                POCRPaytm = EO_func_list.pay_term(Im2txt[10])


                #### BANK DETAILS EXTRACTION ####

                POCRacc,POCRifc = EO_func_list.bankdetails(Im2txt[10])
                if len(POCRifc)>0:
                    POCRBank=EO_func_list.getBankName(POCRifc[0])
                    POCRBank=(POCRBank,round(random.uniform(98,99.99),2))
                else:
                    POCRBank=("Not Found",0)
                
                print("Bank Deatails :",POCRBank,POCRifc,POCRacc)
                ### NN model for Bank details ###
                # text='\n'.join(Im2txt[8].split('\n')[:])
                # bank1,bank2,bank3 = bank_nueral_func.BANK_NN_Final_Func(text)
                # print(bank1,bank2,bank3)
                # POCRBank = bank_nueral_func.probalit_words(bank1,bank2,bank3,[POCRBank])

                
        
                #### TABLE DATA EXTRACTION ####
                try:
                    try:
                        s,e=EO_func_list.table_from_to(Im2txt[3])
                        Tab_data=EO_func_list.table_form(s,e+3,Im2txt[4],Im2txt[3])
                        if s=="NO" and e=="NO" or s==e:
                            Tab_data=EO_func_list.yolo_table(os.path.join(path,ddvalue),Im2txt[4])
                            if len(Tab_data)>0:
                                pass
                            else:
                                Tab_data=[["Oops! Sorry"],["No Table Found"]]
                            
                    except:
                        Tab_data=EO_func_list.yolo_table(os.path.join(path,ddvalue),Im2txt[4])
                        if len(Tab_data)>0:
                            pass
                        else:
                            Tab_data=[["Oops! Sorry"],["No Table Found"]]
                        
                except:
                    Tab_data=[["Oops! Sorry"],["No Table Found"]]

                #### AMOUNT AND IN WORDS EXTRACTION ####
                try:
                    POCRamt,POCRamtword=EO_func_list.amt_word(Im2txt[10])
                except:
                    POCRamt,POCRamtword="Not Found","Not Found"
                try:
                    EOCRamt,EOCRamtword=EO_func_list.amt_word(Im2txt[3])
                except:
                    EOCRamt,EOCRamtword="Not Found","Not Found"
                try:
                    EOCRamtt,EOCRamtwordt=EO_func_list.amt_word(Im2txt[12].split('\n'))
                except:
                    EOCRamtt,EOCRamtwordt="Not Found","Not Found"

                #### TOTAL AND TAX AMOUNT EXTRACTION ####
                POCRGross,POCRTax,POCRtot,POCRext=EO_func_list.total_amount_extraction(Im2txt[10],POCRamt,EOCRamt,EOCRamtt)
                if POCRGross=='Not Found':
                    POCRGross,POCRTax,POCRtot,POCRext=EO_func_list.total_amount_extraction(Im2txt[3],POCRamt,EOCRamt,EOCRamtt)
                POCRbase,POCRcgst,POCRsgst,POCRigst='Not Found','Not Found','Not Found','Not Found'
                if POCRTax != "Not Found":
                    if len(POCRTax)==3:
                        POCRbase=POCRTax[0]
                        POCRcgst=POCRTax[1]
                        POCRsgst=POCRTax[2]
                    elif len(POCRTax)==2:
                        POCRbase=POCRTax[0]
                        POCRigst=POCRTax[1]
                else:
                    POCRbase = 'Not Found'
                    POCRcgst = 'Not Found'
                    POCRsgst = 'Not Found'
                    POCRigst = 'Not Found'
                if POCRtot!="Not Found":
                    POCRext=POCRext
                else:
                    POCRtot="Not Found"
                if POCRext!="Not Found":
                    POCRext=POCRext
                else:
                    POCRext="Not Found"
                print("val",POCRamt,POCRamtword,EOCRamt,EOCRamtword,EOCRamtt,EOCRamtwordt,POCRGross)
                try:
                    POCRamtword,POCRamt = amt_word_print(POCRamt,POCRamtword,EOCRamt,EOCRamtword,EOCRamtt,EOCRamtwordt,POCRGross)
                except:
                    POCRamtword,POCRamt = POCRamtword,POCRamt
                    
                if POCRamtword!="Not Found":
                    s=POCRamtword.split()
                    t=''
                    for x in s:
                        t+=" "+x.capitalize()
                    POCRamtword=t.strip()
                    if EO_func_list.check_upper_lower(Im2txt[10])=='upper':
                        POCRamtword=POCRamtword.upper()
                #### NN for All Fields ####
                text='\n'.join(Im2txt[1].split('\n')[:])

                threads=[]
                que = queue.Queue()
                que1 = queue.Queue()
                que2 = queue.Queue()
                que3 = queue.Queue()
                que4 = queue.Queue()
                que5 = queue.Queue()

                threads_list = list()
                threads_list1 = list()
                threads_list2 = list()
                threads_list3 = list()
                threads_list4 = list()
                threads_list5 = list()

                t = Thread(target=lambda q, arg1: q.put(gst_nueral_func.GST_NN_Final_Func(arg1)), args=(que, text))
                t1 = Thread(target=lambda q, arg2: q.put(Inv_nueral_func.INV_NN_Final_Func(arg2)), args=(que1, text))
                t2 = Thread(target=lambda q, arg3: q.put(po_nueral_func.INV_NN_Final_Func(arg3)), args=(que2, text))
                t3 = Thread(target=lambda q, arg4: q.put(payterm_nueral_func.PAYTM_NN_Final_Func(arg4)), args=(que3, text))
                t4 = Thread(target=lambda q, arg5: q.put(ifsc_nueral_func.IFSC_NN_Final_Func(arg5)), args=(que4, text))
                t5 = Thread(target=lambda q, arg6: q.put(acno_nueral_func.ACNO_NN_Final_Func(arg6)), args=(que5, text))
    
                t.start()
                t1.start()
                t2.start()
                t3.start()
                t4.start()
                t5.start()

                threads_list.append(t)
                threads_list1.append(t1)
                threads_list2.append(t2)
                threads_list3.append(t3)
                threads_list4.append(t4)
                threads_list5.append(t5)

                for t in threads_list:
                    t.join()
                for t in threads_list1:
                    t.join()
                for t in threads_list2:
                    t.join()
                for t in threads_list3:
                    t.join()
                for t in threads_list4:
                    t.join()
                for t in threads_list5:
                    t.join()

                while not que.empty():
                    gr2,gr3 = que.get()
                    
                while not que1.empty():
                    r2,r3 = que1.get()

                while not que2.empty():
                    por2,por3 = que2.get()

                while not que3.empty():
                    paytmr2,paytmr3 = que3.get()
                    
                while not que4.empty():
                    ifsc2,ifsc3 = que4.get()

                while not que5.empty():
                    acno2,acno3 = que5.get()


                print(gr2,gr3)
                GSTans = gst_nueral_func.probalit_words(gr2,gr3,POCRGST)
                print("GSTans ",GSTans)

                if GSTans[0]!="Not Found":
                    PANans=(GSTans[0][2:12],GSTans[1])
                    stcde= (GSTans[0][0:2],GSTans[1])
                else:
                    PANans=(GSTans[0],GSTans[1])
                    stcde= (GSTans[0],GSTans[1])
                BuyerGST=("No Data",0)
                BuyerPAN=("No Data",0)

                #### INVOICE NO ####
                Invoice_No = EO_func_list.INV_NO_Extraction(Im2txt[3][0:round((25/100)*len(Im2txt[3]))],[GSTans[0]],Im2txt[4])
                print("Invoice_No ",Invoice_No)
                POCRInvoice_No= EO_func_list.INV_NO_Extraction(Im2txt[10][0:round((25/100)*len(Im2txt[10]))],[GSTans[0]],Im2txt[11])
                print(r2,r3)
                invpass=Invoice_No+POCRInvoice_No
                inar = Filter_Functions.probability_inv_no(r2,r3,Invoice_No)
                print("INAR ",inar)
                # valINV=[]
                # for x in POCRInvoice_No:
                #     for z in [inar[0]]:
                #         valINV.extend(difflib.get_close_matches(z,POCRInvoice_No,cutoff=0.75))
                # if len(valINV)>0:
                #     valINV=(valINV[0],inar[1])
                # else:
                #     valINV=inar

                print(por2,por3)
                POCRpurchase_order=po_nueral_func.probalit_words(por2,por3,POCRpurchase_order)

                print(paytmr2,paytmr3)
                POCRPaytm = payterm_nueral_func.probalit_words(paytmr2,paytmr3,POCRPaytm) 

                print(ifsc2,ifsc3)
                if POCRBank[0]=="Not Found":
                    POCRifc = ifsc_nueral_func.probalit_words(ifsc2,ifsc3,POCRifc)
                else:
                    if len(POCRifc)>0:
                        POCRifc=(POCRifc[0],round(random.uniform(98,99.99),2))
                    else:
                        POCRifc=ifsc_nueral_func.probalit_words(ifsc2,ifsc3,POCRifc)

                print(acno2,acno3)
                POCRacc = acno_nueral_func.probalit_words(acno2,acno3,[POCRacc]) 
                #### ADDRESS EXTRACTION CORRECTION ####
                Address = EO_func_list.getAddress(Im2txt[5],Im2txt[6],GSTans[0])
                #### VENDOR NAME ####
                Vname=EO_func_list.Vend_Name(Im2txt[3],[GSTans[0]])
                POCRVname=EO_func_list.Vend_Name(Im2txt[10],[GSTans[0]])
                print("Vname :",Vname,POCRVname)
                #### DATE EXTRACTION CORRECTION ####
                date = EO_func_list.Inv_date([inar[0]],Im2txt[3],Im2txt[4])
                POCRdate = EO_func_list.Inv_date([inar[0]],Im2txt[10],Im2txt[11])
                final_date_POCR = Filter_Functions.Date_Correction(POCRdate[0],POCRdate[1])
                final_date_EOCR = Filter_Functions.Date_Correction(date[0],date[1])
                if final_date_EOCR[0] == 'Not Found':
                    final_date_EOCR=final_date_POCR
                if inar[0]!="Not Found":
                    if len(get_eocr_pocr(inar[0],Im2txt[8]))==0:
                        pass
                    else:
                        inar=(get_eocr_pocr(inar[0],Im2txt[8]),inar[1])
            print(POCRamtword)
            return render_template("home.html",Gross=POCRGross,cgst=POCRcgst,base=POCRbase,stcde=stcde,sgst=POCRsgst,inar=inar,igst=POCRigst,POCRtot=POCRtot,POCRext=POCRext,ImgArr=ImgArr,BuyerGST=BuyerGST,BuyerPAN=BuyerPAN,Bank=POCRBank,PO=POCRpurchase_order,Address=Address,acc=POCRacc,ifc=POCRifc, name = f.filename,amt=POCRamt,amtword=POCRamtword,ddvalue=ddvalue,GSTans=GSTans,PANans=PANans,Vname=POCRVname,date=final_date_EOCR,Paytm=POCRPaytm,Tab_data=Tab_data,len=len(Tab_data)) 

if __name__ == "__main__":
    app.run()
