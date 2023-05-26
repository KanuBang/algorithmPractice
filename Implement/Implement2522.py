'''
3

  * => control 1
 ** => control 0
*** => control -1
 **
  *
'''
n = int(input())
control = n-1 #2
turnOver = False

for i in range(0, n*2-1):
    for j in range(0, n):
        
        if j >= control:
            print("*",end="")
        else:
            print(" ",end="")
              
    
    if turnOver == False:
        control-=1

    if turnOver == False and control < 0:
        turnOver = True
        control += 1
    
    if turnOver == True:
        control += 1
    print()
        