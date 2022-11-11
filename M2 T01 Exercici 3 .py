#!/usr/bin/env python
# coding: utf-8

# - Exercici 3
# Crea una llista amb nombres desordenats i respon a les següents preguntes:
# o	Quants números hi ha?
# o	Quantes vegades apareix el número 3.
# o	Quantes vegades apareixen els nombres 3 i 4?
# o	Quin és el número més gran?
# o	Quins són els 3 números més petits?
# o	Quin és el rang d’aquesta llista?
# 

# In[1]:


Lista = [10, 5, 9, 7, 2, 4, 1, 0, 4, 3, 3, 18]
print(Lista)




















#  Quants números hi ha? 

# In[2]:


print (len(Lista))


# In[ ]:





# Quantes vegades apareix el número 3?

# In[6]:


print(Lista.count(3))


#  Quantes vegades apareixen els nombres 3 i 4?

# In[8]:


print (Lista.count(4))


# In[2]:


Lista = [10, 5, 9, 7, 2, 4, 1, 0, 4, 3, 3, 18]
print(Lista)


# Quin és el número més gran?

# In[4]:


max(Lista)


# In[5]:


min(Lista)


#  o Quins són els 3 números més petits? 

# In[4]:


Lista = [10, 5, 9, 7, 2, 4, 1, 0, 4, 3, 3, 18]
print(Lista)


# In[8]:


min(Lista.count(3)) # No vaig poder resoldre aquesta pregunta


# o Quin és el rang d’aquesta llista?

# In[10]:


range(Lista) # El range de una llista entenc es el primer nombre de la llista fins al nombre abans 

# del darrer nombre que es mostra 

