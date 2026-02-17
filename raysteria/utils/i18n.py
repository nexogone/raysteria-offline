from raysteria.utils.data import load_from_json

app_lang = "en"
locales = {
    "api": load_from_json(
        file_path=f"raysteria/assets/locales/{app_lang}/api.json",
    ),
    "webview": load_from_json(
        file_path=f"raysteria/assets/locales/{app_lang}/webview.json",
    ),
}


def localize(from_dict: str, string_id: str) -> str:
    locales_dict = locales.get(from_dict)
    return locales_dict.get(string_id)
