---
title: AI-Browser-Organizer
emoji: 🌍
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# 🌐 AI-Powered Browser Content Organizer

### 🚀 Submission for OpenEnv Hackathon

**GitHub Repository**: [https://github.com/madhusri829/my_env](https://github.com/madhusri829/my_env)

## 📌 Overview
This project is an AI-driven browser history organizer built using the **OpenEnv** framework and **Gymnasium**. It helps users manage their digital life by classifying links, detecting security threats, and providing smart productivity reminders.

## ✨ Key Features
- **Smart Classification**: Automatically sorts links into categories like *Study*, *Hackathon*, *Personal*, and *Movies*.
- **Security Shield**: Detects potentially harmful `http://` links or phishing domains.
- **Time-Based Groups**: Organizes browsing history by the month of access.
- **Usage Tracking**: Identifies "Most Used" categories to understand user behavior.
- **Proactive Reminders**: Suggests actions like "Continue learning Python today!" based on history.

## 🛠️ Technical Implementation
- **Environment**: Custom `Gymnasium` environment (`env.py`).
- **State Space**: Includes Page Title, URL, Date, and Usage Counts.
- **Action Space**: 12 discrete actions covering classification, security, and reminders.
- **Deployment**: Containerized using **Docker** and hosted on **Hugging Face Spaces**.

## 🚀 How to Run Locally
If you have Docker installed, you can test this environment locally:

1. **Build the image**:
   ```bash
   docker build -t browser-ai .