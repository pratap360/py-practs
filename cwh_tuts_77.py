# code with harry tuts 77
# coroutines in python

def searcher():
    import time 
    # some 4 seconds time consuming task
    book="this is a book, purchased from a book shop and i have to give it to bapi"
    time.sleep(4)

while True:
    text=(yield)
    if text in book:
        print("your text is in the book")
    else:
        print("text is not in the book")

search = searcher()
next(search)
print("next method run")
search.send("book")
search.close()


# input("press any key")
# search.send("bapi")
# input("press any key")
# search.send("shop")
# input("press any key")
# search.send("liked")
# input("press any key")


