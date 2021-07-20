#!/usr/bin/env python
# coding: utf-8

# <img src='http://drive.google.com/uc?export=view&id=1PmB2IttC7fpQdCjY9F03KDnV_Oe_MtCp' width="300" align = 'left'> 

# # <font color='lightblue'>Grouping data</font>

# In this exercise we will learn to use the function **groupby**. This is often an important step in data wrangling, and we will come back to it often when getting data ready for visualization or modeling.
# 
# Outline:
# *  Get summary statistics by each group
# 

# # <font color='lightblue'>Summary statistics by group</font>

# We will first use groupby to group the dataframe by airline carrier, to get an idea of which airline has the most delays! 
#  
# Let's get the sum of all the delays for each carrier.
# > We are using method chaining just like we did with the missing data exercise.

# In[1]:


#Group rows by airline carrier, then take the departure delay column values, and finally sum them up.
df_flights.groupby('carrier').dep_delay.sum()


# Let's use another method called **sort_values** to help visualize which airline carrier has accumulated the most departure delays?

# In[ ]:


df_flights.groupby('carrier').dep_delay.sum().sort_values(ascending=False)


# Can you think of a potential problem with using the sum of departure delays?
# 

# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100" align = 'left'>

# Let's try out your new found skills with groupby to see what airline carrier has the highest mean arrival delay? I.e., which airline is most likely to get you to your destination late!

# In[ ]:


df_flights.groupby('?').?.mean().?


# Feel free to post your answer to Slack! 

# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100" align = 'left'>

# Bonus question: Which airline shows the largest ability to make up lost time? 
# > I.e., what is the mean difference between departure delays and arrival delays for each carrier?

# In[ ]:


#Create a new column that is the difference between dep_delay and arr_delay
df_flights['diff_delay'] = ? - ?

#Group by carrier, get the mean difference, and sort it by decending values
df_flights.?.diff_delay.?


# Post your answers to Slack, and see if others agree!
