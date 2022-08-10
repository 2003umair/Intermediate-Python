import multiprocessing

def process(num,num2):
    print('Multiprocessing! {}'.format(num,num2))

if __name__ == '__main__':
    for x in range(45):
        p = multiprocessing.Process(target=process, args=(x,x+1))
        p.start()
       # p.join
