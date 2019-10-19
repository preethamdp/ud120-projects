original = "word_data.pkl"
destination ="word_data_unix.pkl"
content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
    with open(destination, 'wb') as output:
        for line in content.splitlines():
            output.write(line + str.encode('\n'))