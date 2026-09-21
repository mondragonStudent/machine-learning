Purpose of This Lab
The purpose of this lab is to practice the actual application of the NumPy concepts covered in Sections 1–4 of the handout.

This is not a speed competition. The goal is not simply to obtain the correct output or finish the assignment as quickly as possible. The goal is to understand how and why NumPy is being used to solve each problem.

You will practice:

Creating NumPy arrays
Creating arrays using NumPy functions
Understanding shape, ndim, size, and dtype
Converting data types
Indexing arrays
Slicing arrays
Working with 2-D arrays
Boolean filtering
Fancy indexing
Instructions
There are six problems below.

You must choose and complete any FOUR of the six problems.

For each problem:

Write the Python/NumPy code necessary to solve every requirement.
Run your code and verify that it works correctly.
Make sure you understand what each line of your code is doing.
Submit your completed work as instructed in Canvas.
Use of Artificial Intelligence
You ARE allowed and encouraged to use AI for this lab.

However, AI should be used as a learning tool, not simply as a way to copy an answer.

If you do not know how to solve part of a problem, ask AI questions such as:

"What NumPy function should I use for this?"
"Can you explain what this function does?"
"Why am I getting this error?"
"Can you give me a hint without giving me the complete solution?"
"Why does this indexing expression work?"
"What does this output mean?"
"Can you explain this code step by step?"
"What is another way to solve this?"
Ask AI as many questions as necessary until you understand how to reach the solution.

The purpose of this assignment is for you to learn how the NumPy concepts from class are actually applied to solve problems. Getting the correct answer is important, but understanding how you got there is the main objective of the lab.

Problem 1 – Student Scores
Create a NumPy array containing the following student scores:

78, 85, 92, 67, 88, 95, 73, 81
Using NumPy:

Display the complete array.
Display its shape, ndim, size, and dtype.
Display the first score.
Display the fourth score.
Display the last score.
Display the scores from index 2 through index 5.
Problem 2 – Temperature Matrix
Create the following 2-D NumPy array:

72   75   78   80
68   71   74   77
81   83   85   87
Using NumPy:

Display the complete array.
Display its shape.
Display its number of dimensions.
Select and display the entire second row.
Select and display the entire third column.
Select the first two rows and first three columns.
Display the value 85 using row and column indexing.
Problem 3 – Creating Data with NumPy
For this problem, do not manually type every value. Use the appropriate NumPy array-creation functions.

Create:

An array containing:
0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
An array containing 10 evenly spaced values between 0 and 100.
A 3 × 4 array filled with zeros.
A 2 × 5 array in which every value is 25.
A 4 × 4 identity matrix.
For each array, display the resulting array and its shape.

Problem 4 – Product Prices
Create the following NumPy array:

prices = np.array([12.99, 25.50, 7.75, 45.00, 18.25, 60.00])
Using NumPy:

Display the complete array.
Display its dtype.
Convert the array to integers using astype() and display the result.
Display all prices greater than $20.
Display all prices between $10 and $50.
Display the first three prices.
Problem 5 – Employee IDs
Create a NumPy array containing every employee ID from 100 through 120.

Do not manually type all 21 IDs.

Using NumPy:

Display the complete array.
Display every other employee ID.
Display the last five employee IDs.
Display all employee IDs greater than 110.
Use Boolean filtering to display IDs from 105 through 115.
Use fancy indexing to select the employee IDs located at positions 0, 5, 10, and 15.
Problem 6 – 2-D Data Challenge
Create the following NumPy array:

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])
Using NumPy:

Display the complete array.
Display its shape, ndim, size, and dtype.
Extract and display the middle two rows.
Extract and display the last two columns.
Extract the following center 2 × 2 section:
60    70
100   110
Display all values greater than 75.
Use fancy indexing to select and display the first and fourth rows.
Submission Requirements
Choose FOUR of the six problems and submit your completed solutions.

Before submitting, make sure:

Your code runs without errors.
You completed every requirement for each of the four problems you selected.
Your output demonstrates that your code works.
You understand the NumPy functions, indexing, and operations you used.
Remember
Do not simply ask AI to complete the lab for you and copy the answer.

Use AI as your tutor. Ask questions. Ask for explanations. Ask for hints. Show it your errors. Ask why something works. Ask it to explain concepts differently if you do not understand the first explanation.

Ask as many questions as you need until you can understand and solve the problem.

The objective of this lab is not only to produce working code. The objective is to learn how to apply NumPy to solve real programming problems.