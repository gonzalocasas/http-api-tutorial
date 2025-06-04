# HTTP API Tutorials: Part 1

> This part is the absolute minimal HTTP API exercise

## Setup stuff

1. Create a virtual environment using `mamba`, name it `http-api-tutorial` and install `python` on it.
2. Activate the virtual environment.
3. Use mamba to install: `fastpi`, `uvicorn` and `ruff`.

*Now you're ready for the exercise! ✨*

## Exercise

4. Create a file `tutorial_001.py` in this folder
5. Inside the file you will need to do the following:

   1. Import `FastAPI` class from the `fastapi` library
   2. Create an instance of `FastAPI` (no arguments in the constructor) and assign to a variable named `app`.
      > Why `app`? Because it's a convention! We will use the name `app` in step 4.
   3. Create a function (name it whatever you want), the function will only do one thing: return a dictionary, the dictionary can contain any keys and values you want, for example, a `message` key with a string value as a message.
   4. Decorate the function with `@app.get("/hello")` to make it a proper HTTP API endpoint.
   5. Add a `if __name__ == "__main__":` part to the script, and inside it run the app with `uvicorn`. For this, you need to `import uvicorn` and then call `uvicorn.run("tutorial_001:app", reload=True)`.
      > Why? This basically starts a web server and kicks off the entire stuff.

6. Open your terminal, make sure you are located in this folder (otherwise `cd` into it) and run the first example:

    ```bash
    python tutorial_001.py
    ```

7. Open your browser and navigate to `http://127.0.0.1:8000/hello` to see the application.


## Solution

Check the [tutorial_001_solution.py](./tutorial_001_solution.py) file for the solution.
