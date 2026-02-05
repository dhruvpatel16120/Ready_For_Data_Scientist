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
print("Python" in text)
print("Java" not in text)

# String Comparison
print("apple" == "apple")   # True
print("Apple" > "apple")    # False (ASCII based)

# Escape Sequences in Strings
print("Hello\nWorld")
print("Tab\tSpace")
print("Quote: \"Python\"")

# String methods
text = "  python Programming  "
sample = "hello world"
filename = "script.py"
chars = ["P", "y", "t", "h", "o", "n"]

print("Original text:", text)

# Case conversion methods
print("upper():", text.upper())
print("lower():", text.lower())
print("title():", text.title())
print("capitalize():", text.capitalize())
print("swapcase():", text.swapcase())

# Whitespace removal methods
print("strip():", text.strip())
print("lstrip():", text.lstrip())
print("rstrip():", text.rstrip())

# Search and find methods
print("find('Pro'):", text.find("Pro"))
print("rfind('g'):", text.rfind("g"))
print("index('python'):", text.index("python"))
print("count('o'):", text.count("o"))

# Replace method
print("replace():", text.replace("python", "Java"))

# Split and join methods
print("split():", sample.split())
print("rsplit():", sample.rsplit(" ", 1))
print("join():", " ".join(chars))

# String validation methods
print("isalpha():", "Python".isalpha())
print("isdigit():", "123".isdigit())
print("isalnum():", "Py123".isalnum())
print("isspace():", "   ".isspace())
print("islower():", "python".islower())
print("isupper():", "PYTHON".isupper())
print("startswith():", filename.startswith("script"))
print("endswith():", filename.endswith(".py"))

# Alignment and padding methods
print("center():", "Hi".center(10, "*"))
print("ljust():", "Hi".ljust(10, "-"))
print("rjust():", "Hi".rjust(10, "-"))
print("zfill():", "42".zfill(5))

# Encoding and formatting
print("encode():", "Python".encode())
print("format():", "My name is {}".format("Alice"))
print(f'f-strings: My file name is {filename}')

# Translation methods
table = str.maketrans("aeiou", "12345")
print("translate():", "python programming".translate(table))

# Raw Strings
normal_string = "C:\\new_folder\\test.txt"
raw_string = r"C\new_folder\test.txt"
print("Normal string:", normal_string)
print("Raw string:", raw_string)

# Unicode Strings
print("Umicode of chr(66):",chr(66))  # Greek capital letter Omega
print("order of A:",ord('A'))  # Chinese character for "middle"