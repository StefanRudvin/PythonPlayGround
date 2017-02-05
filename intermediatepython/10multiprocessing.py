# Python cannot use all the processing power of a cpu.

# The multiprocessing allows you to create many python processes at 16% processing power and utilise full cpu power.

import multiprocessing

def spawn(num, num2):
    print('Spawned! {0} {1}'.format(num, num2))

if __name__ == '__main__':
    for i in range(50):
        p = multiprocessing.Process(target=spawn, args=(i,i+1))
        p.start()
        #p.join()