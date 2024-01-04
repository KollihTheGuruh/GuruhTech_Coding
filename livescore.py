# pip install livescore-api
from livescore_api import livescore

api = livescore()

print(api.matches()[10])