#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Chris Martinis
# DATE CREATED: November 23, 2018
# REVISED DATE:
# PURPOSE: The function get_pet_labels creates the pet labels from the
#          images' filenames. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list contains the following item
#          at index 0: pet image label (string).
##

# Imports python modules
from os import listdir

# Define function
def get_pet_labels(image_dir):
    in_files = listdir(image_dir)

    # # print 10 of the filenames from folder pet_images/
    # print('\nPrinting filenames from folder containing images')
    # for idx in range(0, len(in_files, 1):
    #     print("\n{:2d} file: {:>30}".format(idx + 1, in_files[idx]))

    # initialise empty dictionary
    results_dic = dict()

    # populate dictionary
    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != '.':
            pet_label = ''
            list_of_words = in_files[idx].lower().split('_')
            for word in list_of_words:
                if word.isalpha():
                    pet_label += word + ' '
            pet_label = pet_label.strip()

            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]
            else:
                print('**Warning: Key=', in_files[idx],
                      'already exists in dictionary with value=',
                      result-dic[in_files[idx]])
    return results_dic

    # # printing keys and vaules for testing purposes
    # print("\nPrinting all key-value pairs in dictionary results_dic:")
    # for key in results_dic:
    #     print("Filename=", key, "   Pet Label=", results_dic[key][0])
    #
    # # printing the length of dictionary for testing purposes
    # items_in_dic = len(results_dic)
    # print('\nDictionary contains n items:', items_in_dic)
    # return results_dic
