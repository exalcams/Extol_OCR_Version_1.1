import pandas as pd
from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en',use_gpu=True)
def line_extract(img):
    l=[]
    ocdf=pd.DataFrame()
    ocrL=ocr.ocr(img, cls=True)
    ocdf['x1']=[x[0][0][0] for x in ocrL ]
    ocdf['x2']=[x[0][0][1] for x in ocrL ]
    ocdf['y1']=[x[0][1][0] for x in ocrL ]
    ocdf['y2']=[x[0][1][1] for x in ocrL ]
    ocdf['w1']=[x[0][2][0] for x in ocrL ]
    ocdf['w2']=[x[0][2][1] for x in ocrL ]
    ocdf['h1']=[x[0][3][0] for x in ocrL ]
    ocdf['h2']=[x[0][3][1] for x in ocrL ]
    ocdf['string']=[x[1][0] for x in ocrL]
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
    return l

