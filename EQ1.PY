import plotly
import json

in_file = open('eq_data_1_day_m1.json','r')
out_file = open ('readable_eq_data.json','w')

eq_data = json.load(in_file)

print(type(eq_data))

json.dump(eq_data, out_file,indent=4)