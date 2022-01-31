# 1)Create a library class
# the default instructor takes values for
      # 1)list of books
      # 2)name of library
"""
2)define methods to display all the books
3)Define methods to lend books to the customer
4)define method to take donation book from the customer(add)
5)return book from customer


*make a dictionary to write who has taken which book
*incase anyone wants to lend a book which is taken by somebody else, tell them who has the book
"""

class Library:
      borrowed_books = {}
      def __init__(self,name,list):
            self.name = name
            self.books = list
      
      # Method to show all books
      def show_all(self):
            print(self.books)
      
      # Method to lend books
      def lend(self):
            bookName = input("Enter the book name\n")
            borrower = input("Enter your name\n")
      
            if bookName in self.borrowed_books.keys():
                  print(f"The book you are searching for is with {self.borrowed_books[bookName]}")
            elif bookName not in self.borrowed_books.keys():
                  self.borrowed_books.update({bookName:borrower})
                  print(f"{bookName} has been lended to you")
      
      # Method to return books back
      def return_books(self):
            bookName = input("Enter the book name that you want to return\n")
            tempName = self.borrowed_books[bookName]
            self.borrowed_books.pop(bookName)
            print(f"Thankyou for returning the book {tempName}")
            
      
      # Method to donate books
      def donate(self):
            print("Adding books to the shelf...\n")
            number_of_books = int(input("How many books do you want to donate\n"))
            for i in range(number_of_books):
                  bookName = input("Enter the name of the books one after another\n")
                  self.books.append(bookName)
                  print(f"{bookName} has been added to the shelf...\n")
            print("Thankyou for donating books\n")

      # Method for infinite while loop:
      def start(self):
            print(f"Welcome to {self.name} library. What would you like to do today?")
            print("1) Show books\n"
            ,"2) Lend Books\n"
            ,"3) Return Books\n"
            ,"4) Donate Books\n"
            ,"5) I am done")
           
                  

Nepalaya = Library("Nepalaya",["arcadius","asylem","R. Dad", "P.dad"])
while True:
      comd = input("press Enter to being the project\n")
      if comd == "":
            Nepalaya.start()
      comod = int(input())
      if comod ==1:
            Nepalaya.show_all()
      elif comod == 2:
            Nepalaya.lend()
      elif comod == 3:
            Nepalaya.return_books()
      elif comod == 4:
            Nepalaya.donate()
      elif comod == 5:
            # Exit the while loop
            print("Thank you for using our library")
            print("Press Ctrl C to exit")
      else:
            print("Please enter a valid option")