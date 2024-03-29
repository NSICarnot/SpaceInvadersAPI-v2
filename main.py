import sanic
import dotenv

from routes.register_score import register_score
from routes.get_score import get_score

dotenv.load_dotenv(".env")

app = sanic.Sanic("SpaceInvadersAPI-v2")

app.add_route(register_score, "/register-score", methods=["POST"])
app.add_route(get_score, "/get-score", methods=["GET"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, workers=4, access_log=True)