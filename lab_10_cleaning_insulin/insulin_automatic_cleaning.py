
insulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn" # Raw insulin Strings

# Get the length of the string
length = len(insulin)
print("Length of the string:", length)

# Print each character and its position
for index, char in enumerate(insulin):
    print(f"Character '{char}' at position {index}")

# Extract substring from position 0 to 24
substring = insulin[0:23]  # Extracts characters from index 0 to index 24 (inclusive)

# Write the substring to another file
Is_clean = "Isinsulin-seq-clean.txt"

with open(Is_clean, "w") as file:
    file.write(substring)

print(f"The substring '{substring}' has been written to '{Is_clean}'.")

# Extract substring from position 24 to 53
substring = insulin[24:53]  # Extracts characters from index 24 to index 53 (inclusive)

# Write the substring to another file
b_clean = "binsulin-seq-clean.txt"

with open(b_clean, "w") as file:
    file.write(substring)

print(f"The substring '{substring}' has been written to '{b_clean}'.")
#--------- second cleaning/ separation --------

substring = insulin[54:88]  # Extracts characters from index 54 to index 88 (inclusive)

# Write the substring to another file
c_clean = "cinsulin-seq-clean.txt"

with open(c_clean, "w") as file:
    file.write(substring)

print(f"The substring '{substring}' has been written to '{c_clean}'.")

#--------- third cleaning/ separation --------

substring = insulin[89:109]  # Extracts characters from index 89 to index 109 (inclusive)

# Write the substring to another file
a_clean = "ainsulin-seq-clean.txt"

with open(a_clean, "w") as file:
    file.write(substring)

print(f"The substring '{substring}' has been written to '{a_clean}'.")