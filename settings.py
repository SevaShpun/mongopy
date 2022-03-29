import json

def settings():
    with open("settings.json", "r", encoding="utf-8") as f:
        return dict(json.loads(f.read()))

CFG = settings()

cfg_url = CFG.get("url")
cfg_server = f'{CFG.get("servers")[0]},{CFG.get("servers")[1]},{CFG.get("servers")[2]}'
cfg_db = CFG.get("db")
cfg_options = CFG.get("options")
