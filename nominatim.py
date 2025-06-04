import requests
import re
from functools import lru_cache


COUNTRYCODEOFFSET = ord("🇦") - ord("A")


def flag(code):
    code = code.upper()
    return chr(ord(code[0]) + COUNTRYCODEOFFSET) + chr(ord(code[1]) + COUNTRYCODEOFFSET)


@lru_cache(maxsize=None)
def reverselookup(lat, lon, zoom=12):
    params = {
        "format": "jsonv2",
        "lat": f"{lat:.7f}",
        "lon": f"{lon:.7f}",
        "email": "aslak@grinsted.com",
        "zoom": f"{zoom:.0f}",
        "accept-language": "en",
    }
    r = requests.get(
        "https://nominatim.openstreetmap.org/reverse", params=params
    ).json()
    try:
        r["unicodeflag"] = flag(r["address"]["country_code"])
    except:
        r["unicodeflag"] = ""
    try:
        r["short_dislay_name"] = re.sub(
            r"^([^,]+,\s*)*?(.{0,50})$", r"\2", r["display_name"]
        )
    except:
        r["short_dislay_name"] = r["display_name"]
    return r


if __name__ == "__main__":
    import re

    answer = reverselookup(52.548, -1.816, 1)
    print(answer)
    regionname = answer["display_name"]
    shortregionname = re.sub(r"^([^,]+,\s*)*?(.{0,50})$", r"\2", regionname)
    print(regionname)
    print(shortregionname)
