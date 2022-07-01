import asyncio
import sys

from errors import INSTALLED_ERRROS


class Fuzzer:
    def __init__(self, domain: str, use_async: str):
        super().__init__()
        self.domain = domain
        self.use_async = use_async

    @property
    def domain(self) -> str:
        return self._domain

    @domain.setter
    def domain(self, _domain: str):
        if not _domain.startswith('https://') and not _domain.startswith('http://'):
            print("[-] First argument should be start with `https://` or `http://` and end end with doesn\'t contain `/`.")
            sys.exit()
        self._domain = _domain

    @property
    def use_async(self) -> bool:
        return self._use_async

    @use_async.setter
    def use_async(self, _use_async: str):
        self._use_async = True if _use_async else False


class App(Fuzzer):
    def __init__(self, domain: str = '', use_async: str = ''):
        super().__init__(domain, use_async)
        pass

    @staticmethod
    async def async_run(tasks):
        await asyncio.gather(tasks)
        return

    def run(self):
        return

    def main(self):
        domain = super().domain
        use_async = super().use_async
        if use_async:
            loop = asyncio.get_event_loop()
            tasks = [_.do_async_req(domain=domain) for _ in INSTALLED_ERRROS]
            loop.run_until_complete(self.async_run(tasks))
        else:
            for idx, error in enumerate(INSTALLED_ERRROS):
                error.do_req(domain=domain)
                print(f'[{idx + 1}]', error.show())
        return


if __name__ == '__main__':
    app = App(*sys.argv[1:])
    app.main()
