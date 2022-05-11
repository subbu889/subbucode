#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:


x= np.array([0, 6])
y= np.array([0, 250])


# In[3]:


plt.plot(x,y)


# ploting without a line , mention the type ex "0"

# In[4]:


plt.plot(x,y,'o')
plt.show()


# In[5]:


x1=[1, 2, 6, 8]
y1=[3, 8, 1, 10]


# In[6]:


plt.plot(x1,y1)
plt.show()


# In[7]:


plt.plot(x1)
plt.show()


# In[8]:


plt.plot(y1)


# In[9]:


plt.plot(x,y,"*")
plt.show()


# Marking each point

# In[10]:


plt.plot(x1,y1,marker="o")


# In[11]:


plt.plot(y, marker = 'X')


# These are the various marker types which we can try to develop 
# 
# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline	

# In[ ]:





# In[ ]:





# 

# In[12]:


plt.plot(y, 'o:r')
plt.show()


# In[13]:


plt.plot(y, 'o:g')
plt.show()


# Marker Size
# z=[3,10,51,20,30]
# plt.plot(ypoints, marker = 'o', ms = 20)
# plt.show()

# In[14]:


z=[3,10,51,20,30]
plt.plot(z,marker='o',ms = 20)
plt.show()


# In[15]:


plt.plot(y,'o:r',ms=25)


# In[16]:


z2=[3,8,1,10,25,30,5]
z3=[10,15,20,5,15,20,15]
plt.plot(z2,marker='X',ms=20,mfc='r')
plt.plot(z3,marker='o',ms=20,mfc='g')

plt.show()


# In[17]:


#Linestyle
plt.plot(z3,linestyle = 'dotted')
plt.show()


# In[18]:


#Use a dashed line:
plt.plot(z2, linestyle = 'dashed')
plt.show()


# In[19]:


plt.plot(z3,ls=':')
plt.show()


# In[20]:


a1 = np.array([0, 1, 2, 3])
a2 = np.array([3, 8, 1, 10])
a3 = np.array([1, 3, 2, 3])
a4 = np.array([6, 2, 7, 11])
plt.plot(a1)
plt.plot(a2)
plt.plot(a3)
plt.plot(a4)
plt.show()


# labeling 
# x axis 
# y axis

# In[21]:


aa = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
bb = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(aa,bb)

plt.xlabel("speed")
plt.ylabel("kms")
plt.title("travel time")
plt.grid()
plt.show()


# In[22]:


aa = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
bb = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(aa,bb)

plt.xlabel("speed")
plt.ylabel("kms")
plt.title("travel time")
plt.grid(axis="x")
# grid can be given a condition x axis and y axis
plt.show()


# Display Multiple Plots  they are also called as subplots

# In[23]:


xx=np.array([0, 1, 2, 3])
yy=np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(xx,yy)

#plot 2:
xa = np.array([0, 1, 2, 3])
yb = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(xa,yb)

plt.show()


# In[24]:


#plot 2:
xa = np.array([0, 1, 2, 3])
yb = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(xa,yb)
plt.show()


# Creating Scatter Plots

# In[25]:


sp1= np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
sp2= np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(sp1,sp2)
plt.show()


# In[26]:


#day one, the age and speed of 13 cars:
sx = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
sy= np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(sx,sy)

#day two, the age and speed of 15 cars:
sx1 = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
sy1 = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(sx1,sy1)

plt.show()


# Creating Bars

# In[27]:


bx = np.array(["A", "B", "C", "D","e"])
by = np.array([3, 8, 1, 10,5])

plt.bar(bx,by)
plt.show()


# In[28]:


bxx = ["APPLES", "BANANAS"]
byy = [400, 350]
plt.bar(bxx,byy)


# In[29]:


bhx = np.array(["A", "B", "C", "D"])
bhy = np.array([3, 8, 1, 10])


plt.barh(bhx,bhy,color = "red")

plt.show()

#barh represents the data in vertical


# Histogram

# In[30]:


y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()


# # Individual Plotings

# In[31]:


plt.plot([1,2,3],[4,5,1])
plt.show()


# In[32]:


cx = [5,2,7,10,5,20]
cy = [2,16,4,10,16,20]
plt.plot(cx,cy)
plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()


# Importing inbuilt themes of Matlplot lib

# In[33]:


from matplotlib import style


# In[36]:


style.use('ggplot')
cx1 = [5,8,10]
cy1= [12,16,6]
cx2 = [6,9,11]
cy2 = [6,15,7]
plt.plot(cx1,cy1,'g',label='line one', linewidth=5)
plt.plot(cx2,cy2,'c',label='line two',linewidth=5)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.grid(True,color='k')
plt.show()


# In[38]:


plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
label="BMW",width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label="Audi", color='g',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()
# here this particular graph has width as new parameter


# In[41]:


population_age = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_age,bins,histtype='bar',rwidth=0.8)
plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.title('Histogram')
plt.show()
# In Histogram one has to create Bin , these are seperating symbols and values


# In[42]:


cx2 = [1,1.5,2,2.5,3,3.5,3.6]
cy2 = [7.5,8,8.5,9,9.5,10,10.5]
 
cx3=[8,8.5,9,9.5,10,10.5,11]
cy3=[3,3.5,3.7,4,4.5,5,5.2]
 
plt.scatter(cx2,cy2,label='high income low saving',color='r')

plt.scatter(cx3,cy3,label='low income high savings',color='b')

plt.xlabel('saving*100')

plt.ylabel('income*1000')

plt.title('Scatter Plot')

plt.legend()

plt.show()


# In[ ]:




