from rm_garbage import *


def main():
    file_path = "../test/SR-02-0005 - 2013.05.16 - File Notes (Public Notice Letter _ List of Abutters).txt"
    Text = []
    with open(file_path) as ocr:
        text = ocr.readlines()                     # Reading the file
        for sentence in text:
            print(sentence)
            sentence = sentence.split(' ')
            isGarbage = np.zeros(len(sentence))
            for pos in range(len(sentence)):
                if len(sentence[pos]) == 0:
                    isGarbage[pos] = 1
                    continue
                isGarbage[pos] = CheckGarbage(sentence[pos])
            sentence = [x for x, y in zip(sentence, isGarbage) if y == 0]
            if len(sentence):
                Text.append(" ".join(x for x in sentence))

if __name__ == "__main__":
    main()