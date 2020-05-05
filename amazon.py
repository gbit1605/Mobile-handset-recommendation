# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 19:16:25 2020

@author: Gunveen Batra
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder 
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer 
import nltk
from textblob import TextBlob
import matplotlib.pyplot as plt
from math import sqrt

data=pd.read_csv('C:\\Gun\\Academics\\6th sem\\DMPA_Lab\\Lab_proj\\amazon_phone_dataset.csv')





#DATA PRE-PROCESSSING

data=data.dropna()
data=data.drop(['Product_url','Product_img','ans_ask'],axis=1)

#Removing all useless series of dots or special characters
data['cust_review'] = data['cust_review'].str.replace("[^a-zA-Z0-9***]", " ") 
#removing all short words having length <3
data['cust_review']=data['cust_review'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3])) 
#Seperating reviews in the dataset
data['cust_review']=data['cust_review'].apply(lambda x: x.split("***"))

data['Product_price']=data['Product_price'].str.replace("[^0-9#]", "") #removing any non-numeric characters
data['Product_price']=[i[:-2] for i in data['Product_price']]

data['total_review']=data['total_review'].str.replace("[^0-9#]", "") #Removing any non-numeric characters

data['rating']=data['rating'].str.replace("[^0-9.#]", "")
data['rating']=[i[:-1] for i in data['rating']]

#Removing all duplicate records
data.sort_values("Product_name", inplace = True) 
data.drop_duplicates(subset ="Product_name", keep = False, inplace = True) 

data['final_reviews']=data['cust_review']





#CLEANING AND ANALYSING REVIEWS FOR EACH PRODUCT

#Tokenization, Stemming   
stemmer = PorterStemmer()
lmtz=WordNetLemmatizer()

data['cust_review']=data['cust_review'].apply(lambda x: [nltk.word_tokenize(i) for i in x]) #tokenization

freq=[] #list of dictionaries, one dictionary for each review, containing frequency of each word in each review
    
for j in data['cust_review']: 
    f=[]
    for i in j:
        fr={}
        for word in i:
            #fr[word] = fr[word] + 1 if word in fr else 1
            if word in fr:
                fr[word]=fr[word]+1
            else:
                fr[word]=1
        f.append(fr)
    freq.append(f)
      

def get_review_sentiment(tweet):   #getting the review of each word 
    # create TextBlob object of passed review text 
    analysis = TextBlob(tweet) 
    # set sentiment 
    if analysis.sentiment.polarity > 0: 
        return 'positive'
    elif analysis.sentiment.polarity == 0: 
        return 'neutral'
    else: 
        return 'negative'
    
   
for datadict in freq:   #getting the sentiment of each word in the freq list
    for d in datadict:
        for key, value in d.items():
            d[key] = (value,get_review_sentiment(key))

  
final_reviews=[]   #analysing the overall reviews for each product
for i in freq:
    t=[]
    for j in i:
        x={}
        positive=0
        negative=0 
    
        for key, value in j.items():
            if value[1]=='positive':
                positive+=1
            elif value[1]=='negative':
                negative+=1
        x['positive']=positive
        x['negative']=negative
        t.append(x)
    final_reviews.append(t)
    

      
data['review']=final_reviews
data=data.drop(['cust_review'],axis=1) 

data['Product_price']=pd.to_numeric(data['Product_price'],errors='coerce') #converting the values in these columns to numeric values
data['rating']=pd.to_numeric(data['rating'],errors='coerce')

data=data.drop(['total_review','prod_des','feature'],axis=1) #dropping out the extra usless columns




'''

#SOME MORE PRE-PROCESSING       

corr_matrix_amazon = data.corr().abs()  #building the correlation matrix to drop unecessary columns

c=0
for index, row in corr_matrix_amazon.iterrows(): #checking if highly correlated attributes present
    for i in row:
        if(i>0.95):
            #print(i)
            c+=1
#since no values above 0.95 hence no columns dropped 

data=data.dropna()#dropping any Nan values that are remaining

'''


'''
#GRAPH PLOTTING

#Plotting price against ratings
ylabel = data["Product_price"]
xlabel = data["rating"]
plt.ylabel("Price")
plt.xlabel("Rating")
plt.scatter(xlabel, ylabel, alpha=0.1)
plt.show()
'''
#plotting price against average rating for each brand
brands=[]
brands=data['by_info']
brands=brands.unique()  
brands=list(brands)    
'''        
xlabel=brands
plt.xlabel("Brands")
ylabel=data.groupby('by_info')['rating'].mean()
plt.ylabel("Mean rating")
plt.scatter(xlabel, ylabel, alpha=0.1)
plt.show()

#plotting price vs number of positive and negative reviews

ylabel = data["Product_price"]
plt.ylabel("Price")

for i in final_reviews:
    for j in i:
        for key,value in j.items():
            if(key=='positive'):
                p+=1
            else:
                n+=1

'''




#KNN MODEL FOR RECOMMENDATION

def euclidean_dist(x1, x2):
    
    dist=0
    dist=((x1[0]-x2[0])**2)+((x1[1]-x2[1])**2)
    
    return sqrt(dist)


def get_neighbors(data_t, test_row, k, names):
    
    distances=[]
    i=0
    for train_row in data_t:
        dist=euclidean_dist(train_row, test_row)
        distances.append((names[i], train_row, dist))
        i+=1
        
    distances.sort(key=lambda tup:tup[2])
    
    neighbors=[]
    
    for i in range(k):
        neighbors.append((distances[i][0], distances[i][1], distances[i][2]))
    
    return neighbors

def send(handset):
    for i in data.iterrows():
        if handset==i[1]['Product_name']:
            price=i[1]['Product_price']
            rating=i[1]['rating']
            break
        
    inp=[rating,price]       
    data_train=[]
    names=[]
    #reviews=[]
    
    for row, j in data.iterrows():
        if j['Product_name']!=handset:
            s=[j['rating'], j['Product_price']]
            k=j['Product_name']
            #l=j['final_reviews']
            data_train.append(s)
            names.append(k)
            #reviews.append(l)
    
    c=get_neighbors(data_train, inp, 5, names)
    return c
d=send("4D MM03 Wireless Telephone (White)")
print(d)

'''
def input_func():
    
    price=float(input("Enter the desired price: "))
    rating=float(input("Enter the desired rating: "))
    recom=int(input("Enter the number of recommendations that you would like to receive: "))
    
    opt=input("Do you wish to view phones of a specific company? (y/n) ")
    if opt=='y':
        opt='Y'
        for i in brands:
            print(i,end='\t')
    elif opt=='n':
        opt='N'        
    else:
        print("Please enter a correct value")
        
    return [rating, price], opt, recom


def output_func(n):
    
    print("")
    print("RECOMMENDED GADGETS FOR YOU ARE: ")
    print("")
    for i in n:
        print(i[0])
        print("Price: ",i[1][1])
        print("Rating: ",i[1][0])
        print("Distance: ",i[2])
        print("Other reviews include: ")
        f=0
        for j in i[3]:
            f+=1
            print(f,"]",j)
            
        print("")

inp,option,r=input_func()

if option=='N':
    
    data_train=[]
    names=[]
    reviews=[]
    
    for row, i in data.iterrows():
        s=[i['rating'], i['Product_price']]
        k=i['Product_name']
        l=i['final_reviews']
        data_train.append(s)
        names.append(k)
        reviews.append(l)
    
    c=get_neighbors(data_train, inp, r, names, reviews)
    
    output_func(c)
    
'''                                        