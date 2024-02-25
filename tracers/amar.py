bad_words = ['/usr/include', "/usr/lib/gcc"]

with open('includefull.txt') as oldfile, open('include.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
