from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def my_first_http_web_service():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("tutorial_001:app", reload=True)
