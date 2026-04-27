# File: 4_XML_Files.py
# Demonstration of XML file operations (.xml) using ElementTree
import xml.etree.ElementTree as ET

filename = "Level_0_Foundation/02_Python_Advanced/code/file_handling/test_file/students.xml"
 
# 1. Creating and Writing an XML file
print("--- Creating an XML file ---")
root = ET.Element("University")

student1 = ET.SubElement(root, "Student")
student1.set("id", "101")
name1 = ET.SubElement(student1, "Name")
name1.text = "Sam"
course1 = ET.SubElement(student1, "Course")
course1.text = "Python Basics"

student2 = ET.SubElement(root, "Student")
student2.set("id", "102")
name2 = ET.SubElement(student2, "Name")
name2.text = "Sara"
course2 = ET.SubElement(student2, "Course")
course2.text = "Advance Python"

# Build the tree and write to file
tree = ET.ElementTree(root)
tree.write(filename, encoding="utf-8", xml_declaration=True)
print(f"XML data written to {filename}")

# 2. Reading and Parsing an XML file
print("\n--- Reading from an XML file ---")
parsed_tree = ET.parse(filename)
parsed_root = parsed_tree.getroot()

print(f"Root tag: {parsed_root.tag}")
for student in parsed_root.findall("Student"):
    student_id = student.get("id")
    name = student.find("Name").text
    course = student.find("Course").text
    print(f"Student ID: {student_id}, Name: {name}, Course: {course}")
