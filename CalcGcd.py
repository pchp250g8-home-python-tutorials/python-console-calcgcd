# --coding:utf-8--

import os

os.system("cls")
print("Input the first integer number:")
iNum1 = int(input())
print("Input the second integer number:")
iNum2 = int(input())
iVal1 = abs(iNum1)
iVal2 = abs(iNum2)
if (iVal1 > 0 and iVal2 > 0):
    while (iVal1 != iVal2):
        if(iVal1 > iVal2):
            iVal1 -= iVal2
        else:
            iVal2 -= iVal1
    
    nGcd = iVal1
    print(f"The Gcd of the numbers {iNum1} and {iNum2} is {nGcd}\r\n")
else:
    print("The numbers must not be equal 0")
