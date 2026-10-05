# Python for AWS DevOps Automation 🐍☁️

This repository showcases the power of **Boto3** (AWS SDK for Python) to automate operational tasks that are too complex for simple CLI commands or Terraform. It focuses on creating "Self-Healing" and "Automated" infrastructure patterns.

## 🎯 Objectives
The primary goal is to reduce manual operational toil by scripting repetitive tasks, implementing automated backups, and integrating infrastructure management into Python applications.

---

## 🛠️ Automation Projects

### 💾 Automated S3 Backup System
**Files**: `upload_backup_to_s3_bucket.py`, `create_bucket.py`
Implemented a Python-based backup utility that:
- Dynamically creates S3 buckets if they don't exist.
- Handles the secure upload of local backups to AWS S3.
- Provides error handling for AWS API limits and permission issues.

### 🏗️ Terraform Orchestration via Python
**Path**: `/creating ec2 instance using terraform via python`
A hybrid approach where Python is used as a wrapper to trigger Terraform executions. This allows for:
- Dynamic input generation based on external API data.
- Complex conditional logic before triggering an `apply`.
- Integration of IaC into a larger Python-based automation framework.

---

## 🛠️ Tech Stack
- **Language**: `Python 3.x`
- **AWS SDK**: `Boto3`
- **Infrastructure**: `AWS S3`, `AWS EC2`
- **Tooling**: `Terraform` (Orchestrated via Python)

## 🚀 Quick Start

### Prerequisites
- Python 3.x installed
- `pip install boto3`
- AWS Credentials configured via `~/.aws/credentials`

### Running the Automation
```bash
# Create a new bucket
python create_bucket.py

# Upload backup to S3
python upload_backup_to_s3_bucket.py
```

---

## 🧠 DevOps Insights
- **Reducing Toil**: By automating S3 backups, I eliminated the need for manual snapshots, reducing the risk of human error.
- **Extensibility**: Using Boto3 allows for the creation of custom Lambda functions to trigger these scripts on a schedule (EventBridge).
- **Hybrid Automation**: Combining Python with Terraform provides the best of both worlds: the declarative power of IaC and the imperative flexibility of Python.
