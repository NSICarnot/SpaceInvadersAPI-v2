import sanic

app = sanic.Sanic("SpaceInvadersAPI-v2")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, workers=4)