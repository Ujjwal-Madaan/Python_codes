# This code is based on real time library management system
# In this code library class is derived from student class so as to take all the sdetails and functionality of student class
# First of all when the student enters the values , he gives details about himself and the book is issued. He also gets the information about the issue date and return date and all this database is stored in the dictionary named book_man, so as to maintain the history of the book details. We can also extract the details of the student along with book details.
# It also gives the functionality that if gthe student returns the book late, then he will have to deposit the fine

from datetime import date
import datetime as DT

class student:
    def __init__(self, roll_no, name, year, batch, email_id):
        self.roll_no = roll_no
        self.name = name
        self.year = year
        self.batch = batch
        self.email_id = email_id

    def display_details(self, roll_no, name, year, batch, email_id):
        print('Roll_no: '+ int(roll_no))
        print('Name: '+name)
        print('Year: ' + year)
        print('Batch: ' + batch)
        print('Email_id: ' + email_id)
        

class library(student):
    book_man = {}
    
    def __init__(self, roll_no, name, year, batch, email_id, book, issue_date, return_date):
        student.__init__(self, roll_no, name, year, batch, email_id)
        self.book = book
        self.issue_date = issue_date
        self.return_date = return_date
        
        self.book_man[book] = (issue_date, return_date)

    def return_book(self, roll_no, name, issue_date, book):
        self.book_man[book] = (issue_date, date.today()) # This date.today() will enter the date of the date of that current day, when the book will be returned
        # In this the database is updated with the return date

    def get_book_details(self, book):     # To get thedetails of the book
        print('Roll no: ' + str(self.roll_no) + '.\nName: ' + self.name)
        print('Book: '+ self.book)
        print('Issue date of book: {}' .format(self.book_man[book][0]))
        print('Return date of book: {}'. format(self.book_man[book][1]))


    def check_fine(self, book, issue_date, return_date):          # Imposement of the fine
        fine = 0
        if date.today() > return_date:
            diff = date.today() - return_date
            fine = diff*5 # Cost of fine is 5 ruppees
        return fine
        
    


stud1 = library(1, 'Ujjwal', 2, 'CS10', 'abc@thapar.edu', 'Book1', date(2021,4,23), date(2021,4,23)+DT.timedelta(days=7))
stud1.get_book_details('Book1')
stud1.return_book(1, 'Ujjwal', date(2021,4,23), 'Book1')
stud1.get_book_details('Book1')



