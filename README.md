# An fast simple example microservice using Sanic and Redis.

Boilerplate code for a microservice.  
- Sanic is one of the fastest python web servers available.  Interchangable with FastAPI and flask.
- Redis is one of the fastest KV stores available. 


## Dependencies:

* Python3.6 or greater
* Redis

(best to use virtualenv as always.)

To install dependencies run:

```
pip install -r requirements.txt

```

To run the application:

```
API_KEY=<your key> python3 .
```

# TODO: 
- tests
- wrap server depenencies in a struct (depinj)
- refactor provider to have common interface 
- port to nim
