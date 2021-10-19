#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/tbonne/peds/blob/main/docs/IntroPython.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# 
# 
# <img src='http://drive.google.com/uc?export=view&id=1qaKkjdduZW96yCyFyPKRK8J0Pfem4Ldk'>

# # <font color='darkorange'>Short introduction to Python</font>
# 
# In this course you'll learn to do data science with python! Rather than aiming to give a grand overview of all the great possibilities of using python, we will learn what we need to know to run through the data science workflow, and build our python skills along the way.
# 
# That said let's learn some basics of python to help us get started!
# 

# ## <font color='darkorange'>Data types in Python</font>

# First we will explore the main kinds of data types you can have in python:
# 1. **Integers** 1,2,3,4
# 2. **Floats** 1.2, 2.3, 5.6
# 3. **Boolean** True / False
# 4. **String** 'this is a string'
# 5. **Lists** ['oneString', 'twoString'] or [1,2,3,4] or [1.2, 2.3, 5.6] or...
# 6. **Dictionaries** {'key':value}

# In[23]:


#This is an integer
c1 = 1

#this is an float
c2 = 1.2

#this is a boolean
c3 = True

#this is a string
c4 = "oneString"

#this is a list
c5 = ["oneString", "twoString", "threeString"]


# We can do simple mathematical opperations with the different data types:

# In[24]:


c1 - c2
c1 + c2
c1 * c2
c1 / c2


# As well as ask questions about relative size:

# In[25]:


c1 > c2
c1 <= c2


# Try doing something that you know should not work. The error message points to the line where the error occured, and tries to help you figure out what went wrong (stack overflow link).

# In[26]:


c4 + c1


# The order of operations is also important. Take a look at the differences below.

# In[27]:


1 + 2 * 3


# In[28]:


(1 + 2) * 3


# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100">
# 

# Add 24 to 200 and then divide by 4

# In[29]:


( 24 + 200 ) / 4


# **List**

# > We'll take a closer look at lists as they will come in very handy throughout the course.

# **List Indexing**
#  
# Indexing is where you'd like to get a value out of a list, or change one value in the list.

# In[30]:


#create list
x = ['apples','oranges']


# Grabing one value:

# In[31]:


#take a look at the first value in the array (note: starts at 0 index)
x[0]


# Modifying the first value:

# In[32]:


#assign a new value!
x[0] = 'watermelon'

#how has it changed?
x


# **List Slicing**

# > Slicing a list is where you'd like to get a few values from a list, or modify a few values in the list
# 
# > To do slicing on a list we use **x2[start:stop:step]**

# Let's make a list of numbers:
# 
# 

# In[33]:


#create a list of numbers 
x2 = [0,1,2,3,4,5,6,7,8,9]

#take a look
x2


# Now when we want to grab a few numbers we can use slicing

# In[34]:


#get the first three values (Note: we did not specify the 'step' size so it defaults to use 1)
x2[0:3]  


# In[35]:


#get everything after the third value
x2[3:]


# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100">
# 

# Try and select only the values 5 to 7

# In[36]:


x2[5:8]


# Create a list of 5 of your favorite foods, then use slicing to select the first three

# In[37]:


#create a list of foods
foods = ['ice cream','pizza','samosa','blue berries','pie']

#use slicing to select the first three
foods[0:3]


# **Dictionaries**
# 
# > Dictionaries are very useful objects in Python. They have *keys* that are associated with *values*, in the same whay that words in a dictionary are associated with definitions.
# 
# Let's take a look at an example.

# In[38]:


#create a dictionary
dict_ages = {"amy": 23, "scott":43, "mel":33}

dict_ages


# Select *values* by using *keys*

# In[39]:


#select the key amy to get the value (age)
dict_ages["amy"]


# Keys are generally strings or numeric, while values can be anything: numeric, strings, lists, other dictionaries... etc
# 

# In[40]:


#create a dictionary with names as keys and a list of test scores as values.
dict_tests = {"amy": [98,87,100], "scott": [56,100,79], "mel":[55,65,75]}

dict_tests['amy']


# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100">
# 

# Create a dictionary with the keys as the different data types we learnt, and the values as a descriptive text.

# In[41]:


dict_dtypes = {"Integer":"e.g., discrete numeric values: 1, 2, 3, 4, 5", "Float":"e.g., continuous numeric values: 1.2, 2.3, 5.6", "Boolean":"true or false","List":"['oneString','twoString] or [1,2,3,4] or [1.2, 2.3, 5.6]", "Dictionary":"{‘key’:value}"}


# Select the value of one data type using the key name

# In[42]:


#Select value using a key
dict_dtypes["List"]


# ## <font color='darkorange'>Further reading</font>
#   
# 
# > There are lot's of resources out there to supplement this introduction to python. One good resource is the book by Jake VanderPlas: [Python data science handbook](https://jakevdp.github.io/PythonDataScienceHandbook/).
#   
#   
# 
# > In this course we will build slowly on our python skills. Each new challendge in developing our data science workflow will require learning new bits of python code. The idea here is that you'll learn python through applied examples.
#   
#   
#     
# > If you would like the notebook without missing code check out the [full code](https://colab.research.google.com/github/tbonne/IntroDataScience/blob/main/fullNoteBooks/IntroClustering1_kmeans_HDBScan_full.ipynb) version.
# 
