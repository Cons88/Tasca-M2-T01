#!/usr/bin/env python
# coding: utf-8

# - Exercici 1
# Crea una llista que agrupi els mesos de l’any en trimestres (1T: gener, febrer i març; 2T: abril, maig, juny...), és a dir, una llista amb 4 llistes dins.
# 

# In[10]:


Any = ['PrimerTrimestre', 'SegonTrimetre', 'TercerTrimetre',' QuartTrimestre']
print(Any)


# In[11]:


PrimerTrimestre = ['Gener, Febrer, Marc']
SegonTrimetre = ['Abril, Maig, Juny']
TercerTrimetre = ['Juliol, Agost, Setembre']
QuartTrimestre = ['Octubre, Novembre, Decembre']


# In[20]:


Any = [PrimerTrimestre, SegonTrimetre, TercerTrimetre,QuartTrimestre]


# In[15]:


Any
[['Gener', 'Febrer', 'Marc'],
['Abril', 'Maig', 'Juny'],
['Juliol','Agost','Setembre'],
['Octubre','Novembre','Decembre']]


# In[27]:


Any [0]


# In[54]:


print(Any[0])


# - Exercici 2
# Crea un codi que et permeti accedir a:
# o	El segon mes del primer trimestre.
# o	Els mesos del primer trimestre.
# o	Setembre i octubre.
# 

# In[62]:


PrimerTrimestre = ['Gener', 'Febrer', 'Marc']
SegonTrimetre = ['Abril', 'Maig', 'Juny']
TercerTrimetre = ['Juliol', 'Agost', 'Setembre']
QuartTrimestre = ['Octubre', 'Novembre', 'Decembre']


# In[63]:


Any = [PrimerTrimestre, SegonTrimetre, TercerTrimetre,QuartTrimestre]


# In[65]:


print (Any)
                            


#  Els mesos del primer trimestre.

# In[66]:


Any [0]


#  El segon mes del primer trimestre

# In[67]:


Any[0][1]


# Setembre i octubre

# In[69]:


Any [2][2], Any [3][0]

