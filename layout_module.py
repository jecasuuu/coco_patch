import streamlit as st
import subprocess
import shutil
import pandas as pd
import sys
import platform
import psutil
import io
import json
from datetime import datetime

# Simulated lookup table
lookup_table = pd.DataFrame([
    {"Software Name": "Google Chrome", "Package": "googlechrome"},
    {"Software Name": "Mozilla Firefox", "Package": "firefox"},
    {"Software Name": "Zoom", "Package": "zoom"},
    {"Software Name": "7-Zip", "Package": "7zip"},
])

# Initialize patch log
if "patch_log" not in st.session_state:
    st.session_state.patch_log = []

# Chocolatey check/install
def check_and_install_choco():
    if shutil.which("choco") is None:
        with st.spinner("Installing Chocolatey..."):
            subprocess.run([
                "powershell",
                "Set-ExecutionPolicy Bypass -Scope Process -Force; "
                "[System.Net.ServicePointManager]::SecurityProtocol = "
                "[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; "
                "iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
            ], shell=True)
        st.success("Chocolatey installed successfully.")
    else:
        st.success("Chocolatey is ready.")

# Apply patch
def apply_patch(package_name):
    check_and_install_choco()
    with st.spinner(f"Patching {package_name}..."):
        subprocess.run(["choco", "upgrade", package_name, "-y"], shell=True)
    st.session_state.patch_log.append({
        "package": package_name,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    st.success(f"Patch applied to {package_name}")

# Rollback simulation
def rollback_patch():
    if st.session_state.patch_log:
        last_patch = st.session_state.patch_log.pop()
        st.warning(f"Simulated rollback for {last_patch['package']} — {last_patch['timestamp']}")
    else:
        st.info("No patches to roll back.")

# Export functions
def export_csv():
    df = pd.DataFrame(st.session_state.patch_log)
    return df.to_csv(index=False).encode("utf-8")

def export_json():
    return json.dumps(st.session_state.patch_log, indent=2).encode("utf-8")

# Diagnostics report
def generate_diagnostics():
    buffer = io.StringIO()
    buffer.write("System Diagnostics Report\n=========================\n\n")
    buffer.write(f"Python version: {sys.version}\n")
    buffer.write(f"Platform: {platform.platform()}\n")
    buffer.write(f"Executable path: {sys.executable}\n\n")

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    buffer.write(f"CPU Usage: {cpu}%\n")
    buffer.write(f"RAM Usage: {ram.percent}% ({ram.used // (1024 ** 2)} MB used of {ram.total // (1024 ** 2)} MB)\n\n")

    buffer.write("Installed Packages:\n")
    result = subprocess.run(["pip", "list"], capture_output=True, text=True)
    buffer.write(result.stdout + "\n")

    buffer.write("Patch History:\n")
    if st.session_state.patch_log:
        for i, entry in enumerate(st.session_state.patch_log[::-1], 1):
            buffer.write(f"{i}. {entry['package']} — {entry['timestamp']}\n")
    else:
        buffer.write("No patches applied yet.\n")
    return buffer.getvalue()

# Wrapped UI function for Patch Dashboard
def show_patch_tab():
    st.title("🛠️ Patch Automation Dashboard")
    selected = st.selectbox("Select software to patch:", lookup_table["Software Name"])
