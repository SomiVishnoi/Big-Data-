
# coding: utf-8

# In[2]:


from sklearn.linear_model import LinearRegression


# In[3]:


linreg=LinearRegression()


# In[4]:


import pandas as pd


# In[5]:


data=pd.read_csv('C:\\Users\\vishn_000\\Desktop\\testings.csv')


# In[6]:


print(data)


# In[7]:


#from sklearn import preprocessing
#from sklearn import utils
#lab_enc = preprocessing.LabelEncoder()
#data=data.apply(lab_enc.fit_transform) 
#print (data)


# In[8]:


feature_cols=['p_rainfall','p_cloud cover','p_evapotranspiration','p_min_temp','p_vapour_pressure','p_max_temp','p_wdf','cloud cover','evapotranspiration','min_temp','vapour_pressure','max_temp','wdf','rainfall','p_pond']


# In[9]:


x=data[feature_cols]


# In[10]:


y=data['pond']
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,random_state=1)


# In[11]:


linreg.fit(x_train,y_train)


# In[12]:


print (linreg.intercept_)


# In[13]:


print (linreg.coef_)


# In[14]:


print (type(linreg.coef_))
zip(feature_cols,linreg.coef_)


# In[16]:


np.savetxt('C:\\Users\\vishn_000\\Desktop\\data_lin.txt','a',fmt='%d')


# In[19]:


for a,b in zip(feature_cols,linreg.coef_):
    print (a,b)


# In[20]:


from sklearn.cross_validation import KFold


# In[21]:


kf=KFold(25,n_folds=6,shuffle=False)


# In[22]:


print('{} {:^61} {}'.format('Iteration','Training set observations','Testing set observations'))
for iteration,data in enumerate(kf,start=1):
    print ('{:^9} {} {!s:^25}'.format(iteration,data[0],data[1]))


# In[23]:


from sklearn.cross_validation import cross_val_score


# In[24]:


from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)


# In[25]:


#lab_enc = preprocessing.LabelEncoder()
#encoded = lab_enc.fit_transform(x_train)
scores=cross_val_score(knn,x,y,cv=6,scoring='accuracy')



# In[29]:


print (scores)


# In[30]:


import matplotlib.pyplot as plt
t=[1,2,3,4,5,6]
fig = plt.figure()
plt.xlabel('Cross folds')
plt.ylabel('Accuracy')
plt.title('Scores of training data')
plt.plot(t,scores)
#plt.plot(t,pred_arr)

fig.savefig('C:\\Users\\vishn_000\\Desktop\\accuracy.png')
plt.show()


# In[31]:


#import matplotlib
i#mport matplotlib.pyplot as plt


#month
#lt.plot(week,z)
#fig = plt.figure()
#ax = plt.subplot(111)
#ax.plot(month,y)
#ax.legend()
#fig.savefig('C:\\Users\\vishn_000\\Desktop\\plot.png')


# In[32]:


#sample of api integration for forest cover
#data2=pd.read_csv('https://api.data.gov.in//resource//e4988775-13f1-441e-bcb9-98466a43a949?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=csv&offset=0&limit=10')


# In[33]:


#print (data2)


# In[34]:



B=arr[1].split(",")
for k in range(len(B)):
    B[k]=int(B[k])

#testing on unseen data
Z=0
for i in range(0,15):
 Z=Z+linreg.coef_[i]*B[i]  
Z=Z+linreg.intercept_



# In[35]:


print (Z)


# In[36]:


#=pd.read_csv('C:\\Users\\vishn_000\\Desktop\\round2tst.csv')


# In[37]:


#print (d)


# In[38]:



f=open('C:\\Users\\vishn_000\\Desktop\\round2tst.csv','r')
j=0
arr=[]
for i in f:
    if j==0:
         j=j+1
    else:
        arr.append(i.strip('\n'))
        j=j+1
f.close()
actual=[76,83,90,92,96,90]
i=0
pred_arr=[]
while i<(j-1):
     B=arr[i].split(",")
     for k in range(len(B)):
        B[k]=int(B[k])

      #testing on unseen data
     Z=0
     for g in range(0,15):
      Z=Z+linreg.coef_[g]*B[g]  
     Z=Z+linreg.intercept_
     pred_arr.append(Z)
     i=i+1
#print (pred_arr)
for k in range(len(pred_arr)):
      pred_arr[k]=int(pred_arr[k])


# In[28]:


f=open('C:\\Users\\vishn_000\\Desktop\\round2tst.csv','r')
j=0
arr=[]
for i in f:
    if j==0:
        j=j+1
    else:
        arr.append(i.strip('\n'))
        j=j+1
f.close()


# In[39]:


actual=[76,83,90,92,96,90]


# In[40]:


i=0
pred_arr=[]
while i<(j-1):
    B=arr[i].split(",")
    for k in range(len(B)):
        B[k]=int(B[k])

    #testing on unseen data
    Z=0
    for g in range(0,15):
     Z=Z+linreg.coef_[g]*B[g]  
    Z=Z+linreg.intercept_
    pred_arr.append(Z)
    i=i+1
global val 
val=pred_arr[1]
 
#print (pred_arr)


# In[41]:


for k in range(len(pred_arr)):
       pred_arr[k]=int(pred_arr[k])


# In[42]:


import matplotlib.pyplot as plt


# In[48]:


"""
plt.plot(actual,pred_arr)
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(pred_arr,actual)
ax.legend()
fig.savefig('C:\\Users\\vishn_000\\Desktop\\plot.png')"""
t=[1,2,3,4,5,6]
fig = plt.figure()
plt.xlabel('Time')
plt.ylabel('Pond Area')
plt.title('Predicted vs actual area of pond')
plt.plot(t,actual,'-b',label="Actual pond area")

plt.plot(t,pred_arr,'-r',label="Predicted pond area")
plt.legend(loc='upper left')
fig.savefig('C:\\Users\\vishn_000\\Desktop\\plqt.png')
plt.show()

