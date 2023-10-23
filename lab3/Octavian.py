

# Press the green button in the gutter to run the script.
def solutie(fname):
    f = open(fname, 'r')
    data = f.read()
    count = 0
    i=0
    while i<len(data):
        word=""
        special="ăĂîÎâÂșȘțȚçÇÑñáÁéÉíÍóÓúÚà"
        if (data[i] >= 'a' and data[i] <= 'z') or (data[i] >= 'A' and data[i] <= 'Z') or data[i] in special:
            j = i + 1
            word+=(data[i])
            while j < len(data) and ( (data[j] >= 'a' and data[j] <= 'z') or (data[j] >= 'A' and data[j] <= 'Z') or data[j] in special) :
                word += (data[j])
                j = j + 1
            count = count + 1
            i=j

        i+=1
    return count

def name():
    return "Octavian"


if __name__ == '__main__':
    fname = 'C:/Users/Octavian/OneDrive/Documents/info/python/lab3.1/input/f3.txt'

    print(solutie(fname))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
