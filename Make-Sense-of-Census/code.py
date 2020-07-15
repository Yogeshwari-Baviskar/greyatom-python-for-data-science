# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
new_record=np.array(new_record)
census=np.concatenate((data,new_record),axis=0)

print("Shape Before Appending New Record: ",np.shape(data))
print("Shape After Appending New Record: ",np.shape(census))

#Checking Age Distribution
age=census[:,0]
max_age=np.max(age)
print("Max Age: ",max_age)
min_age=np.min(age)
print("Min Age: ",min_age)
age_mean=round(np.mean(age),2)
print("Mean Age: ",age_mean)
age_std=round(np.std(age),2)
print("Standard Deviation of Age: ",age_std)


#Checking Race Distribution,to find minority race
race=census[:,2]
race_0=np.array([i for i in race if i==0])
race_1=np.array([i for i in race if i==1])
race_2=np.array([i for i in race if i==2])
race_3=np.array([i for i in race if i==3])
race_4=np.array([i for i in race if i==4])

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

dic = {0: len_0, 1: len_1, 2: len_2, 3: len_3, 4: len_4}
minority_race=min(dic, key=dic.get)

print("Minority race: ",minority_race)

#finding Senior citizens and  find is new govt. policy is followed or not by finding average working hours
age=census[:,0]
senior_citizens=np.array([census[j,:] for i,j in zip(age,range(0,len(age))) if i>60])
working_hours_sum=sum(senior_citizens[:,6])
print("Working hour sum: ",working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=round(working_hours_sum/senior_citizens_len,2)
print("Average working hours: ",avg_working_hours)
if (avg_working_hours > 25):
    print("Govt. policy is followed...")
else:
    print("Govt. policy is not followed...")

#To Check whether the higher educated people have better pay in general
high=np.array([census[j,:] for i,j in zip(census[:,1],range(0,len(census[:,1]))) if i>10])
low=np.array([census[j,:] for i,j in zip(census[:,1],range(0,len(census[:,1]))) if i<=10])

avg_pay_high=round(np.mean(high[:,7]),2)
avg_pay_low=round(np.mean(low[:,7]),2)

print("Average Pay od Higher educated people: ",avg_pay_high)
print("Average Pay od lower educated people: ",avg_pay_low)

if(avg_pay_high>avg_pay_low):
    print('"Better education leads to Better pay" is truth')
else:
    print('"Better education leads to Better pay" is not truth')




