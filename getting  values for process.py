from multiprocessing import Pool

def work(num):
    return num * 5

if __name__ == '__main__':
    x = Pool(processes=10)
    info = x.map(work, range(11))
    info2 = x.map(work, [6,2])
    x.close()
    print(info)
    print(info2)    