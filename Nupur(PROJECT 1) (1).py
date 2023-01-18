#!/usr/bin/env python
# coding: utf-8

# ###### DS_1 PROJECT
#  Inheritimg Mobile Class with its variable

# In[ ]:


class Mobile:
    def __init__(self,name , Displaysize, colour,material ,cost):
        
        self.name = name
        self.Displaysize = Displaysize
        self.colour = colour
        self.material = material
        self.cost = cost
    
    
    def call(self):
        print("Calling")
         
    def msj(self):
        print("Write Something")
    
    def playingGames(self):
        print("Play Something")
    
    def phoneProperties(self):
        print(self.name)
        print(self.Displaysize)
        print(self.colour)
        print(self.material)
        print(self.cost)
        
    


# In[5]:


Apple = Mobile( "I Phone14" ,7.5 , "Mint Green","Metalic",85000)
Motorola = Mobile("Moto G" , 7 ,"Black" ,"Metalic" ,35000)
Samsung = Mobile("Samsung Galaxy A52s" , 7.5 , "Purple" , "Metalic" ,38000)


#heap memory


#Apple

#Name-I Phone14 
# Size-7.5 
# Colour - Mint Green
# Material - Metalic
#cost- 85000

#Motorola

#Name-Moto G 
# Size-7
# Colour - Black
# Material - Metalic
#cost- 35000


#Samsung

#Name-Samsung Galaxy A52s
# Size-7.5
# Colour - Purple
# Material - Metalic
#cost- 38000


# In[8]:


Apple.phoneProperties()
Motorola.phoneProperties()
Samsung.phoneProperties()

