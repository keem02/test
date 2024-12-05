; # 문제 2
; """
; 도서관 관리 시스템을 만드세요.
; Book 클래스를 만들고 다음 기능을 구현하세요:
; - 책의 제목, 저자, 출판연도를 초기화하는 생성자
; - 책 정보를 출력하는 메서드
; - 책의 대여 상태를 관리하는 메서드 (대여/반납)

; 테스트 코드:
; book1 = Book("Python Programming", "John Smith", 2023)
; book1.display_info()
; book1.borrow()
; book1.return_book()
; """

# class Book:
#     def __init__(self, title, author, pub_year):
#         self.title = title
#         self.author = author
#         self.pub_year = pub_year

#    def print_title(self):
#         print(self.title)

#     def print_author(self):
#         print(self.author)

#     def print_pub_year(self):
#         print(self.pub_year)

    def borrow(self):
        if not self.is_borrowed: