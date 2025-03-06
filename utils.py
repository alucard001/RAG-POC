# 在utils.py中添加资源监控
import psutil
import subprocess

def print_system_status():
    # 获取GPU内存使用（M1专用）
    gpu_mem = subprocess.check_output(
        "vmstat | grep 'Pages active' | awk '{print $3}'",
        shell=True).decode().strip()
    active_pages = int(gpu_mem.replace('.',''))
    gpu_usage = (active_pages * 4096) / 1024**3  # 转换为GB
    
    print(f"[System] GPU Memory Used: {gpu_usage:.1f}GB")
    print(f"[Ollama] CPU Usage: {psutil.cpu_percent()}%")