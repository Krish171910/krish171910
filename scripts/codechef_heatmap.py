import sys, requests, matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

def fetch_submissions(handle):
    url = f"https://www.codechef.com/users/{handle}"
    r = requests.get(url)
    if r.status_code != 200:
        print("Error fetching profile")
        return []
    soup = BeautifulSoup(r.text, "html.parser")
    scripts = soup.find_all("script")
    data = []
    for sc in scripts:
        if "fully_solved" in sc.text:  # crude filter
            ts = datetime.now()
            data.append(ts)
    return data or [datetime.now()]  # fallback

def generate_heatmap(handle, outfile):
    dates = fetch_submissions(handle)
    df = pd.DataFrame({"date": dates})
    df["count"] = 1
    df = df.groupby("date").count()
    plt.figure(figsize=(6,3))
    df.plot(kind="bar", legend=False)
    plt.title(f"{handle} CodeChef Activity")
    plt.tight_layout()
    plt.savefig(outfile)
    print(f"Saved heatmap: {outfile}")

if __name__ == "__main__":
    handle = sys.argv[1]
    outfile = sys.argv[2]
    generate_heatmap(handle, outfile)
