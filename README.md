# 📊 SiPhox Health Weekly Operations Dashboard

Automated weekly operations dashboard that pulls live metrics from Slack and displays them in a clean, Notion-style interface.

**Live Dashboard:** [https://evakrasevec.github.io/metrics/](https://evakrasevec.github.io/metrics/)

---

## ✨ Features

- 🤖 **Automated Updates** - Runs every Monday at 9 AM CET
- 📈 **Live Metrics** - Pulls real data from Slack channels
- 🎨 **Notion-Style Design** - Clean, minimal interface that embeds seamlessly
- 📱 **Responsive** - Works on desktop, tablet, and mobile
- 🔄 **GitHub Pages** - Auto-deploys on push

---

## 📋 What It Tracks

### Currently Automated (from Slack)
✅ **Clinical Stats** (from #kit-health-expert-review-pavel)
- Total reports published
- Total assessments completed
- Report backlog
- Assessment backlog
- Expert reviews completed

### Coming Soon
⏳ **Fulfillment Metrics** (from Admin Dashboard)
- Sample processing stats
- On-time delivery rate
- Vendor breakdown (IMPILO, ALOM, Spot)

⏳ **Sales Mix** (from Admin Dashboard)
- Ultimate vs other panels
- Add-on sales
- BioAge sales

⏳ **B2B Activity** (from Admin Dashboard)
- Active accounts
- Kit orders by account

---

## 🚀 Quick Setup

### 1. Clone or Download This Repository

```bash
git clone https://github.com/evakrasevec/evakrasevec.github.io.git
cd evakrasevec.github.io
```

### 2. Add Anthropic API Key to GitHub Secrets

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `ANTHROPIC_API_KEY`
4. Value: Your API key from [Anthropic Console](https://console.anthropic.com/)
5. Click **Add secret**

### 3. Enable GitHub Pages

1. Go to **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: **main** → **/ (root)**
4. Click **Save**

### 4. Test the Automation

1. Go to **Actions** tab
2. Click **Generate Weekly Dashboard**
3. Click **Run workflow** → **Run workflow**
4. Watch it update! 🎉

---

## ⏰ Schedule

- **Automatic:** Every Monday at 9:00 AM CET
- **Manual:** Click "Run workflow" in GitHub Actions anytime

---

## 🎯 How to Embed in Notion

### Method 1: Full-Width Embed (Recommended)

1. Open your Notion page
2. Type `/embed`
3. Paste: `https://evakrasevec.github.io/metrics/`
4. Press Enter
5. Click `•••` menu → **Full width** ✅
6. Drag bottom edge to show full dashboard

### Method 2: Bookmark

1. Type `/bookmark`
2. Paste the URL
3. Creates a clickable card

---

## 📁 File Structure

```
.
├── index.html                      # Dashboard HTML (Notion-style design)
├── generate_weekly_dashboard.py    # Python automation script
├── .github/
│   └── workflows/
│       └── weekly-dashboard.yml    # GitHub Actions workflow
└── README.md                       # This file
```

---

## 🔧 How It Works

```
Every Monday 9 AM CET
        ↓
GitHub Actions triggers
        ↓
Python script runs
        ↓
Searches Slack for Barbara's latest stats
        ↓
Generates new HTML with live data
        ↓
Commits & pushes to GitHub
        ↓
GitHub Pages auto-deploys
        ↓
Dashboard updates at evakrasevec.github.io/metrics/
        ↓
Notion embed refreshes automatically
        ↓
Posts notification to Slack 📢
```

---

## 🛠️ Manual Update

Want to update the dashboard manually? Run locally:

```bash
# Install dependencies
pip install anthropic

# Set API key
export ANTHROPIC_API_KEY="your-key-here"

# Run the script
python generate_weekly_dashboard.py

# Commit and push
git add index.html
git commit -m "Manual dashboard update"
git push
```

---

## 📊 Data Sources

### Slack Channels
- `#kit-health-expert-review-pavel` - Clinical stats (Barbara's weekly posts)

### Admin Dashboard (Coming Soon)
- Fulfillment Analytics Dashboard
- Sales by SKU Dashboard
- B2B Account Management

---

## 🎨 Design

The dashboard uses a **clean Notion-style aesthetic**:
- Pure white background
- Minimal borders (1px dividers)
- Notion color palette (`#37352f`, `#787774`, `#9b9a97`)
- No shadows, no rounded corners
- Clean typography with generous spacing
- Responsive grid layout

**Perfect for embedding** - looks native in Notion pages!

---

## 🔐 Security

- ✅ API key stored as encrypted GitHub Secret
- ✅ Script runs in isolated GitHub Actions environment
- ✅ Only accesses approved Slack channels
- ✅ No sensitive data in code
- ✅ Public dashboard shows aggregated metrics only

---

## 🐛 Troubleshooting

### Dashboard not updating?

1. Check **Actions** tab for errors
2. Verify `ANTHROPIC_API_KEY` is set in Secrets
3. Check Barbara posted stats in `#kit-health-expert-review-pavel`

### Notion embed not refreshing?

1. Click the embed in Notion
2. Click the refresh icon (↻)
3. Or reload the Notion page

### Want to add more metrics?

Edit `generate_weekly_dashboard.py` and add new data sources:

```python
def get_fulfillment_metrics():
    # Add Admin Dashboard API call here
    pass
```

---

## 📞 Support

Questions? 
- Check GitHub Actions logs: **Actions** tab
- Check Slack: `#kit-software-development`
- Dashboard URL: https://evakrasevec.github.io/metrics/

---

## 📜 License

Internal SiPhox Health tool. Not for public distribution.

---

**Auto-generated dashboard** 🤖  
Last setup: May 8, 2026  
Maintained by: Eva Molek Kraševec
