import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import openai

load_dotenv()
api_key = os.getenv("API_KEY")

def generate_email(sender_name, receiver_name, purpose, max_word_limit, word_limit, special_things):
    prompt = f"Compose an email from {sender_name} to {receiver_name} under {word_limit} words.\n\nPurpose: {purpose}\n\nSpecial things to mention: {special_things}\n\n"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=max_word_limit,
        api_key=api_key
    )
    return response.choices[0].text

def generate_button_clicked():
    sender = sender_entry.get()
    receiver = receiver_entry.get()
    email_purpose = purpose_entry.get()
    max_word_limit = 400
    word_limit = int(word_limit_entry.get())
    special_notes = special_notes_entry.get("1.0", tk.END).strip()

    generated_email = generate_email(sender, receiver, email_purpose, max_word_limit, word_limit, special_notes)
    generated_email_text.config(state=tk.NORMAL)
    generated_email_text.delete(1.0, tk.END)
    generated_email_text.insert(tk.END, generated_email)
    generated_email_text.config(state=tk.DISABLED)

# Create main window
window = tk.Tk()
window.title("Email Generator")

# Create and place widgets
sender_label = ttk.Label(window, text="Sender:")
sender_entry = ttk.Entry(window)

receiver_label = ttk.Label(window, text="Receiver:")
receiver_entry = ttk.Entry(window)

purpose_label = ttk.Label(window, text="Email Purpose:")
purpose_entry = ttk.Entry(window)

word_limit_label = ttk.Label(window, text="Word Limit:")
word_limit_entry = ttk.Entry(window)

special_notes_label = ttk.Label(window, text="Special Notes:")
special_notes_entry = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=5)

generate_button = ttk.Button(window, text="Generate Email", command=generate_button_clicked)

generated_email_text_label = ttk.Label(window, text="Generated Email:")
generated_email_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=10, state=tk.DISABLED)

# Place widgets in grid
sender_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
sender_entry.grid(row=0, column=1, padx=5, pady=5)

receiver_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
receiver_entry.grid(row=1, column=1, padx=5, pady=5)

purpose_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
purpose_entry.grid(row=2, column=1, padx=5, pady=5)

word_limit_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
word_limit_entry.grid(row=3, column=1, padx=5, pady=5)

special_notes_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
special_notes_entry.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

generate_button.grid(row=5, column=0, columnspan=2, pady=10)

generated_email_text_label.grid(row=6, column=0, columnspan=2, pady=5)
generated_email_text.grid(row=7, column=0, columnspan=2, pady=5)

# Run the main loop
window.mainloop()
