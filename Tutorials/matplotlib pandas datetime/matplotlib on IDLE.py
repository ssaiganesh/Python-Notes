Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib
>>> import matplotlib.pyplot as plt
>>> plt.plot(x,y)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    plt.plot(x,y)
NameError: name 'x' is not defined
>>> x = [1,2,3,4]
>>> y = [1500,1200,1100,1800]
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000001A404860A00>]
>>> plt.show()
>>> legend = ["January", "February", "March", "April"]
>>> plt.xticks(x,legend)
([<matplotlib.axis.XTick object at 0x000001A4065B0250>, <matplotlib.axis.XTick object at 0x000001A4065B0220>, <matplotlib.axis.XTick object at 0x000001A4049F1430>, <matplotlib.axis.XTick object at 0x000001A4065D2BB0>], [Text(0, 0, 'January'), Text(0, 0, 'February'), Text(0, 0, 'March'), Text(0, 0, 'April')])
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000001A4065DC2E0>]
>>> plt.show()
>>> plt.bar(x,y)
<BarContainer object of 4 artists>
>>> plt.ylabel("Sales in US$")
Text(0, 0.5, 'Sales in US$')
>>> plt.title("Monthly Sales")
Text(0.5, 1.0, 'Monthly Sales')
>>> plt.show()
>>> 