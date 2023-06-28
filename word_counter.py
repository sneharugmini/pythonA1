"""
This code counts the frequency of each word in the sample text names as sample.txt file in the directory. After counting it saves and creates a new txt file with the word frequency report in it.
"""
import os

def count_word_frequency(file_path): #counts the word frequency
    word_frequency = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.lower()
                word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency

def save_report(file_path, word_frequency): #Saves the word frequency
    sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    report = "Word\t\tFrequency\n"
    for word, frequency in sorted_words:
        report += f"{word}\t|\t{frequency}\n"
    with open(file_path, 'w') as file:
        file.write(report)

# File paths
text_file_path = "sample.txt"
report_file_path = "word_frequency_report.txt"

# Count word frequency
word_frequency = count_word_frequency(text_file_path)

# Save it
save_report(report_file_path, word_frequency)

# Print success message.
print(f"Word frequency report is successfully saved as: {os.path.abspath(report_file_path)}")
