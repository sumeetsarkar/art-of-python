from threading import Thread
from github import Github


class ThreadedTask:
    """Decorator class to run target functions in different threads
    """

    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, *args):
        t = Thread(target=self.__fn, args=args)
        print(t.name)
        t.start()


# decorate func with ThreadedTask
@ThreadedTask
def make_http_call(repoName):
    Github().search_repo(repoName)


def main():
    listOfRepos = [
        'art-of-js',
        'art-of-python',
        'solarjs',
    ]
    print('Initiating threads to search for Github repositories...')
    for repo in listOfRepos:
        make_http_call(repo)
    print('Requested...')


if __name__ == '__main__':
    main()
    print('Executed after main')
