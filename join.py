def join_datasets():
    import math
    datasetx1 = float(input('Enter x1 coordinate:'))
    datasetx2 = float(input('Enter x2 coordinate:'))
    datasety1 = float(input('Enter y1 coordinate:'))
    datasety2 = float(input('Enter y2 coordinate:'))
    differenceX = datasetx2 - datasetx1
    differenceY = datasety2 - datasety1
    then = differenceX**2 + differenceY**2
    distance = math.sqrt(then)
    ang = math.atan(differenceY/differenceX)
    angle = math.degrees(ang
                         
    print(distance, angle)
join_datasets()