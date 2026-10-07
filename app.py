import requests
import json

# لیستی از سایت‌های عمومی برای مانیتورینگ
URLS = [
    "https://api.github.com",
    "https://httpstat.us/200",
    "https://httpstat.us/500"  # این لینک عمداً خطای 500 برمی‌گرداند
]

def check_health(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def generate_report():
    report = {}
    for url in URLS:
        status = "UP" if check_health(url) else "DOWN"
        report[url] = status
        print(f"[{status}] {url}")
    
    # ذخیره خروجی در یک فایل
    with open("health_report.json", "w") as f:
        json.dump(report, f, indent=4)
    
    return report

if __name__ == "__main__":
    print("Starting Health Check...")
    generate_report()
    print("Report saved to health_report.json")
