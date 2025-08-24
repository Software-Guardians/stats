import json

# JSON dosyasından verileri oku
with open('commit_summary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Verileri al
timestamp = data.get("timestamp", "N/A")
total_commits = data.get("total_commits", 0)
active_days = data.get("active_days", 0)
avg_per_day = data.get("average_per_day", 0)
monthly_commits = data.get("monthly_commits", 0)  # Son 30 gün
daily_commits = data.get("daily_commits", 0)      # Bugün
last_commit = data.get("last_commit", "N/A")
repos = data.get("repos", {})

# En çok commit'e sahip repo'yu bul
top_repo = max(repos, key=repos.get) if repos else "N/A"
top_repo_commits = repos.get(top_repo, 0)

# README.md dosyasını oluştur
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(f"""\
<div align="center">
  
# 🛡️ **SOFTWARE GUARDIANS**
### *✨ Create • Share • Protect Code ✨*

---

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=35&pause=1000&color=6A5ACD&center=true&vCenter=true&width=800&height=70&lines=Welcome+to+Software+Guardians+%F0%9F%9A%80;Code+Quality+%26+Innovation+%F0%9F%92%8E;Building+The+Future+Together+%F0%9F%8C%9F" alt="Typing SVG" />

---

<div style="display: flex; justify-content: center; gap: 15px; margin: 20px 0;">
  <img src="https://img.shields.io/github/last-commit/Software-Guardians/.github?color=FF6B6B&label=%F0%9F%94%84%20Last%20Update&style=for-the-badge&logo=github&logoColor=white&labelColor=2D3748"/>
  <img src="https://img.shields.io/badge/%E2%9A%A1%20Daily%20Activity-{daily_commits}%20commits-00D9FF?style=for-the-badge&labelColor=1A202C"/>
  <img src="https://img.shields.io/badge/%F0%9F%9A%80%20Monthly%20Activity-{monthly_commits}%20commits-32CD32?style=for-the-badge&labelColor=1A202C"/>
  <img src="https://img.shields.io/badge/%F0%9F%8F%86%20Total%20Commits-{total_commits}-FFD700?style=for-the-badge&labelColor=1A202C"/>
</div>

---

## 📊 **ORGANIZATION STATS** ⚡

*🕒 Real-time Update: **{timestamp}***

<table align="center">
  <tr>
    <td align="center" width="200">
      <img src="https://img.icons8.com/fluency/48/000000/code.png"/>
      <br/><strong>Total Commits</strong>
      <br/><span style="font-size: 24px; color: #FF6B6B;">{total_commits}</span>
    </td>
    <td align="center" width="200">
      <img src="https://img.icons8.com/fluency/48/000000/calendar.png"/>
      <br/><strong>Active Days</strong>
      <br/><span style="font-size: 24px; color: #4ECDC4;">{active_days}</span>
    </td>
    <td align="center" width="200">
      <img src="https://img.icons8.com/fluency/48/000000/lightning-bolt.png"/>
      <br/><strong>Today's Power</strong>
      <br/><span style="font-size: 24px; color: #FFE66D;">{daily_commits} commits</span>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://img.icons8.com/fluency/48/000000/trophy.png"/>
      <br/><strong>Top Repo</strong>
      <br/><code style="color: #FF6B6B;">{top_repo}</code>
      <br/><span style="color: #95A5A6;">{top_repo_commits} commits</span>
    </td>
    <td align="center">
      <img src="https://img.icons8.com/fluency/48/000000/graph.png"/>
      <br/><strong>Daily Average</strong>
      <br/><span style="font-size: 24px; color: #9B59B6;">{avg_per_day}</span>
    </td>
    <td align="center">
      <img src="https://img.icons8.com/fluency/48/000000/rocket.png"/>
      <br/><strong>Last 30 Days</strong>
      <br/><span style="font-size: 24px; color: #E74C3C;">{monthly_commits}</span>
    </td>
  </tr>
</table>

---

<details>
<summary align="center">
  <h3>📁 <strong>REPOSITORY BREAKDOWN</strong> 🔥</h3>
</summary>

<br/>

<table align="center">
  <tr>
    <th align="center">🏗️ <strong>Repository Name</strong></th>
    <th align="center">📊 <strong>Commits</strong></th>
    <th align="center">🌟 <strong>Status</strong></th>
  </tr>""")
    
    # Repo'ları commit sayısına göre sırala (büyükten küçüğe)
    sorted_repos = sorted(repos.items(), key=lambda x: x[1], reverse=True)
    
    # Her repo için satır ekle
    for i, (repo, commits) in enumerate(sorted_repos):
        # Renk seçimi (döngüsel)
        colors = ['FF6B6B', '4ECDC4', 'FFE66D', '9B59B6', 'E74C3C', 'F39C12', '1ABC9C', '3498DB', 'E67E22', '8E44AD', '27AE60', 'D35400', '2ECC71']
        color = colors[i % len(colors)]
        
        # Status belirleme
        if i == 0:
            status = "🔥 <strong>HOT</strong>"
        elif "Godot" in repo:
            status = "🎮 <strong>GAME</strong>"
        elif "Android" in repo or "Kotlin" in repo:
            status = "📱 <strong>MOBILE</strong>"
        elif "QT" in repo or "Qt" in repo:
            status = "🛠️ <strong>TOOL</strong>"
        elif "Python" in repo:
            status = "🐍 <strong>PYTHON</strong>"
        elif "Chat" in repo:
            status = "💬 <strong>CHAT</strong>"
        elif "Template" in repo or "template" in repo:
            status = "📋 <strong>TEMPLATE</strong>"
        elif "Guide" in repo or "Sources" in repo:
            status = "📚 <strong>GUIDE</strong>"
        elif "App" in repo:
            status = "📱 <strong>APP</strong>"
        else:
            status = "⚡ <strong>ACTIVE</strong>"
        
        f.write(f"""  <tr>
    <td align="center"><code>{repo}</code></td>
    <td align="center"><img src="https://img.shields.io/badge/{commits}-{color}?style=for-the-badge"/></td>
    <td align="center">{status}</td>
  </tr>
""")
    
    f.write("""\
</table>

</details>

---

## 🎯 **OUR MISSION** ✨

<img src="https://readme-typing-svg.herokuapp.com?font=Roboto&size=22&pause=1500&color=4ECDC4&center=true&vCenter=true&width=800&lines=Creating+Practical+%26+Reusable+Software+%F0%9F%92%8E;Prioritizing+Code+Quality+%26+Simplicity+%F0%9F%9A%80;Building+Consistent+Tools+%26+Templates+%E2%9C%A8" alt="Mission Typing SVG" />

**Software Guardians** is a developer collective focused on creating  
*practical*, *reusable*, and *clean* software structures.

We are the **guardians** of code quality, simplicity, and consistency! 🛡️

---

## 🛠️ **UPCOMING GOALS** 🚀

<table align="center">
  <tr>
    <th align="center">Status</th>
    <th align="center">Goal</th>
  </tr>
  <tr>
    <td align="center">✅</td>
    <td align="center"><strong>C++, Java, Python, Kotlin Templates</strong></td>
  </tr>
  <tr>
    <td align="center">✅</td>
    <td align="center"><strong>Qt GUI Project Structures</strong></td>
  </tr>
  <tr>
    <td align="center">📱</td>
    <td align="center"><strong>Android Studio Templates & Guides</strong></td>
  </tr>
  <tr>
    <td align="center">🎮</td>
    <td align="center"><strong>Godot 2D & 3D Game Templates</strong></td>
  </tr>
  <tr>
    <td align="center">🔧</td>
    <td align="center"><strong>CLI-based Scaffolding Tool</strong></td>
  </tr>
  <tr>
    <td align="center">📐</td>
    <td align="center"><strong>Contribution & Style Guides</strong></td>
  </tr>
  <tr>
    <td align="center">🌐</td>
    <td align="center"><strong>Multi-language README Support</strong></td>
  </tr>
</table>

---

## 🤝 **JOIN THE GUARDIANS** 🛡️

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=28&pause=2000&color=FF6B6B&center=true&vCenter=true&width=600&lines=We+Welcome+All+Developers!+%F0%9F%91%A9%E2%80%8D%F0%9F%92%BB;From+Beginners+to+Experts+%F0%9F%92%AA;Join+Our+Mission!+%F0%9F%9A%80" alt="Join Us Typing SVG" />

<br/>

### 🌟 **3 Simple Steps to Become a Guardian:**

<table align="center">
  <tr>
    <td align="center" width="200">
      <img src="https://img.icons8.com/fluency/64/000000/code-fork.png"/>
      <br/><br/>
      <strong>1️⃣ FORK</strong>
      <br/>Fork the repository
      <br/>and clone it locally
    </td>
    <td align="center" width="200">
      <img src="https://img.icons8.com/fluency/64/000000/wrench.png"/>
      <br/><br/>
      <strong>2️⃣ BUILD</strong>
      <br/>Choose an issue or
      <br/>add your improvement
    </td>
    <td align="center" width="200">
      <img src="https://img.icons8.com/fluency/64/000000/pull-request.png"/>
      <br/><br/>
      <strong>3️⃣ SHARE</strong>
      <br/>Submit your awesome
      <br/>pull request
    </td>
  </tr>
</table>

<br/>

<div style="display: flex; justify-content: center; gap: 10px;">
  <img src="https://img.shields.io/badge/%F0%9F%94%A5%20Contributors-Welcome-FF6B6B?style=for-the-badge&logo=github"/>
  <img src="https://img.shields.io/badge/%F0%9F%92%A1%20Ideas-Appreciated-4ECDC4?style=for-the-badge&logo=lightbulb"/>
  <img src="https://img.shields.io/badge/%F0%9F%9A%80%20Innovation-Encouraged-FFE66D?style=for-the-badge&logo=rocket"/>
</div>

---

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer&text=&fontSize=40&fontAlignY=65&desc=&descAlignY=51&descAlign=62"/>

<br/>

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=30&pause=3000&color=6A5ACD&center=true&vCenter=true&width=800&lines=We+don't+just+write+code...+%F0%9F%92%BB;We+build+strong+foundations!+%F0%9F%8F%97%EF%B8%8F;Welcome+to+the+future+of+coding!+%F0%9F%9A%80" alt="Footer Typing SVG" />

<br/><br/>

**🛡️ GUARDIANS OF CODE QUALITY 🛡️**

<img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F%20%26%20Code-FF1744?style=for-the-badge"/>

</div>
""")

print("✅ README.md dosyası başarıyla oluşturuldu!")
print(f"📊 İşlenen veriler:")
print(f"   • Toplam commit: {total_commits}")
print(f"   • Aktif günler: {active_days}")
print(f"   • Günlük commit: {daily_commits}")
print(f"   • Aylık commit: {monthly_commits}")
print(f"   • En popüler repo: {top_repo} ({top_repo_commits} commit)")
print(f"   • İşlenen repo sayısı: {len(repos)}")
