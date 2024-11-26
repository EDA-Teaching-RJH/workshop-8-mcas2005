import random 
#list of bible based questions aka dictionary 
questions = [
    {"question": "How many brothers did Joseph have?", "options":[ "1. 4", "2. 11", "3. 8"] , "answer":2}
    {"question": "what was Isaacs's wife's name?", "options" :["1. Racheal", "2. Lucy", "3. Sarah"] , "answer": 1}
    {"question": "How many disciples did Jesus have?", "options": ["1. 12", "2. 5", "3. 78"] , "answer":1},]

def ask_question(question_data):
    print("\n" + question_data["question"])
    for option in question_data["options"]:
        print(option)
    try:
        answer = int(input("Choose the correct option (1-3): "))
        if answer == question_data["answer"]:
            print("Correct!")
            return True
        else:
            print("Incorrect.")
            return False
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        return False

def quiz_game():
    score = 0
    for i, question in enumerate(questions):
        if ask_question(question):
            score += 1     
        print(f"Current Score: {score}")
    
    print(f"\nFinal Score: {score}/{len(questions)}")

if __name__ == "__main__":
    while True:
        quiz_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
