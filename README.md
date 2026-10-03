# Regex Data Extraction

This project uses Python regular expressions to extract useful information from a text file.

The program extracts:

- ALU email addresses
- Credit card numbers
- URLs
- Phone numbers
- Hashtags

It also checks credit card numbers using the Luhn algorithm and includes a simple check for suspicious input.

## Files

- `input/raw-text.txt` contains the sample text
- `src/main.py` contains the Python code
- `output/sample-output.json` contains the extracted results

## Run the program

```bash
python3 src/main.py
```

The extracted results are also saved in `output/sample-output.json`.

## ALU email validation

The program only accepts emails from:

- alueducation.com
- alumni.alueducation.com
- si.alueducation.com

## Security

A simple security check is included to look for suspicious input such as script tags or SQL commands.
