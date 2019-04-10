#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#
# PROGRAMMER: Chris Martinis
# DATE CREATED: November 27, 2018
# REVISED DATE:
# PURPOSE: Creates a function adjust_results4_isadog that adjusts the results
#          dictionary to indicate whether or not the pet image label is of-a-dog,
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both, the pet images and the classifier function,
#          will be found in the dognames.txt file. All dog names in
#          dognames.txt are read into a dictionary where the 'key' is the
#          dog name (from dognames.txt) and the 'value' is one. If a label is
#          found to exist within this dictionary of dog names then the label
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog.
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main.
#           This function uses the extend function to add items to the list
#           that's the 'value' of the results dictionary. It adds whether
#           or not the pet image label is of-a-dog as the item at index 3
#           of the list, and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. The values at indices 3 & 4 are set
#           to 1 when the label is of-a-dog and to 0 when the label isn't a dog.
#
#
def adjust_results4_isadog(results_dic, dogfile):
    dognames_dic = dict()
    with open(dogfile, 'r') as infile:
        line = infile.readline()
        while line != '':
            newline = line.strip()
            if newline not in dognames_dic:
                dognames_dic[newline] = 1
            line = infile.readline()
    for key in results_dic:
        if results_dic[key][0] in dognames_dic:
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1,1))
            else:
                results_dic[key].extend((1,0))
        else:
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0,1))
            else:
                results_dic[key].extend((0,0))
