original = "practice_outliers_net_worths.pkl"
destination ="practice_outliers_net_worths_unix.pkl"
content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
    with open(destination, 'wb') as output:
        for line in content.splitlines():
            output.write(line + str.encode('\n'))