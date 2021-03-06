
import asyncio

async def printer(text: str):
    print(text)
    
async def sleeper(duration: int):
    print(f'sleeping for {duration} seconds')
    await asyncio.sleep(duration)

async def main():
    await sleeper(5)
    await printer('Woke up')
    
asyncio.run(main())
