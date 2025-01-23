import multiprocessing


def do_something():
    print("Doing something!")
    i = 0
    for _ in range(20000000):
        i += 1
    print("Done!", __name__)


if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    for _ in range(5):
        p = multiprocessing.Process(target=do_something, args=())
        p.start()
