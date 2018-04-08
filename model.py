# data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd
import os

# visualization
import seaborn as sns
import matplotlib.pyplot as plt


# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

renames = {
  'Committed to heart health through the Million Hearts® initiative.': 'Million Hearts',
}

def main():
	path = "./data/"
	dataFileNames = os.listdir(path)
	dataFileNames = [path + s for s in dataFileNames]
	dataFileNames.sort()
	#print(dataFileNames)
	df_grpExp = pd.read_csv(dataFileNames[0])
	df_grpPerform = pd.read_csv(dataFileNames[1])
	df_physPerform = pd.read_csv(dataFileNames[2])
	df_physComp = pd.read_csv(dataFileNames[3])
	
	num = df_physComp.count()
	print("Number of (raw) data points for each column: ", num)
	numNull = df_physComp.isnull().sum(axis=0)
	print("Number of null/emply data entries for each column: ",numNull)

	#Solutions on github for Data Incubator Challenge 2:
		#https://github.com/MehtaShruti/The-Data-Incubator-Physicians-Compare-and-NYC-Parking-Ticket/blob/master/ChallengeQuestion_2.ipynb
		#https://github.com/rrpastro/data_incubator/blob/4b0ef3e6207cf41d5a04bbb113d71c157b713090/challenge2_final.ipynb
		#https://github.com/nocibambi/ds-practice/blob/bb36a486a4fbc53ae032652dc21bbf2681fc13e2/DI%20Practice/physicians.py
	#More codes (search results):
		#https://github.com/search?q=data+incubator+Physician+Compare&type=Code

	#How many clinicians are in the dataset, ...
		#...using both PAC ID and NPI together (for individuals)?
		#Solution: 1070399

	#What is the ratio of male to female clinicians?
		#Solution: 1.1742534115

	#What is the highest ratio of female clinicians to ...
		#...male clinicians with a given type of credential?
		#Solution: ?

	#How many states have fewer than 10 healthcare facilities in this dataset? 
		#Including Washington D.C. and U.S.territories in this calculation.
		#Solution: ?

	#All measure performance rates are on a 0 to 100 scale. ...
		#...Compute the average measure performance rate for each clinician ...
		#...(across all measures). Consider the distribution of these ...
		#...average rates for individuals who have at least 10. What is the ...
		#...standard deviation of that distribution?

	#What is the p-value of the linear regression of performance rates vs. ...
		#...graduation year? Consider the average performance rates ...
		#...(across all measures) of every doctor (MD) who graduated between ...
		#...1973 and 2003 (inclusive). Only consider doctors who have at least ...
		#...10 rates. For each graduation year, compute the mean of these rates. ...
		#...Assuming the relationship between graduation year and performance rates ...
		#...is linear, find the slope and determine if the relationship is significant. ...
		#...Return the p-value of the linear regression.

	#What is the absolute difference in the average performance rates between ...
		#...doctors (MD) and nurse practitioners (NP)? For each clinician, ...
		#...use his or her average performance rates across all measures. ...
		#...Furthermore, only consider individuals who have at least 10 rates.

	#What is the p-value of the difference in MD and NP performance rates ...
		#from the previous question? Perform a two-sample t-test and compute ...
		#the two-tailed p-value. Assume that the distributions are normal and ...
		#have equal variance.

if __name__=='__main__':
	main()