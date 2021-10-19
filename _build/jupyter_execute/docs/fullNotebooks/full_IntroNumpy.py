#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/tbonne/peds/blob/main/docs/IntroNumpy.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# <img src='http://drive.google.com/uc?export=view&id=11oIuCZt0sglfxu175KWiLj54wHbossfi'> 

# # <font color='darkorange'>Introduction to Numpy</font>
#  
# We will make use of **arrays** in this course, let's learn what they are and how we can use them!

# ## <font color='darkorange'>Using a python package</font>
# 
# Let's create an **array** using the numpy package.
#  
# > An array is like a list but has some nice built-in features that make them easier to work with. 
# 
# > Here we will use a *function* that has already been built by someone else. We will give it some inputs, and we will get some output(s). 
# 
# > The ever growing list of python packages will let us use very useful code from other data scientists!
# 
# Let's load in the **numpy** package, and create an array

# In[27]:



#importing code from already exhisting python packages!
import numpy as np

#create an array from a list of numbers
x1 = np.array([0,1,2,3,4,5,6,7])

#Take a look at what we made
x1


# ## <font color='darkorange'>Array slicing</font>
# 
# > Now we will try to slice out a portion of the array. We'll do this just like we did with lists, using:
# 
# > Array[start:stop:step]
# 
# 

# 
# Try out a few combinations on our 1d array!

# In[28]:


#first three values
x1[0:3:1]


# As the defaults for the start stop step are 1, you might also use the following.

# In[29]:


#first three values (default step is by 1)
x1[:3]


# In[30]:


#values from the 4th value onwards
x1[3:]


# **2 dimensional array (2d array)**

# Now let's try slicing a 2d array now. You can think of a 2d array as a matrix with rows (i) and columns (j).
# 
# <img src='http://drive.google.com/uc?export=view&id=1JmCw-EvTk5ldztAXnwjmnNtroY9pyzqi'> 
# 
# 
#  To create a 2d array we will use a function from the numpy package.  
# 

# In[31]:


#using code from the np package generate an arry of random integers
x2 = np.random.randint(low=1, high=10, size=(3,3) )  # 3 rows x 3 columns array

x2


# Slicing in 2d works the same way as in 1d, we just have to specify which rows and columns we'd like.
# 
# > array[rows, columns]
# 
# > array[start:stop:step, start:stop:step]

# In[32]:


#let's take the first two rows, and all the columns
x2[0:2,:]


# In[33]:


#let's take all the rows, and the last column
x2[:,2]


# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100">  

# Let's try out what you've learnt. Try and create a 2d array of size 5x5 of integers using the numpy package:

# In[34]:


x3 = np.random.randint(low=1, high=10, size=(5,5) )  # Two-dimensional array

x3


# And now select only the first column:

# In[35]:


x3[:,0]


# **3 dimensional array (3d array)**
# 
# As the demensions of the array grow we use the same techniques to select rows, coloumns, and depths. 

# 
# <img src='http://drive.google.com/uc?export=view&id=1aecsAOPEeofPNgZfH_bqBQGJBlPWDhxI'> 

# We can keep track of the shape of these arrays by using the **shape** method.
# 
# 1d array

# In[36]:


x1.shape


# 2d array

# In[37]:


x2.shape


# For most of this course 2d array slicing will be as far as we go!

# ## <font color='darkorange'>Arithmatic with arrays!</font>

# We can also do arithmatic on arrays. 
# 
# Here we will first add 1 to each value of the first column of your array.

# In[38]:


x1


# In[39]:


x1 + 1


# You can also add two arrays together. For example, let's add the first and fourth columns of the x3 array.
# 
# 

# In[40]:


x3[:,0] + x3[:,1]


# Add you can assign the outcome of this addition to the third column of your array.

# In[41]:


x3[:,2] = x3[:,0] + x3[:,1]

x3


# <img src='http://drive.google.com/uc?export=view&id=1WC4tXGCEF-1_2LQ74gIxJAZ-GLXCwBdK' width="100">  
# 
# 

# Try and create a 2d array with three columns and 10 rows using the numpy package, add the first and second columns together, and place the values in the third column.

# In[42]:


x4 = np.random.randint(low=1, high=10, size=(10,3) )  # Two-dimensional array

x4


# In[43]:


x4[:,2] = x4[:,0] + x4[:,1]

x4


# ## <font color='darkorange'>Further reading</font>
# 
# > If you would like to learn more, the *Python Data Science Handbook* by Jake VanderPlas has a good chapter on [using numpy](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html).
