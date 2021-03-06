# Data Analysis and Visualization
# Andrew Payne
# ISAT 252
# Section 0003

# References
# Matplotlib Scater Plot: http://www.learningaboutelectronics.com/Articles/How-to-create-a-scatter-plot-in-matplotlib-with-Python.php
# Matplotlib Boxplot: http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
# Matplotlib Histogram: https://pythonspot.com/matplotlib-histogram/


# import neccesary packages and libraries
from random import uniform
import statistics
import matplotlib.pyplot as plt

# intiate list with student's names
names=["Bob", "Tayla", "Ricardo","Pierre","Blair","Elly","Jessica","Victoria","Milton",
"Benny","Karla","Roberto","William","Heena","Gage","Beth","Sammy","Taio","Bilaal"]
# initiate list with subjects
subjects=["Math", "Physics", "Recreation","History","English","Chemistry"]
# create dictionaries for each class
# create dictionaries inside each class dictionary for each student
# assign random grade to between 0 and 100 for each student in each subject
dic={subject:{ name:uniform(0,100) for name in names} for subject in subjects}


for subject in subjects:
    # check for the maximum grade in each class
    student_max = max(dic[subject], key=dic[subject].get)
    # display the maximum grade in each class and which student recieved the grade
    print("The maximum grade in",subject,"is a",dic[subject][student_max], "from",student_max)

# print new line for clarity
print("\n")
    
for subject in subjects:
    # check for the minimum grade in each class
    student_min = min(dic[subject], key=dic[subject].get)
    # display the minimum grade in each class and which student recieved the grade
    print("The minimum grade in",subject,"is a",dic[subject][student_min], "from",student_min)

# print new line for clarity
print("\n")

for subject in subjects:
    # access grades for each subject
    mean_vals = [dic[subject][key] for key in dic[subject]]
    # calculate the mean grade
    mean = statistics.mean(mean_vals)
    # display the average grades in each class
    print("The average grade in",subject, "is a",mean)

# print new line for clarity
print("\n")

for subject in subjects:
    # access grades for each subject
    median_vals = [dic[subject][key] for key in dic[subject]]
    # calculate the median grade
    median = statistics.median(median_vals)
    # display the median grades in each class
    print("The median grade in",subject, "is a",median)

# print new line for clarity
print("\n")

for subject in subjects:
    # access grades for each subject
    stdev_vals = [dic[subject][key] for key in dic[subject]]
    # calculate the standard deviation of the population
    stdev = statistics.pstdev(stdev_vals)
    # display the standard deviation in each class
    print("The standard deviation in",subject, "is a",stdev)

## Scater Plot
def scater_plot(names,subjects):
    for subject in subjects:
        # access grades for each subject
        grade_list = [dic[subject][key] for key in dic[subject]]
        # plot grades vs students
        plt.scatter(names, grade_list, label=subject)

    # graph title
    plt.title('Student Grades')
    # x axis
    plt.xlabel('Student Names')
    # y axis
    plt.ylabel('Grades')
    # display legend
    plt.legend()
    # display scaterplot
    plt.show()

# call scaterplot function
scater_plot(names,subjects)

## Boxplot
def boxplot():
    # access history grades
    hist_grades = [dic["History"][key] for key in dic["History"]]
    fig1, ax = plt.subplots()
    # box plot title
    ax.set_title('History Class Boxplot')
    # y axis
    plt.ylabel('History Grades')
    ax.boxplot(hist_grades)
    # display boxplot
    plt.show()
# call boxplot function
boxplot()

## Histogram
def histogram():
    math_grades = [dic["Math"][key] for key in dic["Math"]]
    # agregate the x values by intervals of 10
    bins = [10,20,30,40,50,60,70,80,90,100]
    n, bins, patches = plt.hist(math_grades, bins, histtype='bar', rwidth=0.9)
    # graph title
    plt.title('Student Grades in Math Class')
    # x axis
    plt.xlabel('Grades')
    # y axis
    plt.ylabel('Frequency')
    # display histogram
    plt.show()
# call histogram function
histogram()

