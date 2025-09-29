# 🎓 Masters Portfolio — Semester Update Workflow

This guide outlines how to update your portfolio as new semester content becomes available. It includes folder setup, dashboard regeneration, previewing, and Git syncing—clearly mapped to the tools and applications used.

---

## 🧭 Tools & Applications Overview

| Task | Tool | Application |
|------|------|-------------|
| Create folders & metadata | `setup_semester.sh` | Codespaces Terminal |
| Add notebooks/projects | Manual | VS Code Editor (inside Codespaces) |
| Update dashboard | `generate_index.py` | Codespaces Terminal |
| Preview dashboard | `live-server` or `make serve` | Codespaces Terminal + Browser |
| Track & push changes | Git | Codespaces Terminal |
| Verify updates | GitHub Web | Browser |

---

## 🔄 Step-by-Step Instructions

### ✅ 1. Open Your Codespace
**Application:** GitHub Web  
- Go to your repo → Click **Code** → **Codespaces** tab → Open your Codespace

---

### 📁 2. Create a New Semester Scaffold
**Application:** Codespaces Terminal  
Run:

```bash
./setup_semester.sh 2025-S2 "Semester 2, 2025" "📘" "#4A90E2"
