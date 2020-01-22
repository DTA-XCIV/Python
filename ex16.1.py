from sys import argv

script, filename = argv

print(f"We're going to read the {filename} file we created.")
print("To continue, press RETURN.")

input("?")

txt = open(filename, 'r')

print(txt.read())
