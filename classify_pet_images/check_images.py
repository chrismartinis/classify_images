#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py

# PROGRAMMER: Chris Martinis
# DATE CREATED: November 22, 2018
# REVISED DATE:
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task.
#          Note that the true identity of the pet (or object) in the image is
#          indicated by the filename of the image. Therefore, the program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. This
#          program compares the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # Measures total program runtime by collecting start time
    start_time = time()

    # Function get_input_args is defined in the file get_input_args.py
    # This function retrieves 3 Command Line Arugments as input from
    # the user running the program from a terminal window. This function returns
    # the collection of these Command Line Arguments from the function call as
    # the variable in_arg.
    in_arg = get_input_args()

    # Function that checks Command Line Arguments using in_arg
    check_command_line_arguments(in_arg)

    # Function get_pet_labels is defined in the file get_pet_labels.py
    # This function creates the Results Dictionary that contains the results.
    # This dictionary is returned from the function call as the variable results.
    results = get_pet_labels(in_arg.dir)

    # Function that checks pet images in the Results Dictionary using results
    check_creating_pet_image_labels(results)

    # Function classify_images is defined in the file classiy_images.py
    # Creates classifier labels with classifier function, compares labels,
    # and adds these results to the Results Dictionary (results).
    classify_images(in_arg.dir, results, in_arg.arch)

    # Function that checks Results Dictionary using results
    check_classifying_images(results)

    # Function adjust_results4_isadog is defined in the file adjust_results4_isadog.py
    # Adjusts the Results Dictionary to determine if classifier correctly
    # classified images as 'a dog' or 'not a dog'. This demonstrates if
    # model can correctly classify dog images as dogs (regardless of breed).
    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)

    # Function calculates_results_stats is defined in the file calculates_results_stats.py
    # This function creates the Results Statistics Dictionary that contains a
    # summary of the results statistics (this includes counts & percentages). This
    # dictionary is returned from the function call as the variable results_stats.
    # Calculates results of run and puts statistics in the Results Statistics
    # Dictionary (results_stats).
    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)

    # Function print_results is deined within the file print_results.py
    # Prints summary results, incorrect classifications of dogs (if requested)
    # and incorrectly classified breeds (if requested)
    print_results(results, results_stats, in_arg.arch, True, True)

    # Measure total program runtime by collecting end time
    end_time = time()

    # Computes overall runtime in seconds & print it in hh:mm:ss format
    # Calculate difference between end time and start time
    tot_time = end_time - start_time

    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(round((tot_time%3600)%60)) )


# Call to main function to run the program
if __name__ == "__main__":
    main()
