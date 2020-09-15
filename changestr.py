word = "bruuh"

def main():
    print("Starting")
    rf = open("readfile.txt", "a+")
    wf = open("writefile.txt", "w+")
    rfstr = str(rf.read())
    endstr = ''
    wordsayar = 0
    a = ''
    for i in rfstr:
        if ' ' in i:
            endstr += ' '
        elif '\n' in i:
            endstr += '\n'
        else:
            wordsayar += 1

        if str(wordsayar) in a:
            wordsayar = 0
            a = ''

        a = ''.join(str(wordsayar))

        if wordsayar == 1:
            endstr += word

    wf.write(endstr)
    print(endstr)
    print("Success")

if __name__ == "__main__":
    main()