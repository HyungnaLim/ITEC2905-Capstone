numbers = ['one', 'two', 'three']

try:
    # write file with w mode
    with open('numbers.txt', 'w') as number_file:
        for n in numbers:
            number_file.write(n + '\n')

    # append file with a mode
    with open('numbers.txt', 'a') as number_file:
        for n in numbers:
            number_file.write(n + '\n')
except OSError:
    print('Error writing to file. Operating system error.')
