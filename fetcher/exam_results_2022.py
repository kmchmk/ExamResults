import logging
from queue import Queue
from threading import Thread
import requests

starting_index = 5000000
ending_index = 10000000
thread_count = 500
file_name = "results_2022.txt"


logging.basicConfig(filename='application.log', level=logging.INFO)


def fetch_results(url):
    response = requests.get(url)
    return response.text


def valid_result(results):
    return "Invalid Index/NIC Number" not in results


def append_to_file(results):
    try:
        file = open(file_name, "a")
        file.write(results + "\n")
        file.close()
    except:
        logging.error("Error writing file.")


def get_results(queue, index_no):
    try:
        url = f'https://result.doenets.lk/result/service/AlResult?index={index_no}&nic='
        results = fetch_results(url)
        if valid_result(results):
            logging.info(f'Results fetched for index no: {index_no}')
            queue.put(results)
        else:
            logging.info(f'Results failed for index no: {index_no}')
    except:
        logging.error(f'ERROR in index no: {index_no}')


def produce(index_queue):
    logging.info('Producer: Running')
    for index_no in range(starting_index, ending_index):
        index_queue.put(index_no)
    index_queue.put(None)    # signal that there are no further items
    logging.info('Producer: Done')


def consume(index_queue, results_queue, identifier):
    logging.info(f'Consumer {identifier}: Running')
    while True:
        index_no = index_queue.get()
        if index_no is None:  # check for stop
            index_queue.put(None)  # add the signal back for other consumers
            break
        logging.info(f'>Consumer {identifier} got {index_no}')
        get_results(results_queue, index_no)
    logging.info(f'Consumer {identifier}: Done')


def file_write(queue):
    logging.info('File writer: Running')
    while True:
        result = queue.get()
        if result is None:  # check for stop
            break
        append_to_file(result)
    logging.info('File writer: Done')


results_queue = Queue()
file_writer = Thread(target=file_write, args=(results_queue,))
file_writer.start()

index_queue = Queue()
consumers = [Thread(target=consume, args=(index_queue, results_queue, thread_no)) for thread_no in range(thread_count)]
for consumer in consumers:
    consumer.start()

producer = Thread(target=produce, args=(index_queue,))
producer.start()
producer.join()
for consumer in consumers:
    consumer.join()
results_queue.put(None)  # Finish file writing

file_writer.join()
logging.info('Everything: Done')
