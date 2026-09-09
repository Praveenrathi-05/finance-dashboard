# Finance Dashboard

A data analysis tool that turns raw expense records into clear insights — spending by category, and spending trends over time — using pandas and matplotlib.

## Why this exists

A list of individual transactions doesn't answer the questions that actually matter: where does most of my money go, and is my spending trending up or down? This tool aggregates and visualizes expense data to surface those answers directly, instead of leaving them buried in a flat list of records.

## Features

- Loads expense data and computes total spending per category
- Bar chart of spending by category, sorted to show the biggest spend first
- Monthly spending trend as a line chart, once enough dated history exists
- Built on top of my own expense tracker project's data — a real, working pipeline from data entry to analysis

## A note on the data

Trend analysis requires dated records, which my original expense tracker didn't originally capture. That's been fixed going forward — every new expense now includes a timestamp. Historical entries logged before that change won't have dates, and any trend shown with only a few months of data should be read as illustrative of the tool working, not as a reliable real pattern — that takes genuine time and volume to establish honestly.

## How to run it

\`\`\`bash
python dashboard.py
\`\`\`

Requires Python 3.x, plus:
\`\`\`bash
pip install pandas matplotlib
\`\`\`

## What's next

- Month-over-month comparison, flagging categories that grew unusually
- A simple text or HTML summary alongside the charts
- Handling and clearly flagging missing/incomplete records rather than silently excluding them

## Built as part of a self-directed AI/ML learning journey — Project 5.# finance-dashboard
