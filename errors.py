import asyncio
import aiohttp
import requests

suspicious_words = [
    'nginx',
    'Apache',
    'Tomcat',
]

headers = {
    'User-Agent': 'nopsled',
}


class Base:
    context_path = ''
    data = dict()
    name: str = ''
    method = 'GET'
    status: int = 0
    headers = headers
    result = dict()

    @classmethod
    def show(cls):
        r = cls.result
        detected_suspicious = ['Suspicious word:\r\n']
        status = f"STATUS: {'✅' if r['success'] else '❌'} ({r['before_status']} -> {r['after_status']})"
        url = f"URL: {r['url']}"
        server = f"Server: {r['server']}"
        x_powered_by = f"X-Powered-By: {r['x_powered_by']}"
        for word in r['suspicious']:
            for _ in word.items():
                detected_suspicious.append(f" - {_[0]}: {'✅' if _[1] else '❌'}\r\n")
        return f'''{status}\r\n{url}\r\n{server}\r\n{x_powered_by}\r\n{''.join(detected_suspicious)}'''

    @classmethod
    def do_req(cls, domain):
        url = f'{domain}{cls.context_path}'
        response = requests.request(cls.method, url, headers=cls.headers)
        server = response.headers.get('Server', '')
        x_powered_by = response.headers.get('X-Powered-By', '')
        suspicious = [{word: not bool(response.text.find(word))} for word in suspicious_words]
        cls.result = dict(
            url=url,
            success=response.status_code == cls.status,
            before_status=cls.status,
            after_status=response.status_code,
            server=server,
            x_powered_by=x_powered_by,
            response=response.text,
            suspicious=suspicious,
        )

    @classmethod
    async def do_async_req(cls, domain):
        # TODO: Implement this
        await asyncio.sleep(1)
        pass


class NotFound(Base):
    method = 'GET'
    status = 404
    name = 'NOT FOUND'
    context_path = '/nopsled-fuzzer-web'


class Ok(Base):
    method = 'GET'
    status = 200
    name = 'OK'


class RequestTooLong(Base):
    method = 'GET'
    status = 414
    name = 'Request Too Long'
    context_path = f'/{"A"*9090}'


class BadRequest(Base):
    method = 'GET'
    status = 400
    name = 'Bad Request'
    headers = {
        **headers,
        'Content-Type': 'nopsled'*10000,
        'Accept-Language': 'nopsled'*10000,
    }


INSTALLED_ERRROS = [
    NotFound,
    Ok,
    RequestTooLong,
    BadRequest,
]
