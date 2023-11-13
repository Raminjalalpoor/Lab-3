import tkinter as tk
import string
import random


def generate_key(hex_input):
  """Generates a random key from the entered hexadecimal number."""
  dec_num = str(int(hex_input, 16)).zfill(5)
  options = string.ascii_uppercase + string.digits
  parts = [
      f"{dec_num[i]}{''.join(random.choices(options, k=4))}" for i in range(3)
  ]
  key = "-".join(parts + [dec_num[-2:]])
  return key


def main():
  window = tk.Tk()
  window.title("Software Key Generator")
  window.geometry('920x609')
  window.resizable(False, False)

  bg = tk.PhotoImage(file='background.png')
  my_label = tk.Label(window, image=bg)
  my_label.place(x=0, y=0)

  tk.Label(window,
           text="Enter a five-digit hexadecimal number:",
           font=("Arial", 15)).grid(row=0, column=2, columnspan=2)
  tk.Label(window, text="Generated key:",
           font=("Arial", 12)).grid(row=12, column=2, columnspan=2)

  entry = tk.Entry(window, font=("Arial", 12))
  entry.insert(0, '00000')
  entry.grid(row=1, column=3, columnspan=2)

  generated_key = tk.Label(window,
                           text="XXXXX-XXXXX-XXXXX-XX",
                           font=("Arial", 12))
  generated_key.grid(row=12, column=4, columnspan=2)

  def press():
    generated_key.config(text=generate_key(entry.get()))

  start_button = tk.Button(window,
                           text="Start",
                           font=("Arial", 15),
                           command=press)
  start_button.grid(row=5, rowspan=2, column=3, columnspan=2)

  window.mainloop()


if __name__ == "__main__":
  main()
