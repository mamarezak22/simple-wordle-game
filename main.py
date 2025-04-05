import random
import sys
import time
from .words import five_letter_words


def get_input_word():
    word = input().strip().lower()
    if len(word) != 5:
        print("you must enter a 5 char word...")
        return get_input_word()
    else:
        return word 

def check_answer(answer : str,correct_answer : str)->bool:
    return answer == correct_answer
    

def show_answer_feedback(answer : str,correct_answer : str)->None:
    final_str = ""
    for i in range(len(answer)):
        if answer[i] == correct_answer[i] :
            final_str += f"\033[32m{answer[i]}\033[0m"
        elif answer[i] in correct_answer:
            final_str += f"\033[33m{answer[i]}\033[0m"
        else:
                                                   final_str += f"\033[30m{answer[i]}\033[0m"
    for char in final_str:
        print(char,end="",flush=True)                                               
        time.sleep(0.05)
    print()

        

def main():
    first_time_run = True
    if first_time_run:
        print("Welcome to the Wordle Game!")
        print("Written in holy python")
        print("You have 6 attempts to guess the correct 5-letter word.")
        print("After each guess, you will receive feedback:")
        print("G = Green (correct letter in correct position)")
        print("Y = Yellow (correct letter in wrong position)")
        print("B = Black (incorrect letter)")
        print("Let's start!")

    random_selected_word = random.choice(five_letter_words)
    chances = 6

    while chances != 0:
        user_guessed_word = get_input_word()
        if (user_guessed_word == random_selected_word):
               print("you nailed it boy...!")
               break
        show_answer_feedback(user_guessed_word,random_selected_word)
        chances-=1
    
    print("Game over!")
    print(f"the word was {random_selected_word}")
    print("")
    first_time_run = False
    play_or_not = input("would you like to play again?(y/n)")
    if play_or_not=="y":
        main()
    else:
        sys.exit(0)

        


                                                                                
if __name__ == "__main__":
        main()