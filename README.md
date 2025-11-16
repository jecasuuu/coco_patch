# 🛠️ COCO Command Center

**COCO** is a modular Streamlit dashboard designed for patch automation, system diagnostics, and cybersecurity compliance mapping. Built for academic and community deployment, it integrates Chocolatey-based patching with real-time system insights and exportable logs.

---

## 📁 Project Structure
coco-command-center/
├── layout_module.py # Main dashboard layout and tab navigation
├── patch_module.py  # Wrapped logic for patching and diagnostics

## 🚀 Features

### 🔧 Patch Dashboard (`patch_module.py`)
- Chocolatey-based patch automation
- Simulated rollback functionality
- Timestamped patch history
- Export logs as CSV or JSON

### 🧪 System Diagnostics (`layout_module.py`)
- Python version, platform, and executable path
- CPU and RAM usage metrics
- Installed and outdated Python packages
- Downloadable diagnostics report

### 🛡️ Compliance Map
- Maps system features to NIST cybersecurity standards
- Tracks readiness for OpenVAS integration and exploit simulation

---

## 🖼️ Optional Branding

To embed a custom logo:
1. Add `coco_logo.png` to the project folder
2. Insert this in `layout_module.py`:

```python
st.sidebar.image("coco_logo.png", width=120)

Requirements
- Python 3.8+
- Streamlit
- Chocolatey (auto-installed if missing)
- psutil, pandas

Install dependencies:
pip install streamlit psutil pandas

Run the Dashboard
streamlit run layout_module.py


Notes
- OpenVAS integration is planned but not required to run the dashboard
- All patch actions are logged with timestamps
- Diagnostics are generated dynamically and downloadable


Author
Created by Ma. Jedeca Mae P. Nones
Master’s in Computer Engineering | Data Steward | Systems Designer

