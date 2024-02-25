import sanic
from core.player import Player

async def get_score(request: sanic.Request):
    if "player" in request.args:
        pseudo = request.args["player"][0]
        player = Player(pseudo)
        score = player.get_score()
        return sanic.response.json({"score": score}, status=200)
    else:
        return sanic.response.json({"error": "No pseudo provided"}, status=400)