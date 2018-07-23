# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 14:25:21 2018

"""

LIST_OF_STATES = ['Alaska', 'Alabama ', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

#import cvs

#def open_file():
#fp = open('alltablesGEcrops.csv')

#    return fp
def open_file():
    print("which file")
    return open(input())

def read_file(fp):
    data_dictionary = {}
    fp.readline()
    for line in fp.readlines():
        data = line.strip().split(",")
        state = data[0]
        crop = data[1]
        variety = data[3]
        year = int(data[4])
        value = data[6]

        if state not in LIST_OF_STATES:
            continue

        if "Missouri" in state:
            state = "Missouri"

        if "Alabama" in state:
            state = "Alabama"

        if variety != "All GE varieties":
            continue

        if value == "." or "":
            continue


        if crop not in data_dictionary:
            data_dictionary[crop] = {}

        if state not in data_dictionary[crop].keys():
            data_dictionary[crop][state] = {"Max Yr" : year, "Max Val" : value, "Min Yr" : year, "Min Val" : value}

        if data_dictionary[crop][state]["Max Val"] < value:
            data_dictionary[crop][state]["Max Val"] = value
            data_dictionary[crop][state]["Max Yr"] = year

        #Determine the Absolute Max Year
        if data_dictionary[crop][state]["Max Val"] == value and data_dictionary[crop][state]["Max Yr"] > year:
            data_dictionary[crop][state]["Max Yr"] = year

        #Determine Min Year and Value
        if data_dictionary[crop][state]["Min Val"] > value:
            data_dictionary[crop][state]["Min Val"] = value
            data_dictionary[crop][state]["Min Yr"] = year

        #Determine the Absolute Min Year
        if data_dictionary[crop][state]["Min Val"] == value and data_dictionary[crop][state]["Min Yr"] < year:
            data_dictionary[crop][state]["Min Yr"] = year

    return data_dictionary


def print_dict(data_dictionary):
    for crop in sorted(data_dictionary.keys()):
        print("Crop : " + crop)
        print("{:<20s}{:<8s}{:<6s}{:<8s}{:<6s}".format("State", "Max Yr", "Max", "Min Yr", "Min"))
        for states in sorted(data_dictionary[crop].keys()):
            print("{:<20s}{:<8s}{:<6s}{:<8s}{:<6s}".format(states, str(data_dictionary[crop][states]["Max Yr"]), data_dictionary[crop][states]["Max Val"], str(data_dictionary[crop][states]["Min Yr"]), data_dictionary[crop][states]["Min Val"]))


def main():
    data_dictionary = read_file(open_file())
    print_dict(data_dictionary)
    #print data




if __name__ == "__main__":
    main()


    #print (state, crop, variety, year, value)

#    if crop_state not in data_dictionary:
#        data_dictionary[crop_state]={}
#
#print(data_dictionary)