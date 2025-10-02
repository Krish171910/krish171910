<h1 align="center">Hi 👋, I'm Krish Patel</h1>
<h3 align="center">A passionate programmer from India.</h3>

---

<br>

<table style="border: none;">
  <tr>
    <td>

### 🛠️ About Me:

- 🔭 I’m currently working on: **Empowering myself**  
- 🌱 I’m currently learning: **Web Development**  
- 💡 Ask me about: **C++, IoT, Web Development**  
- ⚡ Fun fact: I enjoy solving errors and diving deep into C++!

    </td>
    <td>
      <img align="right" alt="Coding" width="400" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzl4eWFtY24zZXllMW9wbXFrY3o4bGI1MDIwNXphdGFsNHp4cnV3NyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Y4ak9Ki2GZCbJxAnJD/giphy.gif">
    </td>
  </tr>
</table>

---

<div align="center">
  <h2>🚀 Tech Stack</h2>

<strong>Languages & Markup:</strong><br>
<img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white" />
<img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" />
<img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white" />

<br><br>

<strong>Tools & IDEs:</strong><br>
<img src="https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" />
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
</div>

---

## 🏆 Coder Achievements

<table>
  <tr>
    <td>
      <img src="https://upload.wikimedia.org/wikipedia/commons/6/65/HackerRank_logo.png" width="60px" />
    </td>
    <td>
      <strong>🥈 5-star C++ badge on HackerRank</strong><br>
      <a href="https://www.hackerrank.com/profile/24ce084_krish" target="_blank">
        <img src="https://img.shields.io/badge/HackerRank-Profile-green?style=flat&logo=hackerrank" />
      </a>
    </td>
  </tr>
</table>

---
## 🏆 LeetCode Stats
![LeetCode Stats](https://leetcard.jacoblin.cool/KrishPatel1905?ext=heatmap)

<h2 align="center">💡 Programming Wisdom</h2>
<p align="center">
  <img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical" />
</p>

---

<div align="center">
  <h2>🔥 GitHub Streak 🔥</h2>
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=krish171910&theme=tokyonight&hide_border=true&border_radius=20" width="60%" />
</div>



---

<h2 align="center">🌈 Colorful Contribution Graph</h2>
<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=krish171910&theme=tokyo-night&bg_color=0d1117&color=FF6AC1&line=5D9CEC&point=FAD000&hide_border=true" width="90%" />
<!--    <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=KRISHPATE1905&theme=radical" alt="Profile Summary" /> -->
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=krish171910&theme=radical" alt="Profile Summary" />

</p>

---

<div align="center">
<h2>📈 Github Stats 📈</h2>
<br>

[![Krish’s GitHub Stats](https://github-readme-stats.vercel.app/api?username=krish171910&theme=radical&card_width=900&card_height=400)](https://github.com/krish171910)

---

<h2>🚀 Languages I Use</h2>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=krish171910&layout=compact&theme=radical&hide_border=true&border_radius=20" width="30%" />
</div>





---

## 🏆 My HackerRank Badges

<p>
  <a href="https://www.hackerrank.com/profile/24ce084_krish" target="_blank">
    <img src="https://img.shields.io/badge/HackerRank-Profile-green?style=flat&logo=hackerrank" alt="HackerRank Profile">
  </a>
</p>

## 🧾 CodeChef Stats & Heatmap

![CodeChef Heatmap](https://raw.githubusercontent.com/krishpatel1905/YourRepoName/main/assets/codechef_heatmap.png)

![CodeChef Heatmap](https://raw.githubusercontent.com/YourUser/YourRepo/main/assets/codechef_heatmap.png)

# scripts/generate_codechef_heatmap.py
"""
Generate a GitHub-style calendar heatmap PNG for a CodeChef user.
Usage:
  python generate_codechef_heatmap.py krishpatel1905 assets/codechef_heatmap.png
"""
import sys
import requests
from bs4 import BeautifulSoup
from dateutil import parser
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import math
import time
from pathlib import Path

HEADERS = {"User-Agent": "Mozilla/5.0 (heatmap-generator)"}

def fetch_status_pages(username, max_pages=30, delay=0.3):
    pages = []
    base = f"https://www.codechef.com/users/{username}/status"
    for p in range(1, max_pages + 1):
        url = base + (f"?page={p}" if p > 1 else "")
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code != 200:
            break
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find("table")
        # if no table or only header, break
        if table is None:
            break
        rows = table.find_all("tr")
        if not rows or len(rows) <= 1:
            break
        pages.append(soup)
        time.sleep(delay)
    return pages

def extract_dates(soups):
    dates = []
    for soup in soups:
        # strategy 1: <time datetime="...">
        for t in soup.find_all("time"):
            dt = t.get("datetime") or t.get_text(strip=True)
            try:
                parsed = parser.parse(dt, fuzzy=True)
                dates.append(parsed.date())
            except Exception:
                continue
        # strategy 2: look at td with date-like text (fallback)
        for td in soup.find_all("td"):
            txt = td.get_text(" ", strip=True)
            if not txt:
                continue
            if any(m in txt for m in ["Jan", "Feb", "Mar", "Apr", "May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]) or "/" in txt or "-" in txt:
                try:
                    parsed = parser.parse(txt, fuzzy=True, default=datetime.datetime.now())
                    if parsed.year >= datetime.datetime.now().year - 10:
                        dates.append(parsed.date())
                except Exception:
                    continue
    return dates

def build_series(dates):
    if not dates:
        return pd.Series(dtype=int)
    c = Counter(dates)
    start = min(c.keys())
    end = datetime.date.today()
    idx = pd.date_range(start, end, freq="D").date
    counts = [c.get(d, 0) for d in idx]
    return pd.Series(index=pd.to_datetime(idx), data=counts)

def draw_heatmap(series, out_path, username):
    if series.empty:
        # create a placeholder image
        plt.figure(figsize=(6,2))
        plt.text(0.5,0.5,"No submission data found\n(try Option A or check username)", ha='center', va='center', fontsize=12)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(out_path, dpi=150)
        plt.close()
        return

    s = series.copy()
    s.index = pd.to_datetime(s.index)
    # align start to Sunday
    start = s.index.min()
    start = start - pd.Timedelta(days=(start.weekday()+1) % 7)
    end = s.index.max()
    full = pd.date_range(start, end, freq="D")
    s = s.reindex(full, fill_value=0)

    weeks = math.ceil(len(s) / 7)
    # build matrix rows = 7 weekdays (Sun..Sat), cols = weeks
    mat = []
    for w in range(weeks):
        col = s[w*7:(w+1)*7].values
        if len(col) < 7:
            col = list(col) + [0]*(7-len(col))
        mat.append(col)
    # transpose so rows = weekdays
    mat = list(zip(*mat))
    df = pd.DataFrame(mat)

    plt.figure(figsize=(max(10, weeks/2), 3))
    plt.imshow(df, aspect='auto', interpolation='nearest')
    plt.axis('off')
    plt.title(f"CodeChef activity heatmap — {username}")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_codechef_heatmap.py <username> <output_png>")
        sys.exit(1)
    username = sys.argv[1]
    out = Path(sys.argv[2])
    out.parent.mkdir(parents=True, exist_ok=True)

    print("Fetching user pages...")
    pages = fetch_status_pages(username)
    print(f"Fetched {len(pages)} pages.")
    dates = extract_dates(pages)
    print(f"Found {len(dates)} timestamps.")
    series = build_series(dates)
    print("Drawing...")
    draw_heatmap(series, str(out), username)
    print("Saved:", out)

if __name__ == "__main__":
    main()



