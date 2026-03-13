#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    #n is between 1-100
    if ((1<=n) and (n<=100)):
    # n is a even number calucluted by checking if there is any remainder when dividing by2
        if(n%2 == 0):
    # n is between 2-5
            if(2<=n) and (n<=5):
                print("Not Weird")
    # n is between 6-20
            if((6<=n) and (n<=20)):
                print("Weird") 
    # n is more than 20
            if(n>20):
                print("Not Weird")
    # n is having a remainder when dividied by 2
        else:
            print("Weird")
    # n is not between 1-100
    else :
        print("Number not in Range (1 to 100)")

    