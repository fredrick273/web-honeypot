import asyncio
import websockets

async def listen_notifications():
    url = "ws://localhost:8000/ws/intruder/"  # Adjust this to your WebSocket URL

    async with websockets.connect(url) as websocket:
        print("Connected to WebSocket for intruder notifications...")
        try:
            while True:
                message = await websocket.recv()  # Receive messages from the server
                print("New Notification:", message)  # Display the notification
        except websockets.ConnectionClosed:
            print("Connection closed by the server.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(listen_notifications())
