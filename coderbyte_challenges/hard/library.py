import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

"""
use object-oriented programming (OOP) to design a reading application, given a library of books. 
In the second half of the interview, Keith asks Kylie a dynamic programming (DP) question trying to find the max length of the longest common substring in two strings.

Online cloud reading application similar to amazon kindle 

We need help designing actual application (code that implements this)
- Users have a library of books that they can add to or remove from
- Users can set a book from their library as active.
- The reading application remembers where a user left off in  a given book
- The reading application only displays a page of text at a time in the active book.

--follow up algorithm question
- Having a variable font_size set, how would you account for increase in font when a user doesnt have good sight and 
wants to increase the font size.


class book:
    self.title = title
    self.pages = pages

class library:
    func add_book(title, pages)
    func remove_book(title)
    func set_book_status(title)
    func current_page(title)
    func display_page
    
class Reading:
    func init(self, library):
        self.library = library
        self.font_size = 12
        
    func display_page(self, page_num)
"""


class Book:
    def __init__(self, title, text, pages):
        self.title = title
        self.text = text
        self.pages = pages
        self.progress = 0

    def current_page(self):
        return self.pages[self.progress]

    def turn_page(self):
        self.progress += 1
        return self.current_page()


class Library:
    def __init__(self):
        self.library = dict()
        self.active_book = None

    def add_book(self, title, text, pages):
        new_book = Book(title, text, pages)
        self.library[title] = new_book

    def remove_book(self, title):
        self.library.pop(title)

    def set_active_book(self, title):
        if title in self.library:
            self.active_book = self.library[title]
        else:
            print("Book not in library")

class ReadingApp:
    def __init__(self, library):
        self.library = library
        self.font_size = 12

    def display_page(self, page_num):
        book = self.library.active_book
        if book is None:
            print("No active book selected")
            return
        
        text = book.text[page_num*self.font_size:(page_num+1) * self.font_size]
        print(text)

    def set_font_size(self, font_size):
        self.font_size = font_size

    def get_progress(self):
        book = self.library.active_book
        if books is None:
            print("No active book selected")
            return 
        return book.progress

    def set_progress(self, page_num):
        book = self.library.active_book
        if book is None:
            print("No active book selected")
            return
        book.progress = page_num

"""
Avoid plagiarism
- algo that detects two most likely books that pops up for potential plagiarism
- longest common shared of text, specifically wants to know how many text is been shared between the two books.

Possible way:
1. Preprocess the text data in each book to remove stop words, punctuation, and special characters, 
convert all text to lowercase, and stem or lemmatize words to their base forms.

2. For each pair of books in the library:
    a. Tokenize the text into words or n-grams.
    b. Use the longest common substring algorithm or cosine similarity to compare the text and identify shared sequences of words.
    c. Calculate the percentage of shared text by dividing the length of the shared text by the total length of the two books.
    d. If the percentage of shared text is above a certain threshold (e.g., 10%), flag the pair of books as potentially plagiarized.

3. Report the pairs of books that are flagged as potentially plagiarized, along with the level of similarity and the shared text sequences.

"""


class Library_Two:
    def __init__(self):
        self.library = {}

    def add_book(self, title, text):
        new_book = Book(title, text)
        self.library[title] = new_book

    def preprocess_text(self, text):
        # Remove punctuation and special characters
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Convert to lowercase
        text = text.lower()
        # Tokenize the text into words
        words = word_tokenize(text)
        # Remove stop words
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word not in stop_words]
        # Stem words to their base form
        stemmer = nltk.PorterStemmer()
        stemmed_words = [stemmer.stem(word) for word in filtered_words]
        # Return the preprocessed text as a string
        return " ".join(stemmed_words)

    def compare_books(self, book1, book2, threshold=0.1):
        # Preprocess the text in both books
        text1 = self.preprocess_text(book1.text)
        text2 = self.preprocess_text(book2.text)

        # Calculate the length of the longest common substring using dynamic programming
        n = len(text1)
        m = len(text2)
        LCS = [[0] * (m + 1) for i in range(n + 1)]
        max_len = 0
        max_pos = (0, 0)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i-1] == text2[j-1]:
                    LCS[i][j] = LCS[i-1][j-1] + 1
                    if LCS[i][j] > max_len:
                        max_len = LCS[i][j]
                        max_pos = (i, j)
                else:
                    LCS[i][j] = 0

        # Calculate the percentage of shared text
        total_len = len(text1) + len(text2)
        shared_len = max_len
        shared_percent = shared_len / total_len

        # If the percentage of shared text is above the threshold, return the shared text and the level of similarity
        if shared_percent > threshold:
            shared_text = text1[max_pos[0]-max_len:max_pos[0]]
            similarity = shared_percent * 100
            return (shared_text, similarity)
        else:
            return None

    def detect_plagiarism(self, threshold=0.1):
        # Loop over all pairs of books in the library
        pairs = [(book1, book2) for book1 in self.library.values() for book2 in self.library.values() if book1 != book2]
        for book1, book2 in pairs:
            # Compare the books and print any matches above the threshold
            match = self.compare_books(book1, book2, threshold)
            if match:
                print("Potential plagiarism detected between '{}' and '{}' ({}% similarity):\n{}".format(
                    book1.title, book2.title, match[1], match[0]))
