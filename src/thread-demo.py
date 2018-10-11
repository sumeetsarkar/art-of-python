from threading import Thread

def handler():
  print('running in new thread')

t = Thread(target = handler)
t.daemon = True
t.start()

print('running in main')
