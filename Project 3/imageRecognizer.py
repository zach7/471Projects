# -*- coding: utf-8 -*-
"""
Created on Tue May 17 14:53:29 2016

@author: Zach

Credit to SentDex youtube tutorial for the basics.
"""

from PIL import Image
import numpy as np
from collections import Counter
import sys
import os.path

#Function to create reference dictionary currently set up to draw from provided data set
def createExamples():
    pictureExamples = open('ReferenceDictionary.txt', 'a')
    
    for x in range(1,61):
        if x < 10:
            imgFilePath = 'Data/01/0' + str(x) + '.jpg' #this needs to be modified if dictionary images 
            ei = Image.open(imgFilePath)                #are in another directory
            eiar = threshold(np.array(ei))
            eiar1 = str(eiar)
            
            lineToWrite = '1::'+eiar1+'\n'
            pictureExamples.write(lineToWrite)
        else:
            imgFilePath = 'Data/01/' + str(x) + '.jpg'
            ei = Image.open(imgFilePath)
            eiar = threshold(np.array(ei))
            eiar1 = str(eiar)
            
            lineToWrite = '1::'+eiar1+'\n'
            pictureExamples.write(lineToWrite)
    for x in range(1,61):
        if x < 10:
            imgFilePath = 'Data/02/0' + str(x) + '.jpg'
            ei = Image.open(imgFilePath)
            eiar = threshold(np.array(ei))
            eiar1 = str(eiar)
            
            lineToWrite = '2::'+eiar1+'\n'
            pictureExamples.write(lineToWrite)
        else:
            imgFilePath = 'Data/02/' + str(x) + '.jpg'
            ei = Image.open(imgFilePath)
            eiar = threshold(np.array(ei))
            eiar1 = str(eiar)
            
            lineToWrite = '2::'+eiar1+'\n'
            pictureExamples.write(lineToWrite)
    for x in range(1,61):
        if x < 10:
            imgFilePath = 'Data/03/0' + str(x) + '.jpg'
            ei = Image.open(imgFilePath)
            eiar = threshold(np.array(ei))
            eiar1 = str(eiar)
            
            lineToWrite = '3::'+eiar1+'\n'
            pictureExamples.write(lineToWrite)
        else:
            imgFilePath = 'Data/03/' + str(x) + '.jpg'
            ei = Image.open(imgFilePath)
            eiar = threshold(np.array(ei))
            eiar1 = str(eiar)
            
            lineToWrite = '3::'+eiar1+'\n'
            pictureExamples.write(lineToWrite)
    for x in range(1,61):
        if x < 10:
            imgFilePath = 'Data/04/0' + str(x) + '.jpg'
            ei = Image.open(imgFilePath)
            eiar = threshold(np.array(ei))
            eiar1 = str(eiar)
            
            lineToWrite = '4::'+eiar1+'\n'
            pictureExamples.write(lineToWrite)
        else:
            imgFilePath = 'Data/04/' + str(x) + '.jpg'
            ei = Image.open(imgFilePath)
            eiar = threshold(np.array(ei))
            eiar1 = str(eiar)
            
            lineToWrite = '4::'+eiar1+'\n'
            pictureExamples.write(lineToWrite)
    for x in range(1,61):
        if x < 10:
            imgFilePath = 'Data/05/0' + str(x) + '.jpg'
            ei = Image.open(imgFilePath)
            eiar = threshold(np.array(ei))
            eiar1 = str(eiar)
            
            lineToWrite = '5::'+eiar1+'\n'
            pictureExamples.write(lineToWrite)
        else:
            imgFilePath = 'Data/05/' + str(x) + '.jpg'
            ei = Image.open(imgFilePath)
            eiar = threshold(np.array(ei))
            eiar1 = str(eiar)
            
            lineToWrite = '5::'+eiar1+'\n'
            pictureExamples.write(lineToWrite)
            
#convert image matrix into purely black and white
def threshold(imageArray):
    
    newAr = imageArray.tolist()
    
    i = 0
    for eachRow in imageArray:
        j = 0
        for eachPix in eachRow:
            if eachPix[0] == 255 and eachPix[1] == 255 and eachPix[2] == 255:
                
                newAr[i][j][0] = 255
                newAr[i][j][1] = 255
                newAr[i][j][2] = 255
            else:
                newAr[i][j][0] = 0
                newAr[i][j][1] = 0
                newAr[i][j][2] = 0
            j = j + 1
        i = i + 1
    return newAr

#classify image
def whatIsThis(filePath):
    print('Attempting classification.')
    matchedAr = []
    loadExamps = open('ReferenceDictionary.txt', 'r').read()
    loadExamps = loadExamps.split('\n')
    
    i = Image.open(filePath)
    iar = threshold(np.array(i))
    inQuestion = str(iar)
    
    count1 = 0
    count3 = 0
    count4 = 0
    for eachExample in loadExamps:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentType = splitEx[0]
            currentAr = splitEx[1]
            
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')
            
            x = 0
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentType))
                
                if(int(currentType) == 1):
                    if count1 == 95:
                        matchedAr.append(1)
                        count1 = 0
                    else:
                        count1 += 1 
                if(int(currentType) == 3):
                    if count3 == 40:
                        matchedAr.append(3)
                        count3 = 0
                    else:
                        count3 += 1
                
                if(int(currentType) == 4):
                    if count4 == 75:
                        matchedAr.append(4)
                        count4 = 0
                    else:
                        count4 += 1
                x += 1
    
    y = Counter(matchedAr)
    
    tot1 = y[1]
    tot2 = y[2]
    tot3 = y[3]
    tot4 = y[4]
    tot5 = y[5]
    best = max(tot1, tot2, tot3, tot4, tot5)
    num = 0
    if tot1 == best:
        print('Smile')
        num = 1
    if tot2 == best:
        print('Hat')
        num = 2
    if tot3 == best:
        print('Hash')
        num = 3
    if tot4 == best:
        print('Heart')
        num = 4
    if tot5 == best:
        print('Dollar')
        num = 5
        
    return num

#if dictionary doesn't exist, create it
if not os.path.isfile('ReferenceDictionary.txt'):
    print('Creating Dictionary.')
    createExamples()
    
else:
    print('Dictionary exists.')

#classify image
whatIsThis(sys.argv[1])


#Testing Code
"""

successes = 0
tot1 = 0
suc1 = 0
false1 = 0
tot2 = 0
suc2 = 0
false2 = 0
tot3 = 0
suc3 = 0
false3 = 0
tot4 = 0
suc4 = 0
false4 = 0
tot5 = 0
suc5 = 0
false5 = 0
total = 0

for i in range(61, 73): #86
    filePath = 'Data/01/' + str(i) + '.jpg'
    img = whatIsThis(filePath)
    if img == 1:
        successes += 1
        suc1 += 1
    elif img == 2:
        false2 += 1
    elif img == 3:
        false3 += 1
    elif img == 4:
        false4 += 1
    elif img == 5:
        false5 += 1
    total += 1
    tot1 += 1
    


for i in range(61, 73): 
    filePath = 'Data/02/' + str(i) + '.jpg'
    img = whatIsThis(filePath)
    if img == 2:
        successes += 1
        suc2 += 1
    elif img == 1:
        false1 += 1
    elif img == 3:
        false3 += 1
    elif img == 4:
        false4 += 1
    elif img == 5:
        false5 += 1
    total += 1
    tot2 += 1
    
    

for i in range(61, 73): #89
    filePath = 'Data/03/' + str(i) + '.jpg'
    img = whatIsThis(filePath)
    if img == 3:
        successes += 1
        suc3 += 1
    elif img == 2:
        false2 += 1
    elif img == 1:
        false1 += 1
    elif img == 4:
        false4 += 1
    elif img == 5:
        false5 += 1
    total += 1
    tot3 += 1
    
  
 
for i in range(61, 73): #82
    filePath = 'Data/04/' + str(i) + '.jpg'
    img = whatIsThis(filePath)
    if img == 4:
        successes += 1
        suc4 += 1
    elif img == 2:
        false2 += 1
    elif img == 3:
        false3 += 1
    elif img == 1:
        false1 += 1
    elif img == 5:
        false5 += 1
    total += 1 
    tot4 += 1
    
   
    
for i in range(61, 73): #88
    filePath = 'Data/05/' + str(i) + '.jpg'
    img = whatIsThis(filePath)
    if img == 5:
        successes += 1
        suc5 += 1
    elif img == 2:
        false2 += 1
    elif img == 3:
        false3 += 1
    elif img == 4:
        false4 += 1
    elif img == 1:
        false1 += 1
    total += 1
    tot5 += 1
    

print('Smile Recall:', (suc1/tot1))
print('Smile precision:', (suc1/(suc1+false1)))
print('Hat Recall:', (suc2/tot2)) 
print('Hat precision:', (suc2/(suc2+false2)))
print('Hash Recall:', (suc3/tot3))
print('Hash precision:', (suc3/(suc3+false3)))
print('Heart Recall:', (suc4/tot4))
print('Heart precision:', (suc4/(suc4+false4)))
print('Dollar Recall:', (suc5/tot5))
print('Dollar precision:', (suc5/(suc5+false5)))  
print (successes / total)

"""


            