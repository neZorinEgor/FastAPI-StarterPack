import asyncio

import uvicorn
from fastapi import FastAPI


async def main():
    app = FastAPI()
    # Server settings
    server_config = uvicorn.Config(app, host="0.0.0.0", port=8000, workers=5)
    server = uvicorn.Server(config=server_config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main=main())