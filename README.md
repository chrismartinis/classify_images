# Image Classification for a City Dog Show

This was my very first project for the __[Artificial Intelligence Programming with Python](https://eu.udacity.com/course/ai-programming-python-nanodegree--nd089)__ Nanodegree from Udacity. In this project my task was to use a pre-trained image classifier to identify dog breeds. Below follows an in-depth description of the project, borrowing from the original info-material, as provided by Udacity.

## Project Goal

- Improving my programming skills using Python

In this project I have used a created (ready-to-use) image classifier to identify dog breeds. I was asked to focus on Python and not on the actual classifier (I actually built a classifier of my own, later in the program).

## Description

My city is hosting a citywide dog show and I have volunteered to help the organising committee with contestant registration. Every participant that registers must submit an image of their dog along with biographical information about their dog. The registration system tags the images based upon the biographical information. Some people are planning on registering pets that aren’t actual dogs. I need to use an already developed Python classifier to make sure the participants are dogs.

## My Tasks
- Use my Python skills, to determine which image classification algorithm works the "best" on classifying images as "dogs" or "not dogs";
- Determine how well the "best" classification algorithm works on correctly identifying a dog's breed;
- Time how long each algorithm takes to solve the classification problem. With computational tasks, there is often a trade-off between accuracy and runtime. The more accurate an algorithm, the higher the likelihood that it will take more time to run and use more computational resources to run.

## Important Note
For this image classification task I used an image classification application using a deep learning model called "Convolutional Neural Network", often abbreviated as CNN. CNNs work particularly well for detecting features in images like colours, textures, and edges; then using these features to identify objects in the images. I used a CNN that has already learned the features from a giant dataset of 1.2 million images called __[ImageNet](http://www.image-net.org)__. There are different types of CNNs that have different structures (architectures) that work better or worse depending on the chosen criteria. With this project I explored the three different architectures (AlexNet, VGG, and ResNet) and determined which was best for my application.

Udacity did provide me with a classifier function in classifier.py that allowed me to use these CNNs to classify my images. For this project, I focused on using my Python skills to complete the task at hand using the classifier function.

Note: Certain breeds of dogs look very similar. The more images of two similar looking dog breeds that the algorithm has learned from, the more likely the algorithm will be able to distinguish between those two breeds. Udacity's faculty have found the following breeds to look very similar: Great Pyrenees and Kuvasz, German Shepherd and Malinois, Beagle and Walker Hound, amongst others.

## Principal Objectives
1. Correctly identify which pet images are of dogs (even if breed is misclassified) and which pet images aren't of dogs;

2. Correctly classify the breed of dog, for the images that are of dogs;

3. Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve the objectives 1 and 2;

4. Consider the time resources required to best achieve objectives 1 and 2, and determine if an alternative solution would have given a "good enough" result, given the amount of time each of the algorithms take to run.

## Running the Project on a Local Computer

To run the project on a local computer, you will need to install at least Python 3.6 on your computer. The easiest way to install Python and the appropriate Python modules is to install __[Anaconda](https://www.anaconda.com/download)__.

## Installing PyTorch and Torchvision - Linux, OSX(Mac), Windows

For this project you will also need to install the Python packages PyTorch and Torchvision. If your local computer has a Linux, OSX (Mac), or Windows operating system look to __[Get Started](https://pytorch.org)__ for installation instructions.  

## Files Required to Run check_images.py Locally

The following files and folders need to be put in the same folder as the check_images.py Python program on your local computer.

## Needed Files:

- pet_images (folder of 40 pet images)
- uploaded_images (a folder which will hold your uploaded images)
- classifier.py (classifier function you will be using to classify the images)
- dognames.txt (file that contains all the valid dog names from the classifier function and the pet image files)
- imagenet1000_clsid_to_human.txt (dictionary that converts the classifier function ids to text labels)
- adjust_results4_isadog.py (a program that contains the adjust_results4_isadog function)
- calculates_results_stats.py (a program that contains the calculates_results_stats function)
- classify_images.py (a program that contains the classify_images function)
- get_input_args.py (a program that contains the get_input_args function)
- get_pet_labels.py (a program that contains the get_pet_labels function)
- print_results.py (a program that contains the print_results function)
- run_models_batch.sh (a bash script that will run check_images.py sequentially for all 3 model architectures and output their results to text files - on Unix/Linux/OSX from a terminal window)
- run_models_batch.bat (a batch script that will run check_images.py sequentially for all 3 model architectures and output their results to text files - on Windows from the Anaconda Prompt window)
- run_models_batch_uploaded.sh (a bash script that will run check_images.py sequentially for all 3 model architectures on the uploaded images folder and output their results to text files - on Unix/Linux/OSX from a terminal window)
- run_models_batch_uploaded.bat (a batch script that will run check_images.py sequentially for all 3 model architectures on the uploaded images folder and output their results to text files - on Windows from the Anaconda Prompt window)
- print_functions_for_lab_checks.py (a program that contains functions that checks the code)

## Running Batch Files on Windows OS Locally

To run the files run_models_batch or run_models_batch_uploaded that run all 3 model architectures using check_images.py on a Windows OS locally; you will need to use the files that end with the extension .bat instead of the extension .sh. You will also need to have installed Anaconda on your computer.

## Directions:
- Open the Anaconda Prompt - either from typing Anaconda Prompt within the search bar and selecting it or by clicking on it once it's found within the Anaconda folder of programs.
- Navigate to the folder within the Anaconda Prompt that contains the Project files including check_images.py and run_models_batch.bat using the command cd.
- Type the command within the Anaconda Prompt:
```bash
run_models_batch.bat
```

If instead you are working with the uploaded images, you will replace all instances of run_models_batch.bat from the directions above with run_models_batch_uploaded.bat.

## License
__[MIT](https://github.com/chrismartinis/classify_images/blob/master/LICENSE)__
