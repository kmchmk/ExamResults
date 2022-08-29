
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
    day_str = get_day_str(day)
    file_name = "results_{}.txt".format(day_str)
    for last_number in range(0, 1000000):
        last_number_str = get_last_number_str(last_number)
        nic = "2000{}{}".format(day_str, last_number_str)
        url = "https://result.doenets.lk/result/service/AlResult?index=&nic={}".format(nic)
        results = fetch_results(url)
        if valid_result(results):
            append_to_file(file_name, results)


def save_results_for_range(start, end):
    threads = []
    for day in range(start, end):
        thread = threading.Thread(target=get_results_for_the_day, args=(day,))
        thread.start()
        threads.append(thread)
        print("Started.")

    # Wait for everything to be finished.
    for thread in threads:
        thread.join()
        print("Thread finished")
    print("Range finished.")


def main():
    # for boys
    for i in range(37):
        save_results_for_range(i*10, (i*10)+10)
        print("All threads finished.")

    # for girls
    for i in range(37):
        save_results_for_range(500 + (i*10), 500 + (i*10) + 10)
        print("All threads finished.")


main()
