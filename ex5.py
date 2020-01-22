name = 'Danny Tan'
age = 24 # nog heel jong
height_cm= 1.88e2# cm
inch = 39.37e-2
height_inches = height_cm * inch
weight_kg= 80.0 # kg
pound = 0.22e1
weight_pounds = weight_kg * pound

eyes = 'Bruin'
teeth = 'Wit'
hair = 'Zwart'

print(f"Let's talk about {name}.")
print(f"He's", round(height_inches)," inches tall.")
print(f"He's {weight_pounds} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height_inches + weight_pounds
print(f"If I add {age}", round(height_inches),f" and {weight_pounds} I get {total}.")
