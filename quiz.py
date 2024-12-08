# Function to display the greeting message
def greeting_message():
    print("Fun Quiz")
    # Add a visual separator between them for a nice design
    print("-*-" * 12)
    print("Where Every Answer Counts")
    # Another visual design
    print("-*-" * 5 + " Let's start! " + "-*-" * 5)

# My questions
questions = [
    ("What is the longest river in the world?", ["The River Nile", "The Amazon", "The Rhine", "The Mississippi"], 1),
    ("What is the chemical symbol for silver?", ["H2O", "Mg", "Ag", "Li"], 3),
    ("What is the square root of 64?", ["9", "8", "5", "12"], 2),
    ("Which US president had a pet alligator that he kept in a White House bathtub?", 
    ["George Washington", "Abraham Lincoln", "John F. Kennedy", "John Quincy Adams"], 4),
    ("What is the smallest country in the world?", ["Russia", "China", "Italy", "Vatican City"], 4),
    ("In what European country is it illegal to own just one guinea pig?", 
    ["Romania", "United Kingdom", "India", "Switzerland"], 4),
    ("How long can sloths hold their breath?", ["20 min", "15 min", "40 min", "10 min"], 3),
    ("How many bones do sharks have?", ["143", "142", "141", "None"], 4),
]




# Display the greeting message
greeting_message()

score = 0

# Loop through the questions
for question, options, correct_answer in questions:
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Get the answers
    while True:
        try:
            answer = int(input("Choose an answer between 1-4: "))
            if 1 <= answer <= 4:
                break
            else:
                print("You have to choose an option between 1 and 4.Try again!.")
        except ValueError:
            print("Please enter a number between 1 and 4.")

    # Check if the answer is correct
    if answer == correct_answer:
        score += 1
        print("You chose the right answer!")
    else:
        print("Sorry,wrong one!")



# Show results
print("\nQuiz Completed!")
print(f"Your Score: {score}/{len(questions)}")
if score == len(questions):
    print("You are a superstar! You got all answers correct!")
elif score >= len(questions) // 2:
    print("Good job! You did well.")
else:
    print("Better luck next time!")

print("Thank you for playing!")
