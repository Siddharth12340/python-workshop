#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot
#x axis values
roll_num = [1,2,3,4,5,6,7,8,9]
#y axis values
marks = [55,75,96,75,36,45,87,99,100]
pyplot.plot(roll_num,marks,'b')
pyplot.show()


# In[2]:


from matplotlib import pyplot
marks = [55,75,96,75,36,45,87,99,100]
pyplot.hist(marks,bins = 7)
pyplot.show()


# In[3]:


from matplotlib import pyplot
roll_num = [1,2,3,4,5,6,7,8,9]
marks = [55,75,96,75,36,45,87,99,100]
pyplot.scatter(roll_num,marks)
pyplot.show()


# In[4]:


import numpy as np
import matplotlib.pyplot
city = ('Pune','Satara','Mumbai','Kanpur','Bhopal','Assam')
y_val = np.arange(len(city))
rank = [4,7,1,3,2,5]
pyplot.bar(y_val, rank, align='center')
pyplot.xticks(y_val,city)
pyplot.ylabel('Rank')
pyplot.title('City')
pyplot.show()


# In[5]:


from matplotlib import pyplot
roll_num = [1,2,3,4,5,6,7,8,9]
marks = [55,75,96,75,36,45,87,99,100]
attendace = [25,75,86,74,85,25,35,63,29]
pyplot.plot(roll_num,marks,color = 'green', label = 'Marks')
pyplot.plot(roll_num,attendace,color = 'blue', label = 'Attendance')
pyplot.legend(loc='upper left',frameon=True)
pyplot.show()


# In[ ]:




