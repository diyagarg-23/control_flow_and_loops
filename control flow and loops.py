#!/usr/bin/env python
# coding: utf-8

# In[3]:


#FLOW CONTROL STATEMENTS
#conditional statements

#check if num is even
num = int(input("enter num: "))
if num%2 == 0: #comparision operator
    print("number is even") #indentation


# In[4]:


#check num is even or not
num = int(input("enter a number: "))
if num%2 == 0:
    print("number is even")
else:
    print("number is odd")


# In[5]:


'''create a Python program that calculates and displays the grade of a student based on the
Score >=90: A,80 <= Score <90: B,70<= Score <80: C,60 <= SCore < 70: D, Score < 60: F'''

score = float(input('Enter your score: '))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# In[6]:


#while loop ->repitition
#sum of digits of given number: 12 =3

#initialization
#condition
#update
sum=0
n=int(input('Enter a number: ')) #initialisation
while n!=0: #condition
    r= n%10
    sum= r + sum
    n= n//10 #updation
print(sum)


# In[7]:


#for loop ->sure about end point
#print from 1 to 10

for i in range(1,11): #last one is excluded
    print(i)


# In[8]:


i=1
while i<=10:
    print(i)
    i+=1


# In[9]:


#incrementing by 2
for i in range(1,11,2): #last one is excluded
    print(i)


# In[12]:


#multiples of 5
for i in range(0,20,5):
    print(i)


# In[13]:


#incrementing by 2
i=1
while i<=10:
    print(i)
    i+=2


# In[18]:


#break, continue and pass
for i in range(-5,6):
    if i==4:
        continue
    else:
        print(i)


# In[16]:


#break, continue and pass
for i in range(6):
    if i==4:
        break
    else:
        print(i)


# In[19]:


#break, continue and pass
for i in range(6):
    if i==4:
        pass
    else:
        print(i)


# In[ ]:


#Intro to functions
def add(a,b):
    return a+b
add(8,4)

