from rm_garbage import *


def main():
    file_name = "SR-02-0005 - 2013.03.29 - LOR - Short-Term Response.txt"
    read_path = "./data/ocred_txt/"
    write_path = "./data/cleaned_txt/"
    Text = []
    with open(read_path+file_name) as ocr:
        text = ocr.readlines()        # Readin the file
        for sentence in text:
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
        
    # print(Text)
    with open(write_path+file_name, "w") as f:
        f.write(' '.join(Text))
        print("Rm_garbage completed for file", file_name)

if __name__ == "__main__":
    main()