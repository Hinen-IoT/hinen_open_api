"""
Example usage of the Hinen Open API client.
"""
import asyncio
import sys
import os

# Add the current directory to the path so we can import the client
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from hinen_open_api import HinenOpen

async def main():
    """Example of using the Hinen Open API client."""
    # Initialize the client with your credentials
    async with HinenOpen(
        host="https://api.hinen.com",
        app_id="your_app_id",
        app_secret="your_app_secret"
    ) as client:
        # Set user authentication if needed
        await client.set_user_authentication(
            token="user_token",
            refresh_token="refresh_token"
        )
        
        # Now you can use the client to make requests
        print("Hinen Open API client initialized successfully!")
        
        # Example of making a GET request (uncomment and modify as needed)
        # response = await client.get("/devices")
        # print(f"Response: {response}")
        
        # Example of making a POST request (uncomment and modify as needed)
        # data = {"name": "New Device", "type": "sensor"}
        # response = await client.post("/devices", json=data)
        # print(f"Created device: {response}")

if __name__ == "__main__":
    asyncio.run(main())