import re
import difflib
from difflib import get_close_matches
date='(\\d{1,2}-[a-zA-Z]{3,9}-\\d{2,4}|\\d{1,2}\\.\\d{1,2}\\.\\d{2,4}|\\d{1,2}/\\d{1,2}/\\d{2,4}|[A-Z]{3,9}\\.\\d{1,2}[a-zA-Z]{2}\\,\\d{4}|\\d{1,2}-\\d{1,2}-\\d{2,4}|\\d{1,2}-[A-Z]{3,9}-\\d{2,4}|[A-Z]{3,9}\\.\\d{1,2},\\d{4}|\\d{2,4}/\\d{1,2}/\\d{1,2}|[a-zA-z]{3,9}\\s\\d{1,2}\\,\\s\\d{2,4}|\\d{1,2}\\s[a-zA-z]{3,9}\\,\\s\\d{4}|\\d{1,2}[A-Za-z]{2}[A-Za-z]{3,9}\\d{2,4}|[A-Za-z]{3,9}.\\d{1,2}[A-Za-z]{2}.\\d{2,4}|)'
import collections,random
from collections import *

def Vend_Name_Correction(VnameList):
    for x in VnameList:
        for y in VnameList:
            if y==x:
                continue
            if y in x:
                try:
                    VnameList.remove(y)
                except:
                    pass
    return VnameList

def Date_Correction(POCRdate,conf):
    monthlist=['jan','feb','mar','apr','may','jun','june','jul','july','aug','sep','oct','nov','dec','january','february','march','april','august','september','october','november','december']
    date2=[]
    dateL=[]
    finaldate=[]
    if len(POCRdate)>0:
        try:
            for x in POCRdate:
                if any(char.isdigit() for char in x):
                    date2.append(x)
        except:
            pass
        print("DTE1 :",date2)    
        if len(date2)>0:
            for x in date2:
                if len(x)>15:
                    continue
                else:
                    dateL.append(x)  
        print("DTE2",dateL)     
        try:
            for x in dateL:
                for y in dateL:
                    if y==x:
                        continue
                    if y in x:
                        try:
                            dateL.remove(y)
                        except:
                            pass
        except:
            pass
        print("DTE3 :",dateL)

        for x in dateL:
            if any(char.isalpha() for char in x):
                for m in monthlist:
                    if m in x.lower():
                        finaldate.append(x.upper())
                    else:
                        pass
        if len(finaldate)>0:
            pass
        else:
            finaldate=dateL
        print("DTE4 :",finaldate)
        if len(finaldate)>0:
            val=[]
            for tst in finaldate:
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
                            return(val[0],conf)
                        else:
                            finaldate = [x for x in dict.fromkeys(finaldate)]
                            return(finaldate[0],conf)
            else:
                return finaldate[0],conf
        else:
            return ("Not Found",0)
    else:
        return ("Not Found",0)


def PO_Number_Correction(POCRpurchase_order):
    try:
        for po in POCRpurchase_order:
            if po in POCRInv_Arr:
                POCRpurchase_order.remove(po)
    except:
        POCRpurchase_order = POCRpurchase_order
    return POCRpurchase_order


def inv_cleaner_for_nn(result):
    text1=' '.join(result)
    text1=' '.join(dict.fromkeys(text1.split()))
    text1=re.sub(date,'',text1)
    text1=[x for x in text1.split() if len(x)>2]
    text1=[x for x in text1 if any(map(str.isdigit,x))==True]
    return text1


def probability_inv_no(r2,r3,inv):
    inv=[i.lower() for i in inv]
    inv=' '.join(inv).split()
    r2,r3=[inv_cleaner_for_nn(x) for  x in (r2,r3)]
    ans=Counter(r2+r3).most_common()
    print('ansss',ans)
    if len(ans)==0 and len(inv)==0:
        return ("Not Found",0)
    if len(ans)==0 and len(inv)>0:
        return (inv[0],round(random.uniform(75,80),2))

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
        inv_no=ans[0][0]
        v=ans[0][1]
        if v==2 or v>2:
            prb_val=random.uniform(92,95)
        if v==1:
            prb_val=random.uniform(85,90)

    return inv_no,round(prb_val,2)
