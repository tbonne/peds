#!/usr/bin/env python
# coding: utf-8

# <img src='http://drive.google.com/uc?export=view&id=1PmB2IttC7fpQdCjY9F03KDnV_Oe_MtCp' width="300" align = 'left'> 

# # <font color='lightblue'>Combining data</font>

# This exercise will walk you through how to combine dataframes. Often combining dataframes will let you add aditional information to each row, or add additional rows.
# 
# Outline:
# *  Look at how to add more rows of data using **concat**
# *  Look at how to add more columns of data using **merge**
# 

# ## <font color='lightblue'>Concatinating</font>
# 
#  Concatinating let's us combine two dataframes, that share similar columns, vertically. You can think of this as stacking one dataframe ontop of another.

# In[1]:


#import pandas 
import pandas as pd
import numpy as np


# In[ ]:


#create a simple dataframe
df_top = pd.DataFrame({'score':[12,22,13,24,15], 'class':['1','1',np.NaN,'2','2']})

#take a look
df_top


# In[ ]:


#create a simple dataframe
df_bottom = pd.DataFrame({'score':[16,17,18,19,20], 'class':['3','3','4','4','4']})

#take a look
df_bottom


# In[ ]:


#contaconate the dataframes together. Note: the square brackets are there to pass the dataframes to the concat method as a list of dataframes.
pd.concat([df_top,df_bottom])


# But what happends when there are extra or missing columns?

# In[ ]:


#create a simple dataframe without the B column and a new column
df_messy = pd.DataFrame({'score':[11,21],'school':['1','2']})

#take a look
df_messy


# In[ ]:


pd.concat([df_top,df_bottom,df_messy])


# We can see that when we contatinate the dataframes, pandas adds in missing values where there are no values.

# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100" align = 'left'>

# Try to create two dataframes with the same column names, and then use concat to combine them.

# In[ ]:


#create first
df1 = pd.DataFrame({???})

#create second
df2 = ?

#combine the dataframes
pd.concat(?)


# ## <font color='lightblue'>Joining</font>
# 
# 
# Joining lets us combine two dataframes that share similar values horizontally. You can think of this as sliding two dataframes next to each other.
# 
# When joining you often want to increase the amount of information in each row (i.e., adding more columns).
# 
# Let's try a **left join**

# In[ ]:


#let's use as the dataframe of interest
df_top


# In[ ]:


#create some extra information
df_right = pd.DataFrame({'class':['1','2','3'],
                         'teacher':['Robby','Sarah','Alex']})

#take a look
df_right


# In[ ]:


#Let's add some extra information to each row
pd.merge(left=df_top,right=df_right,on='class', how="left")


# Notice how the merge took the two teacher names and associated them with the right class. Here we end up with many rows with Robby and Sarah. This is an example of a many-to-one join. 

# Right join

# In[ ]:


pd.merge(left=df_top,right=df_right,on='class', how="right")


# Inner join

# In[ ]:


pd.merge(left=df_top,right=df_right,on='class', how="inner")


# outer join

# In[ ]:


pd.merge(left=df_top,right=df_right,on='class', how="outer")


# Generally when joining two dataframes the left join is the most common. In this case you have a main dataframe that you'd like to add information to.

# ## <font color='lightblue'>Join airport data</font>

# Let's load in the flight data again and add airport size information using joins!

# In[ ]:


#load flight data from google drive
df_flights = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/DataScience/dataDSI/nyc_flight_data.csv")

#take a look
df_flights


# Download the data with the destination [information](https://drive.google.com/file/d/1-ACJcTJkGlHG_lNqeNIjACh6Dt7NHxBZ/view?usp=sharing).

# In[ ]:


#place the file in your google drive folder, and load it into colab using pd.read_cvs()
df_dest = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/DataScience/dataDSI/destination_size.csv')

#take a look
df_dest


# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100" align = 'left'>

# Can you merge the two dataframes (df_flights and df_dest) so that you'll have all the destination airport sizes. 
# > This might be useful to compare arrival delays of individual flights to the size of the airport?

# In[ ]:


#join the two dataframes so that you'll have 
pd.merge(?)


#  What kind of join did you use?

# By merging the two dataframes we now have the amount of delay along with the size of the destination airport. We could then look at the relationship between the two using a figure or a model.

# Further reading
# 
# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
# 
# 
