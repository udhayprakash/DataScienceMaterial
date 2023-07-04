import re
from collections import Counter

import docx
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud


def read_docx(file_path):
    doc = docx.Document(file_path)
    paragraphs = []
    for paragraph in doc.paragraphs:
        paragraphs.append(paragraph.text)
    return "\n".join(paragraphs)


# Provide the path to your Word file
docx_path = r"D:\Personal\my_resumes\Udhay_Prakash_Python_Go_Developer.docx"
docx_content = read_docx(docx_path)

# Text cleaning
docx_content = docx_content.lower()  # Convert to lowercase
docx_content = re.sub(r"\busing\b", "", docx_content)  # Remove specific word 'using'

# Remove punctuation and special characters
docx_content = re.sub(r"[^\w\s]", "", docx_content)

# Tokenization
tokens = docx_content.split()

# Stop word removal
stop_words = set(stopwords.words("english"))
tokens = [word for word in tokens if word not in stop_words]

# Calculate word frequencies
word_freq = Counter(tokens)

# Sort word frequencies in descending order
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Print word frequencies
print("Frequency\tWord")
for word, freq in sorted_word_freq:
    print(f"{freq}\t\t{word}")

# Generate word cloud
cleaned_text = " ".join(tokens)
wc = WordCloud(background_color="white").generate(cleaned_text)

# Plot the word cloud
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
