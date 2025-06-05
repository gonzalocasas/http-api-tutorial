# HTTP API Tutorials: Part 3

> Adding a tiny web UI to use your HTTP API

## Setup

*No extra setup, we keep working on the same environment! 🚀*

## Exercise

On this exercise, we will create a minimal web user interface (i.e. a webpage that we can open with a browser) that also uses our HTTP API.

The web interface will have a text input field where we can type a name, and a button that will send a request to our web server (specifically, to the `/hello/{name}` HTTP API endpoint of our web server). The response of the HTTP API endpoint will be displayed in the web interface.

1. Create a file `tutorial_003.py` in this folder and copy the content of the previous solution as a starting point.
2. Add a new method to the web server that will be providing the "HTML" for the web interface. This is the method, study it and compare it to the other ones to understand what it does:
    ```python
    @app.get("/ui", response_class=HTMLResponse)
    async def web_ui():
        html_path = os.path.join(os.path.dirname(__file__), "webui.html")
        with open(html_path, "r") as file:
            html_content = file.read()

        return html_content
    ```
3. Create a file `webui.html` in this folder, and paste the content of the [`webui-ugly.html`](./webui-ugly.html) file into it.

4. Open your terminal, make sure you are located in this folder (otherwise `cd` into it) and run the first example:

    ```bash
    python tutorial_003.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:8000/ui` to see the application. If you type a name in the text input field and click the button, you should see the response of the HTTP API endpoint displayed in the web interface. If you open the `Dev console` of your browser, and go to `Network`, you will notice that when you press the button, the request to the API is made, and the response arrives in the JSON content.

6. Now make it pretty: replace the content of the `webui-ugly.html` file with the content of the [`webui-pretty.html`](./webui-pretty.html) file, and refresh your browser. Nothing has changed except we added some styling to make it look better.

> **Notice that** we're not accessing the API directly in the browser anymore, we access the web UI that is on `/ui` and that will in turn use the API to get the data.