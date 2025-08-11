#!/usr/bin/env python3
import json
import random
import subprocess
from datetime import datetime

# Fetch posts from Ghost API
api_key = "0630660400a036d397f3c64e66"
url = f"https://blog.aubo.cl/ghost/api/content/posts/?key={api_key}&limit=15&fields=title,slug,feature_image,published_at,excerpt&order=published_at%20desc"

result = subprocess.run(["curl", "-H", "Content-Type: application/json", url], capture_output=True, text=True)
data = json.loads(result.stdout)

# Select 3 random posts
posts = data["posts"]
selected_posts = random.sample(posts, 3)

# Format dates in Spanish
def format_date(date_str):
    dt = datetime.fromisoformat(date_str.replace('-04:00', '+00:00').replace('-03:00', '+00:00'))
    months = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    return f"{months[dt.month]} {dt.day}, {dt.year}"

# Output selected posts
for i, post in enumerate(selected_posts, 1):
    print(f"Post {i}:")
    print(f"  Title: {post['title']}")
    print(f"  Slug: {post['slug']}")
    print(f"  Image: {post['feature_image']}")
    print(f"  Date: {format_date(post['published_at'])}")
    print(f"  URL: https://blog.aubo.cl/{post['slug']}/")
    print()