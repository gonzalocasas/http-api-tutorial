# HTTP API Tutorials: Part 2

> Now let's make it "parametric" (as in, our API will accept parameters)

## Setup

*No extra setup, we keep working on the same environment! 🚀*

## Exercise

1. Create a file `tutorial_002.py` in this folder and copy the content of the previous solution as a starting point.
2. Now let's add a second function to our API. It will also be an "HTTP API endpoint" (which means it will be accessible via the browser -and any other software that can make HTTP requests, including Grasshopper):

   1. Create a new function -again, any name goes: the difference to the first one is that it will accept a parameter (let's call it `name`). The dictionary that it returns can be the almost the same, but include the name in the values. For example, if you added a `message` key with a string value as a message, you can do something like `message="Hi {}!".format(name)` to include the name.
   2. Decorate the method with `@app.get("/hello/{name}")`. This does not only make it an HTTP API endpoint, but also it will accept a parameter called `name`.

3. Open your terminal, make sure you are located in this folder (otherwise `cd` into it) and run the first example:

    ```bash
    python tutorial_002.py
    ```

4. Open your browser and navigate to `http://127.0.0.1:8000/hello/johnny` to see the application.


## Solution

Check the [tutorial_002_solution.py](./tutorial_002_solution.py) file for the solution.

## Next

Now go to the next step [003-web-ui](../003-web-ui/README.md).