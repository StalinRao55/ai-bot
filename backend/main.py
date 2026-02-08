from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "FastAPI is running"}

@app.get("/docs-test")
def docs_test():
    return {"docs": "working"}
