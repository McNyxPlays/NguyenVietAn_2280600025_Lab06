import requests

def get_vendor_by_mac(mac):
    try:
        response = requests.get(f"https://api.macvendors.com/{mac}")
        if response.status_code == 200:
            return response.text
        else:
            return "Unknown"
    except Exception as e:
        print(f"Error fetching vendor information: {e}")
        return "Unknown"

def main():
    ip_range = "192.168.0.1/24"
    devices = local_network_scan(ip_range)
    print("Devices on the local network:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}, Vendor: {device['vendor']}")

if __name__ == "__main__":
    main()