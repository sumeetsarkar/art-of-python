from threading import Thread


def handler():
    for x in range(1, 10, 1):
        print('running in new thread', x)


t = Thread(target=handler)
t.daemon = True
t.start()

print('running in main')

t.join()
