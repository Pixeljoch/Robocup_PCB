import math

x = 0
y = 0

for x in range(24):
    pos_x = x * 15
    sum_x = (math.cos((math.radians(pos_x+90)) * 104.7194))
    print("Angle: " + str(pos_x) + " Pos: " + str(math.degrees(sum_x)))