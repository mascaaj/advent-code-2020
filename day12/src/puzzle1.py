""" Puzzle for dayX advent of code 2020
"""

from time import time
import re

def direction_test(direction,value):
    """Test for direction, add to respective direction
    """
    [x,y]=[0,0]
    if direction=="N":
        y=y+int(value)
    elif direction=="S":
        y=y-int(value)
    elif direction=="E":
        x=x+int(value)
    elif direction=="W":
        x=x-int(value)
    return x,y


def rotation_test(rot_dir,current_theta,rot_mag):
    """Test for rotation, lookup correct direction
    """
    rotate = {
            -270 : "S",
            -180 : "W",
            -90 : "N",
              0 : "E",
             90 : "S",
            180 : "W",
            270 : "N"
            }
    if rot_dir=="R":
        current_theta = current_theta + int(rot_mag)
        if current_theta >= 360:
            current_theta=current_theta-360
    elif rot_dir=="L":
        current_theta = current_theta - int(rot_mag)
        if current_theta <= -360:
            current_theta=current_theta+360
    new_direction = rotate[current_theta]
    flag=1
    return new_direction,flag,current_theta

def solve(data):
    """Solution for puzzle 1
    """
    #initialization
    [x,y]=[0,0]
    theta = 0
    #dictionary for cardinal directions

    direction=" "
    last_direction="E"
    new_direction=" "
    flag = 0
    for i in enumerate(data):
        if flag==1:
            direction = new_direction
            flag = 0
            last_direction = new_direction
        else:
            direction =  last_direction
        match = re.match(r"([A-Z])([0-9]+)", i[1], re.I)
        items = match.groups()
        #test for rotation:
        if items[0]=="R" or items[0]=="L":
            new_direction,flag,theta = rotation_test(items[0],theta,items[1])

        if items[0]=="F":
            xp,yp = direction_test(direction,items[1])
            [x,y]=[x+xp,y+yp]
        elif items[0]!="R" or items[0]!="L":
            direction = items[0]
            xp,yp = direction_test(direction,items[1])
            [x,y]=[x+xp,y+yp]

    return (abs(x)+abs(y)), 0

if __name__ == "__main__":
    filename = "../data/data.txt"
    input_data = [i[:-1] for i in open(filename, "r").readlines()]
    t_start = time()

    part1, part2 = solve(input_data)
    print("Part 1: %d" % part1)

    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
