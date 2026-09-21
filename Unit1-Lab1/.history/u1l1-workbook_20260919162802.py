# Unit 1 Lab 1 - workbook
# Type your own code under each requirement. Run with: python u1l1-workbook.py
# Keep the labels in the print calls so each output maps to a requirement.

import numpy as np


def problem_1():
    print("\n=== Problem 1 - Student Scores ===")
    # scores: 78, 85, 92, 67, 88, 95, 73, 81

    # 1. complete array
    scores = np.array([78, 85, 92, 67, 88, 95, 73, 81])

    # 2. shape, ndim, size, dtype
    print("")

    # 3. first score

    # 4. fourth score

    # 5. last score

    # 6. index 2 through index 5


def problem_2():
    print("\n=== Problem 2 - Temperature Matrix ===")
    # 72 75 78 80
    # 68 71 74 77
    # 81 83 85 87

    # 1. complete array

    # 2. shape

    # 3. ndim

    # 4. entire second row

    # 5. entire third column

    # 6. first two rows, first three columns

    # 7. the value 85 by row and column index


def problem_3():
    print("\n=== Problem 3 - Creating Data ===")
    # Display each array and its shape.

    # 1. 0, 5, 10, ... 50

    # 2. 10 evenly spaced values between 0 and 100

    # 3. 3 x 4 zeros

    # 4. 2 x 5 all 25

    # 5. 4 x 4 identity


def problem_4():
    print("\n=== Problem 4 - Product Prices ===")
    prices = np.array([12.99, 25.50, 7.75, 45.00, 18.25, 60.00])

    # 1. complete array

    # 2. dtype

    # 3. convert to integers with astype

    # 4. prices greater than 20

    # 5. prices between 10 and 50  (state inclusive or exclusive in a comment)

    # 6. first three prices


def problem_5():
    print("\n=== Problem 5 - Employee IDs ===")
    # IDs 100 through 120, do not type them out

    # 1. complete array

    # 2. every other ID

    # 3. last five IDs

    # 4. IDs greater than 110

    # 5. boolean filter: 105 through 115 inclusive

    # 6. fancy index: positions 0, 5, 10, 15


def problem_6():
    print("\n=== Problem 6 - 2-D Data Challenge ===")
    data = np.array([
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160]
    ])

    # 1. complete array

    # 2. shape, ndim, size, dtype

    # 3. middle two rows

    # 4. last two columns

    # 5. center 2 x 2:  60 70 / 100 110

    # 6. values greater than 75

    # 7. fancy index: first and fourth rows


if __name__ == "__main__":
    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()
    problem_6()
