#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint
 
attempts = 1
Var1 = randint(1,101)
print ('Загадано число от 1 до 100')
Var2 = int(input('Ваш вариант? - '))
while Var1 != Var2:
    if Var1 > Var2: print ('Угадываемое число больше ' + {Var2})
    elif Var1 < Var2: print ('Угадываемое число меньше ' + {Var2})
    attempts += 1
    Var2 = int(input('Ваш вариант? - '))
print ('Вы угадали число' + {Var1} +' за ' + {attempts} + ' попыток')


# In[ ]:




