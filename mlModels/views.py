from django.shortcuts import render
from joblib import load

import numpy as np
import pandas as pd
import faiss
import re

model = load('./model.joblib')
index = faiss.read_index('./models/demo_index1.bin')
input = open('./models/law_records1.csv',encoding='utf8',errors='backslashreplace')
df = pd.read_csv(input)

def predictor(request):
    return render(request,'result.html')

def search(request):
    userquery = request.GET['userquery']
    userquery_list = [userquery]
    vector = model.encode(list(userquery_list))
    queryEncode = np.array(vector).astype("float32")
    

    D, I = index.search(queryEncode, 15)

    result_pdf =[list(df[df.ID == idx]['PDF']) for idx in I[0]]
    result_date =[list(df[df.ID == idx]['DATE']) for idx in I[0]]
    result_content =[list(df[df.ID == idx]['SUMMARY']) for idx in I[0]]
    title1 =[list(df[df.ID == idx]['TITLE']) for idx in I[0]]
    
    advocates1 = [list(df[df.ID == idx]['ADVOCATES']) for idx in I[0]]
    judges1 = [list(df[df.ID == idx]['JUDGES']) for idx in I[0]]

    advocates=[]
    title = []
    judges =[]


    for i in title1:
        res = str(i[0])
        [2010]
        res = re.sub(r"[\d]{1,2} [ADF JMNOS]\w* [\d]{4}","",res)
        
        res = re.sub(r'\[.*?\]',"",res)

        res= res.replace('(', '').replace(')', '')
        title.append(res)

    for i in advocates1:
        
        res = str(i[0])
        res= res.replace('[', '').replace(']', '')
        advocates.append(res)

    for i in judges1:
        
        res = str(i[0])
        res= res.replace('[', '').replace(']', '')
        judges.append(res)

    print(judges)

    results = {'q':userquery}
    result=[]

    result0={'id':123,'title':title[0],'summary':result_content[0][0],'pdf':result_pdf[0][0],'NOP':32,'date':result_date[0][0],'Judges':judges[0],'Advocates':advocates[0]}
    result1={'id':223,'title':title[1],'summary':result_content[1][0],'pdf':result_pdf[1][0],'NOP':132,'date':result_date[1][0],'Judges':judges[1],'Advocates':advocates[1]}
    result2={'id':323,'title':title[2],'summary':result_content[2][0],'pdf':result_pdf[2][0],'NOP':2,'date':result_date[2][0],'Judges':judges[2],'Advocates':advocates[2]}
    result3={'id':323,'title':title[3],'summary':result_content[3][0],'pdf':result_pdf[3][0],'NOP':2,'date':result_date[2][0],'Judges':judges[3],'Advocates':advocates[3]}
    result4={'id':323,'title':title[4],'summary':result_content[4][0],'pdf':result_pdf[4][0],'NOP':2,'date':result_date[2][0],'Judges':judges[4],'Advocates':advocates[4]}
    result5={'id':323,'title':title[5],'summary':result_content[5][0],'pdf':result_pdf[5][0],'NOP':2,'date':result_date[2][0],'Judges':judges[5],'Advocates':advocates[5]}
    result6={'id':323,'title':title[6],'summary':result_content[6][0],'pdf':result_pdf[6][0],'NOP':2,'date':result_date[2][0],'Judges':judges[6],'Advocates':advocates[6]}
    result7={'id':323,'title':title[7],'summary':result_content[7][0],'pdf':result_pdf[7][0],'NOP':2,'date':result_date[2][0],'Judges':judges[7],'Advocates':advocates[7]}
    result8={'id':323,'title':title[8],'summary':result_content[8][0],'pdf':result_pdf[8][0],'NOP':2,'date':result_date[2][0],'Judges':judges[8],'Advocates':advocates[8]}
    result9={'id':323,'title':title[9],'summary':result_content[9][0],'pdf':result_pdf[9][0],'NOP':2,'date':result_date[2][0],'Judges':judges[9],'Advocates':advocates[9]}

    result.append(result0)
    result.append(result1)
    result.append(result2)
    result.append(result3)
    result.append(result4)
    result.append(result5)
    result.append(result6)
    result.append(result7)
    result.append(result8)
    result.append(result9)


    for i in range(len(result)):
        flag=1
        flag1= 2
        for key,value in result[i].items():
            if key == 'summary':
                if (value.__eq__('nan')):
                    # print(value)
                    flag=0
           
            if key == 'Judges':
                if len(value)<150:
                        print(flag)
                        flag1=3
                

        if flag == 1 and flag1 == 3:
            results[i]=result[i]



    return render(request,'result.html',{'data':results})
