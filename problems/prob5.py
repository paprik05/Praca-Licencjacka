import time
from multiprocessing import Process, Queue

def safe_power_worker(k, queue):
    try:
        result = (2**(2**(6*k + 2)) + 3) % 19 == 0
        queue.put(result)
    except Exception as e:
        queue.put(e)

def prob5(r, max_time=5):
    if r <= 0:
        return {"error": "r must be a positive integer"}

    results = []

    for k in range(0, r + 1):

        queue = Queue()
        p = Process(target=safe_power_worker, args=(k, queue))
        p.start()
        p.join(max_time)

        if p.is_alive():
            p.terminate()
            p.join()
            return {"result": f"{results}, timeout (potęgowanie zbyt długie)"}

        result = queue.get()
        if isinstance(result, Exception):
            continue
        if result:
            results.append(k)

    return {"result": results}
