#選擇『華氏轉攝氏』還是攝式轉華氏

def F2C(F):
    C=(F-32) * 5 /9
    return C

def C2F(C):
    F= C * (9/5) + 32
    return F

degree = float(input("請輸入温度："))
conversion=float(input("１、華氐　-> 攝氐 \n２、攝氐　-> 華氐\n請選擇："))
if conversion == 1:
    F=C2F(degree)
    print ("結果為\n%d 華氐 = %.2f 攝氐" % (degree,F))
elif conversion == 2:
    C=F2C(degree)
    print ("結果為\n%d 攝氐 = %.2f 華氐" % (degree,C)) 


#
    #def F2C(F):
    #'F -> Fahrenheit'
#     C=(F-32) * 5 /9
#     return C

# def C2F(C):
#     F= C * (9/5) + 32
#     return F



#     help(F2C)
# Help on function F2C in module __main__:

# F2C(F)
#'''F -> Fahrenheit''