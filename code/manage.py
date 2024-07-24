import subprocess
import sys

def run_script(script_name):
    """Run a Python script concurrently."""
    return subprocess.Popen([sys.executable, script_name])

if __name__ == "__main__":
    server_process = run_script("server.py")
    buzzer_process = run_script("buzzer.py")
    
    # Wait for both processes to complete
    server_process.wait()
    buzzer_process.wait()