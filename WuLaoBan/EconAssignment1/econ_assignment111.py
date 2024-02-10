#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:25:00 2024

@author: wubaobao
"""
import pandas as pd
import numpy as np

# df = pd.read_csv('Macintosh HD:/Users/Wubaobao/Downloads/ECON6600_youth_unemployment_self_employment_COVID.csv')
df = pd.read_csv('ECON6600_youth_unemployment_self_employment_COVID.csv')

# print(df.shape)


df_young_workers = df[(df['AGE_12'] == '15 to 19 years') & (df['SEX'] == 'Male')]
df = df_young_workers

# concatenate year and month
df_young_workers['YearMonth'] = df_young_workers['SURVYEAR'].astype(str) +'_' + df['SURVMNTH']
df_young_workers

# drop month, year, city columns 
df_young_workers.drop('SURVYEAR', axis=1, inplace=True)
df_young_workers.drop('SURVMNTH', axis=1, inplace=True)
df_young_workers.drop('CMA', axis=1, inplace=True)

df = df_young_workers

# Covenrsion for the category variables.
# Find columns with string (object) data type
string_columns = df.select_dtypes(include=['object'])
# Use get_dummies to one-hot encode all string columns
df = pd.get_dummies(df, columns=string_columns.columns)
df.columns = df.columns.str.replace(' ', '_')
# covnert the bool values to numeric values
df = df * 1
df.columns.tolist()

df_no_emp = df.drop('unemp', axis=1).drop('selfemp', axis=1)
df_selfemp = df.drop('unemp', axis=1)
df_unemp = df.drop('selfemp', axis=1)

df_columns = ''
for i in range(len(df_no_emp.columns)):
    df_columns += str(df_no_emp.columns[i]) + ' + '

df_columns = df_columns.strip()
ols_parameter = 'unemp ~ ' + df_columns
ols_parameter = ols_parameter[:-2]

print(ols_parameter)
# here is the ols_parameter output:
'unemp ~ AFTER + PROV_Alberta + PROV_British_Columbia + PROV_Manitoba + PROV_New_Brunswick + PROV_Newfoundland_and_Labrador + PROV_Nova_Scotia + PROV_Ontario + PROV_Prince_Edward_Island + PROV_Quebec + PROV_Saskatchewan + YearMonth_2019_April + YearMonth_2019_February + YearMonth_2019_July + YearMonth_2019_June + YearMonth_2019_March + YearMonth_2019_May + YearMonth_2020_April + YearMonth_2020_February + YearMonth_2020_July + YearMonth_2020_June + YearMonth_2020_March + YearMonth_2020_May'

# # run ols model
# results = ols(ols_parameter, data=df_unemp).fit()
# print(results.summary())
