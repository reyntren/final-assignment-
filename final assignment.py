import random


def is_valid_integer(text: str) -> bool:
    """
    Check if a string is a valid integer (supports negative numbers).

    Args:
        text (str): The user input.

    Returns:
        bool: True if the text is a valid integer, otherwise False.
    """
    return text.lstrip("-").isdigit()


def generate_question(level: int, mode: str) -> tuple[str, int]:
    """
    Generate a math question based on the level and selected mode.

    Levels scale difficulty by increasing the maximum random number:
    max_number = level * 10

    Args:
        level (int): Current level (1 to 5).
        mode (str): "1" addition, "2" subtraction, "3" mixed (+ and -).

    Returns:
        tuple[str, int]: (question_text, correct_answer)
    """
    max_number = level * 10
    num1 = random.randint(0, max_number)
    num2 = random.randint(0, max_number)

    # operators are stored in a list.
    if mode == "1":
        operators = ["+"]
    elif mode == "2":
        operators = ["-"]
    else:
        operators = ["+", "-"]

    operator = random.choice(operators)

    if operator == "+":
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2

    question_text = f"{num1} {operator} {num2}"
    return question_text, correct_answer


# ----------------------------
# Main Program
# ----------------------------
print("=== Math Quiz Game ===")

# Mode selection wont immediately start the game.
while True:
    print("\nSelect a mode:")
    print("1. Addition only")
    print("2. Subtraction only")
    print("3. Addition and Subtraction")

    mode = input("Enter your choice (1, 2, or 3): ").strip()

    if mode not in ("1", "2", "3"):
        print("Invalid choice. Please try again.")
        continue

    mode_name = (
        "Addition only" if mode == "1"
        else "Subtraction only" if mode == "2"
        else "Addition and Subtraction"
    )

    print(f"\nYou selected: {mode_name}")
    start_choice = input("Press ENTER to start or type 'c' to change mode: ").strip().lower()

    if start_choice != "c":
        break

level = 1
score = 0
playing = True
MAX_LEVEL = 5  # number of levels

while playing and level <= MAX_LEVEL:
    print(f"\n--- Level {level} ---")

    # Number of questions increases each level: Level 1 = 1 question, etc.
    questions_this_level = level
    question_count = 0

    while question_count < questions_this_level:
        question, correct_answer = generate_question(level, mode)
        print("Question:", question)

        user_input = input("Your answer: ").strip()

        # Input validation without try/except
        while not is_valid_integer(user_input):
            user_input = input("Invalid input. Please enter a whole number: ").strip()

        user_answer = int(user_input)

        # Check answer
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer was:", correct_answer)

        question_count += 1

    print("Your current score:", score)

    # Ask user if they want to continue (only if not at max level)
    if level < MAX_LEVEL:
        continue_choice = input("Do you want to continue to the next level? (y/n): ").strip().lower()
        if continue_choice != "y":
            playing = False

    level += 1

print("\n=== Game Over ===")
print("Final score:", score)
print("Thanks for playing!")
