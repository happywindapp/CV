import base64
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIETNAMESE = "U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB"
LATIN = "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"


def b64(path):
    return base64.b64encode(path.read_bytes()).decode()


def font_css():
    faces = []
    for subset, ranges in (("vietnamese", VIETNAMESE), ("latin", LATIN)):
        for weight in (400, 600):
            font = b64(ROOT / "assets" / "fonts" / f"bvp-{subset}-{weight}.woff2")
            faces.append(
                f'@font-face{{font-family:"Be Vietnam Pro";font-style:normal;font-weight:{weight};'
                f"font-display:swap;src:url(data:font/woff2;base64,{font}) format(\"woff2\");unicode-range:{ranges}}}"
            )
    return "\n".join(faces)


def icon_sprite(html):
    symbols = []
    for name in sorted(set(re.findall(r'href="#i-([\w-]+)"', html))):
        svg = (ROOT / "assets" / "icons" / f"{name}.svg").read_text(encoding="utf-8")
        attrs, body = re.search(r"<svg([^>]*)>(.*)</svg>", svg, re.S).groups()
        attrs = re.sub(r'\s(xmlns|class|width|height|role)="[^"]*"', "", attrs)
        body = re.sub(r">\s+<", "><", re.sub(r"<title>.*?</title>", "", body).strip())
        symbols.append(f'<symbol id="i-{name}" {" ".join(attrs.split())}>{body}</symbol>')
    return '<svg hidden aria-hidden="true">' + "".join(symbols) + "</svg>"


# Usage: python -I scripts/build-cv-html.py <person_dir>  ->  cv_<person_dir>.html at repo root
person = sys.argv[1].strip("/\\")
src = ROOT / person
html = (src / "cv-template.html").read_text(encoding="utf-8")
html = html.replace("{{FONT_CSS}}", font_css())
html = html.replace("{{PHOTO}}", "data:image/jpeg;base64," + b64(src / "photo.jpg"))
html = html.replace("{{ICON_SPRITE}}", icon_sprite(html))
html = re.sub(r"\{\{LOGO:([\w-]+)\}\}", lambda m: "data:image/png;base64," + b64(src / "logos" / f"{m[1]}.png"), html)
target = ROOT / f"cv_{person}.html"
target.write_text(html, encoding="utf-8", newline="\n")
print(target, target.stat().st_size)
