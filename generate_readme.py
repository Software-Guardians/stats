import json

with open('commit_summary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

timestamp = data.get("timestamp", "N/A")
total_commits = data.get("total_commits", 0)
active_days = data.get("active_days", 0)
avg_per_day = data.get("average_per_day", 0)
monthly_commits = data.get("monthly_commits", 0)  # Son 30 gün
daily_commits = data.get("daily_commits", 0)      # Bugün
last_commit = data.get("last_commit", "N/A")
repos = data.get("repos", {})

top_repo = max(repos, key=repos.get) if repos else "N/A"
top_repo_commits = repos.get(top_repo, 0)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(f"""\
<p align="center">
  <img src="../software-guardians-banner.jpg" alt="Software Guardians Banner" width="320"/>
</p>
<h1 align="center">🛡️ Software Guardians</h1>
<p align="center"><em>Create, Share, and Protect Code.</em></p>
<p align="center">
  <img src="https://img.shields.io/github/last-commit/Software-Guardians/.github?color=purple&label=Last%20Update&style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Daily%20Activity-{daily_commits}%20commits-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Monthly%20Activity-{monthly_commits}%20commits-green?style=for-the-badge"/>
</p>
<hr/>
<div align="center">
### 📊 Organization Activity Summary  
<sub><i>🕒 Last Updated: <b>{timestamp}</b></i></sub>
<table>
  <tr><td align="right">🔢 <b>Total Commits</b></td><td>{total_commits}</td></tr>
  <tr><td align="right">📅 <b>Active Days</b></td><td>{active_days}</td></tr>
  <tr><td align="right">🌅 <b>Today's Commits</b></td><td>{daily_commits}</td></tr>
  <tr><td align="right">📊 <b>Last 30 Days</b></td><td>{monthly_commits} commits</td></tr>
  <tr><td align="right">📈 <b>Average per Day</b></td><td>{avg_per_day}</td></tr>
  <tr><td align="right">🧾 <b>Last Commit</b></td><td>{last_commit}</td></tr>
  <tr><td align="right">🏆 <b>Top Repository</b></td><td><code>{top_repo}</code> ({top_repo_commits} commits)</td></tr>
</table>
</div>
<br/>
<details>
<summary align="center">📁 <strong>Repository Commit Breakdown</strong></summary>
<br/>
<div align="center">
<table>
  <tr>
    <th align="left">📂 Repository</th>
    <th align="center">🔢 Commits</th>
  </tr>""")
    
    for repo, commits in repos.items():
        f.write(f"  <tr><td><code>{repo}</code></td><td align=\"center\">{commits}</td></tr>\n")
    
    f.write("""\
</table>
</div>
<br/>
</details>
<hr/>
<div align="center">
## 🎯 Our Mission
> <strong>Software Guardians</strong> is a developer collective focused on creating  
> practical, reusable, and clean software structures.  
> We prioritize **code quality**, **simplicity**, and **consistency** across all tools and templates.
</div>
<br/>
<div align="center">
## 🛠️ Upcoming Goals
<table>
        <tr><td><span class="emoji">✅</span>Maintain boilerplates for C++, Java, Python, Kotlin, HTML, Gdscript with modular and clean architecture</td></tr>
        <tr><td><span class="emoji">✅</span>Qt GUI project structures</td></tr>
        <tr><td><span class="emoji">📱</span>Android Studio project templates and development guides</td></tr>
        <tr><td><span class="emoji">🎮</span>Godot 2D and 3D game project templates and development resources</td></tr>
        <tr><td><span class="emoji">🔧</span>CLI-based scaffolding tool</td></tr>
        <tr><td><span class="emoji">📐</span>Contribution & style guides</td></tr>
        <tr><td><span class="emoji">🌐</span>Multi-language README support</td></tr>
</table>
</div>
<hr/>
<div align="center">
## 🤝 Contributing
We welcome developers from all backgrounds and skill levels!
**Steps:**
1. 🍴 Fork the repository  
2. 🛠️ Choose an issue or add your own improvement  
3. 📬 Submit a pull request
</div>
---
<p align="center"><i>🧱 We don't just write code — we build a strong foundation.</i></p>
""")
