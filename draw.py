#!/usr/bin/env python3
"""news-23 b55 front-page-dense: THE WORLD TODAY, Monday 23 November 2026 (31 stories)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
F = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = F + "DejaVuSerif-Bold.ttf"
SANS = F + "DejaVuSans.ttf"
SANS_B = F + "DejaVuSans-Bold.ttf"

BLACK = (17, 17, 17)
WHITE = (255, 255, 255)
GOLD = (201, 162, 39)
GOLD_L = (232, 184, 0)
RED = (176, 30, 36)
RED_D = (140, 20, 25)
TEAL = (14, 124, 123)
NAVY = (18, 40, 75)
CREAM = (245, 239, 224)
GREY = (90, 90, 90)
LGREY = (230, 230, 230)
GREEN = (46, 125, 50)

img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)


def font(path, size):
    return ImageFont.truetype(path, size)


def tw(text, f):
    return d.textlength(text, font=f)


def wrap(text, f, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if tw(t, f) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text(x, y, s, f, fill=BLACK, anchor="la"):
    d.text((x, y), s, font=f, fill=fill, anchor=anchor)


# ---------- masthead ----------
d.rectangle([0, 0, W, 50], fill=BLACK)
text(14, 8, "THE WORLD TODAY", font(SERIF_B, 34), WHITE)
text(W - 14, 15, "MONDAY 23 NOVEMBER 2026", font(SANS_B, 15), GOLD_L, anchor="ra")

# ---------- kicker ----------
text(14, 55, "AI rout hits Asia  ·  UN chief urges AI rules  ·  US lead over China at record low  ·  Anthropic IPO $107.3B",
     font(SANS_B, 12), RED)

# ---------- number strip (2 rows x 5) ----------
nums = [
    ("-3.3%", "KOSPI", RED), ("5.3", "US-CHINA POWER GAP", NAVY),
    ("11,762", "EBOLA CASES, DRC", GREEN), ("10T won", "SEOUL STABILISATION FUND", (150, 110, 0)),
    ("2%", "BILLIONAIRE TAX IN PARIS", (110, 60, 140)),
    ("$450M", "SKUBAL DEAL", (110, 60, 140)), ("165", "RUSSIAN MISSILES IN A WEEK", RED),
    ("12,000", "CLEARED IN MANCHESTER", NAVY), ("264 kg", "EXPLOSIVES SEIZED IN LEBANON", (150, 110, 0)),
    ("$107.3B", "ANTHROPIC IPO — LARGEST", (110, 60, 140)),
]
colw = 200
for i, (v, lab, col) in enumerate(nums):
    r, c = divmod(i, 5)
    x = 14 + c * colw
    yv = 74 + r * 30
    text(x, yv, v, font(SANS_B, 17), col)
    text(x, yv + 19, lab, font(SANS_B, 8), BLACK)

# ---------- region bar ----------
regions = [("ASIA-PACIFIC 7", TEAL, 200), ("AMERICAS 8", NAVY, 200),
           ("MIDDLE EAST 6", (190, 130, 0), 200), ("EUROPE 5", (110, 60, 140), 150),
           ("AFRICA 3", RED, 140), ("WORLD 2", GREY, 134)]
x = 0
for name, col, wdt in regions:
    d.rectangle([x, 136, x + wdt, 152], fill=col)
    text(x + wdt // 2, 140, name, font(SANS_B, 10), WHITE, anchor="ma")
    x += wdt

# ---------- UTC strip ----------
d.rectangle([0, 152, W, 166], fill=BLACK)
text(14, 155, "THE DAY IN UTC   ~00:00 Kospi dives   ~06:30 Guterres opens   ~09:00 Power Index   ~12:00 Paris 2% tax   ~15:00 Kyiv missiles   ~18:00 IPO $97.17",
     font(SANS, 10), WHITE)
text(W - 12, 155, "~ APPROX", font(SANS_B, 9), GOLD_L, anchor="ra")

# ---------- hero scenes ----------
SX, SY, SW, SH = 12, 170, 326, 150
GAP = 6

# scene 1: Kospi chart
x0 = SX
d.rectangle([x0, SY, x0 + SW, SY + SH], fill=(10, 22, 48))
text(x0 + 10, SY + 6, "-3.3%", font(SANS_B, 30), (255, 70, 60))
pts = [(x0 + 12 + i * 30, SY + 92 - v) for i, v in enumerate([8, 26, 14, 34, 20, 40, 28, 46, 36, 52, 44])]
d.line(pts, fill=(255, 170, 60), width=3)
for px, py in pts:
    d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=(255, 200, 90))
import random
random.seed(55)
bx = x0 + 8
while bx < x0 + SW - 14:
    bw = random.randint(12, 22)
    bh = random.randint(18, 46)
    d.rectangle([bx, SY + SH - 22 - bh, bx + bw, SY + SH - 22], fill=(30, 55, 95))
    for wy in range(SY + SH - 22 - bh + 4, SY + SH - 24, 8):
        for wx in range(bx + 3, bx + bw - 2, 6):
            if random.random() < 0.6:
                d.rectangle([wx, wy, wx + 2, wy + 3], fill=(255, 220, 110))
    bx += bw + 4
d.rectangle([x0, SY + SH - 22, x0 + SW, SY + SH], fill=BLACK)
text(x0 + 10, SY + SH - 19, "KOSPI 4,708.54  ·  -161 PTS", font(SANS_B, 11), WHITE)

# scene 2: Guterres globe
x0 = SX + SW + GAP
d.rectangle([x0, SY, x0 + SW, SY + SH], fill=TEAL)
text(x0 + 12, SY + 10, "150 DELEGATES", font(SANS_B, 30), GOLD_L)
text(x0 + 12, SY + 44, "BACK A RISK", font(SANS_B, 30), WHITE)
text(x0 + 12, SY + 78, "FRAMEWORK", font(SANS_B, 30), WHITE)
cx, cy, r = x0 + SW - 52, SY + 108, 34
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=WHITE, width=2)
d.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=WHITE, width=1)
d.line([cx - r, cy, cx + r, cy], fill=WHITE, width=1)
d.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 0, 360, fill=WHITE, width=1)
d.rectangle([x0, SY + SH - 22, x0 + SW, SY + SH], fill=BLACK)
text(x0 + 10, SY + SH - 19, "UN  ·  BRIDGETOWN", font(SANS_B, 11), WHITE)

# scene 3: Power Index bars
x0 = SX + 2 * (SW + GAP)
d.rectangle([x0, SY, x0 + SW, SY + SH], fill=CREAM)
text(x0 + 12, SY + 8, "NARROWEST SINCE 2018", font(SANS_B, 12), BLACK)
text(x0 + SW - 12, SY + 8, "GAP 5.3", font(SANS_B, 12), (150, 110, 0), anchor="ra")
bars = [("78.9", "US", NAVY, 78), ("73.6", "CHINA", RED, 72), ("40.5", "INDIA", GOLD, 44)]
bx = x0 + 26
for val, lab, col, bh in bars:
    text(bx + 34, SY + 30, val, font(SANS_B, 15), BLACK, anchor="ma")
    d.rectangle([bx, SY + 50, bx + 68, SY + 50 + bh], fill=col)
    text(bx + 34, SY + 50 + bh - 22, lab, font(SANS_B, 11), WHITE, anchor="ma")
    bx += 92
d.rectangle([x0, SY + SH - 22, x0 + SW, SY + SH], fill=BLACK)
text(x0 + 10, SY + SH - 19, "ASIA POWER INDEX 2026", font(SANS_B, 11), WHITE)

# ---------- hero headlines ----------
HY = SY + SH + 8  # 328
heroes = [
    ("1", "AI ROUT HITS ASIA",
     "Kospi closes -3.3% to 4,708.54, sheds 161 pts; intraday -5.8%. Samsung -3.1%, SK Hynix -2.5%.",
     "KOREA EXCHANGE"),
    ("2", "GUTERRES: REGULATE AI BEFORE IT'S TOO LATE",
     "UN chief urges global AI safety rules at the Bridgetown summit; 150 delegates back a risk framework.",
     "UNITED NATIONS"),
    ("3", "US LEAD OVER CHINA AT RECORD LOW",
     "Asia Power Index 2026: US 78.9, China 73.6 — gap 5.3, narrowest since 2018. India third at 40.5.",
     "LOWY INSTITUTE"),
]
for i, (num, head, body, src) in enumerate(heroes):
    x0 = SX + i * (SW + GAP)
    d.ellipse([x0, HY + 2, x0 + 20, HY + 22], fill=RED)
    text(x0 + 10, HY + 3, num, font(SANS_B, 12), WHITE, anchor="ma")
    lines = wrap(head, font(SANS_B, 18), SW - 26)
    ly = HY
    for ln in lines[:2]:
        text(x0 + 26, ly, ln, font(SANS_B, 18), BLACK)
        ly += 21
    by = HY + 46
    for ln in wrap(body, font(SANS, 11), SW - 4)[:2]:
        text(x0, by, ln, font(SANS, 11), BLACK)
        by += 14
    # source + chip on their own bottom row
    text(x0, HY + 78, src, font(SANS, 9), GREY)
    chip = "REPORTED"
    cw = tw(chip, font(SANS_B, 9)) + 12
    d.rectangle([x0 + SW - cw, HY + 76, x0 + SW, HY + 90], fill=NAVY)
    text(x0 + SW - cw // 2, HY + 78, chip, font(SANS_B, 9), WHITE, anchor="ma")

# ---------- MORE OF THE DAY ----------
MY = 428
d.rectangle([0, MY, W, MY + 18], fill=BLACK)
text(12, MY + 2, "MORE OF THE DAY  —  10 STORIES", font(SANS_B, 12), WHITE)

# ---------- cards ----------
cards = [
    ("AMERICAS", TEAL, "BESSENT: NVIDIA ANSWERS", "Treasury chief wants China answers.", "Reuters", "REPORTED", NAVY),
    ("FBI", RED_D, "FBI PROBES NCIC HACK", "Hackers hit police NCIC database.", "AP", "REPORTED", NAVY),
    ("WHITE HOUSE", (150, 110, 0), "TRUMP: IRAN STRIKES MAY RESUME", "Strikes may resume in New Year.", "Reuters", "REPORTED", NAVY),
    ("MARKETS", NAVY, "US FUTURES JUMP 3%", "Holiday rally lifts futures 3%.", "Bloomberg", "REPORTED", NAVY),
    ("SPORT", RED_D, "SKUBAL'S $450M METS DEAL", "Nine-year deal, largest ever.", "AP", "REPORTED", NAVY),
    ("SPORT", RED_D, "TOM JACKSON DIES AT 75", "Broncos LB, ESPN voice, dies.", "ESPN", "REPORTED", NAVY),
    ("LEGAL", (110, 60, 140), "STATES SUE SPACEX", "Ten states challenge AI claims.", "AP", "REPORTED", NAVY),
    ("TECH", (60, 90, 160), "ANTHROPIC IPO: $107.3B", "Raised at $83; closes $97.17.", "WSJ", "REPORTED", NAVY),
    ("EUROPE", (110, 60, 140), "POLAND: 3 MISSILES CROSSED AIRSPACE", "Kyiv: three Kh-101s crossed.", "AP", "CLAIM", RED),
    ("SPACE", GREY, "RUSSIAN NUCLEAR SATELLITE", "Intel: satellite may carry a nuke.", "Reuters", "CLAIM", RED),
]
CW, CH, CG = 196, 80, 8
for i, (cat, ccol, head, body, src, chip, chipcol) in enumerate(cards):
    r, c = divmod(i, 5)
    x0 = 12 + c * (CW + CG)
    y0 = MY + 18 + 4 + r * (CH + 6)
    d.rectangle([x0, y0, x0 + CW, y0 + 14], fill=ccol)
    text(x0 + 4, y0 + 2, cat, font(SANS_B, 9), WHITE)
    text(x0 + CW - 4, y0 + 2, str(i + 1), font(SANS_B, 9), WHITE, anchor="ra")
    ly = y0 + 17
    for ln in wrap(head, font(SANS_B, 12), CW - 6)[:2]:
        text(x0 + 2, ly, ln, font(SANS_B, 12), BLACK)
        ly += 14
    text(x0 + 2, y0 + 47, body, font(SANS, 10), BLACK)
    text(x0 + 2, y0 + 65, src, font(SANS, 9), GREY)
    cw = tw(chip, font(SANS_B, 9)) + 12
    d.rectangle([x0 + CW - cw, y0 + 63, x0 + CW, y0 + 77], fill=chipcol)
    text(x0 + CW - cw // 2, y0 + 65, chip, font(SANS_B, 9), WHITE, anchor="ma")

# ---------- map + ALSO ----------
AY = MY + 18 + 4 + 2 * (CH + 6) + 6  # 622
d.rectangle([0, AY, W, AY + 18], fill=BLACK)
text(12, AY + 2, "WHERE IT HAPPENED", font(SANS_B, 12), WHITE)
text(344, AY + 2, "ALSO ON MONDAY", font(SANS_B, 12), WHITE)

MAPX, MAPY, MAPW, MAPH = 12, AY + 22, 320, 200
d.rectangle([MAPX, MAPY, MAPX + MAPW, MAPY + MAPH], outline=BLACK, width=1)
for gx in range(MAPX, MAPX + MAPW, 16):
    d.line([gx, MAPY, gx, MAPY + MAPH], fill=(220, 230, 220), width=1)
for gy in range(MAPY, MAPY + MAPH, 16):
    d.line([MAPX, gy, MAPX + MAPW, gy], fill=(220, 230, 220), width=1)
# stylised land blobs
d.ellipse([MAPX + 8, MAPY + 20, MAPX + 130, MAPY + 150], fill=(170, 205, 150))
d.ellipse([MAPX + 130, MAPY + 10, MAPX + 250, MAPY + 130], fill=(170, 205, 150))
d.ellipse([MAPX + 90, MAPY + 130, MAPX + 190, MAPY + 195], fill=(170, 205, 150))
d.ellipse([MAPX + 210, MAPY + 140, MAPX + 300, MAPY + 195], fill=(170, 205, 150))
pins = [(30, 60, 1), (100, 145, 2), (185, 55, 3), (52, 88, 4), (95, 78, 5),
        (150, 108, 6), (40, 40, 7), (28, 112, 8), (60, 128, 9), (122, 150, 10),
        (170, 30, 11), (205, 48, 12), (235, 28, 13)]
for px, py, n in pins:
    cx, cy = MAPX + px, MAPY + py
    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=RED, outline=WHITE, width=1)
    text(cx, cy - 6, str(n), font(SANS_B, 9), WHITE, anchor="ma")
leg = ["Pins 1–13: 1 Seoul · 2 Bridgetown · 3 Beijing",
       "4 Washington · 5 New York · 6 Tehran · 7 Chicago",
       "8 SF · 9 Denver · 10 Austin · 11 Warsaw · 12 Kyiv · 13 Moscow"]
ly = MAPY + MAPH - 34
for ln in leg:
    text(MAPX + 4, ly, ln, font(SANS, 8), BLACK)
    ly += 11

also = [
    "14. Paris: 100+ back 2% billionaire tax", "15. Manchester: 12,000 cleared",
    "16. Zelenskyy: 165 missiles in a week", "17. COP31: the day after pact rejected",
    "18. Benghazi: UN demands port probe", "19. Israel unity talks resume",
    "20. Gaza: two killed in Israeli strike", "21. West Bank settler attacks",
    "22. Iran war: no deal in sight", "23. Lebanon seizes 264 kg explosives",
    "24. Bahrain: strike hits plant, 2 hurt", "25. Sudan: defences down drones",
    "26. DRC: fighting traps Ebola teams", "27. Bangladesh: Hasina jailed if she returns",
    "28. Seoul minister quits in exam row", "29. SK Telecom -7.3% as hype cools",
    "30. China eases margin rules", "31. Seoul readies 10T-won fund",
]
ax = 344
for i, item in enumerate(also):
    col = i // 9
    row = i % 9
    text(ax + col * 340, MAPY + 4 + row * 21, item, font(SANS, 11), BLACK)

# ---------- DATE CHECK ----------
DY = AY + 22 + MAPH + 8  # 852
d.rectangle([12, DY, W - 12, DY + 76], outline=RED, width=2)
text(16, DY + 4, "DATE CHECK", font(SANS_B, 13), RED)
text(W - 16, DY + 4, "READ 23 NOV 2026, 23:59 UTC — STORIES DATED 23 NOV ONLY",
     font(SANS_B, 9), RED, anchor="ra")
text(16, DY + 22, "LEFT OUT — NOT 23 NOV: Democrats reach 258 seats (22 Nov) · Sparta II fire (22 Nov) · El Chapo Isidro captured (22 Nov) ·",
     font(SANS, 10), BLACK)
text(16, DY + 37, "EU–Indonesia pact (21 Nov) · Nigeria boat (21 Nov) · ICJ Myanmar ruling (19 Nov)",
     font(SANS, 10), BLACK)
text(16, DY + 52, "NOT YET: Dymer search continues (14 missing) · 4 House races uncalled · COP32 venue not set · WHO evacuating trapped Ebola staff",
     font(SANS, 10), BLACK)

# ---------- sources + footer ----------
SY2 = DY + 76 + 6
text(14, SY2, "Sources: Reuters · AP · Bloomberg · AFP · Yonhap · BBC · WSJ · NYT · ESPN · Lowy Institute (Asia Power Index 2026).",
     font(SANS, 9), GREY)
text(14, SY2 + 12, "CHIPS: REPORTED = confirmed by wires · CLAIM = one side's claim, not independently confirmed · ONGOING = still developing.",
     font(SANS, 9), GREY)
text(14, SY2 + 24, "All times UTC. Figures as reported 23 Nov 2026. Scenes are drawn illustrations, not photographs.",
     font(SANS, 9), GREY)
d.rectangle([0, H - 26, W, H], fill=BLACK)
text(W // 2, H - 22, "THE WORLD TODAY  —  Monday 23 November 2026  ·  31 stories  ·  6 regions",
     font(SANS_B, 12), GOLD_L, anchor="ma")

img.save("entry.png")
print("saved entry.png", img.size)
