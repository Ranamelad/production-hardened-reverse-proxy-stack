# 🛡️ Production-Hardened Reverse Proxy Stack

A high-performance, security-focused Reverse Proxy architecture built to withstand production-grade traffic and mitigate common security threats.

## 🚀 Overview
This project demonstrates a real-world scenario of implementing a **Reverse Proxy** with **Nginx** and a **Python application**, focusing on "Defense in Depth" principles. It showcases the ability to containerize applications while applying rigorous security hardening techniques.

## 🔑 Key Security Implementations
- **Distroless Images:** Minimized attack surface by using minimal base images (no package managers/shells).
- **Read-Only File System:** Configured containers to prevent write-access to system files.
- **Network Isolation:** Micro-segmentation between Proxy and App layers using internal networks.
- **Rate Limiting:** Mitigated DoS/DDoS vectors using Nginx request limiting.
- **No-new-privileges:** Dropped excessive Linux capabilities for container runtime security.

## 🏗️ Architecture
- **Proxy Layer:** Nginx (Reverse Proxy/Load Balancer)
- **App Layer:** Python Flask Application
- **Orchestration:** Docker Compose

## 🛠️ Tech Stack
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ⚡ Quick Start
Ensure you have Docker installed.

1. **Clone the repository:**
   `git clone <your-repo-url>`
2. **Build and Spin up the stack:**
   ```bash
   docker compose up -d --build