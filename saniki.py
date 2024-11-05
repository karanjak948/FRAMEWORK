from sanic import Sanic
from sanic.response import json
app = Sanic("MyApp")

@app.route("/hello")
async def test(request):
    return json({"message": "Hello, Kelvin Family"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000)