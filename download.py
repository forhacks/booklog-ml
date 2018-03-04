from goodreads import client
import pickle

gc = client.GoodreadsClient("ueUMoVwAkXNUPcOA4Y35yA", "R2N1HWPOdt4EEwQionNz0h3BgkY2z0yP5T3eXp8djc")

book_dict = {}


def get_book(i):
    try:
        book = gc.book(str(i))
        book_dict[i] = (book.publisher, book.description, book.average_rating)
    except:
        return None

num_threads = 2
vectors = []

for i in range(10000):
    get_book(i)
    print(i)

pickle.dump(book_dict, "data.pkl")
