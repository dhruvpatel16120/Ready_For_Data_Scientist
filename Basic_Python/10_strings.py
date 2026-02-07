# strings

# Creating strings
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
triple_quote_string = '''Hello,
World!'''

# String operations
concatenation = single_quote_string + " How are you?"
repetition = single_quote_string * 3
slicing = single_quote_string[0:5]
length = len(single_quote_string)

# Membership in Strings
text = "Python Programming"
# print("Python" in text)
# print("Java" not in text)

# String Comparison
# print("apple" == "apple")   # True
# print("Apple" > "apple")    # False (ASCII based)

# Esape sequences in Python
# print("Hello\t World")  # tab space
# print("Hello\n World")  # new line
# print("Hello\\ World")  # backslash
# print("Hello\' World")  # single quote
# print("Hello\" World")  # double quote
# print("Hello\r World")  # carriage return
# print("Hello\b World")  # backspace
# print("Unicode character: \u00A9")  # Unicode character
# print("hex value: \x48\x65\x6C\x6C\x6F")  # hex value

# String methods
text = "  python programming  "
sample = " hello world"
filename = "script.py"
chars = ["p", "y", "t", "h", "o", "n"]

print("Original text:", text)

# Case conversion methods
# print("upper():", text.upper())
# print("lower():", text.lower())
# print("title():", text.title())
# print("capitalize():", sample.capitalize()) # it will capitalize and work only string[0]
# print("swapcase():", text.swapcase())

# Whitespace removal methods
# print("strip():", text.strip())
# print("lstrip():", text.lstrip())
# print("rstrip():", text.rstrip())

# Search and find methods
# print("find('Pro'):", text.find("p"))
# print("index('python'):", text.index("python"))
# print("count('o'):", text.count("o"))

# Replace method
# print("replace():", text.replace("python", "Java"))

# Split and join methods
# print("split():", sample.split())
# print("rsplit():", sample.rsplit(" ", 1))
# print("join():", " ".join(chars))

# String validation methods
# print("isalpha():", "Python".isalpha())
# print("isdigit():", "123".isdigit())
# print("isalnum():", "Py123".isalnum())
# print("isspace():", "   ".isspace())
# print("islower():", "python".islower())
# print("isupper():", "PYTHON".isupper())
# print("startswith():", filename.startswith("script"))
# print("endswith():", filename.endswith(".py"))

# Alignment and padding methods
print("center():", "Hi".center(10, "*"))
print("ljust():", "Hi".ljust(10, "-"))
print("rjust():", "Hi".rjust(10, "-"))
print("zfill():", "42".zfill(5))

# Encoding and formatting
print("encode():", "Python".encode()) # it will convert string to bytes
print("format():", "My name is {}".format("Alice")) # it will replace {} with value
print(f'f-strings: My file name is {filename}') # it will replace {} with value

# Translation methods
table = str.maketrans("aeiou", "12345")
print("translate():", "python programming".translate(table)) # it will replace aeiou with 12345

# Raw Strings
normal_string = "C:\\new_folder\\test.txt" # it will convert \\ to \ and it will be stored as C\new_folder\test.txt
raw_string = r"C\new_folder\test.txt" # it will store as it is C\new_folder\test.txt
print("Normal string:", normal_string)
print("Raw string:", raw_string)

# Unicode Strings
print("Umicode of chr(66):",chr(66))  # it will convert ASCII value 66 to character 'B'
print("order of A:",ord('A'))  # it will convert A to ASCII value 65