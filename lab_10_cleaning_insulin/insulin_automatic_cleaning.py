
insulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn" # Raw insulin Strings

# Get the length of the string
length = len(insulin)
print("Length of the string:", length)

# Print each character and its position
for index, char in enumerate(insulin):
    print(f"Character '{char}' at position {index}")

#------- here based on instruction on the lab description page, we separtate the  insulin character and assign to the variable called "isulin_separation"
insulin_separtion = [
    {"separation_range":(0,23), "file_name": "Isinsulin-seq-clean.txt"}, # each diactionary has two kye value pairs, the range of sub_insulin_string and file name
    {"separation_range": (24, 52), "file_name": "binsulin-seq-clean.txt"},
    {"separation_range": (53, 87), "file_name": "cinsulin-seq-clean.txt"},
    {"separation_range": (88, 108), "file_name": "ainsulin-seq-clean.txt"}
]
# now we have the range and file name , the below for loop iterates over the "insulin_separation list" and creates the files based on the given range 
for sub_insulin in insulin_separtion:
    start,end = sub_insulin["separation_range"]
    substring = insulin[start:end+1]
    # takes the file name from the list and put to file_name variable
    file_name = sub_insulin["file_name"]
    # open function create the files based on their names, <<with>> before the open function is to automatically handle file opens and closes during file creation
    with open(file_name, "w") as file:
        file.write(substring)
        
        print(f"The substring '{substring}' has been written to '{file_name}'. ")
    

# ---------- the above code is a short version of the this commeted code which is does the same thing and give the same result ----------#


'''  
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
'''