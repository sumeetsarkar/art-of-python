"""
Demonstrates a simple http Get call to gihub search API
"""

import sys
import urllib.request as request
import urllib.parse
import json

# https://api.github.com/search/repositories?sort=stars&order=desc&q=repo-to-search&page=n


class Github:

    SERVICE = 'https://api.github.com'
    ENDPOINT_SEARCH = '{}/search/repositories?sort=stars&order=desc&q={}&page={}'

    def __get_request_url(self, repoName, page=1):
        repoName = urllib.parse.quote(repoName)
        return Github.ENDPOINT_SEARCH.format(Github.SERVICE, repoName, page)

    def __parse_response(self, response, encoding):
        print('\n')
        response = response.decode(encoding)
        responseJSON = json.loads(response)
        print('Total search results: ' +
              str(responseJSON['total_count']) + '\n')
        for repo in responseJSON.get('items'):
            print(repo['full_name'])
            print(repo['html_url'])
            print('Author: ' + repo['owner']['login'])
            print('stars: {0} forks: {1} issues: {2}'.format(
                str(repo['stargazers_count']), str(repo['forks']), str(repo['open_issues'])))
            print('----------------------------\n')

    def search_repo(self, repoName):
        myreq = request.Request(
            method='GET', url=self.__get_request_url(repoName))
        with request.urlopen(myreq) as r:
            print(r.status, r.reason)
            print('\nResponse Headers')
            print('----------------\n')
            print(r.headers)
            response = r.read()
            print('\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('Displaying search results for: ' + repoName)
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            self.__parse_response(response, 'utf8')


def main():
    try:
        Github().search_repo(sys.argv[1])
    except IndexError as e:
        print(e)


if __name__ == '__main__':
    main()
