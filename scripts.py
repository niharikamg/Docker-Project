import os
import socket
from collections import Counter
import re

# File paths
file1 = "IF.txt"
file2 = "AlwaysRememberUsThisWay.txt"
output_file = "/home/data/output/result.txt"

# Function to read and process a file
def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()
        words = re.findall(r"\b[a-zA-Z']+\b", text)
        return words

# Count words
words_file1 = process_file(file1)
words_file2 = process_file(file2)

# Word count calculations
count_file1 = len(words_file1)
count_file2 = len(words_file2)
grand_total = count_file1 + count_file2

# Get top 3 frequent words in each file
top_words_file1 = Counter(words_file1).most_common(3)
top_words_file2 = Counter(words_file2).most_common(3)

# Get container's IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Prepare output
output_text = f"""Word Count for {file1}: {count_file1}
Word Count for {file2}: {count_file2}
Grand Total: {grand_total}

Top 3 words in {file1}: {top_words_file1}
Top 3 words in {file2}: {top_words_file2}

Container IP Address: {ip_address}
"""

# Write results to file and print to console
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, "w") as out:
    out.write(output_text)

print(output_text)
