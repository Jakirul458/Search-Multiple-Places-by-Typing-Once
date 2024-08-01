import tkinter as tr
from tkinter import Label, Button, Text
import webbrowser

# main window
root = tr.Tk()
root.title("Search Multiple Places by Typing Once")
root.geometry("600x400")  # Set a fixed size for the window

# set background color
root.configure(bg='teal')

# for YouTube search
def search_youtube():
    query = text_input.get("1.0", tr.END).strip()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

# for Google search
def search_google():
    query = text_input.get("1.0", tr.END).strip()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Create input field, labels, and buttons with styles
Label(root, text="Enter here what you want to search for", bg='teal', fg='white', font=('Arial', 14)).pack(pady=20)
text_input = Text(root, width=50, height=2, font=('Arial', 12))
text_input.pack(pady=10)
Button(root, text="Search on Google", command=search_google, bg='white', fg='green', font=('Arial', 12), width=20).pack(pady=10)
Button(root, text="Search on YouTube", command=search_youtube, bg='white', fg='red', font=('Arial', 12), width=20).pack(pady=10)

# Run the GUI event loop
root.mainloop()
