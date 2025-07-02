import file_manager


def add_book():
    book_id = input("enter book id: ")
    title = input("enter book title: ")
    price = int(input("enter book price: "))
    author = input("enter book author: ")
    
    data = {
        "id": book_id,
        "title": title,
        "price": price,
        "author": author     
    }

    books = read_from_json(file="books.json")
    books.append(data)
    write_to_json(file="books.json", data= books)


def show_books():
    books = read_from_json
    
        
    

