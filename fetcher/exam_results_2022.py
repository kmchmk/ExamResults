#!/usr/bin/python3


import threading
import requests


def prefix_zeros(number, length_should_be):
    diff = length_should_be - len(str(number))
    return ("0"*diff) + str(number)


def get_day_str(day):
    length_should_be = 3
    return prefix_zeros(day, length_should_be)


def get_last_number_str(last_number):
    length_should_be = 5
    return prefix_zeros(last_number, length_should_be)


def fetch_results(url):
    response = requests.get(url)
    return response.text


def valid_result(results):
    return "Invalid Index/NIC Number" not in results


def append_to_file(file_name, results):
    file = open(file_name, "a")
    file.write(results + "\n")
    file.close()


def get_results_for_the_day(day):
    try:
        day_str = get_day_str(day)
        file_name = "results_{}.txt".format(day_str)
        for last_number in range(0, 1000000):
            last_number_str = get_last_number_str(last_number)
            nic = "2000{}{}".format(day_str, last_number_str)
            url = "https://result.doenets.lk/result/service/AlResult?index=&nic={}".format(nic)
            results = fetch_results(url)
            if valid_result(results):
                append_to_file(file_name, results)
                print(nic, "Successful.", flush=True)
            else:
                print(nic, "Failed", flush=True)
    except:
        print("ERROR in", day, flush=True)


def save_results_for_range(start, end):
    threads = []
    for day in range(start, end):
        thread = threading.Thread(target=get_results_for_the_day, args=(day,))
        thread.start()
        threads.append(thread)
        print("Started.", flush=True)

    # Wait for everything to be finished.
    for thread in threads:
        thread.join()
        print("Thread finished", flush=True)
    print("Range finished.", flush=True)


def main():
    step = 100
    # for boys
    for i in range((366//step) + 1):
        save_results_for_range(i*step, (i*step)+step)
        print("All threads finished.", flush=True)

    # for girls
    for i in range((366//step) + 1):
        save_results_for_range(500 + (i*step), 500 + (i*step) + step)
        print("All threads finished.", flush=True)


main()
