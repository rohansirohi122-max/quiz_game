import tkinter as tk
from tkinter import messagebox

# Quiz Questions
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Earth", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["J.K. Rowling", "Shakespeare", "Agatha Christie", "Charles Dickens"],
        "answer": "J.K. Rowling"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"],
        "answer": "Carbon Dioxide"
    }
]

# Main Class for Quiz Game
class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        self.question_index = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center")
        self.question_label.pack(pady=20)
        
        self.var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Arial", 12))
            btn.pack(anchor="w", padx=100, pady=5)
            self.option_buttons.append(btn)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 12), bg="blue", fg="white")
        self.next_button.pack(pady=20)
        
        self.load_question()
    
    def load_question(self):
        self.var.set(None)
        data = quiz_data[self.question_index]
        self.question_label.config(text=f"Q{self.question_index+1}: {data['question']}")
        
        for i, option in enumerate(data['options']):
            self.option_buttons[i].config(text=option, value=option)
    
    def next_question(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an option!")
            return
        
        if selected == quiz_data[self.question_index]['answer']:
            self.score += 1
        
        self.question_index += 1
        
        if self.question_index < len(quiz_data):
            self.load_question()
        else:
            self.show_result()
    
    def show_result(self):
        percentage = (self.score / len(quiz_data)) * 100
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(quiz_data)}\nPercentage: {percentage:.2f}%")
        self.root.destroy()

# Run the Game
if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()
