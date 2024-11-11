import re

def extract_numbers(input_text):
    # Use regex to find all numbers after "Bug 8 Found:"
    numbers = re.findall(r"Bug 8 Found:\s(\d+)", input_text)
    print(numbers)
    return numbers

# Example input text
input_text = """
Bug 8 Found: 44621933015138949

"""

listy = extract_numbers(input_text)

