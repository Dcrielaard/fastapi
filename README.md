# FastAPI

### How to use this repo?
1. First: start the server on your local machine with the following command in zsh: 
`uvicorn app:app --reload`. This will start the server on the default location (http://127.0.0.1:8000)
2. Send a request to the server with the following command:
`curl -X GET http://127.0.0.1:8000`
3. You can also send a post request with the following command:
```
curl --request POST \
  --url http://127.0.0.1:8000/items/ \
  --header 'Content-Type: application/json' \
  --data '{"name": "Dennis","price": 5.0}'
```

Documentation of the code can be found at:
http://127.0.0.1:8000/docs

#### Scalability
Calls made to the API are syncronous. It may be helpful to send the requests a-syncronuous using asyncio.
This can be tested using boom

`boom http://127.0.0.1.8000/sleep_fast -c 20 -n 100`
(100 requests send in batches of 20)

This repo is based on the videos by calmcode.io (https://calmcode.io/fastapi/hello-world.html)

