# Server Status Checker
This app will be sending the weird payload to web server for analyzing. thought more status code will be implementing.


### How it looks
```bash
[1] STATUS: ✅ (404 -> 404)
URL: http://localhost/nopsled-fuzzer-web
Server: Apache/2.4.51 (Unix) LibreSSL/2.8.3
X-Powered-By: 
Suspicious word:
 - nginx: ❌
 - Apache: ❌
 - Tomcat: ❌

[2] STATUS: ✅ (200 -> 200)
URL: http://localhost
Server: Apache/2.4.51 (Unix) LibreSSL/2.8.3
X-Powered-By: 
Suspicious word:
 - nginx: ❌
 - Apache: ❌
 - Tomcat: ❌

[3] STATUS: ✅ (414 -> 414)
URL: http://localhost/AAAAAAAAAAAAAAAAAAAAAAAA...
Server: Apache/2.4.51 (Unix) LibreSSL/2.8.3
X-Powered-By: 
Suspicious word:
 - nginx: ❌
 - Apache: ❌
 - Tomcat: ❌

[4] STATUS: ✅ (400 -> 400)
URL: http://localhost
Server: Apache/2.4.51 (Unix) LibreSSL/2.8.3
X-Powered-By: 
Suspicious word:
 - nginx: ❌
 - Apache: ❌
 - Tomcat: ❌
```


### Env
```bash
$ python -V
python 3.7.3
```


### Install
```bash
python3 -m venv venv
source venv/bin/activate
pip install requirements.txt
```

### Run
* Should be start with `http://` or `https://`
```bash
python main.py http://example.com
```

<br/>

### Supported status
| STATUS | NAME             | SUPPORTED |
|--------|------------------|:---------:|
| 200    | Ok               |     O     |
| 400    | Bad Request      |     O     |
| 404    | Not Found        |     O     |
| 414    | Request Too Long |     O     |


### Features TODO
- [ ] Handle the sys argv parse error
- [ ] Async request with gather
