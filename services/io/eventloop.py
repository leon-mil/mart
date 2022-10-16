import asyncio
import time

async def steps21_worker():
    
    print('Starting StEPTS21 worker.')
    time.sleep(5)
    print("Completed StEPS21 work.")
    
    loop = asyncio.get_event_loop()
    
    try:
        loop.run_until_complete(steps21_worker())
    finally:
        loop.close()