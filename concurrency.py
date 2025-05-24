import threading
import time

# function that simulates the processing of a request
def process_request(request_id):
    print(f'Processing request {request_id}')
    time.sleep(3)
    print(f'Request {request_id} completed')

threads = []

for i in range (3):
    #creat new thread that will execute the function
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

# wait till all threads finish
for thread in threads:
    # makes sure the program waits for each thread to finish
    thread.join()

print('All requests completed')