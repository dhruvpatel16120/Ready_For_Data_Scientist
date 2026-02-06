import re

def regex_demo():
    print("--- Python Regular Expressions (re) ---")
    
    text = "Contact us at support@example.com or sales@company.org. Phone: +1-555-0199"

    # 1. re.findall() - Finding all occurrences
    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    print(f"Emails found: {emails}")

    # 2. re.search() - Finding the first occurrence
    phone_pattern = r'\+\d{1}-\d{3}-\d{4}'
    match = re.search(phone_pattern, text)
    if match:
        print(f"Phone number found: {match.group()}")

    # 3. re.sub() - Replacing text
    # Hide email addresses for privacy
    hidden_text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[HIDDEN EMAIL]', text)
    print(f"Sanitized text: {hidden_text}")

    # 4. Compiled patterns (more efficient for repeated use)
    pattern = re.compile(r'\d+')
    numbers = pattern.findall("There are 10 types of people, those who know binary and 2 others.")
    print(f"Numbers found: {numbers}")

    print("\nRegex demo completed.\n")

if __name__ == "__main__":
    regex_demo()
