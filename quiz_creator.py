def display_welcome_message():
    # Display a stylish welcome message on the terminal
    print("=" * 50)
    print("        Welcome to the Quiz Creator System        ")
    print("=" * 50)
    print("\nThis program will help you create a quiz by collecting")
    print("questions and multiple choice answers and saving them")
    print("into a formatted text file (`quiz_output.txt`).\n")

def collect_quiz_data():
    # Collect quiz question and answers from the user
    question = input("Enter the quiz question: ").strip() # for whitespaces
    answer_a = input("Enter answer option (a): ").strip()
    answer_b = input("Enter answer option (b): ").strip()
    answer_c = input("Enter answer option (c): ").strip()
    answer_d = input("Enter answer option (d): ").strip()
    correct_answer = input("Enter the correct answer (a/b/c/d): ").strip().lower() # just incase the user types in CAPITAL letter

    # Return collected data as dictionary
    return {
        "question": question,
        "a": answer_a,
        "b": answer_b,
        "c": answer_c,
        "d": answer_d,
        "correct": correct_answer
    }

def format_quiz_data(quiz):
    # Format the quiz data into a readable string for the text file
    formatted_data = (
        f"Question: {quiz['question']}\n"
        f"a) {quiz['a']}\n"
        f"b) {quiz['b']}\n"
        f"c) {quiz['c']}\n"
        f"d) {quiz['d']}\n"
        f"Correct Answer: {quiz['correct']}\n"
        + "-" * 50 + "\n"
    )

    return formatted_data

def write_to_file(formatted_quiz, filename="quiz_output.txt"):
    # Write the formatted quiz data to the specified text file
    with open(filename, "a", encoding="utf=8") as file:
        file.write(formatted_quiz)

def main():
    display_welcome_message()

    while True:
        # It is referred from the Phase 3 Design: Input, Process, Output
        quiz_data = collect_quiz_data() # Input
        formatted_quiz = format_quiz_data(quiz_data) # Process
        write_to_file(formatted_quiz) # Output

        print("\nQuiz question saved successfully!")

        # Ask if the user wants to add another question
        another = input("\nDo you want to add another question (yes/no): ").strip().lower()
        if another != "yes":
            break

    # Final output/terminal design for successful conversion
    print("\n" + "=" * 55)
    print("All quiz questions have been saved to `quiz_output.txt`")
    print("=" * 55)
    print("Thank you for using Quiz Creator System!")
    print("Stay tuned for the Quiz Taker Program\n")

if __name__ == "__main__":
    main()