#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#
# PROGRAMMER: Chris Martinis
# DATE CREATED: November 26, 2018
# REVISED DATE:
# PURPOSE: Creates a function classify_images that uses the classifier function
#          to create the classifier labels and then compares the classifier
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images function
#             and as in_arg.dir for function call within main.
#            -The Results Dictionary as results_dic within classify_images
#             function and results for the functin call within main.
#            -The CNN Model Architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main.
#           This function uses the extend function to add items to the list
#           that's the 'value' of the results dictionary. In particular, it adds the
#           classifier label as the item at index 1 of the list and the comparison
#           of the pet and classifier labels as the item at index 2 of the list.
#

from classifier import classifier

def classify_images(images_dir, results_dic, model):
    for key in results_dic:
        test_image = images_dir + key
#        print(test_image)
        image_classification = classifier(test_image, model)
        model_label = image_classification.lower().strip()
#        print(model_label)
        truth = results_dic[key][0]
        if truth in model_label:
            results_dic[key].extend([model_label, 1])
        else:
            results_dic[key].extend([model_label, 0])
