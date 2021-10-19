#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/tbonne/peds/blob/main/docs/introData/IntroData2_LoadingData.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# <img src='http://drive.google.com/uc?export=view&id=1FZW6_R4T8PailZCgLSdNTZLIDoAG9VM5' width="300" align = 'center'> 

# ## <font color='darkorange'>Using existing data</font>

# ***

# In this exercise we will start working with some real data. We will first learn how to load in data, then test out what you've learnt about DataFrames.
# 
# Outline:
# *   Load in data
# *   Explore the dataframe
# *   Manipulate the dataframe

# In[ ]:


#Load in pandas
import pandas as pd


# ### <font color='darkorange'>Loading data</font>

# There are many ways to load in datasets, here we'll look at two methods.

# But first let's get the data:
# > Goto the shared [data folder](https://drive.google.com/drive/folders/1s2Civxvys_SR1sFF7D2ept1GSmFbICQb?usp=sharing) for the class and download nyc_flight_data.csv
# 
# 

# Let's then load in the flights data using a function from pandas called *read_csv*.

# Option 1 - load from temporary folder (easier but not permanent). 
# 1. Drag and drop the data into the files tab on the left. 
# 2. Then right click and copy the path.
# 3. Then paste the path into the pd.read_csv(PATH_HERE) 

# In[ ]:


#load in the nyc flight data
df_flights = pd.read_csv('/content/nyc_flight_data.csv') 


# Option 2 - load from your google drive
# 1. mount your google drive

# In[ ]:


#mount your google drive
from google.colab import drive
drive.mount('/content/gdrive')


# 2. Use the files tab on the left to find the file you like to load 
# 3. Right click on the file and copy the path
# 4. Paste the path into the pd.read_csv()

# In[ ]:


##load in the nyc flight data 
df_flights = pd.read_csv('/content/gdrive/MyDrive/Colab Notebooks/DataScience/dataDSI/nyc_flight_data.csv') 


# ### <font color='darkorange'>Exploring the dataframe</font>

# Now that we have the dataset loaded, let's take a look at it. Let's first look at it's shape.

# In[ ]:


df_flights.shape


# Here we can get a quick look the dataframe using the **head** method.

# In[ ]:


df_flights.head(5)


# Or if you like a little more options you can use the folowing to help visualize the table better.

# In[ ]:


get_ipython().run_line_magic('load_ext', 'google.colab.data_table')


# Now try looking at your dataframe again.

# In[ ]:


df_flights.head(5)


# We can also see what kinds of variables are in the dataframe by using the **dtype** method:

# In[ ]:


#find the data types
df_flights.dtypes


# We can get a quick description of the numeric data using the **describe** method:

# In[ ]:


df_flights.describe()


# We can also take a look at the dataframe by double clicking on the nycflights.csv file in the files tab on the left. This gives us a more dynamic view as we can use filter to explore the data a little more.
# Try filtering for carrier: e.g., AA

# ### <font color='darkorange'>Manipulate the dataframe</font>

# Let's now use your new found skills to answer some questions!

# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100">

# Make a dataframe with only carrier, arr_delay, dep_delay, and air_time as columns.

# In[ ]:


#keep only the a subset of columns
df_flights_sub = df_flights.loc[ : , ['carrier','arr_delay','dep_delay','air_time']  ]  #Warning: the column names will be case sensitive!

#take a look at the new dataframe
df_flights_sub


# Make a dataframe of all flights that have an arrival delay of greater than 60min

# In[ ]:


#keep only the rows with arr_delay of greater than 60 minutes
df_flights_delayed60 = df_flights[df_flights.arr_delay>60]

#What is the shape of this new dataframe
df_flights_delayed60.shape


# Can you also calculate how many flights arrived earlier than expected (i.e., where the plane arrived before the scheduled arrival time). 

# In[ ]:


#keep only the rows with arr_delay less than 0 minutes (i.e., negative delay!)
df_flights_early = df_flights[df_flights.arr_delay<0]

#what is the shape of this new dataframe
df_flights_early.shape


# Finally can you express these numbers as percentages?

# In[ ]:


#percentage of flights delayed more than 60mins, i.e., number delayed rows / number total rows
df_flights_delayed60.shape[0]/df_flights.shape[0] * 100

#or just
226 / 3614


# In[1]:


#percentage of flights arriving before scheduled time, i.e., number early rows / number total rows
len(df_flights_early) / len(df_flights) * 100


# Post to slack once you've got an answer!

# ### <font color='darkorange'>Further reading</font>

# The many ways to work with [data in colab](https://neptune.ai/blog/google-colab-dealing-with-files).
# 
# > If you would like the notebook without missing code check out the [full code](https://colab.research.google.com/github/tbonne/peds/blob/main/docs/fullNotebooks/full_IntroData2_LoadingData.ipynb) version.
