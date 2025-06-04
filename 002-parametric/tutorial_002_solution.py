from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def my_first_http_web_service():
    return {"message": "Hello World!"}


@app.get("/hello/{name}")
def personalized_greeting(name: str):
    return {"message": f"Hello {name}!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("tutorial_002:app", reload=True)
