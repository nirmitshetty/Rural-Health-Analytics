'''
HDI(human developmental index) for a country
is a measure of the overall well being of a citizen in the country.
p
It mainly takes three parameters, life expectancy at birth, educational developmental index(edi), and Net income of the country.

The given project, by evaluating the three parameters,finds out the coefficient of contribution of each parameter to the overall hdi





'''






import numpy as np
import xlrd
import xlwt
import matplotlib.pyplot as plt
file_location = "parameters for finding out hdi actual.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
life_expectancy=[]
edi=[]
gross_income=[]
hdi=[]
empty=[]
for i in range(1,16):
	life_expectancy.append(float(sheet.cell_value(i,1)))
	edi.append(float(sheet.cell_value(i,2)))
	gross_income.append(float(sheet.cell_value(i,3)))
	hdi.append(float(sheet.cell_value(i,4)))
	
a=np.matrix([life_expectancy,edi,gross_income]) #Ax=b here a of our python code is analogues to A.(A=a)
hdi_matrix=np.matrix([hdi]) #hdi_matrix is analogues to b (b=hdi_matrix)
#Ax=b,then x=(A.transpose().A).inverse().(a.transpose()).b
b=a*(a.getT())

c=b.getI()
d=c*a
hdi_matrix_2=hdi_matrix.getT()
e=d*hdi_matrix_2
print(e)



sum=e[0]+e[1]+e[2]
x0=(e[0]*100)/(sum)
x1=(e[1]*100)/(sum)
x2=(e[2]*100)/(sum)
# you can find that coefficient of life_expectancy is negative,implying the fact that the increase in income is less rigorous,as compared to the required 
#increase in life_expectancy,hence to nullify the effect,life expectancy,should increase at a slower rate and gross income must increase at a higher rate,.
print(str(x0[0][0])+"is the percentage contribution of life_expectancy to national hdi")
print(str(x1)+"is the percentage contribution of educational development index to national hdi")
print(str(x2)+"is the percentage contribution of gross income to national hdi")