bad_words = ['std::', '__gnu_cxx', '__gthread_active_p', "QuantLib::Date", "QuantLib::Calendar"]

with open('../cmake-build-debug/Examples/CVAIRS/amar1.txt') as oldfile, open('final.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
