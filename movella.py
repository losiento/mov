import csv
from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Goalies.csv')

display(df)
print(list(df))
