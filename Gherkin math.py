import math

def bottom(x):
    y = -166 + (1/3.6)*x**2 - (1/20000)*x**4 + (1/21000000)*x**6 - (1/30000000000000000000000000000)*x**20
    return y

def top(x):
    #y = 180 - (1/7.3)*x**2 + (1/4200)*x**4 - (1/2800000)*x**6 + (1/9000000000)*x**8 - (1/100000000000000)*x**10 + (1/100000000000000000)*x**12 #lower bound
    #y = 180 - (1/7.7)*x**2 + (1/4800)*x**4 - (1/3100000)*x**6 + (1/8000000000)*x**8 - (1/400000000000000)*x**10 + (1/700000000000000000)*x**12 #most accurate
    y = 180 - (1/7.7)*x**2 + (1/4800)*x**4 - (1/3200000)*x**6 + (1/8600000000)*x**8 - (1/400000000000000)*x**10 + (1/700000000000000000)*x**12 #upper bound
    return y

def middle(x):
    return 28.25

def find_volume(increment = 0.25):
    height = 0
    volume = 0
    prev_width = 0
    while (height <= 180):
        if (height <= 50 and height >= 0):  
            n = 24
            while (n < 28.5):
                if (round(bottom(n), 4) == height):
                    width = n
                    break
                n += 0.000001

            if prev_width == width:
                print("Width couldn't be found at height: " + str(height))

        elif (height > 50 and height < 85):
            width = middle(height)

        elif (height >= 85 and height <= 180):
            n = 0
            while (n < 28.5):
                if (round(top(n), 4) == height):
                    width = n
                    break
                n += 0.000005

            if prev_width == width: 
                print("Width couldn't be found at height: " + str(height))

        prev_width = width
    
        volume += width * width * math.pi * increment
        height += increment
        print(height)
    return volume

def find_surface(increment = 0.25):
    height = 0
    surfaceArea = 0
    prev_width = 0
    while (height <= 180):
        if (height <= 50 and height >= 0):  
            n = 24
            while (n < 28.5):
                if (round(bottom(n), 4) == height):
                    width = n
                    break
                n += 0.000001

            if prev_width == width:
                print("Width couldn't be found at height: " + str(height))

        elif (height > 50 and height < 85):
            width = middle(height)

        elif (height >= 85 and height <= 180):
            n = 0
            while (n < 28.5):
                if (round(top(n), 4) == height):
                    width = n
                    break
                n += 0.00001

            if prev_width == width: 
                print("Width couldn't be found at height: " + str(height))

        prev_width = width
    
        surfaceArea += width * 2 * math.pi * increment
        height += increment
        print(height)
    final_area = surfaceArea + (25*25*math.pi)
    return final_area

print(find_surface())

###### lower bound ######
#volume: 337,679.28105151094
#surface area: 28,677.631114826105

##### most accurate #####
#volume: 343,062.6911421616
#surface area: 28,907.615426308785

##### upper bound #####
#volume: 344,504.6210788532
