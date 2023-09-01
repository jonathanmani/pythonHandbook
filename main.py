from string import capwords

def main():
    books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    key = 'C Programming Language'

    print(f'The price of {key} is ${books[key]}')



if __name__ =='__main__':
    main()