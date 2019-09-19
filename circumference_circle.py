#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program calculates circumference of a circle
#     with user input

import constants


def main():
    # this function calculates circumference

    # input
    radius = int(input("Enter radius of circle (mm): "))

    # process
    circumference = constants.TAU*radius

    # output
    print("")
    print("Circumference is {}mm".format(circumference))


if __name__ == "__main__":
    main()
