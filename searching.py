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
        if seq[i:i+okno] == vz:
            poz.add(i)

    print(f"Nalezené pozice:{poz}")
    return poz



def main():
    data = read_data("sequential.json",  "dna_sequence")

    lin = linear_search(data, 1)
    # print(lin)
    pat = pattern_search(data,"ATA")



if __name__ == '__main__':
    main()