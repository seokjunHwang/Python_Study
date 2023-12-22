from multiprocessing import Process, Queue

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total) # Save result(= Queue) / .put :  Queue method
    return

if __name__ == "__main__":
    START, END = 0, 100000000
    result_queue = Queue()
    pr1 = Process(target=work, args=(1, START, END//2, result_queue))
    pr2 = Process(target=work, args=(2, END//2, END, result_queue))

    pr1.start()     # Start each process
    pr2.start()
    pr1.join()      # Wait for pc1 to complete
    pr2.join()

    # put 'STOP' message to 'result_queue' Queue
    result_queue.put('STOP') 
    total = 0

    # while 루프를 사용하여 큐에서 결과를 꺼내어 합산 
    while True:
        tmp = result_queue.get()
        if tmp == 'STOP':     # 'STOP' 신호를 만나면 루프 closing
            break
        else:
            total += tmp
    print(f"result_queue: {total}")
    
