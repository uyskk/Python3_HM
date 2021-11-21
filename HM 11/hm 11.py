# Реализовать решение следующей задачи: 
# «Есть два писателя, которые по очереди в течении 
# определенного времени (у каждого разное) пишут в одну книгу. 
# Данная книга очень популярна, у неё есть как минимум 3 фаната (читателя), 
# которые ждут не дождутся, чтобы прочитать новые записи из неё. Каждый читатель и писатель – отдельный поток. 
# Одновременно книгу может читать несколько читателей, но писать единовременно может только один писатель.»

# *Дополнительно:
# Реализовать решение «Задачи об обедающих философах»

import time
from threading import Thread, Event, get_ident, BoundedSemaphore
import threading

event = Event()
bs = BoundedSemaphore(2)
variable = [1, 2, 2, 3, 3, 4, 4, 5, 5, 1]
mutex = threading.Lock()

s = [0, 0]
k = [0, 0]
ko = [0, 0]
va = [0, 0]
p = [0, 0]
'''Это проверка все ли поели'''


def sokrat(interval):
    while True:
        bs.acquire()
        if variable[0] == 1:
            print("Сократ говорит: Я выпью вина и заем это спагети")
            variable.append(variable.pop(0))
            bs.release()
            s[0] += 1
            time.sleep(interval)


        else:
            print("Сократ говорит: Я думаю наш метод не идеален")
            bs.release()
            s[1] += 1
            time.sleep(interval)


def kant(interval):
    while True:
        bs.acquire()
        if variable[0] == 2:
            print("Кант говорит: Я выкурю трубку и поем")
            variable.append(variable.pop(0))
            bs.release()
            k[0] += 1
            time.sleep(interval)

        else:
            print("Кант говорит: Интуиция подсказывает что метод не идеален")
            bs.release()
            k[1] += 1
            time.sleep(interval)


def konfuci(interval):
    while True:
        bs.acquire()
        if variable[0] == 3:
            print("Конфуций говорит: Принесите чаю и палочки я буду есть")
            variable.append(variable.pop(0))
            bs.release()
            ko[0] += 1
            time.sleep(interval)

        else:
            print("Конфуций говорит: Я жду своей очереди это идеальный метод")
            bs.release()
            ko[1] += 1
            time.sleep(interval)


def vacia(interval):
    while True:
        bs.acquire()
        if variable[0] == 4:
            print("Вася говорит: Есть чё? Макароны по флотски отлично")
            variable.append(variable.pop(0))
            bs.release()
            va[0] += 1
            time.sleep(interval)

        else:
            print("Вася говорит: Я думаю мы всего лишь потоки...и даже не сознания")
            bs.release()
            va[1] += 1
            time.sleep(interval)


def platon(interval):
    while True:
        bs.acquire()
        if variable[0] == 5:
            print("Платон говорит: Диалоги хорошо но я лучше поем")
            variable.append(variable.pop(0))
            bs.release()
            p[0] += 1
            time.sleep(interval)

        else:
            print("Платон говорит: Я думаю наш метод не идеален")
            bs.release()
            p[1] += 1
            time.sleep(interval)


def static(interval):
    while True:
        print(variable)
        print(s, k, ko, va, p)
        time.sleep(interval)


if __name__ == '__main__':
    thread1 = threading.Thread(target=sokrat, args=(0.1,))
    thread2 = threading.Thread(target=kant, args=(0.1,))
    thread3 = threading.Thread(target=konfuci, args=(0.1,))
    thread4 = threading.Thread(target=vacia, args=(0.1,))
    thread5 = threading.Thread(target=platon, args=(0.1,))
    static_thread = threading.Thread(target=static, args=(30,))  # Поток проверки все ли поели и подумали

    threads = [thread1, thread5, thread4, thread3, thread2, static_thread]

    for t in threads:
        t.start()
    for t in threads:
        t.join()
