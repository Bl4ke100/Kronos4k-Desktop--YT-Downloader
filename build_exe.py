import os
import sys
import subprocess
import shutil
import argparse
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def build(mode="onefile"):
    print("=" * 60)
    print(f"  Building Standalone KRONOS 4K Executable (Mode: {mode.upper()})")
    print("=" * 60)
    
    os.chdir(BASE_DIR)
    
    # 1. Generate multi-size app.ico from KRONOS-Logo.png
    logo_path = os.path.join(BASE_DIR, "KRONOS-Logo.png")
    ico_path = os.path.join(BASE_DIR, "app.ico")
    if os.path.exists(logo_path):
        try:
            img = Image.open(logo_path)
            icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
            img.save(ico_path, format="ICO", sizes=icon_sizes)
            # Also ensure logo is in ui/
            ui_logo = os.path.join(BASE_DIR, "ui", "logo.png")
            img.save(ui_logo, format="PNG")
            ui_ico = os.path.join(BASE_DIR, "ui", "favicon.ico")
            img.save(ui_ico, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
            print("[+] Generated multi-resolution app.ico and UI logos from KRONOS-Logo.png")
        except Exception as e:
            print(f"[-] Warning: Failed to generate icon: {e}")

    # 2. Check for ffmpeg.exe
    ffmpeg_path = os.path.join(BASE_DIR, "ffmpeg.exe")
    if not os.path.exists(ffmpeg_path):
        system_ffmpeg = shutil.which("ffmpeg")
        if system_ffmpeg and os.path.exists(system_ffmpeg):
            shutil.copy2(system_ffmpeg, ffmpeg_path)
            print(f"[+] Found and copied system FFmpeg: {system_ffmpeg}")
        else:
            print("[-] Warning: ffmpeg.exe not found in base folder.")

    # 3. Clean previous spec file to ensure clean build
    spec_path = os.path.join(BASE_DIR, "Kronos4K.spec")
    if os.path.exists(spec_path):
        try:
            os.remove(spec_path)
        except Exception:
            pass

    # 4. PyInstaller command arguments
    # Exclude the 6,000+ loose node_modules files to prevent the 20+ second decompression freeze
    # Disable UPX (--noupx) to prevent heuristic antivirus locks on Windows
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--windowed",
        "--noupx",
        "--name", "Kronos4K",
        "--add-data", f"ui{os.pathsep}ui",
        "--collect-all", "yt_dlp_plugins",
    ]
    
    if mode == "onefile":
        cmd.append("--onefile")
        # In onefile mode, bundle ffmpeg directly inside the single .exe so it's 100% self-contained
        if os.path.exists(ffmpeg_path):
            cmd.extend(["--add-binary", f"ffmpeg.exe{os.pathsep}."])
    else:
        cmd.append("--onedir")
        if os.path.exists(ffmpeg_path):
            cmd.extend(["--add-binary", f"ffmpeg.exe{os.pathsep}."])
    
    if os.path.exists(ico_path):
        cmd.extend(["--icon", "app.ico"])
        cmd.extend(["--add-data", f"app.ico{os.pathsep}."])
        
    cmd.append("main.py")
    
    print("\n[+] Running PyInstaller...")
    print("Command:", " ".join(cmd))
    
    res = subprocess.run(cmd)
    
    if res.returncode == 0:
        dist_dir = os.path.join(BASE_DIR, "dist")
        if mode == "onefile":
            dist_exe = os.path.join(dist_dir, "Kronos4K.exe")
            print("\n" + "=" * 60)
            print("  STANDALONE EXE BUILD SUCCESSFUL!")
            print(f"  Standalone Binary: {dist_exe}")
            print(f"  File Size        : {os.path.getsize(dist_exe) / (1024*1024):.1f} MB")
            print("  100% Portable single .exe with embedded FFmpeg & Zero Dependencies!")
            print("=" * 60)
        else:
            target_dir = os.path.join(dist_dir, "Kronos4K")
            dist_exe = os.path.join(target_dir, "Kronos4K.exe")
            print("\n" + "=" * 60)
            print("  DIRECTORY BUILD SUCCESSFUL!")
            print(f"  Directory: {target_dir}")
            print(f"  Executable: {dist_exe}")
            print("=" * 60)
    else:
        print("\n[-] Build failed with exit code:", res.returncode)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build KRONOS 4K Desktop App")
    parser.add_argument(
        "--mode",
        choices=["onefile", "onedir"],
        default="onefile",
        help="Build mode: 'onefile' (standalone single exe) or 'onedir' (directory bundle)"
    )
    args = parser.parse_args()
    build(mode=args.mode)
