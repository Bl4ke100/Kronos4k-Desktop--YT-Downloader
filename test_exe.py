import sys
import traceback
import time

def main():
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    
    sys.stdout = None
    sys.stderr = None
    sys.stdin = None
    
    try:
        from downloader_core import create_download_task, active_tasks
        
        task_id = create_download_task(
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            option_id="video_1080",
            option_type="video",
            save_dir=".",
            browser_cookie=None
        )
        
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        print("Task started, waiting for completion...")
        
        for _ in range(10):
            if task_id in active_tasks:
                break
            time.sleep(1)
            
        while True:
            task = active_tasks.get(task_id)
            if not task:
                break
            status = task.get("status")
            if status in ["completed", "error", "stopped"]:
                print(f"Task finished with status: {status}")
                if status == "error":
                    print(f"Error details:\n{task.get('error')}")
                break
            time.sleep(1)
            
    except Exception as e:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        print("CRASHED WITH TRACEBACK:")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()
