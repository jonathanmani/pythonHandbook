
def main():
    name = input("What's your name?")
    age = int(input(f'How old are you {name}?'))
    year = int(input('What year is it?'))

    print(f'So {name}, that means you were born in {year - age}!')


if __name__ =='__main__':
    main()