import sys
import pandas as pd
class Library:
      def __init__(self,listofbooks):
            self.availablebooks=listofbooks

      def displayAvailablebooks(self):
                   print("The books we have in our library are as follows:")
                   print("================================")
                   for book in self.availablebooks:
                         print(book)
      def borrow_Book(self,requestedBook):
            if requestedBook in self.availablebooks:
                  print("The book you requested has now been borrowed.")
                  self.availablebooks.remove(requestedBook)
            else:
                  print("Currently unavailable")
                  
      def return_Book(self,returnedBook):
            self.availablebooks.append(returnedBook)
            print("Thanks for returning your borrowed book")

      class Shelf():
       def __init__(self,catalogue):  
            self.booksinshelf=catalogue
              for book in self.booksinshelf:
                         print(book)
       def populate_book(self,book):                   
             filepath = "library.xlsx"
             df = pd.read_excel(filepath)
             og_dict = df.to_dict()
             name_dict = og_dict['Name']
             for book in name_dict:
                   self.append(Book)

            

class Student:
      def requestBook(self):
            print("Enter the name of the book you'd like to borrow>>")
            self.book=input()
            return self.book

      def returnBook(self):
            print("Enter the name of the book you'd like to return>>")
            self.book=input()
            return self.book

      def reserveBook(self):
            print("Enter the name of the book you'd like to reserve>>")
            self.book=input()
            return self.book      

def main():   
      filepath = "library.xlsx"
      df = pd.read_excel(filepath)
      og_dict = df.to_dict()
      name_dict = og_dict['Name']
  
      library=Library(["The Last Battle","The Screwtape letters","The Great Divorce"])
      shelf=Shelf(name_dict)
      student=Student()
      done=False
      while done==False:
            print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Reserve a book
                  5. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        library.displayAvailablebooks()
            elif choice==2:
                        library.borrow_Book(student.requestBook())
            elif choice==3:
                        library.return_Book(student.returnBook())
            elif choice==4:
                        library.displayAvailablebooks(student.reserveBook())
            elif choice==5:
                  sys.exit()
                  
main()