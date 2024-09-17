try:
    with open('data.txt') as data_file:     # content manager - better way to read file than just open/close
        # if something goes wrong with opening the file, it will close the file & it will make sure the file is closed
        contents = data_file.read()     # what if the file is large
        print(contents)
except FileNotFoundError:
    print('Sorry, file not found')