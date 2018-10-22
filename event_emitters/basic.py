"""
Demonstrates a simple event emmiter
"""


class EventEmiiter:

    def __init__(self):
        # initialize empty event map
        self.__eventMap = {}

    def on(self, name, target):
        """Appends the target function in array against name key in __eventMap dict
        """
        targets = self.__eventMap.get(name, [])
        targets.append(target)
        self.__eventMap[name] = targets

    def emit(self, name, *args):
        """Calls all the target functions in array against name key in __eventMap dict
        """
        for e in self.__eventMap.get(name, []):
            callable(e) and e(*args)

    def remove_all_listeners(self, name):
        """Removes name key in __eventMap dict
        """
        self.__eventMap.pop(name, '')

    def remove_listener(self, name, target):
        """Removes specific target function for a given name key in __eventMap dict
        """
        list = []
        for e in self.__eventMap.get(name, []):
            if e is not target:
                list.append(e)
        self.__eventMap[name] = list

    def off(self, name, target):
        """Alias for remove_listener
        """
        self.remove_listener(name, target)

    def listeners(self, name):
        """Returns all the listeners currently registered for an event
        """
        return self.__eventMap.get(name, [])

    def listener_count(self, name):
        """Returns count of the listeners currently registered for an event
        """
        return len(self.listeners(name))

    def event_names(self):
        """Returns all the event names set currently registered
        """
        return self.__eventMap.keys()


# ------------------------------------------------------------------------


def on_some_event_occured(*args):
    print('on event emitted', args)


def result(*args):
    print('computation_result from result()', args[0])


def add_numbers(emitter, *args):
    sum = 0
    for n in args:
        sum += n
    # both target functions result() and some_other_result_listener()
    # will recieve the computation_result event
    emitter.emit('computation_result', sum)


def main():
    emitter = EventEmiiter()
    # registering events
    # eventA is registered 3 times
    emitter.on('eventA', on_some_event_occured)
    emitter.on('eventA', on_some_event_occured)
    emitter.on('eventA', on_some_event_occured)
    # eventB is registered 1 time
    emitter.on('eventB', on_some_event_occured)

    # events now emitted with arguments
    # eventA when emitted will result in the target function on_event_a() called thrice
    emitter.emit('eventA', 'eventA', 'data1', 'data2')
    # eventB when emitted will result in the target function on_event_b() called once
    emitter.emit('eventB')

    # a more practical illustration is below
    # computation_result is registered for 2 different target functions
    emitter.on('computation_result', result)
    emitter.on('computation_result', on_some_event_occured)
    # add_numbers is passed on the emitter to emit event upon computation completion
    add_numbers(emitter, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    # emitter removes all listeners for eventA
    emitter.remove_all_listeners('eventA')
    # since no target is registered, below emit has not effect on any target function
    emitter.emit('eventA')

    # unregister target on_some_event_occured() for event 'computation_result
    emitter.off('computation_result', on_some_event_occured)
    # call add_numbers() again now results in 'computation_result' emit only to result() target
    add_numbers(emitter, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


if __name__ == '__main__':
    main()
