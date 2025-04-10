import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path,"r") as file:
        data = json.load(file)

    if field not in data.keys():
        return None
    else:
        ret = data[field]
        print(ret)
        return ret


def linear_search(seq,num):
    """

    :param seq:
    :param num:
    :return:
    """

    keys = ["positions", "count"]
    pos = []

    for i in range(len(seq)):
        if seq[i] == num:
            pos.append(i)
        else:
            continue

    if pos == []:
        return f"Číslo {num} se v zadaném seznamu nenachází"
    else:
        vals = [pos, len(pos)]
        ret = dict(zip(keys,vals))
        return ret


def pattern_search(seq,vz):

    okno = len(vz)
    poz = set()
    vz = vz.upper()
    for i in range(len(seq)-okno):
        j = 0
        while j < okno:
            if seq[i+j] == vz[j]:
                j += 1
            else:
                break
            if j == okno:
                poz.add(i)

    print(f"Nalezené pozice:{poz}")
    return poz


def  binary_search(numseq,num):
    lft = 0
    rght = len(numseq) - 1

    while lft <= rght:
        mid = (lft + rght) // 2
        if numseq[mid] == num:
            print(f"pozice je: {mid}")
            return mid
        elif numseq[mid] > num:
            rght = mid - 1
        else:
            lft = mid + 1




def main():
    data = read_data("sequential.json",  "dna_sequence")

    lin = linear_search(data, 1)
    # print(lin)
    pat = pattern_search(data,"ATA")

    ordered = read_data("sequential.json",  "ordered_numbers")
    print(binary_search(ordered,-1))




if __name__ == '__main__':
    main()