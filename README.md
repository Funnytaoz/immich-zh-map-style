# immich-zh-map-style

Chinese-labelled copies of [Immich](https://immich.app)'s default map styles.

Immich's vector tiles (`tiles.immich.cloud`, Protomaps schema) already contain `name:zh-Hans` and `name:zh-Hant`, but the stock styles label the map with `name:en`. These styles change every label layer to prefer **Simplified Chinese → Traditional Chinese → local name → English**. Everything else (tiles, sprites, fonts, colours) is unchanged and still served by Immich's own infrastructure.

| File | Use as |
|---|---|
| `light-zh.json` | Immich → Administration → Settings → Map → Light style |
| `dark-zh.json` | Immich → Administration → Settings → Map → Dark style |

Via jsDelivr:

```
https://cdn.jsdelivr.net/gh/Funnytaoz/immich-zh-map-style@v1.0.0/light-zh.json
https://cdn.jsdelivr.net/gh/Funnytaoz/immich-zh-map-style@v1.0.0/dark-zh.json
```

Regenerate after Immich changes its styles: `python3 make_zh_map_style.py .`

Both files validate with `gl-style-validate` (@maplibre/maplibre-gl-style-spec).

## 中文说明

把 Immich 默认地图样式的标注改成优先显示简体中文（其次繁体中文、当地名称、英文）。瓦片、图标、字体仍使用 Immich 官方服务，只替换样式文件。在 Immich 管理后台 → 设置 → 地图，把浅色/深色样式地址换成上面两个链接即可；恢复官方样式填回 `https://tiles.immich.cloud/v1/style/light.json` / `dark.json`。

## Attribution

Derived from Immich's map styles (`https://tiles.immich.cloud/v1/style/*.json`), which are based on [Protomaps basemaps](https://github.com/protomaps/basemaps). Map data © [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors.
