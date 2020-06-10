

# %% [markdown]
Load Necessary Libraries

#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %% [markdown]
Basic Graph

#%%
x = [1,2,3]
y=[4,5,6]
plt.plot(x,y)

plt.title('Our First Graph', fontdict ={'fontname': 'Comics Sans MS', 'fontsize': 20})
plt.xlabel('X Axis', fontdict = {'fontname': 'Comics Sans MS'})
plt.ylabel('Y Axis')

plt.show() 


#%%
#check documentation for more details and more features
x = [0,1,2,3,4]
y = [0,2,4,6,8]

#Resize your graph (dpi specifies pizels per inch. When saving probably should use 300)
plt.figure(figsize = (5,3), dpi = 100) #ratio of x to y is by figsize. and specify pixels with dpi. Recommended around 300. 
#change the size and dpi according to your requirement

#Line 1

#Keyword Argument Notation
#plt.plot(x,y, label = '2x', color = 'red', linewidth = 2, marker='.', linestyle = '--', markersize = 10 , markeredgecolor = 'blue' ) #label and coloefor the line with x and y values

#Use Shorthand Notation
#fmt = '[color][marker][line]
plt.plot(x,y, 'r.--', label = '2x')

##Line 2

#select interval we want to plot points at
x2 = np.arange(0,4.5,0.5)

#plot part of the graph as line
plt.plot(x2[:6], x2[:6]**2,'r', label = 'X^2')

#plot remainder of graph as a dot
plt.plot(x2[5:],x2[5:]**2, 'r--')

#Add a title (specify font parameters with fontdict)
plt.title('Our First Graph', fontdict ={'fontname': 'Comics Sans MS', 'fontsize': 20})

#X and Y labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

#X , Y axis TIckmarks (scale of your graph)
plt.xticks([0,1,2,3,4]) #Value labels on axis
#plt.yticks([0,2,4,6,8,10])   #by default it has its own labels

#Add a legend
plt.legend()

#Save figure (dpi 300 is good when saving as grpah has high resolution)
plt.savefig('mygraph.png', dpi = 300) #can pass another dpi parameter to save in 

#Show plot
plt.show() 


# %% [markdown]
Bar Chart

#%%
labels = ['A', 'B', 'C']
values = [1,4,2]

bars = plt.bar(labels, values)
patterns = ['/','o','*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

#bars[0].set_hatch('/')
#bars[1].set_hatch('o')
#bars[2].set_hatch('*')

plt.figure(figsize = (6,4))


plt.figure(figsize = (6,4))

plt.show()

#%% [markdown] 
Line Graph

#%%
gas  = pd.read_csv('gas_prices.csv')  #saved to same folder as the python file 
#if not saved to same folder have to specify. E.g. './data/gas_prices.csv'

plt.figure(figsize = (8,5))

plt.plot(gas.Year, gas.USA, 'b.-') # x, y
plt.plot(gas.Year, gas.Canada, 'r.-')
plt.plot(gas.Year, gas['South Korea'], 'g.-') #due to presence of Space within name

plt.title('USA vs Canada Gas Prices', fontdict ={'fontweight': 'bold', 'fontsize': 22}) 

"""
#Another way to plot many values
countries_to_look_at = ['Australia', 'USA', 'Canada', 'South Korea']

for country in gas:
    #if country != 'Year': #because it is considering year also in the loop
     #   plt.plot(gas.Year, gas[country], marker = '.')
    if country in countries_to_look_at:
        plt.plot(gas.Year, has[country], marker = '.')
"""


plt.xlabel('Year')
plt.ylabel('Dollars/Gallon')

plt.legend()

plt.xticks(gas.Year[::3].tolist()*[2011]) #every 3 years 

plt.savefig('Gas_price_figure.png', dpi = 300)

plt.show()

# %% 
Histogram

#%%
fifa = pd.read_csv('fifa_data.csv')

#fifa.head(5) #to show first 5 rows

#Resize your Graph
plt.figure(figsize = (8,5), dpi = 100)

bins = [40,50,60,70,80,90,100]
plt.hist(fifa.Overall, bin = bins, color = '#abcdef') #google color picker for choosing color 
#and it's hexadecimal value

plt.xticks(bins)

#a = plt.hist(fifa.Overall, bin=5, color='blue')

plt.title('Distrubution of Player Skills in FIFA')
plt.ylabel('Number of Players')
plt.xlabel('FIFA Skill Level (Overall)')


#plt.axis.XAxis(0,1000)

plt.show()

#%% [markdown]
Pie Chart

#%%
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0] #.loc look up specific condition. Just count() alone gives array therefore add [0]
right = fifa.loc[fifa['Preferred Foot']== 'Right'].count()[0]

labels = ['Left Foot', 'Right Foot']
colors = ['#aabbcc'. '#adadad']

plt.title('Professional Soccer Preferred Foot')

plt.pie([left,right], labels=leabels, colors=colors, autopct= '%.2f %%')

plt.show()

#%%
plt.figure(figsize=(8,5), dpi = 100)

plt.style.use('ggplot')

fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]
light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
medium = fifa[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa[fifa.Weight >= 175 & (fifa.Weight < 200)].count()[0]
heavy = fifa[(fifa.Weight >= 200)].count()[0]

weights = [light, light_medium, medium, medium_heavy, heavy]
label = ['under 125', '125-150', '150-175', '175-200', 'over 200']
explode = (.4,.1,0,0,.4) #0 means don't explode, .1 explode a little bit, and .. follows the weights list. 

plt.title('Weight of Professional Soccer Players (lbs)')

plt.pie(weights, labels=label, explode= explode, pctdistance = 0.8, autopct = '%.2f %%') #percentage distance, and autpercentage is for percentage label 
#explode split the chart apart without it touching

plt.show()

# plt.legend()


# %% [markdown] 
Box and Whiskers Chart

#%%

plt.figure(figsize = (5,8), dpi = 100)

plt.style.use('default')

barcelona = fifa.loc[fifa.Club == "FC Barcelona"]['Overall'] #filter out all the players under the club Barcelona
madrid = fifa.loc[fifa.Club == "Real Madrid"]['Overall']
revs = fifa.loc[fifa.Club == "New England Revloution"]['Overall']

#bp = plt.boxplot([barcelona, madrid, revs], labels=['a','b','b'], boxprops = dict(facecolor = 'red'))
bp = plt.boxplot([barcelona, madrid, revs], labels = ['Fc Barcelona', 'Real Madrid', 'NE Revloution'], patch_artist = True, medianprops = {'linewidth':2})

plt.title('Professional Soccer Team Comparison')
plt.ylabel('FIFA Overall Rating')

for box in bp['boxes']:
    # change outline color
    box.set(color = '#4286f4', linewidth = 2)
    #change fill color
    box.set(facecolor = '#e0e0e0')
    #change hatch
    #box.set(hatch = '/')
    #chnage median line

plt.show()