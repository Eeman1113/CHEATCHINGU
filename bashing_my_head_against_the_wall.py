import  google 
import  wikipedia 
import os

def question_extracter():
    with open('recognized.txt','r') as g:
        b=g.read()
        '''remove empty strings from b'''
        b=list(filter(None,b.split('\n')))#remove empty strings from b
        

            
    
    
    b=list(b)
    l=[]
    t=[]
    f=len(b)
    for i in range(0,f):#loop running for length of b
        
        if b[i]=='Q':#if statement to find weather index value is q or not 
            for j in b[i:]:#loop running for all elements of b from index of Q to end
                if j=='?':#breaking loop if a ? is found
                    l.append(j)#appending ? to l
                    t.append(l)#appending l to t for making a list with all the questions
                    l=[]#emptying the list l
                    break#breaking loop and starting the if statement again
                else:#if a ? is not found then appending the elements to l
                    l.append(j)
        else:# if a q is not found then continue the loop
            continue
    print(t)#the list with all the questions is printed
question_extracter()