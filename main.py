import tkinter as tk
import random
import time

#programmer : aria pourmand
#instagram : @aria.pmd
#telegram : @ariapmd
#ariapour77@gmail.com 


class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Math Game")
        self.master.geometry("400x300")

        # initialize variables
        self.score = 0
        self.answer = None
        self.timer_running = False
        self.seconds_left = 30

        # create widgets
        self.question_label = tk.Label(self.master, text="")
        self.answer_entry = tk.Entry(self.master)
        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer)
        self.score_label = tk.Label(self.master, text=f"Score: {self.score}")
        self.timer_label = tk.Label(self.master, text=f"Time Left: {self.seconds_left}")

        # add widgets to window
        self.question_label.pack(pady=10)
        self.answer_entry.pack(pady=5)
        self.submit_button.pack(pady=5)
        self.score_label.pack(pady=5)
        self.timer_label.pack(pady=5)

        # start game
        self.generate_question()
        self.start_timer()

    def generate_question(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*"])
        if operator == "+":
            self.answer = num1 + num2
        elif operator == "-":
            self.answer = num1 - num2
        elif operator == "*":
            self.answer = num1 * num2
        self.question_label.configure(text=f"What is {num1} {operator} {num2}?")

    def check_answer(self):
        try:
            guess = int(self.answer_entry.get())
        except ValueError:
            return
        if guess == self.answer:
            self.score += 1
            self.score_label.configure(text=f"Score: {self.score}")
            self.master.configure(background="green")
            self.master.after(2000, self.reset_background_color)
            self.generate_question()
            self.seconds_left += 5
            self.timer_label.configure(text=f"Time Left: {self.seconds_left}")
        else:
            self.score -= 1
            self.score_label.configure(text=f"Score: {self.score}")
            self.master.configure(background="red")
            self.master.after(2000, self.reset_background_color)
            if self.seconds_left < 0:
                self.seconds_left = 0
            self.timer_label.configure(text=f"Time Left: {self.seconds_left}")
        self.answer_entry.delete(0, tk.END)

    def start_timer(self):
        self.timer_running = True
        self.countdown()

    def countdown(self):
        if self.timer_running:
            self.seconds_left -= 1
            self.timer_label.configure(text=f"Time Left: {self.seconds_left}")
            if self.seconds_left == 0:
                self.timer_running = False
                self.game_over()
            else:
                self.master.after(1000, self.countdown)

    def game_over(self):
        self.question_label.configure(text=f"Game Over! Your score is {self.score}")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.configure(state="disabled")
        self.submit_button.configure(state="disabled")

    def reset_background_color(self):
        self.master.configure(background="white")


if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
