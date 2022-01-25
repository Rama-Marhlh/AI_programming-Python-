# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 18:59:06 2022

@author: miraz
"""





def copy(file_name):
    sheet=[]
    f=open( file_name , 'r')
    csv_reader= csv.reader(f)
    for row in csv_reader:
       sheet.append(row)
    return sheet


def transpose():
    dicta={}
    sheet=copy('workbook1.csv')
    for i in range(1,5): 
        avg=0
        row_count=0
        for row in sheet:
           if  row != sheet[0] and row_count<= 3: 
               value=int(row[i])
               avg+=value
               row_count+=1   
        key=sheet[0][i]
        dicta[key]=int(avg)
    return print(dicta)

transpose()

