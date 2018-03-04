import tensorflow
import spacy
import pandas
import pickle

nlp = spacy.load('en')
users = pandas.read_csv("to_read.csv").as_matrix()
books = pickle.load("data.pkl")

user_dict = {}
publisher_dict = {}

for user in users:
    key = user[0]
    book_id = user[1]
    if key not in user_dict:
        user_dict[key] = []
    user_dict[key].append(book_id)
    publisher_dict[books[book_id][0]] = len(publisher_dict)
    print(len(user_dict))


def get_book(i):
    try:
        book = books[book_id]
        vector = nlp(book[1]).vector
        publisher = [0] * len(publisher_dict)
        publisher[publisher_dict[book[0]]] = 1
        vector.extend(publisher)
        vector.append(book[2])
        return vector
    except Exception:
        return None

book_vectors = {}
for i in range(10000):
    book_vectors[i] = get_book(i)

connections = [[[False] * 10000] for _ in range(10000)]
for key in user_dict:
    values = user_dict[key]
    if len(values) <= 1:
        continue
    vectors = []
    for i in values:
        for j in values:
            connections[i][j] = True
            connections[j][i] = True



