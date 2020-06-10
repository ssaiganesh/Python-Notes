#Area of Rectangle
def area(d, l): 
    # your code here
    if( d <= l):
        area_rect = "Not a rectangle"
        return area_rect
    else:
        area_rect = l * ((d**2 - l**2) ** 0.5)
        area_rect = round(area_rect,2)
        return area_rect