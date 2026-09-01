import os
import sys
import json
import urllib.request
import tempfile
import subprocess
import time

CURRENT_VERSION = "v1.0.1"
REPO_URL = "https://api.github.com/repos/Bl4ke100/Kronos4k-Desktop--YT-Downloader/releases/latest"

def check_for_updates():
    try:
        req = urllib.request.Request(REPO_URL, headers={"User-Agent": "Kronos4K-Updater"})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            
        latest_tag = data.get("tag_name", "")
        if not latest_tag:
            return {"update_available": False}
            
        if latest_tag.lower() != CURRENT_VERSION.lower():
            # Find the exe asset
            download_url = None
            for asset in data.get("assets", []):
                if asset.get("name", "").lower().endswith(".exe"):
                    download_url = asset.get("browser_download_url")
                    break
                    
            if download_url:
                return {
                    "update_available": True,
                    "version": latest_tag,
                    "download_url": download_url,
                    "release_notes": data.get("body", "No release notes provided.")
                }
                
        return {"update_available": False, "current_version": CURRENT_VERSION}
    except Exception as e:
        return {"update_available": False, "error": str(e)}

def perform_update(download_url):
    try:
        if not getattr(sys, 'frozen', False):
            return {"success": False, "error": "Self-update only works in the compiled executable version."}
            
        # 1. Download to temp directory
        temp_dir = tempfile.gettempdir()
        new_exe_path = os.path.join(temp_dir, f"Kronos4K_Update_{int(time.time())}.exe")
        
        req = urllib.request.Request(download_url, headers={"User-Agent": "Kronos4K-Updater"})
        with urllib.request.urlopen(req, timeout=30) as response, open(new_exe_path, 'wb') as out_file:
            out_file.write(response.read())
            
        # 2. Get current exe path
        current_exe_path = sys.executable
        
        # 3. Create batch script
        bat_path = os.path.join(temp_dir, f"kronos_updater_{int(time.time())}.bat")
        
        # Batch logic:
        # Wait 3 seconds for python process to die
        # Move new exe over old exe
        # Launch new exe
        # Delete self
        bat_content = f"""@echo off
timeout /t 3 /nobreak > NUL
move /y "{new_exe_path}" "{current_exe_path}"
start "" "{current_exe_path}"
del "%~f0"
"""
        with open(bat_path, "w", encoding="utf-8") as f:
            f.write(bat_content)
            
        # 4. Launch batch script detached
        CREATE_NO_WINDOW = 0x08000000
        subprocess.Popen(["cmd.exe", "/c", bat_path], creationflags=CREATE_NO_WINDOW)
        
        return {"success": True}
        
    except Exception as e:
        return {"success": False, "error": str(e)}
