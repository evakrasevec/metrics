#!/usr/bin/env python3
"""
SiPhox Health Weekly Dashboard Generator
Automatically pulls metrics from Slack and generates HTML dashboard
"""

import os
import re
from datetime import datetime, timedelta
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def get_latest_clinical_stats():
    """
    Fetch latest clinical stats from Barbara's Slack posts
    Returns: dict with clinical metrics
    """
    print("🔍 Searching for Barbara's latest clinical stats...")
    
    # Use Claude with Slack MCP to search for latest stats
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": """Search Slack channel #kit-health-expert-review-pavel for the most recent message from Barbara Evdokimova containing "Clinical Weekly Stats". 
            
Extract these exact numbers:
- Total reports
- Total assessments  
- Report backlog
- Assessment backlog
- Expert reviews

Return ONLY a JSON object with these fields, no other text:
{
    "reports": 0,
    "assessments": 0, 
    "report_backlog": 0,
    "assessment_backlog": 0,
    "expert_reviews": 0,
    "week_ending": "YYYY-MM-DD"
}"""
        }],
        mcp_servers=[{
            "type": "url",
            "url": "https://mcp.slack.com/mcp",
            "name": "slack-mcp"
        }]
    )
    
    # Extract JSON from response
    response_text = message.content[0].text
    # Parse the JSON (remove any markdown formatting)
    import json
    json_text = response_text.strip()
    if json_text.startswith("```json"):
        json_text = json_text.split("```json")[1].split("```")[0]
    elif json_text.startswith("```"):
        json_text = json_text.split("```")[1].split("```")[0]
    
    stats = json.loads(json_text.strip())
    print(f"✅ Found clinical stats: {stats['reports']} reports, {stats['assessments']} assessments")
    
    return stats


def get_week_range():
    """Get the date range for current week (Monday to Sunday)"""
    today = datetime.now()
    # Find the most recent Monday
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)
    
    return monday.strftime("%B %d"), sunday.strftime("%B %d, %Y")


def generate_dashboard_html(clinical_stats):
    """
    Generate the complete HTML dashboard with live data
    """
    start_date, end_date = get_week_range()
    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p CET")
    
    # Read the template
    template_path = "./index.html"
    with open(template_path, 'r') as f:
        html = f.read()
    
    # Replace placeholders with live data
    replacements = {
        # Date range in header
        'May 1 - May 8, 2026': f'{start_date} - {end_date}',
        
        # Key stats (top 4 cards)
        '<div class="stat-value">328</div>': f'<div class="stat-value">{clinical_stats["reports"]}</div>',
        '<div class="stat-value">312</div>': f'<div class="stat-value">{clinical_stats["reports"] - clinical_stats["report_backlog"]}</div>',
        
        # Clinical section
        'Total reports - 328': f'Total reports - {clinical_stats["reports"]}',
        'Total assessments - 21': f'Total assessments - {clinical_stats["assessments"]}',
        'Report backlog - 0': f'Report backlog - {clinical_stats["report_backlog"]}',
        'Assessment backlog - 0': f'Assessment backlog - {clinical_stats["assessment_backlog"]}',
        'Expert reviews - 15': f'Expert reviews - {clinical_stats["expert_reviews"]}',
        
        # Clinical operations metrics
        '<div class="metric-value">328</div>': f'<div class="metric-value">{clinical_stats["reports"]}</div>',
        '<div class="metric-value">21</div>': f'<div class="metric-value">{clinical_stats["assessments"]}</div>',
        '<div class="metric-value">15</div>': f'<div class="metric-value">{clinical_stats["expert_reviews"]}</div>',
        '<div class="metric-value">0</div>': f'<div class="metric-value">{clinical_stats["report_backlog"]}</div>',
        
        # Footer timestamp
        'Last updated: May 8, 2026 at 11:45 PM CET': f'Last updated: {timestamp}'
    }
    
    for old, new in replacements.items():
        html = html.replace(old, new, 1)  # Replace only first occurrence
    
    return html


def save_dashboard(html_content, output_path="./index.html"):
    """Save the generated dashboard"""
    with open(output_path, 'w') as f:
        f.write(html_content)
    print(f"✅ Dashboard saved to {output_path}")


def post_to_slack(channel_id="C03PRQQNHLL"):
    """
    Post notification to Slack that dashboard is updated
    """
    print("📢 Posting update to Slack...")
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[{
            "role": "user",
            "content": f"""Send this message to Slack channel {channel_id}:

📊 **Weekly Operations Dashboard Updated**

The weekly dashboard has been automatically updated with the latest metrics.

🔗 View dashboard: https://evakrasevec.github.io/metrics/

✅ Clinical stats from Barbara's latest post
📈 All sections updated
🕒 Generated: {datetime.now().strftime("%B %d, %Y at %I:%M %p CET")}

cc: <@U09V97M4U4A> <@UURJ9HHMJ>"""
        }],
        mcp_servers=[{
            "type": "url",
            "url": "https://mcp.slack.com/mcp",
            "name": "slack-mcp"
        }]
    )
    
    print("✅ Slack notification sent")


def main():
    """
    Main execution function
    """
    print("\n" + "="*60)
    print("🚀 SiPhox Weekly Dashboard Generator")
    print("="*60 + "\n")
    
    try:
        # Step 1: Get clinical stats from Slack
        clinical_stats = get_latest_clinical_stats()
        
        # Step 2: Generate HTML with live data
        print("\n📝 Generating dashboard HTML...")
        html = generate_dashboard_html(clinical_stats)
        
        # Step 3: Save the dashboard
        print("\n💾 Saving dashboard...")
        save_dashboard(html)
        
        # Step 4: Post to Slack
        print("\n📢 Notifying team...")
        post_to_slack()
        
        print("\n" + "="*60)
        print("✅ Dashboard generation complete!")
        print("="*60 + "\n")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
