import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='blue')
    

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    res = linregress(x,y)
    x_new = list(range(1880,2051))
    y_new = [(res.intercept + res.slope*i) for i in x_new]
    plt.plot(x_new, y_new, 'r', label='fitted line')

    x_2 = df[df['Year']>1999]['Year']
    y_2 = df[df['Year']>1999]['CSIRO Adjusted Sea Level']
    res2 = linregress(x_2,y_2)
    
    x_3 = list(range(2000,2051))
    y_3 =  [(res2.intercept + res2.slope*i) for i in x_3]
    plt.plot(x_3,y_3, color='purple', label='Fitted From 2000-2050')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
        
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()