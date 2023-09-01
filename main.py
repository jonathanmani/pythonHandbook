from string import capwords

def main():
    numbers = [1,3,5,6,7,8,10,24,56,67]

    even_numbers = filter(lambda item:  True if item % 2 == 0 else False, numbers)

    print(list(even_numbers))



if __name__ =='__main__':
    main()