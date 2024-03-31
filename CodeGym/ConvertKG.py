import tkinter as tk

def convert_weight():
    try:
        weight = float(entry.get())
        grams = weight * 1000
        pounds = weight * 2.20462
        ounces = weight * 35.274

        result_label.config(text=f"Grams: {grams:.2f}\nPounds: {pounds:.2f}\nOunces: {ounces:.2f}")
    except ValueError:
        result_label.config(text="Invalid input")

# Khởi tạo cửa sổ 
window = tk.Tk()
window.title("Weight Conversion")

# Khỏi tạo lable 
label = tk.Label(window, text="Enter weight in kilograms:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# khỏi tạo button
convert_button = tk.Button(window, text="Convert", command=convert_weight)
convert_button.pack()

result_label = tk.Label(window)
result_label.pack()

window.mainloop()