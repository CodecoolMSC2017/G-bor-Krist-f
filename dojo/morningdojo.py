import string
def grades(point):
    if point < 38:
        print(point)
    elif point[1] == 3 or point[1] == 8:
        print(point + 2)
    elif point[1] == 4 or point[1] == 9:
        print(point + 1)
    else:
        print(point)
            
          


grade_points = int(input(""))
grades(grade_points)