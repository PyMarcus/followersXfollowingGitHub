import json
import os

import requests
from requests import Response


class AreTheyFollowMe:
    followers: list = []
    following: list = []

    def __init__(self, url_base: str, token: str, endpoint: str):
        self.__url_base = url_base
        self.__token = token
        self.__endpoint = endpoint

    @property
    def url_base(self) -> str:
        return self.__url_base

    @property
    def token(self) -> str:
        return self.__token

    @property
    def endpoint(self) -> str:
        return self.__endpoint

    @endpoint.setter
    def endpoint(self, new_endpoint) -> None:
        self.__endpoint = new_endpoint

    def auth(self) -> Response:
        """
        Faz a autenticação
        :return: Response (SESSION)
        """
        print("[*] authantication...")
        session = requests.Session()
        session.headers['Authorization'] = 'token ' + self.token
        send_payload = session.post(self.url_base + self.endpoint)
        return send_payload

    def startRequest(self, **kwargs) -> str:
        """
        Faz a requisição para o endpoint seguidores e seguindo
        :param kwargs: endpoint1, endpoint2 ex: /users
        :return:
        """
        self.auth()  # inicia a sessão
        followers: Response = Response()
        if kwargs['followers']:
            print("Followers found")
            print(followers.content)
            try:
                for n in range(len(followers.content.decode())):
                    self.followers.append(dict(json.loads(followers.content.decode())[n]).get('login'))
            except IndexError:
                ...
        if kwargs['followings']:
            print('followings found')
            followings = requests.get(self.url_base + kwargs['followings'] + '?per_page=100')
            try:
                for n in range(len(followings.content.decode())):
                    self.following.append(dict(json.loads(followers.content.decode())[n]).get('login'))
            except IndexError:
                ...

    def compareUsers(self, end, end2):
        req.startRequest(followers=end, followings=end2)
        print(len(self.followers))
        print(len(self.following))
        x = set(self.followers)
        y = set(self.following)






if __name__ == '__main__':
    base: str = "api.github.com"
    os.environ['GITHUBTOKEN'] = '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'
    token: str = os.environ.get('GITHUBTOKEN')
    endpoint = '/user'
    if "/" not in endpoint:
        raise Exception("Endpoint may start with / ")
    req = AreTheyFollowMe('https://' + base, token, endpoint)
    req.compareUsers('/users/PyMarcus/followers', '/users/PyMarcus/following')