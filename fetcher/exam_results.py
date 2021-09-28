import requests
import threading


def get_result(nic):
    URL = "https://result.doenets.lk/result/service/OlResult?index=&nic={}".format(nic)
    content = requests.get(URL).text
    if "try again" not in content:
        with open("../results/{}.txt".format(nic), "w") as f:
            f.write(content)


YEARS = [200400000000]
DAYS = range(100000, 36600000, 100000)
# Uncomment following 2 lines and run again
# YEARS = [200500000000]
# DAYS = range(100000, 6100000, 100000) # Jan & Feb of 2005
GENDERS = [0, 50000000]
DAILY_BIRTHS = range(10000)

for YEAR in YEARS:
    for DAY in DAYS:
        for GENDER in GENDERS:
            threads = []
            for DAILY_BIRTH in DAILY_BIRTHS:
                nic = YEAR + DAY + GENDER + DAILY_BIRTH
                if nic % 1000 == 0:
                    for thread in threads:
                        thread.join()
                    print("Thousand complete.")
                    threads = []
                thread = threading.Thread(target=get_result, args=(nic,))
                threads.append(thread)
                thread.start()


# threads = []
# for ind in range(200426707000, 200426710000):
#     thread = threading.Thread(target=get_result, args=(ind,))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()
