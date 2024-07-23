from asyncio import create_task, gather, run
from apps.server_files.server import Server
from apps.domain import Domain


async def main():
    """Главная функция программы"""
    domain = create_task(Domain().get_domain())
    server = create_task(Server().start_server())
    await gather(domain, server)


if __name__ == '__main__':
    try:
        run(main())
    except KeyboardInterrupt:
        print("Exit")
    except Exception as e:
        print(f"Error: {e}")
