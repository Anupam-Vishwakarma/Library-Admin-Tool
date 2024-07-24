import secrets
import string
import os
import time
passkey="kri56467"
admin_name="krishna"
books = [
    "To Kill a Mockingbird",
    "1984",
    "The Great Gatsby",
    "Pride and Prejudice",
    "The Catcher in the Rye",
    "The Lord of the Rings",
    "The Hunger Games",
    "The Lion, the Witch and the Wardrobe",
    "The Da Vinci Code",
    "The Alchemist",
    "The Picture of Dorian Gray",
    "War and Peace",
    "The Adventures of Huckleberry Finn",
    "The Scarlet Letter",
    "The Count of Monte Cristo",
    "The Princess Bride",
    "The Hitchhiker's Guide to the Galaxy",
    "The Handmaid's Tale",
    "The Nightingale",
    "The Power",
    "The Song of Achilles",
    "The Poppy War",
    "The Fifth Season",
    "The Obelisk Gate",
    "The Stone Sky",
    "The House of Shattered Wings",
    "The City of Brass",
    "The Kingdom of the Blazing Phoenix",
    "The Star-Touched Queen",
    "The Winner's Curse",
    "The Darkest Part of the Forest",
    "The Glass Spare",
    "The Last Namsara",
    "The Belles",
    "The Hazel Wood",
    "The Wicked King",
    "The Queen's Rising",
    "The Warrior Heir",
    "The Iron King",
    "The Lost City of Z",
    "The Devil in the White City",
    "The Sixth Extinction",
    "The Emperor of All Maladies",
    "The Ghost Map",
    "The Immortal Life of Henrietta Lacks",
    "The Sixth Extinction",
    "The Emperor of All Maladies",
    "The Ghost Map",
    "The Immortal Life of Henrietta Lacks"
]

no_of_books=[3, 3, 3, 4, 2, 3, 1, 3, 5, 3, 5, 3, 5, 1, 3, 3, 5, 3, 2, 3, 4, 3, 3, 1, 3, 2, 4, 3, 2, 5, 4, 5, 3, 4, 5, 5, 2, 3, 3, 5, 1, 2, 4, 5, 1, 1, 2, 3, 1]

total_no_books=sum(no_of_books)

reasons_to_remove = [
    "Damaged or worn out",
    "Outdated or obsolete information",
    "Low circulation or usage",
    "Duplicate copy",
    "Inaccurate or misleading information",
    "Offensive or inappropriate content",
    "Lost or missing pages",
    "Water damage or mold",
    "Pest or rodent infestation",
    "No longer relevant to the library's collection",
    "Superseded by a newer edition",
    "Not aligned with the library's collection development policy",
    "Space constraints or storage issues",
    "Digitized version available",
    "No longer supports the curriculum or research needs",
    "Contains outdated or harmful stereotypes",
    "No longer meets the library's standards for quality or accuracy"
]
book_id=[]

def verifyyourself():
    while True:
        name=input("Enter your name:")
        your_key=input("enter your key")
        if name==admin_name and your_key==passkey:
            print("Welcome admin")
            return 0
        else:
            print("Invalid username or password")

def verify_book_id():
    while True:
        your_id=input("enter your book id: ")
        if your_id in book_id:
            book_id.remove(your_id)
            return 0
        else:
            print("this book was not issued from this library ")
            checkchoice=(input("if you have an id then  press 1 to again enter the book id or press any other key to end the program "))
            if checkchoice==1 or checkchoice=="1":
                continue
            else:
                print("Thank you !")
                exit()

def issue_book():
    verifyyourself()
    name=input("Enter the name of the book you want to issue:\n")
    if name in books:
        bookindex=books.index(name)
        no_of_books[bookindex]=no_of_books[bookindex]-1
        book_id.append(''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(5)))
        print(f"Book issued successfully\nyour book id is {book_id[-1]}")
        print("database updated successfully.")
        time.sleep(5)
    else:
        print("Book not available")
        time.sleep(2)

def add_book():
    verifyyourself()
    name=input("Enter the name of the book you are adding:\n")
    if name in books:
        bookindex=books.index(name)
        no_of_books[bookindex]=no_of_books[bookindex]+1
        print("Book already exists . one more copy of this book has been added.")
        time.sleep(3)
    else:
        books.append(name)
        no_of_books.append(1)
        print(f"{name} has been added successfully .")
        print("database updated successfully.")
        time.sleep(3)


def remove_book():
    verifyyourself()
    name=input("Enter the name of the book you want to delete:\n")
    if name in books:
        print(reasons_to_remove)
        reason=input("please write down the exact reason why are you removing this book\n(write anyone of these)")
        if(reason or reason.upper or reason.lower in reasons_to_remove):
            bookindex=books.index(name)
            books.remove(name)
            no_of_books.remove(no_of_books[bookindex])
            print("Book deleted successfully")
            print("database updated successfully.")
            time.sleep(3)           
        else:
            print("Invalid reason ! try again")
            time.sleep(2)
    else:
        print("Book not available")
        time.sleep(2)


        
def return_book():
    verifyyourself()
    name=input("Enter the name of the book you want to return:\n")
    if name in books:
        verify_book_id()
        bookindex=books.index(name)
        no_of_books[bookindex]=no_of_books[bookindex]+1
        print("Book returned successfully")
        print("database updated successfully.")
        time.sleep(2)
    else:
        print("This books was not issued from here.")
        time.sleep(2)

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to the library management system.\nPress\n")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Return a book")
        print("4. issue a book")
        print("5. total no of books")
        print("6. Exit")
        choice=int(input("Enter your choice:\n"))
        if choice==1:
            add_book()
        elif choice==2:
            remove_book()
        elif choice==3:
            return_book()
        elif choice==4:
            issue_book()
        elif choice==5:
            print(f"Total no of books: {total_no_books}")
            time.sleep(3)
        elif choice==6:
            exit()

if __name__ == "__main__":
    main()