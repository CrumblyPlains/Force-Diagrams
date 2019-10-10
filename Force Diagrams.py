#Force Diagram Calculator
import math

#check


#Variables

#Loop Variables
foundAngle = False
foundVerticalComponent = False
foundHorizontalComponent = False
calculating = False

#Calculation Variables
angle = None
horizontalComponent = None
verticalComponent = None
resultantForce = None
horizontalAngle = None
verticalAngle = None

#Temp storage
tempStore1 = None
tempStore2 = None
tempStore3 = None
tempStore4 = None
tempStore5 = None



while True:
    while foundAngle == False:
        angle = input("What is your angle?\n")
        try:
            angle = int(angle)
            if angle >= 360:
                print("Angle too large\n")
            elif angle <= 0:
                print("Angle too small\n")
            else:
                foundAngle == True
                break
        except:
            print("incorrect angle entered\n")

    while foundVerticalComponent == False:
        verticalComponent = input("What is your vertical component?\n")
        try:
            verticalComponent = int(verticalComponent)
            foundVerticalComponent = True
        except:
            print("Incorrect value entered\n")

    while foundHorizontalComponent == False:
        horizontalComponent = input("What is your horizontal component?\n")
        try:
            horizontalComponent = int(horizontalComponent)
            foundHorizontalComponent = True
        except:
            print("Incorrect value entered\n")

    if angle == 90:
        resultantForce = math.sqrt(math.pow(verticalComponent, 2) + math.pow(horizontalComponent, 2))
        tempStore1 = verticalComponent/horizontalComponent
        horizontalAngle = math.atan(tempStore1)
        horizontalAngle = math.degrees(horizontalAngle)
        verticalAngle = angle - horizontalAngle
        
    else:
        tempStore1 = 180 - angle
        resultantForce = math.sqrt(math.pow(verticalComponent, 2) + math.pow(horizontalComponent, 2) - 2 * verticalComponent * horizontalComponent * math.cos(math.radians(tempStore1)))

        horizontalAngle = math.degrees(math.asin((math.sin(math.radians(tempStore1))/resultantForce) * verticalComponent))
        verticalAngle = angle - horizontalAngle

        
    print("Resultant Force = " + str(resultantForce) + " N")
    print("Angle from horizontal = " + str(horizontalAngle) + "°")
    print("Angle from vertical = " + str(verticalAngle) + "°")
    resultantForce = None
    horizontalAngle = None
    verticalAngle = None
    foundAngle = False
    foundVerticalComponent = False
    foundHorizontalComponent = False
        
