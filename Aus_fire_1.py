import matplotlib.pyplot as plt
import csv
from datetime import datetime
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


def main():
        
    filenames=["MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2019331.csv","MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2020026.csv"]          
    map_title =['Australian Fires-November 2019','Australian Fires-January 2020']
    i=0
    for file in filenames:
        longitude, latitude, brightness = fileplot(file)
        title = map_title[i]
        tee(longitude, latitude, brightness,title)   
        i+=1
  
def fileplot(N):                                            
    import csv
    from datetime import datetime
    open_file = open(N, "r")
    csv_file = csv.reader(open_file, delimiter=",")
    header_row =next(csv_file)
    
    longs =[]
    lats =[]
    bright=[]
    
    
    for row in csv_file:
        try:
            lng = (row[header_row.index('longitude')])
            lat =(row[header_row.index('latitude')])
            brit= int(float((row[header_row.index('brightness')])))
        except ValueError:
            print(f"missing data for v")
        else:
            longs.append(lng) 
            lats.append(lat)
            bright.append(brit)
    open_file.close() 
    return longs,lats,brits


def tee (a,b,c,CC):                             
    
    from plotly.graph_objs import Scattergeo, Layout
    from plotly import offline
    data =[dict(type='scattergeo',lon=a,lat=b, mode = 'markers', marker = dict(size = 30,colorscale= 'reds', 
    color = c, colorbar = dict(title = 'Brightness',titleside = 'top',tickmode = 'array',)))]

    layout = dict(title = CC,geo = dict(showland = True, lataxis = dict(range=[-38.798,-10.154]),
    lonaxis = dict(range=[112.804,155.329]),landcolor = "rgb(250, 250, 250)",subunitcolor = "rgb(217, 217, 217)",
    countrycolor = "rgb(217, 217, 217)",countrywidth = 0.5,subunitwidth = 0.5),)

    fig = dict(data=data, layout=layout)
    offline.plot(fig, filename='Australian_Fires.html')


main()