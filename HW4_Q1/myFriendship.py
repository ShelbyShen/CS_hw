import myList
import myPeople
import myBooks
import MB


class myFriendship:
    def __init__(self):
        self.people = myList.myList()
        self.books = myList.myList()

    def add_people(self, person):
        self.people.append(person)

    def add_book(self, book):
        self.books.append(book)

    def get_people_list(self):
        return self.people

    def get_books_list(self):
        return self.books

    def get_info(self):
        for i in range(0, self.people.len):
            print(self.people.find(i).item)


library_one = myFriendship()
person_one = myPeople.myPeople("PersonA", 111, 6)
person_two = myPeople.myPeople("PersonB", 112, 8)
person_three = myPeople.myPeople("PersonC", 113, 9)
person_one.add_friend(person_two)
person_two.add_friend(person_one)
person_two.add_friend(person_three)
person_three.add_friend(person_one)
book_one = myBooks.myBooks("BookA", "Simon", 1)
book_two = myBooks.myBooks("BookB", "Simon", 1)
book_three = myBooks.myBooks("BookC", "Simon", 1)
book_four = myBooks.myBooks("BookD", "Simon", 1)
book_five = myBooks.myBooks("BookE", "Simon", 1)
book_six = myBooks.myBooks("BookF", "Simon", 1)
person_one.borrow_book(book_one)
person_one.borrow_book(book_two)
person_two.borrow_book(book_three)
person_two.borrow_book(book_four)
person_three.borrow_book(book_five)
person_three.borrow_book(book_six)

library_one.add_people(person_one)
library_one.add_people(person_two)
library_one.add_people(person_three)
library_one.add_book(book_one)
library_one.add_book(book_two)
library_one.add_book(book_three)
library_one.add_book(book_four)
library_one.add_book(book_five)
library_one.add_book(book_six)

person_one.return_book("BookA", 1)
library_one.get_info()

"""
SZW Work
"""
mb = MB.MB(library_one)
print("------------")
print("sort people by their names")
result = mb.sort_people(sort_by_name=True, reverse=False)
print("------------")
for n in range(0, result.len):
    print(result.find(n).item.name)

print("")

print("------------")
print("sort people by their ages")
result = mb.sort_people(sort_by_age=True, reverse=False)
print("------------")
for n in range(0, result.len):
    print(result.find(n).item.name)
    print("Age:")
    print(result.find(n).item.age)

print("")

print("------------")
print("sort people by their id")
result = mb.sort_people(sort_by_id=True, reverse=False)
print("------------")
for n in range(0, result.len):
    print(result.find(n).item.name)
    print(result.find(n).item.id)

print("")

print("------------")
print("sort people by their current owned book number")
result = mb.sort_people(sort_by_book=True, reverse=False)
print("------------")
for n in range(0, result.len):
    print(result.find(n).item.name)
    print("Owns:")
    print(result.find(n).item.current_book.len)

print("")

print("------------")
print("sort books by their title")
result = mb.sort_book(sort_by_title=True, reverse=False)
print("------------")
for n in range(0, result.len):
    print(result.find(n).item.title)

print("")

print("------------")
print("sort books by their author")
result = mb.sort_book(sort_by_author=True, reverse=False)
print("------------")
for n in range(0, result.len):
    print(result.find(n).item.title)
    print("Written by")
    print(result.find(n).item.author)

print("")
