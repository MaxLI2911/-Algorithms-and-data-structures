import matplotlib.pyplot as plt
import time
import gc
from src.sort_algorithms import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort
)

words_to_sort = range(0, 10001, 100)
bubble_sort_times = []
selection_sort_times = []
insertion_sort_times = []
merge_sort_times = []
quick_sort_times = []


def measure_time(sort_function, arr: list):
    gc_old = gc.isenabled()
    gc.disable()

    start = time.process_time()

    sort_function(arr)

    stop = time.process_time()
    if gc_old:
        gc.enable()

    return stop - start


def read_file(filename="pan-tadeusz.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            return text.split()
    except FileNotFoundError:
        print('File not found')
        exit()


def draw_charts():
    fig, ax = plt.subplots(2, 3, constrained_layout=True, figsize=(16, 9))

    # Bubble sort
    ax[0, 0].plot(words_to_sort, bubble_sort_times)
    ax[0, 0].set(
        xlabel="Liczba elementów",
        ylabel="Czas (s)",
        title="Sortowanie bąbelkowe",
    )
    ax[0, 0].grid()

    # Selection sort
    ax[0, 1].plot(words_to_sort, selection_sort_times)
    ax[0, 1].set(
        xlabel="Liczba elementów",
        ylabel="Czas (s)",
        title="Sortowanie przez wybieranie",
    )
    ax[0, 1].grid()

    # Insertion sort
    ax[0, 2].plot(words_to_sort, insertion_sort_times)
    ax[0, 2].set(
        xlabel="Liczba elementów",
        ylabel="Czas (s)",
        title="Sortowanie przez wstawianie",
    )
    ax[0, 2].grid()

    # Merge sort
    ax[1, 0].plot(words_to_sort, merge_sort_times)
    ax[1, 0].set(
        xlabel="Liczba elementów",
        ylabel="Czas (s)",
        title="Sortowanie przez scalanie",
    )
    ax[1, 0].grid()

    # Quick sort
    ax[1, 1].plot(words_to_sort, quick_sort_times)
    ax[1, 1].set(
        xlabel="Liczba elementów",
        ylabel="Czas (s)",
        title="Sortowanie szybkie",
    )
    ax[1, 1].grid()

    # All sorts
    ax[1, 2].plot(words_to_sort, bubble_sort_times, label="Bubble sort")
    ax[1, 2].plot(words_to_sort, selection_sort_times, label="Selection sort")
    ax[1, 2].plot(words_to_sort, insertion_sort_times, label="Insertion sort")
    ax[1, 2].plot(words_to_sort, merge_sort_times, label="Merge sort")
    ax[1, 2].plot(words_to_sort, quick_sort_times, label="Quick sort")
    ax[1, 2].legend()
    ax[1, 2].set(
        xlabel="Liczba elementów",
        ylabel="Czas (s)",
        title="Wszystkie sortowania",
    )
    ax[1, 2].grid()

    fig.savefig("sorting_times.png")


def main():
    print("Starting main")
    text_to_sort = read_file()
    for words in words_to_sort:
        arr = text_to_sort[:words]
        bubble_sort_times.append(measure_time(bubble_sort, arr))
        selection_sort_times.append(measure_time(selection_sort, arr))
        insertion_sort_times.append(measure_time(insertion_sort, arr))
        merge_sort_times.append(measure_time(merge_sort, arr))
        quick_sort_times.append(measure_time(quick_sort, arr))
        print(f"Finished loop for {words} words")
    print("Drawing plot...")
    draw_charts()


if __name__ == "__main__":
    main()
