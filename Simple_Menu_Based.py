import pandas as pd
import numpy as np
from sklearn import linear_model
from prettytable import PrettyTable
import matplotlib.pyplot as plt
x=PrettyTable()

class Node:

    def __init__(self,yr,sh,inc,pr):

        self.left = None
        self.right = None
        self.yr = yr
        self.sh = sh
        self.inc = inc
        self.pr = pr

    def insert(self,yr,sh,inc,pr):
        if self.yr:
            if yr < self.yr:
                if self.left is None:
                    self.left = Node(yr,sh,inc,pr)
                else:
                    self.left.insert(yr,sh,inc,pr)
            elif yr > self.yr:
                if self.right is None:
                    self.right = Node(yr,sh,inc,pr)
                else:
                    self.right.insert(yr,sh,inc,pr)
        else:
            self.yr = yr

    def search(self,key):
        x=PrettyTable()
        x.field_names = [data.columns[0], data.columns[1], data.columns[2], data.columns[3]]
        if key < self.yr:
            return self.left.search(key)
        elif key > self.yr:
            return self.right.search(key)
        else:
            x.add_row([ self.yr,self.sh,self.inc,self.pr])
        return x
        del(x)

# Print the tree
    def PrintTree(self):
        x.field_names = [data.columns[0], data.columns[1], data.columns[2], data.columns[3]]
        if self.left:
            self.left.PrintTree()
        x.add_row([ self.yr,self.sh,self.inc,self.pr]),
        if self.right:
            self.right.PrintTree()
        return x

data=pd.read_csv("Nvidia.csv")
i=0
n=len(data)
#print(n)
year=[]
income=[]
profit=[]
shares=[]

for i in range(0,n):
    year.append(float(data.iloc[i,0]))
    shares.append(float(data.iloc[i,1]))
    income.append(float(data.iloc[i,2]))
    profit.append(float(data.iloc[i,3]))

root=Node(year[0],shares[0],income[0],profit[0])
for i in range(0,n):
    root.insert(year[i],shares[i],income[i],profit[i])

X = data[['Year','Shares','Net Income']]
Y = data['Profit']
regr = linear_model.LinearRegression()
regr.fit(X, Y)

def showdata():
    print(root.PrintTree())

def searchdata():
    a=data.iloc[0,0]
    b=data.iloc[n-1,0]
    #print(root.search(2006))
    find_yr=float(input("Enter a year between {}-{}:".format(a,b)))
    print(root.search(find_yr))

def centraltendency():
    #Calculating Mean ,median and mode
    mean=np.mean(profit)
    median=np.median(profit)
    print("Mean:",mean)
    print("Median:",median)

def graph():
    plt.plot(data['Year'], data['Profit'], color='red')
    plt.plot(data['Year'], data['Shares'], color='green')
    plt.plot(data['Year'], data['Net Income'], color='blue')
    plt.title('Year Vs Profit,Income and Shares', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.grid(True)
    plt.legend()
    plt.show()

def correg():
    print('Intercept: \n', regr.intercept_)
    print('Coefficients: \n', regr.coef_)
    print("Pearson's Correlation Matrix:\n")
    print(data.corr(method='pearson'))

def prediction():
    New_year= float(input("Enter the year:"))
    New_share=float(input("Enter the share amount:"))
    New_income=float(input("Enter the income amount:"))
    print ('Profit amount: \n', regr.predict([[New_year ,New_share,New_income]]))


def menu():
    print("********************MAIN MENU***********************")
    print()

    choice = input("""
                      A: Show data
                      B: Graph
                      C: Central tendency values of profit
                      D: Search for a data
                      E: Correlation and regression
                      F: Prediction
                      Q: Quit

                      Please enter your choice: """)

    while True:
        if choice == "A" or choice =="a":
            showdata()
            menu()
        elif choice =="B" or choice=="b":
            graph()
            menu()
        elif choice =="C" or choice=="c":
            centraltendency()
            menu()
        elif choice =="D" or choice=="d":
            searchdata()
            menu()
        elif choice =="E" or choice=="e":
            correg()
            menu()
        elif choice =="F" or choice=="f":
            prediction()
            menu()
        elif choice=="Q" or choice=="q":
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Thank You!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            exit(1)
        else:
            print("You must only select either A,B,C,D,E,F or Q")
            print("Please try again")
            menu()

menu()
