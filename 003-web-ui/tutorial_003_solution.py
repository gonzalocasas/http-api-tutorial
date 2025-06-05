import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/hello")
def my_first_http_web_service():
    return {"message": "Hello World!"}


@app.get("/hello/{name}")
def personalized_greeting(name: str):
    return {"message": f"Hello {name}!"}


@app.get("/ui", response_class=HTMLResponse)
async def web_ui():
    html_path = os.path.join(os.path.dirname(__file__), "webui.html")
    with open(html_path, "r") as file:
        html_content = file.read()

    return html_content


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("tutorial_003:app", reload=True)
