import pandas as pd

##file = pd.read_csv('tips.csv')

##print(file)

html = pd.read_html('https://github.com/mwaskom/seaborn-data/blob/master/tips.csv')

print(html)
