st = input("Enter a letter to get its binary representation in base 2: ")
print(' '.join(format(ord(x), 'b') for x in st)) #convert and print
