#!/usr/bin/env python
# coding: utf-8

# - Exercici 4
# Crea un diccionari de la següent forma i respon a les preguntes:
# compra = { "Pomes" : {"Qty": 5, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66} }
# o	Afegeix alguna fruita més
# o	Quant han costat les peres en total?
# o	Quantes fruites hem comprat en total?
# o	Quina és la fruita més cara?
# 

# In[2]:


compra = {"Pomes" : {"Qty": 5, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66}}
compra


# - Afegeix alguna fruita més

# In[6]:


compra.update({"Mango": {"Qty" : 9, "€": 0.92,}})
print(compra)


# - Quant han costat les peres en total? 

# In[4]:


compra = {"Pomes" : {"Qty": 5, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66}}
compra


# In[6]:


compra["Peres"]["Qty"] * compra["Peres"]["€"]


# o Quantes fruites hem comprat en total?

# In[7]:


compra = {'Pomes': {'Qty': 5, '€': 0.42}, 'Peres': {'Qty': 3, '€': 0.66}, 'Mango': {'Qty': 9, '€': 0.92}}
print(len(compra))


# o Quina és la fruita més cara?

# In[17]:


compra_dict = {'Pomes': {'Qty': 5, '€': 0.42}, 'Peres': {'Qty': 3, '€': 0.66}, 'Mango': {'Qty': 9, '€': 0.92}}

find_max = max(compra) 
find_max
# No he pogut resoldra aquesta pregunta 


# In[ ]:


compra_dict = {'Pomes': {'Qty': 5, '€': 0.42}, 'Peres': {'Qty': 3, '€': 0.66}, 'Mango': {'Qty': 9, '€': 0.92}}

