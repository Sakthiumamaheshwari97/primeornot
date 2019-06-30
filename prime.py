op=int(input())
if(op>1):
   for i in range(2,op):
        if(op%i)==0:
            print("no")
            break
   else:
       print("yes")
else:
      print("no")
