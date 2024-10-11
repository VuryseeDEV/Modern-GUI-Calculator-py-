import customtkinter as ctk
import math

# Set appearance mode ("System" sets it to follow the OS theme)
ctk.set_appearance_mode("Dark")  # Options: "System" (default), "Dark", "Light"
# Set color theme
ctk.set_default_color_theme("blue")  # Options: "blue" (default), "dark-blue", "green"

calculation = ""

def addToCalc(symbol):
    global calculation
    if symbol == "*":
        symbol = "×"
    elif symbol == "/":
        symbol = "÷"
    
    calculation += str(symbol)
    txtResult.delete("1.0", "end") 
    txtResult.insert("1.0", calculation)

def evalCalc():
    global calculation
    try:
        calc = calculation.replace("×", "*").replace("÷", "/")
        while "√" in calc:
            index = calc.index("√")
            number_start = index + 1
            number_end = number_start
            while number_end < len(calc) and calc[number_end].isdigit():
                number_end += 1
            number = calc[number_start:number_end]
            calc = calc[:index] + str(math.sqrt(float(number))) + calc[number_end:]

        calculation = str(eval(calc))
        txtResult.delete("1.0", "end")
        txtResult.insert("1.0", calculation)
    except Exception:
        clearField()
        txtResult.insert("1.0", "Error..")

def clearField(): 
    global calculation
    calculation = ""
    txtResult.delete("1.0", "end")

def create_button(root, text, row, column, command, bg_color=None, fg_color=None, font=("Arial", 12), width=70, height=50):
    button = ctk.CTkButton(root, 
                           text=text, 
                           command=command,
                           width=70, 
                           height=60,
                           text_color=fg_color, 
                           fg_color=bg_color,
                           font=("Arial", 12)
                           )
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    return button

# Main window
root = ctk.CTk()
root.geometry("300x400")
root.configure(bg="#222326")
root.title("Modern Calculator GUI")

# Text result display
txtResult = ctk.CTkTextbox(root, 
                           height=50, 
                           width=240, 
                           font=("Arial", 18),
                           text_color="black",
                           fg_color="white"
                           )
txtResult.grid(columnspan=5, sticky="nsew")

# Configure grid layout
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Number buttons
create_button(root, "1", 2, 1, lambda: addToCalc(1), bg_color="#787673", fg_color="black")
create_button(root, "2", 2, 2, lambda: addToCalc(2), bg_color="#787673", fg_color="black")
create_button(root, "3", 2, 3, lambda: addToCalc(3), bg_color="#787673", fg_color="black")
create_button(root, "4", 3, 1, lambda: addToCalc(4), bg_color="#787673", fg_color="black")
create_button(root, "5", 3, 2, lambda: addToCalc(5), bg_color="#787673", fg_color="black")
create_button(root, "6", 3, 3, lambda: addToCalc(6), bg_color="#787673", fg_color="black")
create_button(root, "7", 4, 1, lambda: addToCalc(7), bg_color="#787673", fg_color="black")
create_button(root, "8", 4, 2, lambda: addToCalc(8), bg_color="#787673", fg_color="black")
create_button(root, "9", 4, 3, lambda: addToCalc(9), bg_color="#787673", fg_color="black")
create_button(root, "0", 5, 2, lambda: addToCalc(0), bg_color="#787673", fg_color="black")

# Operator buttons
create_button(root, "+", 2, 4, lambda: addToCalc("+"), bg_color="#474645", fg_color="black")
create_button(root, "-", 3, 4, lambda: addToCalc("-"), bg_color="#474645", fg_color="black")
create_button(root, "×", 4, 4, lambda: addToCalc("*"), bg_color="#474645", fg_color="black")
create_button(root, "÷", 5, 4, lambda: addToCalc("/"), bg_color="#474645", fg_color="black")
create_button(root, "=", 6, 3, evalCalc, bg_color="#f0ad4e", fg_color="black")
create_button(root, "√", 6, 4, lambda: addToCalc("√"), bg_color="#474645", fg_color="black")
create_button(root, "^", 5, 4, lambda: addToCalc("**"), bg_color="#474645", fg_color="black")

# Extra buttons
create_button(root, "C", 6, 1, clearField, bg_color="#787673", fg_color="black")
create_button(root, "(", 5, 1, lambda: addToCalc("("), bg_color="#787673", fg_color="black")
create_button(root, ")", 5, 3, lambda: addToCalc(")"), bg_color="#787673", fg_color="black")
create_button(root, ".", 6, 2, lambda: addToCalc("."), bg_color="#787673", fg_color="black", font=("Arial", 26, "bold"), width=60, height=50)

# Start the GUI event loop
root.mainloop()
