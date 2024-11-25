import threading
from time import sleep
from datetime import datetime
from threading import Thread,Lock
import random
from queue import Queue
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, "r") as file:
        for line in file:
            all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.now()
    for name in filenames:
        read_info(name)
    print(f'линейный вызов: {datetime.now() - start_time}')


    start = datetime.now()
    with Pool(4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'Многопроцессный вызов: {end - start}')