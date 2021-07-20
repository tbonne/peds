#!/usr/bin/env python
# coding: utf-8

# <img src='http://drive.google.com/uc?export=view&id=100E8FHwZxTg2d27HMWeXf05Av4IIqXT9' width="300" align = 'left'> 

# # <font color='lightblue'>Missing Data</font>

# In this exercise we will learn how to handle missing data. 
# 
# Outline:
# *  How to find missing data
# *  How to remove missing data (if appropriate!)
# 
# 

# ## <font color='lightblue'>Load Data</font>

# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100" align = 'left'>

# First load in the pandas library and bring in the NYC flight data

# In[1]:


#Import pandas library
get_ipython().run_line_magic('pinfo2', '')

#read in the NYC flight data
df_flights = ??


# Give a thumbs up in Slack once your done!

# # <font color='lightblue'>Identifying Missing Data</font>

# Most data that you'll find will have missing values, or values that cannot be true (i.e., errors). Here we will look at how to find missing values, and how to handle them.

# Below we use the method **isna()** to identify cells in the dataframe where the values are **NA**. We use the sum function ontop of the **isna** method to count the number of **NA** values.
# 
# > Note: when you combine methods in this way the outputs of the first (going left to right) act as inputs for the second. This is called method chaining, and we will use it with pandas objects!

# In[ ]:


#count Null values for each column of the dataframe
df_flights.isna().sum()


# So we can see that there are not that many missing values in this dataframe. Let's take a look at how many rows of data we have:

# In[ ]:


len(df_flights)


# And at what proportion of data is missing:

# In[ ]:


df_flights.isnull().sum() / len(df_flights)


# We can take a look at these missing values within the dataframe by opening the dataframe in colab (Files - dubble click on the file - then filter by NA)

# So we can see in this dataset there is very little in the way of missing data! But what should we do with those data entries? We could:
# 
# 1. Understand how/why they are missing (data story!)
# 1. Remove those data entries (missing at random?)
# 2. Fill them in with estimates (impute the missing data)

# # <font color='lightblue'>Drop Missing Data</font>

# Below we will remove the rows with missing data in one column. So if there is no data in this column then it will remove that entire row from the data.

# In[ ]:


#drop rows if air time contains missing values
df_flights_airtime_na = df_flights[df_flights.air_time.isna()==False]

#take a look at the new length of the dataframe
len(df_flights_airtime_na)


# It is also possible to remove any row that has missing values.

# In[ ]:


#drop rows if any column contain missing values
df_flights_sub_na = df_flights.dropna(how='any')

len(df_flights_sub_na)


# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100" align = 'left'>

# Try removing all the rows with NAs in arr_time.

# In[ ]:


#drop rows if arrival time contains missing values
df_flights_arr_time_na = ?

#check the length


# # <font color='lightblue'>Add column of missingness</font>

# Here the idea is that missing data might be useful for making predictions. Let's add another column to the DataFrame to identify missing data in *air time*.
# 
# > Here we use method chaining to select a column 'air_time', see if each row has an NA value. This gives us true and false values for each row.

# In[ ]:


#create new column with true/false if there is missing data in air time
df_flights['missingAirTime'] = df_flights.air_time.isna()

#take a look 
df_flights


# Let's add one more step to that method chain, and convert the true false into integers. To do so we'll add the method **asType('int')**, which converts the true/false into 1/0.

# In[ ]:


#create new column with true/false if there is missing data in air time
df_flights['missingAirTime'] = df_flights.air_time.isna().astype('int')

#take a look 
df_flights


# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100" align = 'left'>

# Try adding a column of missingness for plane tail number (i.e., tailnum).

# In[ ]:


#create new column with 1/0 if there is missing data in tailnum
df_flights[?] = ?

#take a look
get_ipython().show_usage()


# # <font color='lightblue'>Further reading</font>

# There are many ways to deal with [missing data with pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html). Just remember that some ways are more justifyable than others, and a good understanding of how the data came to be is key in deciding which ways might work best.
