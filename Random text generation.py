import random
import tkinter as tk
from tkinter import messagebox

# List of words for random text generation
words = ["AI", "design", "creative", "technology", "innovation", "future", "vision", 
         "sustainable", "impact", "experience", "learning", "development", "data", 
         "machine", "intelligence", "research", "discovery", "progress", "automation"]

def generate_random_text():
    """Generates and displays a random sentence."""
    try:
        word_count = int(word_count_entry.get())
        if word_count <= 0:
            messagebox.showwarning("Invalid Input", "Please enter a positive number!")
            return
        random_text = " ".join(random.choices(words, k=word_count)) + "."
        output_label.config(text=random_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Create GUI Window
root = tk.Tk()
root.title("Random Text Generator")
root.geometry("400x300")
root.configure(bg="white")

# Heading
title_label = tk.Label(root, text="Random Text Generator", font=("Arial", 14, "bold"), bg="white")
title_label.pack(pady=10)

# Input: Number of Words
word_count_label = tk.Label(root, text="Enter number of words:", font=("Arial", 10), bg="white")
word_count_label.pack()
word_count_entry = tk.Entry(root, font=("Arial", 12))
word_count_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", 
                            command=generate_random_text)
generate_button.pack(pady=10)

# Output Label
output_label = tk.Label(root, text="", font=("Arial", 12, "italic"), wraplength=350, bg="white", fg="black")
output_label.pack(pady=10)

# Run the GUI
root.mainloop()
