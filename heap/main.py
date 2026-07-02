import matplotlib.pyplot as plt
import gc
from time import process_time
from random import randint
from heap import Heaps

size_to_test = range(10000, 100001, 10000)
numbers = [randint(1, 300000) for _ in range(100000)]

make_heap2_times = []
make_heap5_times = []
make_heap7_times = []

delete_heap2_times = []
delete_heap5_times = []
delete_heap7_times = []


def draw_plots():
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.plot(size_to_test, make_heap2_times, label="Kopiec 2-arny")
    ax.plot(size_to_test, make_heap5_times, label="Kopiec 5-arny")
    ax.plot(size_to_test, make_heap7_times, label="Kopiec 7-arny")
    ax.legend()
    ax.set(
        xlabel="Liczba elementów",
        ylabel="Czas (s)",
        title="Tworzenie kopca",
    )
    ax.grid()
    fig.savefig("creating_heaps.png")

    fig, ax = plt.subplots(figsize=(16, 9))
    ax.plot(size_to_test, delete_heap2_times, label="Kopiec 2-arny")
    ax.plot(size_to_test, delete_heap5_times, label="Kopiec 5-arny")
    ax.plot(size_to_test, delete_heap7_times, label="Kopiec 7-arny")
    ax.legend()
    ax.set(
        xlabel="Liczba elementów",
        ylabel="Czas (s)",
        title="Usuwanie elementu maksymalnego",
    )
    ax.grid()
    fig.savefig("deleting_max_heaps.png")


def measure_time_make(heap: Heaps, size):
    start_time = process_time()
    for number in numbers[:size]:
        heap.push(number)
    stop_time = process_time()
    gc.collect()
    return stop_time - start_time


def measure_time_delete(heap: Heaps, size):
    start_time = process_time()
    for i in range(size):
        heap.delete_peak()
    stop_time = process_time()
    gc.collect()
    return stop_time - start_time


def main():
    gc_old = gc.isenabled()
    gc.disable()
    for size in size_to_test:
        heap2 = Heaps(2)
        heap5 = Heaps(5)
        heap7 = Heaps(7)
        print("Size:", size)

        make_heap2_times.append(measure_time_make(heap2, size))
        delete_heap2_times.append(measure_time_delete(heap2, size))

        make_heap5_times.append(measure_time_make(heap5, size))
        delete_heap5_times.append(measure_time_delete(heap5, size))

        make_heap7_times.append(measure_time_make(heap7, size))
        delete_heap7_times.append(measure_time_delete(heap7, size))
    if gc_old:
        gc.enable()
    draw_plots()


if __name__ == "__main__":
    main()
