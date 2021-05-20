import numpy as np
import math

def calculate(list):
    #MAXIMUM
    #FOR CALCULATING ROW Max
    if len(list) !=9:
     raise ValueError("List must contain nine numbers.")
    arr = list
    max2 = 0
    max1 = 0
    max3 = 0
    for i in range(0,3):
     if arr[i] > max1:
      max1 = arr[i]
#print(max1)

    for i in range(3,6):
     if arr[i] > max2:
      max2 = arr[i]
#print(max2)

    for i in range(6,9):
     if arr[i] > max3:
      max3 = arr[i]
#print(max3)

#FOR CALCULATING COLUMN MAX
    max02 = 0
    max01 = 0
    max03 = 0

    for i in range(0,7,3):
     if arr[i] > max01:
      max01 = arr[i]
#print(max01)

    for i in range(1,8,3):
     if arr[i] > max02:
      max02 = arr[i]
#print(max02)

    for i in range(2,9,3):
     if arr[i] > max03:
      max03 = arr[i]
#print(max03)



#MINIMUM
#for calculating row minimum
    min1=arr[0]
    min2=arr[3]
    min3=arr[6]

    for i in range(0,3):
     if arr[i] <= min1:
      min1 = arr[i]
#print(min1)

    for i in range(3,6):
     if arr[i] <= min2:
      min2 = arr[i]
#print(min2)

    for i in range(6,9):
     if arr[i] <= min3:
      min3 = arr[i]
#print(min3)

#FOR CALCULATING COLUMN MIN
    min01=arr[0]
    min02=arr[1]
    min03=arr[2]
    for i in range(0,7,3):
     if arr[i] <= min01:
      min01 = arr[i]
#print(min01)

    for i in range(1,8,3):
     if arr[i] <= min02:
      min02 = arr[i]
#print(min02)

    for i in range(2,9,3):
     if arr[i] <= min03:
      min03 = arr[i]
#print(min03)

#FOR FLATTENED
#FOR CALCULATING FLATTEND

    minf=arr[0]
    maxf=arr[0]
    sumf=0
    varf=0

    for i in range(0,9):
     sumf = sumf+arr[i]
     meanf = sumf/9
     if arr[i] < minf:
      minf = arr[i]
     elif arr[i] > maxf:
      maxf = arr[i]
  
  
#print("minf,maxf,sumf,meanf") 
#print(minf,maxf,sumf,meanf)


#SUMMATION
#FOR CALCULATING ROW SUM
    sum1=0
    var1=0

    for i in range(0,3):
     sum1 = sum1 + arr[i]
    mean1=sum1/3
 #print(sum1)

    sum2=0
    for i in range(3,6):
     sum2 = sum2 + arr[i]
    mean2=sum2/3
#print(sum2)

    sum3=0
    for i in range(6,9):
     sum3 = sum3 + arr[i]
    mean3=sum3/3
#print(sum3)

#FOR COLUMN SUM
    sum01=0
    for i in range(0,7,3):
     sum01 = sum01 + arr[i]
    mean01 = sum01/3
#print(sum01)

    sum02=0
    for i in range(1,8,3):
     sum02 = sum02 + arr[i]
    mean02=sum02/3
#print(sum02)

    sum03=0
    for i in range(2,9,3):
     sum03 = sum03 + arr[i]
    mean03=sum03/3
#print(sum03)


#VARIANCE
#FOR CALCULATING VARIANCE FLAT

    for i in range(0,9):
     varf = varf+(arr[i] - meanf)**2
    varf=varf/9
    sdf = math.sqrt(varf)
#print(varf,sdf)

#FOR VARIANCE IN ROW
    var2=0
    var3=0
    for i in range(0,3):
     var1 = var1+(arr[i] - mean1)**2
    var1=var1/3
    sd1= math.sqrt(var1)

    for i in range(3,6):
     var2 = var2+(arr[i] - mean2)**2
    var2=var2/3
    sd2= math.sqrt(var2)

    for i in range(6,9):
     var3 = var3+(arr[i] - mean3)**2
    var3=var3/3
    sd3=math.sqrt(var3)


#FORVARIANCE IN column
    var01=0
    var02=0
    var03=0
    for i in range(0,7,3):
     var01 = var01+(arr[i] - mean01)**2
    var01=var01/3
    sd01=math.sqrt(var01)

    for i in range(1,8,3):
     var02 = var02+(arr[i] - mean02)**2
    var02=var02/3
    sd02=math.sqrt(var02)

    for i in range(2,9,3):
     var03 = var03+(arr[i] - mean03)**2
    var03=var03/3
    sd03=math.sqrt(var03)

#print("mean")
    mean = ([[mean01,mean02,mean03],[mean1,mean2,mean3],meanf])
   
#print("variance")
    var = ([[var01,var02,var03],[var1,var2,var3],varf])
#print("standard deviation")
    std = ([[sd01,sd02,sd03],[sd1,sd2,sd3],sdf])
  
#print(std)

#print("maximum")
    max = ([[max01,max02,max03],[max1,max2,max3],maxf])
    
#print(max)


#print("minimum")
    min =[[min01,min02,min03],[min1,min2,min3],minf]


#print("sum")
    sum=[[sum01,sum02,sum03],[sum1,sum2,sum3],sumf]
#print(sum)

    calculate={"mean":mean,"variance":var,"standard deviation":std,"max":max,"min":min,"sum":sum}
     #print(type(calculate))
    
#print(calculate)

    return calculate