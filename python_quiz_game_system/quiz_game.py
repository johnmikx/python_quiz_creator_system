import random # To shuffle questions randomly

def load_questions_from_file(filename="quiz_output.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    # Split content into individual questions
    blocks = content.strip().split("--------------------------------------------------")
    questions = []

    for block in blocks:
        lines = block.strip().splitlines()
        if len(lines) < 6:
            continue # Skip if incomplete

        # Parse question and options
        question_text = lines[0][len("Question: "):] # [Row][Column] (indexing)
        options = {
            'a': lines[1][3:],
            'b': lines[2][3:],
            'c': lines[3][3:],
            'd': lines[4][3:]
        }
        correct = lines[5][len("Correct Answer: "):].strip().lower()

        questions.append({
            'question': question_text,
            'options': options,
            'answer': correct
        })

    return questions

def display_question(q):
    print("\n" + "=" * 100)
    print(f"Question: {q['question']}")
    for key, value in q['options'].items():
        print(f"  {key}) {value}")
    print("=" * 100)

def quiz():
    print("\nWelcome to the Quiz Game! 🤗")
    print("Answer the following questions. Type a, b, c, or d.\n")

    questions = load_questions_from_file()
    random.shuffle(questions)

    for q in questions:
        display_question(q)

        user_answer = input("Your Answer: ").strip().lower()
        while user_answer not in ['a', 'b', 'c', 'd']:
            user_answer = input("Invalid. Please enter a, b, c, or d: ").strip().lower()

        if user_answer == q['answer']:
            print("✅ Correct!\n")
        else:
            correct_text = q['options'][q['answer']]
            print(f"❌ Incorrect! The correct answer is ({q['answer']}) {correct_text}\n")

    print("🎉 You've completed the quiz. Well done! :)")

if __name__ == "__main__":
    quiz()