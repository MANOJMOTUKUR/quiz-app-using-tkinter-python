import tkinter as tk

class QuizApp:  
    def __init__(self):
        self.quiz_data = [
            {
                "question": "what is the capital of japan ?" ,
                "options": ["tokyo", "beijing", "seoul", "bangkok"],
                "correct_answer": 0
            },
            {
                "question": "who wrote the novel pride and prejudice ?",
                "options": ["jane austen", "emily bronte", "charlotte bronte","emma stone"],
                "correct_answer": 0
            },
            {
                "question": "what is the chemical symbol for the element gold ?",
                "options": ["ag", "au", "cu", "fe"],
                "correct_answer": 1
            }
        ]
        self.current_question_index = 0
        self.score = 0

        self.window = tk.Tk()
        self.window.title("Quiz App")

        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.window, text="", command=lambda i=i: self.check_answer(i))
            button.pack()
            self.option_buttons.append(button)

        self.load_question()

        self.window.mainloop()

    def load_question(self):
        if self.current_question_index < len(self.quiz_data):
            question_data = self.quiz_data[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            options = question_data["options"]
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
        else:
            self.question_label.config(text="Quiz completed! Your score: {}/{}".format(self.score, len(self.quiz_data)))

    def check_answer(self, selected_option):
        correct_answer = self.quiz_data[self.current_question_index]["correct_answer"]
        if selected_option == correct_answer:
            self.score += 1
        self.current_question_index += 1
        self.load_question()

quiz_app = QuizApp()
