# comver - WIP

TODO: make web server, in simple way

## How to start
```
$ python3 -m venv venv
(venv) $ pip install -r requirements.txt
...
(venv) $ comver server ...
```

#### Make simple server with few GET request
```
$ comver server \
  --get /hello '{"name": "comver"}' \
  --get /world '{"year": 2022}'
```

and check with new terminal
```
$ curl localhost:9000/hello
"{\"name\": \"comver\"}"%

$ curl localhost:9000/world
"{\"year\": 2022}"%
```

