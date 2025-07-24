# Simple Python Quiz by Affan

def run_quiz():
    print("Welcome to the Quiz!")

    name = input("Enter your name: ")
    if name.strip() == "":
        name = "Guest"

    questions = [
        ["What is the capital of France?", "Paris"],
        ["Which planet is known as the Red Planet?", "Mars"],
        ["What is 3-2+5+2-7x0?", "0"],
        ["Who wrote Romeo and Juliet?", "Shakespeare"],
        ["What is the square root of 81?", "9"],
        ["What gas do plants use to make food?", "Carbon Dioxide"],
        ["Which ocean is the biggest?", "Pacific"],
        ["What is H2O commonly known as?", "Water"],
        ["Which animal is the king of the jungle?", "Lion"],
        ["What is the capital of Pakistan?", "Islamabad"]
    ]

    score = 0

    for i in range(len(questions)):
        print(f"\nQuestion {i+1}: {questions[i][0]}")
        ans = input("Your answer: ")

        if ans.strip().lower() == questions[i][1].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {questions[i][1]}")

    print(f"\n{name}, your score is {score} out of {len(questions)}")

    try:
        with open("scores.txt", "a") as f:
            f.write(f"{name}: {score}/{len(questions)}\n")
    except:
        print("Could not save the score.")

def view_scores():
    print("\nPrevious Scores:")
    try:
        with open("scores.txt", "r") as f:
            print(f.read())
    except:
        print("No scores yet.")

while True:
    print("\n----- Quiz Menu -----")
    print("1. Take the quiz")
    print("2. View scores")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        run_quiz()
    elif choice == "2":
        view_scores()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")




#second if first not good

def run_quiz():
    print("Welcome to the Quiz!")

    name = input("Enter your name: ")
    if name.strip() == "":
        name = "Guest"

    questions = [
        ["What is the capital of France?", "Paris"],
        ["Which planet is known as the Red Planet?", "Mars"],
        ["What is 3-2+5+2-7x0?", "0"],
        ["Who wrote Romeo and Juliet?", "Shakespeare"],
        ["What is the square root of 81?", "9"],
        ["What gas do plants use to make food?", "Carbon Dioxide"],
        ["Which ocean is the biggest?", "Pacific"],
        ["What is H2O commonly known as?", "Water"],
        ["Which animal is the king of the jungle?", "Lion"],
        ["What is the capital of Pakistan?", "Islamabad"]
    ]

    score = 0

    for i in range(len(questions)):
        print(f"\nQuestion {i+1}: {questions[i][0]}")
        ans = input("Your answer: ")

        if ans.strip().lower() == questions[i][1].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {questions[i][1]}")

    print(f"\n{name}, your score is {score} out of {len(questions)}")

    try:
        with open("scores.txt", "a") as f:
            f.write(f"{name}: {score}/{len(questions)}\n")
    except:
        print("Could not save the score.")

def view_scores():
    print("\nPrevious Scores:")
    try:
        with open("scores.txt", "r") as f:
            print(f.read())
    except:
        print("No scores yet.")

while True:
    print("\n----- Quiz Menu -----")
    print("1. Take the quiz")
    print("2. View scores")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        run_quiz()
    elif choice == "2":
        view_scores()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
