class Library:
    
    def __init__(self,booklist):
        self.books =booklist
    def displaybooksavailable(self):
        print("Books present in library are")
        for book in self.books:
            print(book)
    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"you have been issued the book named{bookname}")
            self.books.remove(bookname)
            return True
        else:
            print("book is already issues sorry! or the book is unavailable ")
            return False
    def returnBook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning the book")

class Student:
    def requestBook(self):
        self.books=input("enter the name of book you want to issue:  ")
        return self.books
    def returnBook(self):
        self.books=input("enter the name of book you want to return:  ")
        return self.books

if __name__=="__main__":
    schoolLibrary=Library(["Software testing","Data mining", "PPLE","DAI","MOOC","PROJECTS"])
    student=Student()
    #schoolLibrary.displaybooksavailable()
    while(True):
        message='''  Welcome to school library,Please choose following options
        1. list all booknames
        2. Issue a book
        3. Return a book or add a book 
        4. Exit the library
        '''
        
        print(message)
        a= int(input("Enter your choice:"))
        if a==1:
            schoolLibrary.displaybooksavailable()
        elif a==2:
            schoolLibrary.borrowBook(student.requestBook())
        elif a==3:
            schoolLibrary.returnBook(student.returnBook())
        elif a==4:
            print("THANK YOU")
            exit()
        else:
            print("Invalid choice")




    


