from string import capwords

def main():
    book = "7 habits's of highly effective people"
    print(book.title())
    print(book.capitalize())
    print(capwords(book))


if __name__ =='__main__':
    main()