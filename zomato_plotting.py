#Import necessary Python libraries.
import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd 

# Create the data frame.
df=pd.read_csv('Zomato data .csv')

# Convert the data type of the “rate” column to float and remove the denominator.
def handledata(value):
      value=str(value).split('/')
      value=value[0]
      return float(value)
df['rate']=df['rate'].apply(handledata)
print(df.head())

#Explore the listed_in (type) column.
sns.countplot(x=df['listed_in(type)'],saturation=1)
plt.xlabel('Types of restaurant')
plt.show()

#Analyze votes by restaurant type
grouped_data=df.groupby('listed_in(type)')['votes'].sum()
result=pd.DataFrame(grouped_data)
plt.plot(result,c='green',marker='h')
plt.xlabel('Types of restaurant',c='red',size=20)
plt.ylabel('Votes',c='red',size=20)
plt.show()

#Determine the restaurant with maximum votes .
max_votes = df['votes'].max()
restaurant_with_max_votes = df.loc[df['votes'] == max_votes, 'name']
print("Restaurant(s) with the maximum votes:")
print(restaurant_with_max_votes)

#Explore the online_order distribution
sns.countplot(x=df['online_order'])
plt.show()

#Explore the rate column.
plt.hist(x=df['rate'],bins=5)
plt.title('Rating Distribution')
plt.show()

#Explore the approximate cost for two people column.
couple_data=df['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.show()

#Rating vs Online Order
plt.figure(figsize=(6,6))
plt.title('Ratings by Online Order Availability')
sns.boxplot(x=df['Online_order'],y=df['rate'])
plt.show()

#Create a heatmap of online order by restaurant type
pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()
