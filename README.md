<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SiPhox Weekly Operations Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
            background: #fafbfc;
            padding: 24px;
            color: #1a1a1a;
        }

        .dashboard-container {
            max-width: 1400px;
            margin: 0 auto;
        }

        .header {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            padding: 40px;
            border-radius: 16px;
            color: white;
            margin-bottom: 32px;
            box-shadow: 0 8px 24px rgba(99, 102, 241, 0.15);
            position: relative;
            overflow: hidden;
        }

        .header::before {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 300px;
            height: 300px;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            border-radius: 50%;
            transform: translate(30%, -30%);
        }

        .header h1 {
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 4px;
            position: relative;
            z-index: 1;
        }

        .header .siphox-brand {
            font-size: 14px;
            opacity: 0.95;
            font-weight: 600;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 16px;
            position: relative;
            z-index: 1;
        }

        .header .date-range {
            font-size: 18px;
            opacity: 0.95;
            font-weight: 500;
            position: relative;
            z-index: 1;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .header .date-range::before {
            content: '📅';
            font-size: 20px;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 24px;
        }

        .stat-card {
            background: white;
            padding: 28px;
            border-radius: 16px;
            box-shadow: 0 2px 8px rgba(99, 102, 241, 0.08);
            border: 1px solid rgba(99, 102, 241, 0.1);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: linear-gradient(180deg, #6366f1 0%, #8b5cf6 100%);
        }

        .stat-card:hover {
            box-shadow: 0 8px 24px rgba(99, 102, 241, 0.15);
            transform: translateY(-4px);
            border-color: rgba(99, 102, 241, 0.2);
        }

        .stat-label {
            font-size: 13px;
            color: #6b7280;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
        }

        .stat-value {
            font-size: 36px;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 4px;
        }

        .stat-change {
            font-size: 14px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .stat-change.positive {
            color: #10b981;
        }

        .stat-change.negative {
            color: #ef4444;
        }

        .stat-change.neutral {
            color: #6b7280;
        }

        .section {
            background: white;
            padding: 32px;
            border-radius: 12px;
            margin-bottom: 24px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
            border: 1px solid #e5e7eb;
        }

        .section-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 24px;
            padding-bottom: 16px;
            border-bottom: 2px solid #f3f4f6;
        }

        .section-icon {
            width: 40px;
            height: 40px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }

        .section-icon.purple {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        }

        .section-icon.blue {
            background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
        }

        .section-icon.green {
            background: linear-gradient(135deg, #10b981 0%, #14b8a6 100%);
        }

        .section-icon.orange {
            background: linear-gradient(135deg, #f59e0b 0%, #f97316 100%);
        }

        .section-icon.teal {
            background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%);
        }

        .section-title {
            font-size: 20px;
            font-weight: 700;
            color: #1a1a1a;
        }

        .metrics-row {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }

        .metric-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px;
            background: #f9fafb;
            border-radius: 8px;
            border-left: 4px solid;
        }

        .metric-item.primary {
            border-left-color: #6366f1;
        }

        .metric-item.success {
            border-left-color: #10b981;
        }

        .metric-item.warning {
            border-left-color: #f59e0b;
        }

        .metric-item.danger {
            border-left-color: #ef4444;
        }

        .metric-item.info {
            border-left-color: #3b82f6;
        }

        .metric-label {
            font-size: 14px;
            color: #6b7280;
            font-weight: 500;
        }

        .metric-value {
            font-size: 24px;
            font-weight: 700;
            color: #1a1a1a;
        }

        .percentage {
            font-size: 14px;
            color: #6b7280;
            font-weight: 600;
        }

        .progress-bar {
            width: 100%;
            height: 8px;
            background: #e5e7eb;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 8px;
        }

        .progress-fill {
            height: 100%;
            border-radius: 4px;
            transition: width 0.3s ease;
        }

        .progress-fill.success {
            background: linear-gradient(90deg, #10b981 0%, #059669 100%);
        }

        .progress-fill.warning {
            background: linear-gradient(90deg, #f59e0b 0%, #d97706 100%);
        }

        .progress-fill.danger {
            background: linear-gradient(90deg, #ef4444 0%, #dc2626 100%);
        }

        .breakdown-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .breakdown-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 16px;
            background: #f9fafb;
            border-radius: 8px;
            transition: background 0.2s ease;
        }

        .breakdown-item:hover {
            background: #f3f4f6;
        }

        .breakdown-name {
            font-weight: 600;
            color: #1a1a1a;
            font-size: 15px;
        }

        .breakdown-count {
            font-weight: 700;
            font-size: 18px;
            color: #6366f1;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .badge.success {
            background: #d1fae5;
            color: #065f46;
        }

        .badge.warning {
            background: #fef3c7;
            color: #92400e;
        }

        .badge.danger {
            background: #fee2e2;
            color: #991b1b;
        }

        .badge.info {
            background: #dbeafe;
            color: #1e40af;
        }

        .footer {
            margin-top: 32px;
            padding: 24px;
            text-align: center;
            color: #6b7280;
            font-size: 14px;
        }

        .footer .siphox-logo {
            font-weight: 700;
            color: #6366f1;
            font-size: 16px;
            margin-bottom: 8px;
        }

        @media (max-width: 768px) {
            .stats-grid {
                grid-template-columns: 1fr;
            }

            .metrics-row {
                grid-template-columns: 1fr;
            }

            .header h1 {
                font-size: 24px;
            }

            .stat-value {
                font-size: 28px;
            }
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <!-- Header -->
        <div class="header">
            <div class="siphox-brand">SiPhox Health</div>
            <h1>Weekly Operations Dashboard</h1>
            <div class="date-range">May 1 - May 8, 2026</div>
        </div>

        <!-- Key Stats Overview -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">Total Reports</div>
                <div class="stat-value">328</div>
                <div class="stat-change positive">
                    ↑ 109% vs last week
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-label">Samples Resulted</div>
                <div class="stat-value">312</div>
                <div class="stat-change positive">
                    ↑ 95.1% success rate
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-label">On-Time Rate</div>
                <div class="stat-value">87%</div>
                <div class="stat-change positive">
                    ↑ 3% vs last week
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-label">Report Backlog</div>
                <div class="stat-value">0</div>
                <div class="stat-change success">
                    ✓ All clear
                </div>
            </div>
        </div>

        <!-- Sample Processing Section -->
        <div class="section">
            <div class="section-header">
                <div class="section-icon purple">🧪</div>
                <div class="section-title">Sample Processing</div>
            </div>

            <div class="metrics-row">
                <div class="metric-item success">
                    <div>
                        <div class="metric-label">Resulted</div>
                        <div class="metric-value">312</div>
                    </div>
                    <span class="percentage">95.1%</span>
                </div>

                <div class="metric-item warning">
                    <div>
                        <div class="metric-label">Not Processed</div>
                        <div class="metric-value">16</div>
                    </div>
                    <span class="percentage">4.9%</span>
                </div>

                <div class="metric-item primary">
                    <div>
                        <div class="metric-label">Avg Turnaround</div>
                        <div class="metric-value">3.2d</div>
                    </div>
                    <span class="badge success">Fast</span>
                </div>
            </div>

            <div style="margin-top: 20px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                    <span style="font-weight: 600; color: #1a1a1a;">On-Time Processing (≤4 days)</span>
                    <span style="font-weight: 700; color: #6366f1;">271 / 312 (87%)</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill success" style="width: 87%;"></div>
                </div>
            </div>

            <div style="margin-top: 16px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                    <span style="font-weight: 600; color: #1a1a1a;">Delayed (5-7 days)</span>
                    <span style="font-weight: 700; color: #f59e0b;">41 / 312 (13%)</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill warning" style="width: 13%;"></div>
                </div>
            </div>
        </div>

        <!-- Fulfillment & Kits Section -->
        <div class="section">
            <div class="section-header">
                <div class="section-icon blue">📦</div>
                <div class="section-title">Fulfillment & Kits</div>
            </div>

            <div class="metrics-row">
                <div class="metric-item primary">
                    <div>
                        <div class="metric-label">Orders Placed</div>
                        <div class="metric-value">342</div>
                    </div>
                </div>

                <div class="metric-item primary">
                    <div>
                        <div class="metric-label">Kits Shipped</div>
                        <div class="metric-value">338</div>
                    </div>
                    <span class="percentage">98.8%</span>
                </div>

                <div class="metric-item success">
                    <div>
                        <div class="metric-label">Delivered</div>
                        <div class="metric-value">321</div>
                    </div>
                    <span class="percentage">94.4%</span>
                </div>

                <div class="metric-item warning">
                    <div>
                        <div class="metric-label">Exceptions</div>
                        <div class="metric-value">12</div>
                    </div>
                </div>
            </div>

            <div style="margin-top: 24px;">
                <h3 style="font-size: 16px; font-weight: 700; color: #1a1a1a; margin-bottom: 16px;">Fulfillment Vendor Breakdown</h3>
                <div class="breakdown-list">
                    <div class="breakdown-item">
                        <span class="breakdown-name">IMPILO</span>
                        <span class="breakdown-count">278 (81%)</span>
                    </div>
                    <div class="breakdown-item">
                        <span class="breakdown-name">ALOM</span>
                        <span class="breakdown-count">52 (15%)</span>
                    </div>
                    <div class="breakdown-item">
                        <span class="breakdown-name">Spot</span>
                        <span class="breakdown-count">12 (4%)</span>
                    </div>
                </div>
            </div>

            <div style="margin-top: 20px; padding: 16px; background: #fef3c7; border-left: 4px solid #f59e0b; border-radius: 8px;">
                <div style="font-weight: 600; color: #92400e; margin-bottom: 4px;">⚠️ Replacement Kits Sent</div>
                <div style="font-size: 24px; font-weight: 700; color: #92400e;">24</div>
            </div>
        </div>

        <!-- Clinical Section -->
        <div class="section">
            <div class="section-header">
                <div class="section-icon green">🏥</div>
                <div class="section-title">Clinical Operations</div>
            </div>

            <div class="metrics-row">
                <div class="metric-item success">
                    <div>
                        <div class="metric-label">Reports Published</div>
                        <div class="metric-value">328</div>
                    </div>
                </div>

                <div class="metric-item success">
                    <div>
                        <div class="metric-label">Assessments</div>
                        <div class="metric-value">21</div>
                    </div>
                </div>

                <div class="metric-item success">
                    <div>
                        <div class="metric-label">Expert Reviews</div>
                        <div class="metric-value">15</div>
                    </div>
                </div>

                <div class="metric-item success">
                    <div>
                        <div class="metric-label">Report Backlog</div>
                        <div class="metric-value">0</div>
                    </div>
                    <span class="badge success">Clear</span>
                </div>
            </div>
        </div>

        <!-- Sales Mix Section -->
        <div class="section">
            <div class="section-header">
                <div class="section-icon orange">💰</div>
                <div class="section-title">Sales Mix</div>
            </div>

            <div style="margin-bottom: 24px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <span style="font-weight: 600; color: #1a1a1a; font-size: 15px;">Ultimate Panel</span>
                    <span style="font-weight: 700; color: #6366f1; font-size: 18px;">156 orders (46%)</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 46%; background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 100%);"></div>
                </div>
            </div>

            <div style="margin-bottom: 24px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <span style="font-weight: 600; color: #1a1a1a; font-size: 15px;">Other Panels</span>
                    <span style="font-weight: 700; color: #3b82f6; font-size: 18px;">186 orders (54%)</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 54%; background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);"></div>
                </div>
            </div>

            <div class="metrics-row" style="margin-top: 24px;">
                <div class="metric-item primary">
                    <div>
                        <div class="metric-label">Add-On Sales</div>
                        <div class="metric-value">87</div>
                    </div>
                </div>

                <div class="metric-item primary">
                    <div>
                        <div class="metric-label">BioAge Sales</div>
                        <div class="metric-value">43</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- B2B Activity Section -->
        <div class="section">
            <div class="section-header">
                <div class="section-icon teal">🏢</div>
                <div class="section-title">B2B Activity</div>
            </div>

            <div class="metrics-row">
                <div class="metric-item primary">
                    <div>
                        <div class="metric-label">Active Accounts</div>
                        <div class="metric-value">24</div>
                    </div>
                </div>

                <div class="metric-item primary">
                    <div>
                        <div class="metric-label">B2B Kit Orders</div>
                        <div class="metric-value">156</div>
                    </div>
                </div>
            </div>

            <div style="margin-top: 24px;">
                <h3 style="font-size: 16px; font-weight: 700; color: #1a1a1a; margin-bottom: 16px;">Top Accounts by Volume</h3>
                <div class="breakdown-list">
                    <div class="breakdown-item">
                        <span class="breakdown-name">The Health Institute</span>
                        <span class="breakdown-count">52 orders</span>
                    </div>
                    <div class="breakdown-item">
                        <span class="breakdown-name">Salus</span>
                        <span class="breakdown-count">34 orders</span>
                    </div>
                    <div class="breakdown-item">
                        <span class="breakdown-name">Miracare</span>
                        <span class="breakdown-count">28 orders</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <div class="siphox-logo">SiPhox Health</div>
            <div>Generated automatically • Last updated: May 8, 2026 at 11:45 PM CET</div>
        </div>

    </div>
</body>
</html>
