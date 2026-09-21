# Unit 1 Lab 1 - workbook
# Type your own code under each requirement. Run with: python u1l1-workbook.py
# Keep the labels in the print calls so each output maps to a requirement.

import numpy as np

class Color:
    RED = '\033[31m'
    RESET = '\033[0m'


def problem_1():
    print(Color.RED + "\n======= Problem 1 - Student Scores =======" + Color.RESET)
    # scores: 78, 85, 92, 67, 88, 95, 73, 81

    # 1. complete array
    print("1. Display the complete array: ")
    scores = np.array([78, 85, 92, 67, 88, 95, 73, 81])
    print("Scores array: ", scores)

    # 2. shape, ndim, size, dtype
    print("\n 2. Array properties:")
    print("Shape of scores ", scores.shape)
    print("Number of Dimensions of scores ", scores.ndim)
    print("Size of scores ", scores.size)
    print("Data type of scores ", scores.dtype)

    # 3. first score
    print("\n 3. First score:")
    print(scores[0])

    # 4. fourth score
    print("\n 4. Fourth score:")
    print(scores[3])

    # 5. last score
    print("\n 5. Last score:")
    print(scores[-1])

    # 6. index 2 through index 5
    print("\n 6. Index 2 through index 5:")
    print(scores[2:6])


def problem_2():
    print(Color.RED + "\n======= Problem 2 - Temperature Matrix =======" + Color.RESET)
    # 72 75 78 80
    # 68 71 74 77
    # 81 83 85 87

    # 1. complete array
    print("1. Display the complete array: ")
    temperatures = np.array([[72,75,78,80],
                             [68,71,74,77],
                             [81,83,85,87]])
    print("Temperatures: ", "\n", temperatures)

    # 2. shape
    print("\n 2. Shape of the  Temperature array:")
    print(temperatures.shape)

    # 3. ndim
    print("\n 3. Number of Dimensions of the Temperature array:")
    print(temperatures.ndim)

    # 4. entire second row
    print("\n 4. Entire second row of the Temperatures:")
    print(temperatures[1])

    # 5. entire third column
    print("\n 5. Entire third column of the Temperatures:")
    print(temperatures[:,2])

    # 6. first two rows, first three columns
    print("\n 6. First two rows, first three columns of the Temperatures:")
    print(temperatures[:2,:3])

    # 7. the value 85 by row and column index
    print("\n 7. The value 85 by row and column index in the Temperatures:")
    print(temperatures[2,2], "in position (2,2)")


def problem_3():
    print(Color.RED + "\n======= Problem 3 - Creating Data =======" + Color.RESET)
    # Display each array and its shape.
    # 1. 0, 5, 10, ... 50
    print("\n 1. Multiples of five to fifty:")
    five_multiples = np.arange(0, 51, 5)
    print(five_multiples)

    # 2. 10 evenly spaced values between 0 and 100
    ten_evenly_spaced = np.linspace(0, 100, 10)
    print("\n 10 evenly spaced values between 0 and 100: ")
    print(np.round(ten_evenly_spaced,2))

    # 3. 3 x 4 zeros
    print("\n 3. 3 x 4 zeros:")
    three_by_four_zeros = np.zeros((3,4))
    print(three_by_four_zeros)

    # 4. 2 x 5 all 25
    print("\n 4. 2 x 5 all 25:")
    two_by_five_25 = np.full((2,5), 25)
    print(two_by_five_25)

    # 5. 4 x 4 identity
    print("\n 5. 4 x 4 identity:")
    four_by_four_identity = np.eye(4)
    print(four_by_four_identity)


def problem_4():
    print(Color.RED + "\n======= Problem 4 - Product Prices =======" + Color.RESET)
    prices = np.array([12.99, 25.50, 7.75, 45.00, 18.25, 60.00])

    # 1. complete array
    print("\n 1. Complete array of prices:")
    # 2. dtype

    # 3. convert to integers with astype

    # 4. prices greater than 20

    # 5. prices between 10 and 50  (state inclusive or exclusive in a comment)

    # 6. first three prices


def problem_5():
    print(Color.RED + "\n======= Problem 5 - Employee IDs =======" + Color.RESET)
    # IDs 100 through 120, do not type them out

    # 1. complete array

    # 2. every other ID

    # 3. last five IDs

    # 4. IDs greater than 110

    # 5. boolean filter: 105 through 115 inclusive

    # 6. fancy index: positions 0, 5, 10, 15


def problem_6():
    print(Color.RED + "\n======= Problem 6 - 2-D Data Challenge =======" + Color.RESET)
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
