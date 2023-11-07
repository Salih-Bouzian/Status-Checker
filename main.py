import argparse
from server_manager import add_server, remove_server, list_servers
from network_checker import ping, generate_html_report
from server_manager import *

def interactive_mode():
    while True:
        print("\nNetwork Monitoring Tool Menu:")
        print("1. Add Server")
        print("2. Remove Server")
        print("3. List Servers")
        print("4. Run Checks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter server name: ")
            address = input("Enter server address (IP/hostname): ")
            add_server(name, address)
        elif choice == "2":
            name = input("Enter server name to remove: ")
            remove_server(name)
        elif choice == "3":
            list_servers()
        elif choice == "4":
            run_checks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select a valid option.")

def run_checks():
    servers = load_servers()  # Laad servers vanuit server_manager.py
    for server in servers:
        ping_result = ping(server["name"], server["address"])
        print(f"Ping result for {server['name']} ({server['address']}):")
        print(ping_result)

    generate_html_report()
    print("HTML report generated: report.html")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Monitoring Tool")
    parser.add_argument("--mode", choices=["interactive", "check"], default="interactive", help="Operating mode")
    args = parser.parse_args()

    if args.mode == "interactive":
        interactive_mode()
    elif args.mode == "check":
        run_checks()
