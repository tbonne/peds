#!/usr/bin/env python
# coding: utf-8

# <img src='http://drive.google.com/uc?export=view&id=1_zplE3GeQqAtwo5GzGOJIdN-EpkM1gxy' width="500" height="200">

# # <font color='lightblue'>Introduction to colaboratory notebooks!</font>
# 
# We'll go through some simple steps to using notebooks.
# 
# 
# Notebooks are made up of **text blocks** like this one, and **code blocks** (like the one just below)
# 
# 
# 
# 

# In[1]:


#add code here (a hashtag in the code creates a comment)
#let's create a variable i, make it equal to 1, and then print it
i = 1
print(i)

#you can run this code by clicking the play button (or pressing ctr-enter)
#you will see the output of the print command just below


# Let's add another code block, this time we will add 1 to i and print it.

# In[2]:


#let's add 1 to i and print it again
i = i + 1
print(i)


# By combining text blocks with code blocks we can build an analysis in a way that tells a story.
# 
# It is important to note the order you run the blocks can matter. You can see the current order by looking at the square brackets [ ] next to your code chunks. 
#  
#  Try playing around with running the above blocks a number of different ways and watch how the outputs change.

# ## <font color='lightblue'>Saving your work</font>
# 
# When we save our work it will place the code in our google drive. Try saving it. Do you see it in your google drive in the colaboratory folder?
#  
# We also have the option of searching you google drive for data. When we start bringing in data this is a very useful option. To the left of the screen you should see the files button. If you click on it and then on "mount drive" and give it permission to connect to your google drive. 
# 
# You should now be able to navigate using the files tab on the left to see all your files.
# 

# ## <font color='lightblue'>Collaborating!</font>
# 
# Working with colab also allows us to share access to a notebook. We will use this in class when we do small group projects, but feel free to help out your classmates and share especially useful bits of code you might find as we go through the course!

# ## <font color='lightblue'>Staying organized</font>
# 
# If you click on the text blocks you'll see you have options to **bold**, *italize*, or [add hyper links](https://colab.research.google.com/notebooks/markdown_guide.ipynb). You can also add heading, which you can then see in table of contents (to the left). These are all great tools to create a really organized and readable analysis.
# 
# Try adding a text box below with some formatting!

# 

# If you'd like to dig a litte deeper into how to with colab text blocks you can take a look at this [overview](https://colab.research.google.com/notebooks/markdown_guide.ipynb).

# ## <font color='lightblue'>Code version control</font>
# 
# An important option when your code gets more complicated is that you might want to jump back to an older version. To do so you can click on File -> Revision History. This history will show you the older versions of your notebook and how they have changed.

# ## <font color='lightblue'>Important limitations</font>
# 
# We are running this notebook on the cloud using colaboratory which has some advantages (i.e., quick setup, access to some neat hardware) and some disadvantages. The main disadvantage for us is that if we leave the computer idle for more than 30min it will reset. The code we write will be saved, but we might have to rerun the code.
