import tkinter as tk
from tkinter import ttk

# Conversion factors to feet
conversion_factors = {
    'Meter': 3.28084,
    'Inch': 1 / 12,
    'Feet': 1,
    'Acre': 43560,
    'Cm': 0.0328084,
    'Mm': 0.00328084,
    'Mile': 5280,
    'Kilometre': 3280.84,
    'US Football Field': 360,
    'UK Soccer Field': 330,
    'USB Port': 0.0459318,
    'Tyrannosaurus Rex': 40.000000,
    'Banana': 0.541667,
    'Olympic Swimming Pool': 164.041995,
    'Wiener Mobile': 60.000000,
    'Blue Whale': 98.425197,
    'Hollywood Walk of Fame Star': 2.000000,
    'Great Wall of China Width': 20.000000,
    'Rubber Chicken': 1.500000,
    'Empire State Building': 1454.000000,
    'Golden Gate Bridge Width': 90.000000,
    'NBA Basketball Court': 94.000000,
    'Hockey Rink': 200.000000,
    'Slice of Bread': 0.041667,
    'Space Needle': 605.000000,
    'Average Turkish Grandmother': 5.166667,
    'Ping Pong Table': 9.000000,
    'King Size Bed': 6.666667,
    'Giraffe Neck': 6.000000,
    'Volkswagen Beetle': 13.450000,
    'Sasquatch Step': 4.000000,
    'Tennis Net Length': 42.000000,
    'London Bus': 36.083333,
    'Golf Tee': 0.008333,
    'London Double Decker Bus': 27.887760,
    'The Mona Lisa': 0.062500,
    'Grand Piano': 8.200000,
    'Standard Refrigerator': 6.000000,
    'Sneaker': 0.833333,
    'Elephant': 24.000000,
    'Bowling Pin': 0.250000,
    'Average Smartphone': 0.157480,
    'Red London Telephone Box': 8.202100,
    'Vespa Scooter': 5.250000,
    'Tennis Racquet': 2.297000,
    'Ice Cream Scoop': 0.066667,
    'Doorway': 6.888890,
    'Giant Tortoise': 4.000000,
    'Cruise Ship': 984.250000,
    'Microwave Oven': 1.500000,
    'Bicycle': 5.740157,
    'Shopping Cart': 3.280840,
    'New York City Subway Car': 51.000000,
    'Hot Dog': 0.500000,
    'Dorito': 0.125000,
    'Xbox Game Pass Card': 0.281250,
    'Chinese Takeaway Container': 0.333333,
}

def convert_units():
    # Get the user input
    number = float(number_entry.get())
    from_unit = from_combobox.get()
    to_unit = to_combobox.get()

    # Convert the input to feet first
    from_feet = number * conversion_factors[from_unit]

    # Now convert feet to the target unit
    result = from_feet / conversion_factors[to_unit]

    # Display the result
    result_label.config(text=f"{number:.0f} {from_unit} is equal to: {result:.6f} {to_unit}s")


# Set up the main window
root = tk.Tk()
root.title("Universal Converter")
root.geometry("500x250")  # Adjust window size

# Adding a label before the entry for better understanding
enter_number_label = tk.Label(root, text="Enter Number:")
enter_number_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

# Entry for the number
number_entry = tk.Entry(root, width=20)
number_entry.grid(row=0, column=1, padx=10, pady=10)

# Label and combobox for 'from' unit
from_label = tk.Label(root, text="From:")
from_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)
from_combobox = ttk.Combobox(root, values=list(conversion_factors.keys()), state="readonly", width=40)
from_combobox.grid(row=1, column=1, padx=10, pady=10)
from_combobox.set('feet')  # set default value

# Label and combobox for 'to' unit
to_label = tk.Label(root, text="To:")
to_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)
to_combobox = ttk.Combobox(root, values=list(conversion_factors.keys()), state="readonly", width=40)
to_combobox.grid(row=2, column=1, padx=10, pady=10)
to_combobox.set('US Football Field')  # set default value

# Button to perform conversion
convert_button = tk.Button(root, text="Convert", command=convert_units)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display result
result_label = tk.Label(root, text="Output:", font=("Helvetica", 12), fg="blue")
result_label.grid(row=4, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
