import time
import asyncio
from bleak import BleakScanner
from bleak import BleakClient
from bleak import BleakGATTCharacteristic

def notify_callback(sender: BleakGATTCharacteristic, data: bytearray):
    print(f"{sender}: {data.hex()}")

async def scan_devices():
    print("Scanning for BLE devices...")
    devices = await BleakScanner.discover()
    for d in devices:
        print(f"Device: {d.name} ({d.address}), RSSI: {d.rssi}dB")
        if "Polar" in d.name:
            # await BleakScanner.stop()
            async with BleakClient(d.address) as client:
                print(f"Connected: {client.is_connected}")
                
                services = await client.get_services()
                for service in services:
                    print(f"Service: {service.uuid}")
                    if service.uuid == "0000180d-0000-1000-8000-00805f9b34fb":
                        for char in service.characteristics:
                            print(f"  Characteristic: {char.uuid} (Properties: {char.properties})")
                            if char.uuid == "00002a37-0000-1000-8000-00805f9b34fb":
                                print("start_notify")
                                await client.start_notify(char.uuid, notify_callback)

if __name__ == "__main__":
    asyncio.run(scan_devices())
    time.sleep(10)
