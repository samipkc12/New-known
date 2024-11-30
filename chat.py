import random

def quiz_game():
    # List of questions with options and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "What is the largest mammal on Earth?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"],
            "answer": "Blue Whale"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["Shakespeare", "Hemingway", "Austen", "Dickens"],
            "answer": "Shakespeare"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["6", "7", "8", "9"],
            "answer": "8"
        }
    ]
    
    # Shuffle the questions
    random.shuffle(questions)
    
    score = 0
    
    print("Welcome to the Randomized Quiz Game!")
    print("Answer the following questions:\n")
    
    for i, question_data in enumerate(questions, 1):
        print(f"Question {i}: {question_data['question']}")
        
        # Shuffle the options
        options = question_data["options"]
        random.shuffle(options)
        
        # Display options
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        
        # Get user's answer
        try:
            user_choice = int(input("Enter the number of your choice: "))
            if options[user_choice - 1] == question_data["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question_data['answer']}\n")
        except (ValueError, IndexError):
            print(f"Invalid input! The correct answer was: {question_data['answer']}\n")
    
    print(f"Quiz Over! Your score: {score}/{len(questions)}")
    print("Thanks for playing!")

# Run the quiz game
quiz_game()
