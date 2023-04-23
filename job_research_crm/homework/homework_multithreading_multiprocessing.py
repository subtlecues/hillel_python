
import threading
import multiprocessing
import datetime


def write_file(file_name):
    with open(file_name, 'a') as f:
        for i in range(100000):
            f.write(str(i) + '\n')


if __name__ == '__main__':
    start_time_threading = datetime.datetime.now()

    threading1 = threading.Thread(target=write_file, args=('threading_testfile1.txt',))
    threading2 = threading.Thread(target=write_file, args=('threading_testfile2.txt',))

    threading1.start()
    threading2.start()

    threading1.join()
    threading2.join()

    end_time_threading = datetime.datetime.now()

    print(f'Total threading method execution time: {end_time_threading - start_time_threading} seconds')

    start_time_no_threading = datetime.datetime.now()

    write_file('nothreading_testfile1.txt')
    write_file('nothreading_testfile2.txt')

    end_time_no_threading = datetime.datetime.now()

    print(f'Total single thread execution time: {end_time_no_threading - start_time_no_threading} seconds')

    start_time_multiprocessing = datetime.datetime.now()

    process1 = multiprocessing.Process(target=write_file, args=('multiprocessing_testfile1.txt',))
    process2 = multiprocessing.Process(target=write_file, args=('multiprocessing_testfile2.txt',))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end_time_multiprocessing = datetime.datetime.now()

    print(f'Total multiprocessing execution time: {end_time_multiprocessing - start_time_multiprocessing} seconds')