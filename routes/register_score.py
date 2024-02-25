import sanic

from core.player import Player

async def register_score(request: sanic.Request):
    if "pseudo" in request.args:
        pseudo = request.args["pseudo"][0]
        if "score" in request.args:
            score = int(request.args["score"][0])
            player = Player(pseudo)
            if "hash" in request.args:
                hash = request.args["hash"][0]
                if player.get_md5() == hash:
                    if player.get_score() < score:
                        player.change_score(score)
                        return sanic.response.json({"success": "Score registered"}, status=200)
                    else:
                        return sanic.response.json({"error": "Score not high enough"}, status=400)
                else:
                    return sanic.response.json({"error": "Invalid hash"}, status=400)
            else:
                return sanic.response.json({"error": "No hash provided"}, status=400)
        else:
            return sanic.response.json({"error": "No score provided"}, status=400)
    else:
        return sanic.response.json({"error": "No pseudo provided"}, status=400)