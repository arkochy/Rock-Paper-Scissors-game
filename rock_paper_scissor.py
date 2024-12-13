from tkinter import *
import random

def playGame(choice):
    global player_wins, computer_wins, draws
    player_choice = choice.lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        result_output.delete(0, END)
        result_output.insert(0, "It's a draw!")
        draws += 1
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        result_output.delete(0, END)
        result_output.insert(0, "You win this round!")
        player_wins += 1
    else:
        result_output.delete(0, END)
        result_output.insert(0, "Computer wins this round!")
        computer_wins += 1

    score_label.config(
        text=f"Score - You: {player_wins}, Computer: {computer_wins}, Draws: {draws}"
    )

def resetGame():
    global player_wins, computer_wins, draws
    player_wins = 0
    computer_wins = 0
    draws = 0
    result_output.delete(0, END)
    computer_choice_label.config(text="Computer chose: -")
    score_label.config(text="Score - You: 0, Computer: 0, Draws: 0")


player_wins = 0
computer_wins = 0
draws = 0


root = Tk()
root.geometry("600x400")
root.title("Rock, Paper, Scissors")


Label(root, text="Rock, Paper, Scissors Game", font=("Arial", 20)).pack(pady=10)


Label(root, text="Choose your move:", font=("Arial", 14)).pack(pady=5)
frame = Frame(root)
frame.pack(pady=5)
Button(frame, text="Rock", command=lambda: playGame("rock"), bg="lightgray", font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
Button(frame, text="Paper", command=lambda: playGame("paper"), bg="lightgray", font=("Arial", 12), width=10).pack(side=LEFT, padx=10)
Button(frame, text="Scissors", command=lambda: playGame("scissors"), bg="lightgray", font=("Arial", 12), width=10).pack(side=LEFT, padx=10)


Button(root, text="Reset", command=resetGame, bg="lightblue", font=("Arial", 12)).pack(pady=10)


computer_choice_label = Label(root, text="Computer chose: -", font=("Arial", 14))
computer_choice_label.pack(pady=5)


score_label = Label(root, text="Score - You: 0, Computer: 0, Draws: 0", font=("Arial", 14))
score_label.pack(pady=5)


Label(root, text="Result:", font=("Arial", 14)).pack(pady=5)
result_output = Entry(root, font=("Arial", 12), width=50)
result_output.pack(pady=5)


mainloop()
