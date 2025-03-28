from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title> Elasticsearch</title>
           <h2> Elasticsearch </h2>
        </head>
        <body>
           <h4> Get your Document </h4>
            <form action="/get" method="post">
                <input type="text" name="query"/>
                <button type="submit">Get</button>
            </form>
            <br/>
           <h4> Insert your Document </h4>
            <form action="/insert" method="post">
                <textarea name="document"></textarea>
                <button type="submit">Insert</button>
            </form>
        </body>
    </html>
    """
