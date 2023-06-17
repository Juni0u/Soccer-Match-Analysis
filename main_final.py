# Import necessary libraries

import pandas as pd
from Experiment import Experiment

# %% Data Processing 
print('====================DATA PROCESSING====================')
#Read dataframe
bra = pd.read_csv('BRA.csv')

#Determine columns of interest and put them in another dataframe
cols = ['Home','Away','HG','AG','Res']
df = bra[cols]

#Check integrity of the relevant data
values_null = pd.isnull(df).sum()
print('Quantity of null values of each column:\n',values_null)

#Erase null data
df = df.dropna()
values_null = pd.isnull(df).sum()
print('\nQuantity of null values of each column:\n',values_null)
print('============================================================')

#%% Common parameter to all experiments
data = df['Res'].value_counts()

#%% Experiment 1
print('\n\n====================EXPERIMENT 1====================')
print("Successes (Positive Result) = Home Team win \nFailures (Negative Result) = Away Team Win + Draw")
exp1 = Experiment(data['H'],(data['D'] + data['A']),1)
exp1_mean = [exp1.mean(),exp1.mean(m='True')]
exp1_var = [exp1.variance(),exp1.variance(m='True')]
[xtremes1, inter1] = exp1.conf_int(0.95)
inter1_m = exp1.conf_int(0.95,m=[True,1.96])

print('\np (proportion of sucesses) = {}'.format(exp1.p))
print('q (proportion of failures) = {}'.format(exp1.q))
print('n (sample size) = {}'.format(exp1.n))
print('Mean = {}'.format(exp1_mean[0]))
print('Variance = {}'.format(exp1_var[0]))

exp1.plot_mass_function()
exp1.plot_mass_function(zoomed=[True,xtremes1])

# Confidence Interval
print('\n\n\n---------------CONFIDENCE INTERVAL---------------')
print('\n---------------BINOM LIBRARY---------------')
print('The confidence interval using BINOM LIBRARY is:')
print(inter1[0],'< p <',inter1[1])
print('\n So, it is possible to conclude with 95% of confidence that between',inter1[0]*100,'% and',inter1[1]*100,'% of games have a positive result to the home team.')

print('\n---------------MANUALLY---------------')
print('The confidence interval according to the Walt Method (manually) is:')
print(inter1_m[0],'< p <',inter1_m[1])
print('\n So, it is possible to conclude with 95% of confidence that between',inter1_m[0]*100,'% and',inter1_m[1]*100,'% games have a positive result to the home team.')

#%% Experiment 2
print('\n\n====================EXPERIMENT 2====================')
print("Successes (Positive Result) = Home Team win + Draw \nFailures (Negative Result) = Away Team Win")
exp2 = Experiment((data['H'] + data['D']),(data['A']),2)
exp2_mean = [exp2.mean(),exp2.mean(m='True')]
exp2_var = [exp2.variance(),exp2.variance(m='True')]
[xtremes2, inter2] = exp2.conf_int(0.95)
inter2_m = exp2.conf_int(0.95,m=[True,1.96])

print('\np (proportion of sucesses) = {}'.format(exp2.p))
print('q (proportion of failures) = {}'.format(exp2.q))
print('n (sample size) = {}'.format(exp2.n))
print('Mean = {}'.format(exp2_mean[0]))
print('Variance = {}'.format(exp2_var[0]))

exp2.plot_mass_function()
exp2.plot_mass_function(zoomed=[True,xtremes2])

# Confidence Interval
print('\n\n\n---------------CONFIDENCE INTERVAL---------------')
print('\n---------------BINOM LIBRARY---------------')
print('The confidence interval using BINOM LIBRARY is:')
print(inter2[0],'< p <',inter2[1])
print('\n So, it is possible to conclude with 95% of confidence that between',inter2[0]*100,'% and',inter2[1]*100,'% of games have a positive result to the home team.')

print('\n---------------MANUALLY---------------')
print('The confidence interval according to the Walt Method (manually) is:')
print(inter2_m[0],'< p <',inter2_m[1])
print('\n So, it is possible to conclude with 95% of confidence that between',inter2_m[0]*100,'% and',inter2_m[1]*100,'% games have a positive result to the home team.')

#%% Experiment 3
print('\n\n====================EXPERIMENT 3====================')
print("Successes (Positive Result) = Home Team win \nFailures (Negative Result) = Away Team Win")
print("Draws were not considered. Sample size is lower in this case.")
exp3 = Experiment((data['H']),(data['A']),3)
exp3_mean = [exp3.mean(),exp3.mean(m='True')]
exp3_var = [exp3.variance(),exp3.variance(m='True')]
[xtremes3, inter3] = exp3.conf_int(0.95)
inter3_m = exp3.conf_int(0.95,m=[True,1.96])

print('\np (proportion of sucesses) = {}'.format(exp3.p))
print('q (proportion of failures) = {}'.format(exp3.q))
print('n (sample size) = {}'.format(exp3.n))
print('Mean = {}'.format(exp3_mean[0]))
print('Variance = {}'.format(exp3_var[0]))

exp3.plot_mass_function()
exp3.plot_mass_function(zoomed=[True,xtremes3])

# Confidence Interval
print('\n\n\n---------------CONFIDENCE INTERVAL---------------')
print('\n---------------BINOM LIBRARY---------------')
print('The confidence interval using BINOM LIBRARY is:')
print(inter3[0],'< p <',inter3[1])
print('\n So, it is possible to conclude with 95% of confidence that between',inter3[0]*100,'% and',inter3[1]*100,'% of games have a positive result to the home team.')

print('\n---------------MANUALLY---------------')
print('The confidence interval according to the Walt Method (manually) is:')
print(inter3_m[0],'< p <',inter3_m[1])
print('\n So, it is possible to conclude with 95% of confidence that between',inter3_m[0]*100,'% and',inter3_m[1]*100,'% games have a positive result to the home team.')

# %%