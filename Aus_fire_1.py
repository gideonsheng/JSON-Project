import matplotlib.pyplot as plt
import csv
from datetime import datetime
import json


open_file = open("MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2019331.txt", "r")

csv_file = csv.reader (open_file, delimiter = ",")

header_row = next(csv_file)

brightness,lons,lats,hover_texts = [],[],[],[]