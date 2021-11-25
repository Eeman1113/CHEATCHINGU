import  google 
import  wikipedia 
import os

def question_extracter(a):
    l=[]
    t=[]
    for i in a:
        
        if i=='Q':
            for j in a[a.index(i):]:
                if j=='?':
                    l.append(j)
                    print(l)
                    t.append(l) 
                    break
                else:
                    l.append(j)
        else:
            continue
                
a=input("Enter the question: ")
a=list(a)
print(a)
question_extracter(a)