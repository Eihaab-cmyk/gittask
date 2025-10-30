import re

text = """
Contact us at support@example.com or sales@example.org.
You can also reach us at +1-800-555-1234 or (021) 9876543.
For personal queries, email john.doe99@gmail.com
"""

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'(?:\+\d{1,3}[-\s]?)?(?:\(?\d{2,4}\)?[-\s]?)?\d{3,4}[-\s]?\d{3,4}'

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

print("Emails found:")
print(emails)

print("\nPhone numbers found:")
print(phones)