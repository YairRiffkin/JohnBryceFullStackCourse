import flask
app = flask.Flask("my app")
@app.route("/")
async def main_page():
    return "hello world"

if __name__ == "__main__":
    app.run()
