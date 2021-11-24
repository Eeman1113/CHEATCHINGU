import  google 
import  wikipedia 
import os

def question_extracter(a):
    l=[]
    for i in a:
        print(i)
        if i=='Q':
            for j in a[a.index(i):]:
                if j=='?':
                    l.append(j)
                    print(l)
                    break
        else:
            continue
                
a=input("Enter the question: ")
a=list(a)
print(a)
question_extracter(a)