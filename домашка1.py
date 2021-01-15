#!/usr/bin/env python
# coding: utf-8

# In[26]:


word = input('введите слово')

formula = len(word)/2

if len(word)% 2 == 0:
    print(word[int(formula)-1:int(formula)+1], '- четное число')
elif len(word)% 2 != 0:
    print(word[int(formula)], '- нечетное число')
    


# In[7]:





# In[32]:


a = 0
x ='введите число'
while x != 0:
    x = int(input())
    a += x
    print(a)
    


# In[115]:


boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len (girls):
    print('без пары:')
elif len(boys) == len (girls):
   #  print(boys,'и', girls)
    for b, g in zip(sorted(boys), sorted(girls)):
        print(b,'и', g)


# In[255]:



countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]


# In[256]:


countries_temperature[0]


# In[257]:


for countries in countries_temperature:
    x=sum(countries[1])//len(countries[1])
    a=(x-32)/(1+8/10)
    print(a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# x=user_1[-1-2:]+user_2[-1-2:]
# print(x)

# In[ ]:





# In[ ]:




