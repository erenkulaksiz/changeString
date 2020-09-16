import sys

# Mode 0 : word mode
# Mode 1 : i cant name this mode but it changes wOrDs LiKe ThIs
mode = 1

# Word for mode 0
word = "bruh"

def reverse(args):
    return not args

def main():
    if(mode == 0):
    #since python does not have switch case, i should use if else statement
        print("Starting mode",mode)
        rf = open("readfile.txt", "r+")
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
    elif(mode == 1):
        print("Starting mode",mode)
        rf = open("readfile.txt", "r+")
        wf = open("writefile.txt", "w+")
        rfstr = str(rf.read())
        endstr = ''
        isputletter = False
        for i in rfstr:
            if ' ' in i:
                endstr += ' '
            else:
                isputletter = reverse(isputletter)

            if isputletter:
                endstr += i.lower()
            else:
                endstr += i.upper()
        wf.write(endstr)
        print(endstr)
        print("Success")
    else:
        print("Invalid mode")
        sys.exit()

if __name__ == "__main__":
    main()