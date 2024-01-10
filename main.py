import self

from bookLibrary import book

book_name = input("type the book title you are finding? ")
booklet = str(book_name)


book1 = book("Parable of a dollar", "Sam Adeyemi",  "RL/2024/00001", "motivation", "010", "60", "ground floor", True)
book2 = book("China INC",  "Ted C. Fishman", "RL/2024/00002",  "business",  "020",  "30",  "10th floor",  False)
book3 = book("Americanah", "Chimamanda Adichie",  "RL/2024/00003", "Novel", "078",  "12",  "2nd floor",  True)
if booklet != book_name:
  print("Book does not exist in Library")
elif book_name == "Parable of a dollar":
  print(book)
  print(book1.book_name)
  print(book1.book_author)
  print(book1.book_serial_number)
  print(book1.book_type)
  print(book1.shelf_number)
  print(book1.room_number)
  print(book1.building_floor)
  print(book1.is_book_borrowed_returned_status)

elif book_name == "China INC":
  print(book2.book_name)
  print(book2.book_author)
  print(book2.book_serial_number)
  print(book2.book_type)
  print(book2.shelf_number)
  print(book2.room_number)
  print(book2.building_floor)
  print(book2.is_book_borrowed_returned_status)

elif book_name == "Americanah":
  print(book3.book_name)
  print(book3.book_author)
  print(book3.book_serial_number)
  print(book3.book_type)
  print(book3.shelf_number)
  print(book3.room_number)
  print(book3.building_floor)
  print(book3.is_book_borrowed_returned_status)





