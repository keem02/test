from fastapi import FastAPI, HTTPException


app = FastAPI()


@app.get("/not_found")
def read_items():
    return HTTPException(status_code=404, detail="Not Found")


@app.get("/found")
def read_items():
    return {"detail": "Found"}


@app.get("/server_error")
def read_items():
    return HTTPException(status_code=500, detail="Server Error")