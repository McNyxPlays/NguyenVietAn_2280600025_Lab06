from scapy.all import *

def get_interfaces():
    result = subprocess.run(["ifconfig" if platform.system() != "Windows" else "ipconfig", "/all"], capture_output=True, text=True)
    output_lines = result.stdout.splitlines()[3:]
    interfaces = [line.split()[3] for line in output_lines if len(line.split()) > 4]
    return interfaces

def main():
    interfaces = get_interfaces()
    print("Available network interfaces:")
    for interface in interfaces:
        print(interface)

if __name__ == "__main__":
    main()