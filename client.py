import asyncio
import websockets
import json
from datetime import datetime

async def listen_notifications():
    url = "ws://localhost:8000/ws/intruder/"
    
    async with websockets.connect(url) as websocket:
        print("Connected to WebSocket for intruder notifications...")
        
        while True:
            try:
                # Receive messages from the server
                message = await websocket.recv()
                
                # Parse the JSON message
                data = json.loads(message)
                
                # Extract fields for readability
                ip_address = data.get("ip_address")
                user_agent = data.get("user_agent")
                path = data.get("path")
                method = data.get("method")
                timestamp = data.get("timestamp")
                params = data.get("params", "None")
                headers = data.get("headers", {})
                
                # Convert timestamp to a readable format if needed
                timestamp = datetime.fromisoformat(timestamp).strftime("%Y-%m-%d %H:%M:%S")
                
                # Print the notification in a clean, structured format
                print(f"\n---{timestamp}: Intruder {ip_address} at {path} ---")
                print(f"Timestamp     : {timestamp}")
                print(f"IP Address    : {ip_address}")
                print(f"Path          : {path}")
                print(f"Method          : {method}")
                print(f"User Agent    : {user_agent}")
                print(f"Parameters    : {params}")
                
                # Optionally print headers in a structured way
                print("Headers       :")
                for key, value in headers.items():
                    print(f"  {key}: {value}")
                
            except (asyncio.CancelledError, KeyboardInterrupt):
                print("Connection closed.")
                break
            except Exception as e:
                print(f"Error: {e}")
                
asyncio.run(listen_notifications())
