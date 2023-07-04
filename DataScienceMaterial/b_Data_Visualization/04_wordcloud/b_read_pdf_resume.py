import re
from collections import Counter, defaultdict

import matplotlib.pyplot as plt
import PyPDF2
from nltk.corpus import stopwords
from wordcloud import STOPWORDS, WordCloud


def read_pdf(file_path):
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        content = []
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            content.append(page.extract_text())

        return "\n".join(content)


# Provide the path to your PDF file
pdf_path = r"D:\Personal\my_resumes\Udhay_Prakash_Python_Go_Developer.pdf"
pdf_content = read_pdf(pdf_path)
# print(pdf_content)

# Text cleaning
pdf_content = pdf_content.lower()  # Convert to lowercase
pdf_content = re.sub(r"\busing\b", "", pdf_content)  # Remove specific word 'using'

# Remove punctuation and special characters
pdf_content = re.sub(r"[^\w\s]", "", pdf_content)
pdf_content = re.sub(r"\d+", "", pdf_content)

# Tokenization
tokens = pdf_content.split()

# Stop word removal
# import nltk
# nltk.download('stopwords')
stop_words = set(STOPWORDS)
stop_words.update(set(stopwords.words("english")))
tokens = set(tokens) - stop_words

# Generate word cloud
cleaned_text = " ".join(tokens)

# Calculate word frequencies
word_freq = Counter(tokens)
# sorted_word_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
word_freq_agg = defaultdict(set)
for wd, ct in word_freq.items():
    word_freq_agg[ct].add(wd)

print(word_freq_agg)
# Print word frequencies
print("Word Frequencies:")
for freq, words in word_freq_agg.items():
    print(f"{freq:10}| {','.join(words)}")

wc = WordCloud(background_color="white").generate(pdf_content)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
