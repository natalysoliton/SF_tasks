#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint
 
attempts = 1
Var1 = randint(1,101)
print ("Загадано число от 1 до 100")

Var2 = int(input("Ваш вариант? - "))

while Var1 != Var2:  #Цикл на совпадение задуманного числа с задаваемым
    if Var1 > Var2: 
        print (f"Угадываемое число больше {Var2} ") #Когда задаваемое чило больше задуманного
    elif Var1 < Var2: 
        print (f"Угадываемое число меньше {Var2} ") #Когда задаваемое чило меньше задуманного
    attempts += 1 #Плюсуем попытку
    Var2 = int(input("Ваш вариант? - ")) #Любое вводимое число превращать в целое int
print (f"Вы угадали число {Var1} за {attempts} попыток ") #Вывод на экран результата


# In[ ]:




