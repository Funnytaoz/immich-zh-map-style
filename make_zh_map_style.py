#!/usr/bin/env python3
"""Make Chinese-labelled copies of Immich's map styles (tiles.immich.cloud, Protomaps schema).

The vector tiles already carry name:zh-Hans / name:zh-Hant; the stock style prefers name:en.
Every label that shows a place/road/POI name is rewritten to prefer Simplified Chinese.
usage: make_zh_map_style.py OUT_DIR
"""
import json, sys, urllib.request
ZH = ["coalesce", ["get", "name:zh-Hans"], ["get", "name:zh-Hant"], ["get", "pgf:name"], ["get", "name"], ["get", "name:en"]]
out = sys.argv[1]
for flavor in ("light", "dark"):
    req = urllib.request.Request(f"https://tiles.immich.cloud/v1/style/{flavor}.json", headers={"User-Agent": "Mozilla/5.0 (immich-115 map style)"})
    style = json.load(urllib.request.urlopen(req, timeout=60))
    n = 0
    for layer in style["layers"]:
        tf = layer.get("layout", {}).get("text-field")
        if tf is not None and ('"name' in json.dumps(tf) or '"pgf:name' in json.dumps(tf)):
            layer["layout"]["text-field"] = ZH
            n += 1
    style["name"] = style.get("name", flavor) + " (zh-Hans)"
    json.dump(style, open(f"{out}/{flavor}-zh.json", "w"), ensure_ascii=False)
    print(f"{flavor}: {n} label layers switched to Chinese")
