# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here

#Check variables which has categorical value
categorical_var=bank_data.select_dtypes(include = 'object')
print("Categorical Variable: ",categorical_var.columns)

#Check variables which has numeric value
numeric_var=bank_data.select_dtypes(include = 'number')
print("Numeric Variable: ",numeric_var.columns)

#Drop  column Loan_ID
banks=bank_data.drop('Loan_ID',axis=1)

#Check Null values and filling it with mode value of respective column
print('Null Values : ')
print(banks.isnull().sum())

bank_mode=banks.mode()
for i in banks.columns:
    banks[i]=banks[i].fillna(value=bank_mode[i].iloc[0])
print('Checking if all the missing values are filled : ',banks.isnull().sum().values.sum())

#check the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print("Average loan amount based on Gender,Married,Self Employed")
print(avg_loan_amount.head(5))

#check the percentage of loan approved based on a person's employment type
loan_approved_se=len(banks[banks['Self_Employed']=='Yes'][banks['Loan_Status']=='Y'])

loan_approved_nse=len(banks[banks['Self_Employed']=='No'][banks['Loan_Status']=='Y'])

percentage_se=round(loan_approved_se/banks['Loan_Status'].count()*100,2)
print("Percentage of Loan Approved in case of self employed: ",percentage_se)

percentage_nse=round(loan_approved_nse/banks['Loan_Status'].count()*100,2)
print("Percentage of Loan Approved in case of Non self employed: ",percentage_nse)

#Find Company with long loan amount term
loan_term=pd.DataFrame(banks['Loan_Amount_Term'].apply(lambda x: x//12))

big_loan_term=loan_term[:][loan_term['Loan_Amount_Term']>=25]

print('Number of applicants having long amount term grater than or equal to 25: ',len(big_loan_term))

#check the average income of an applicant and the average loan given to a person based on their income
loan_groupby=banks.groupby(['Loan_Status'])
loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
mean_values=loan_groupby.mean()
print("Loan status based on Average income and credit history: ")
print(mean_values)







