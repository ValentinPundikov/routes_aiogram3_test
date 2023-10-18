import asyncio
from func_main import *

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)