# GitHub Actions Setup Guide

## 📋 Project Setup

### 1. Add Source Code to GitHub

- Create a new **public** repository on GitHub
- Add your scraper source code to the repository

### 2. Repository Configuration

Navigate to your repository **Settings**:

#### A. Actions Permissions

- Go to: `Actions` → `General`
- Scroll to **Workflow permissions**
- Check ✅ **Read and write permissions**
- Click **Save**

#### B. Repository Secrets Configuration

- Go to: `Secrets and variables` → `Actions`
- Click **New repository secret** and add the following:

**Secret 1:**

```
Name: MY_USERNAME
Secret: [Your website account username]
```

**Secret 2:**

```
Name: MY_PASSWORD
Secret: [Your website account password]
```

## ⚙️ GitHub Actions Configuration

### Scheduled Execution

- The scraper is configured to run via a cron job **daily at 3:38 AM UTC**
- The workflow file is located at: `.github/workflows/actions.yml`

### ⚠️ Important Note on Scheduled Tasks

GitHub Actions scheduled workflows operate on a **best-effort basis** and are not 100% guaranteed to execute. According to [GitHub's documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule), scheduled tasks may be delayed or skipped during periods of high load.

### 🔧 Troubleshooting

If scheduled tasks fail to execute:

1. **Manual Trigger**: Run the workflow manually once
   - This can help "whitelist" the job for subsequent scheduled executions
   - Navigate to: `Actions` → click `workflow_dispatch`

2. **Monitor Execution**: Check the Actions tab regularly to ensure jobs are running as expected

## 📁 Repository Structure

```
├── .github/
│   └── workflows/
│       └── actions.yml   # GitHub Actions workflow
├── main.py/              # Script entry point
├── utils.py/             # utility functions
├── spreadsheet.py/       # manage xlsx output file
├── ticket.py/            # scraper business logic
├── driver.py/            # selenium setup
├── requirements.txt      # Python dependencies
└── data.xlsx             # scraped data sheet
└── README.md             # This file
```
