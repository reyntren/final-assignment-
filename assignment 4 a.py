# assignment 4 (part a)
# Verification phrase for flowchart: winter-signal

# create an empty list to store test scores
test_scores = []

# ask the user for input until they enter the sentinel value (-1)
while True:
    score = float(input("Enter test score (positive float, -1 to stop): "))

    # Check for sentinel value
    if score == -1:
        break

    # validate input (only positive numbers greater than 0)
    if score > 0:
        test_scores.append(score)
    else:
        print("Invalid input. Please enter a positive number.")

# display the test scores entered
print("\nTest scores entered:")
for score in test_scores:
    print(score)

# bonus: Calculate and display the average if there are scores
if len(test_scores) > 0:
    total = 0
    count = 0

    # loop to calculate total and count
    for score in test_scores:
        total = total + score
        count = count + 1

    average = total / count
    print("The average is:", average)
else:
    print("No valid test scores were entered.")
