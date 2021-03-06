#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/tbonne/peds/blob/main/docs/introData/IntroData1_DataFrames.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# <img src='http://drive.google.com/uc?export=view&id=1RkQNovXbpa5a43mEAIpdWlL_ungUN-8j' width="300" align = 'center'>

# ***

# # <font color='darkorange'>Introduction to DataFrames</font>
# 
# In this exercise we will introduce **dataframes** which are objects in python that we will work a lot with in this class. These **dataframes** will be how we work with data, and get the data ready for visualizing and modeling.

# Outline:
# 
# 
# *   Creating dataframes
# *   Selecting from DataFrames
# *   Creating new columns
# *   Filtering rows
# *   DataFrame functions
# 
# 

# We'll be using the **Pandas** library to do most of this work. Let's take a look at how to create and modify dataframes using **Pandas**! 

# ## <font color='darkorange'>Creating DataFrames</font>

# In[1]:


#import python libraries that we will use
import numpy as np
import pandas as pd


# Create a dataframe from scratch

# In[2]:


## create a dictionary
d = {'A':[1,2,3,4], 'B':[5,6,7,8] }

## convert the dictionary to a dataframe
df_test = pd.DataFrame(data=d)

#take a look at the dataframe
df_test


# Add a column to the data frame

# In[3]:


#add list of names
df_test['ID'] = ['Steve','Sarojini','Emil','Sarah']

#add country
df_test['country'] = 'Canada'

#take a look (notice how it filled in the country!)
df_test


# All dataframes also have an index, which keeps track of what data is in each row/column.

# In[4]:


#index of the rows
df_test.index


# In[5]:


#index of the columns
df_test.columns


# ## <font color='darkorange'>Selecting from a Dataframe</font>

# In[6]:


#take a look at the full dataframe
df_test


# In[7]:


#grab the A column
df_test['A']


# In[8]:


#or similarly grab the A column
df_test.A


# In[9]:


#grab the first three rows
df_test[0:3]


# It is also possible to select by slicing similar to the numpy array! 
# > Here we use the method **loc** with square brackets to select rows and columns 
# [rows , columns] with the similar slicing [start:stop:steps]. The **loc** method uses the index and the column names of the dataframe.
# 
# Below we take the first three rows and only the A and B columns:

# In[10]:


#first three rows and the A and B columns
df_test.loc[ 0:2 , ["A","B"] ]


# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100" align = 'left'>  
# <br>
# <br>
# <br>
# Let's try out what you've learnt. Try and select the ID and Country columns and only the third row:

# In[11]:


#ID and country columns, and the third row
df_test.loc[2,['ID','country']]


# ## <font color='darkorange'>Selecting from a Dataframe: using positions</font>

# In[12]:


#full dataframe
df_test


# In[13]:


#first three rows and the second and thrid columns - using :
df_test.iloc[0:3,1:3]


# In[14]:


#second, and fourth rows, and second and fourth columns - using lists
df_test.iloc[ [1,3] , [1,3] ]


# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100" align = 'left'>  
# <br>
# <br>
# <br>
# Try and select the ID and Country columns and only the third row using iloc:

# In[15]:


#ID and country columns, and the third row
df_test.iloc[2, 2:4]


# ## <font color='darkorange'>Creating new variables</font>

# In[16]:


#multiply the B column by 4 to create a new variable C
df_test['C'] = df_test['B'] * 4

#multiply the C column by A to create a new variable D
df_test['D'] = df_test['C'] * df_test['A']

#take a look
df_test


# ## <font color='darkorange'>Filtering DataFrames</font>

# Keep only the rows/columns that you'd like

# In[17]:


#keep only the rows where A is less than 3
df_test_sub = df_test[df_test.A<3]

#keep only the columns A and ID
df_test_sub = df_test_sub[['A','B']]

#take a look
df_test_sub


# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100" align = 'left'>  
# <br>
# <br>
# <br>
# Add the C and D columns together and select only the rows with values greater than 100:

# In[18]:


#Add the columns C and D together
df_test['E'] = df_test['C'] + df_test['D']

#keep only the rows where D is greater than 100
df_test_100 = df_test[df_test.E>100]

#take a look
df_test_100


# ## <font color='darkorange'>Dataframe functions</font>

# When we create a dataframe we are creating an object, and this dataframe object has functions built in. Let's take a look at a few now, and we will see more as we go along in this course. 
# 
# Try just typing df_test. 
# 
# After typing the "." you should see the list of functions available to you once you've created a dataframe object. 

# In[19]:


df_test.


# One useful function is the *dtypes* function. It will tell us what data type is in each column.

# In[20]:


#What data type is stored in each column
df_test.dtypes


# The *sum* function is very useful for quickly summing up the values in a column.

# In[21]:


#What is the sum of the A column
df_test.A.sum()


# The *?* is a very useful function in general, and can provide us with useful information about most objects.

# In[22]:


#find help on functions, objects, ... etc
get_ipython().run_line_magic('pinfo', 'df_test')


# ## <font color='darkorange'>Further reading</font>
# 
# Pandas quick intro:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
# </br>
# Pandas longer intro:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
#   
# > If you would like the notebook without missing code check out the [full code](https://colab.research.google.com/github/tbonne/peds/blob/main/docs/fullNotebooks/full_IntroNumpy.ipynb) version.
