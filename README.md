# Sanic Test App

### Just a dummy Sanic app for me to have around to pull down when I am messing around with config management tools

To run (w is # of workers):
```
gunicorn app:app --bind 127.0.0.1:8080 -w 4 --worker-class sanic.worker.GunicornWorker
```
