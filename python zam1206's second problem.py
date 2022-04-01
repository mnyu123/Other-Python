num = 100
con = 0
row = 10

while num <= 200:
    if(num % 5 == 0 or num % 6 == 0 ) and not (num % 5 == 0 and num % 6 == 0 ):
        print(format(num,'4d'),end='') 

        con +=1
        if con % row == 0:
            print()
    
    num +=1
