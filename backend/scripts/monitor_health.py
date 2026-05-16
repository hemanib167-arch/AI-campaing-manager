import requests
import time
import sys
from datetime import datetime

BASE_URL = "http://localhost:8000"
ENDPOINTS = [
    {"name": "General Health", "url": "/api/health/"},
    {"name": "Projects API", "url": "/api/projects/"},
    {"name": "Campaigns API", "url": "/api/campaign_entities/"},
    {"name": "Assets API", "url": "/api/assets/"},
    {"name": "Analytics API", "url": "/api/analytics/"},
]

def check_health():
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] --- Health Check ---")
    all_ok = True
    
    for ep in ENDPOINTS:
        try:
            # Ping with GET
            response = requests.get(f"{BASE_URL}{ep['url']}", timeout=2)
            # 200 is success, 405 means the route exists but expects POST (which is fine for a health check)
            if response.status_code in [200, 405]:
                print(f"[OK] {ep['name']}: Running (Status: {response.status_code})")
            else:
                print(f"[WARN] {ep['name']}: Responded with {response.status_code}")
                all_ok = False
        except requests.exceptions.RequestException as e:
            print(f"[DOWN] {ep['name']}: ERROR ({str(type(e).__name__)})")
            all_ok = False
            
    return all_ok

if __name__ == "__main__":
    interval = 10 # seconds
    if len(sys.argv) > 1:
        interval = int(sys.argv[1])
        
    print(f"Starting 6E Creative Studio Health Monitor (Interval: {interval}s)")
    print(f"Target: {BASE_URL}")
    
    try:
        # Run at least once
        check_health()
        
        # Then loop if not in "one-shot" mode (if interval > 0)
        if interval > 0:
            while True:
                time.sleep(interval)
                check_health()
    except KeyboardInterrupt:
        print("\nMonitor stopped.")
