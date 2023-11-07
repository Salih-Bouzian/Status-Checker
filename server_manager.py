import json

# Bestandsnaam voor serverinformatie
SERVER_DATA_FILE = "data.json"

def load_servers():
    try:
        with open(SERVER_DATA_FILE, "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_servers(servers):
    with open(SERVER_DATA_FILE, "w") as file:
        json.dump(servers, file, indent=4)

def add_server(server_name, server_address):
    servers = load_servers()
    servers.append({"name": server_name, "address": server_address})
    save_servers(servers)

def remove_server(server_name):
    servers = load_servers()
    updated_servers = [server for server in servers if server["name"] != server_name]
    save_servers(updated_servers)

def list_servers():
    servers = load_servers()
    for i, server in enumerate(servers, start=1):
        print(f"{i}. Name: {server['name']}, Address: {server['address']}")

if __name__ == "__main__":
    while True:
        print("Server Management Menu:")
        print("1. Add Server")
        print("2. Remove Server")
        print("3. List Servers")
        print("4. Exit")
        
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
            break
        else:
            print("Invalid choice. Please select a valid option.")
