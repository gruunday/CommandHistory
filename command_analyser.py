import random
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as op
import configparser as conf
import config

def main():
    
    # Going through logs and collecting data
    dic = get_data()
    # Taking labels out of dictionary and returning in a list
    labels = make_label(dic)
    # Taking values out of dictionary and returning in a list
    values = insert_values(dic)
    # Gets random colors every time
    colors = []
    for i in range(len(dic)):
        colors.append(get_color())
    
    # Settig up data for graph
    trace=go.Pie(labels=labels,values=values,marker={'colors': colors})
    # Plotting the graph
    url_2 = op.plot([trace], filename=config.name_file, auto_open=config.auto_open)
    op.plot([trace], filename=config.name_file)

def get_color():
    color = ''
    for n in range(6):
        color += random.choice('0123456789abcdef')
    return color
    
def insert_values(d):
    print('Working on Values')
    values = []
    for item in (d):
        if d[item] > config.min_use:
            values.append(d[item])
    return values

def make_label(d):
    print('Getting Some Labels')
    label = []
    for item in d:
        if d[item] > config.min_use:
            label.append(item)
    return label

def get_data():
    print('Retriving your data')
    # Make dictionary to return
    d = {}

    # Open the file to read
    f = open(config.file_location, 'r')

    # Vist every line count time command occurs
    for line in f:
        line = line.split()
        if line == []:
            continue
        if line[0] not in d:
            d[line[0]] = 1
        else:
            d[line[0]] += 1
    
    return d

if __name__ == '__main__':
    main()
