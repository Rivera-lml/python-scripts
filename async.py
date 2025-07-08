import asyncio

async def process_data(data):
    print(f'Processing {data}...')
    #simulate operation
    await asyncio.sleep(10)
    print(f'{data} processed.')
    return data * 2

async def main():
    print('start processing')
    result = await process_data('archivo.txt')
    print(f'Result: {result}')

asyncio.run(main())


