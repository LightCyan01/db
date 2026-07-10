# FastAPI JSON API

A minimal Python server with two JSON endpoints.

## Run

```powershell
py -m pip install -r requirements.txt
py -m uvicorn server:app --reload
```

## Try it

```powershell
curl.exe http://127.0.0.1:8000/
curl.exe http://127.0.0.1:8000/hello/LightCyan01
```

You can also open these URLs in your browser. FastAPI's interactive documentation is at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
