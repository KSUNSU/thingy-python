import asyncio
from bleak import BleakScanner
from bluepy.thingy52 import Thingy52

async def scan():
    devices = await BleakScanner.discover()
    for d in devices:
        if d.name == 'Fidget':
            print(d.name)
            print(d.details)
            print(d.metadata)
            print(d.rssi)
            return d.address

address = asyncio.run(scan())
thingy = Thingy52(address)


#working