import json
import re
import json

with open("input/raw-text.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)

# find ALU emails
username_pattern = r"[A-Za-z0-9._-]+"
domain_pattern = r"(?:alueducation\.com|alumni\.alueducation\.com|si\.alueducation\.com)"
email_pattern = username_pattern + "@" + domain_pattern
emails = re.findall(email_pattern, text)

print("\nALU emails found:")
print(emails)

# find card numbers
card_pattern = r"\d{4}[ -]\d{4}[ -]\d{4}[ -]\d{4}"
cards = re.findall(card_pattern, text)

print("\nCard numbers found:")
print(cards)

# check if a card number is valid
def valid_card(card):
    clean = card.replace(" ", "").replace("-", "")
    if len(clean) != 16 or not clean.isdigit():
        return False

    digits = [int(digit) for digit in clean]
    total = 0
    for position, digit in enumerate(digits):
        if position % 2 == 0:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        total += digit
    return total % 10 == 0

valid_cards = []

for card in cards:
    if valid_card(card):
        valid_cards.append(card)

print("\nValid cards:")
print(valid_cards)

# find urls
url_pattern = r"https?://[^\s]+"
urls = re.findall(url_pattern, text)

print("\nURLs found:")
print(urls)


# find phone numbers
phone_pattern = r"(?:\+\d{3}\s\d{3}\s\d{3}\s\d{3}|\d{4}\s\d{3}\s\d{3})"
phones = re.findall(phone_pattern, text)

print("\nPhone numbers found:")
print(phones)


# find hashtags
hashtag_pattern = r"#[A-Za-z0-9_]+"
hashtags = re.findall(hashtag_pattern, text)

print("\nHashtags found:")
print(hashtags)

# simple check for suspicious input
unsafe_words = ["<script>", "DROP TABLE", "DELETE FROM"]

unsafe_found = False

for word in unsafe_words:
    if word.lower() in text.lower():
        unsafe_found = True

print("\nSecurity check:")

if unsafe_found:
    print("Suspicious input found")
else:
    print("No suspicious input found")

# save the results in a json file
results = {
    "alu_emails": emails,
    "valid_cards": valid_cards,
    "urls": urls,
    "phone_numbers": phones,
    "hashtags": hashtags,
    "security_check": "Suspicious input found" if unsafe_found else "No suspicious input found"
}

with open("output/sample-output.json", "w") as file:
    json.dump(results, file, indent=4)

print("\nResults saved in output/sample-output.json")
