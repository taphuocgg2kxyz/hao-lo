import asyncio
import sys
from mcstatus import JavaServer

TIMEOUT = 2.0  # Thời gian chờ phản hồi từ server (giây)
CONCURRENCY = 300  # Số lượng IP xử lý cùng lúc
semaphore = asyncio.Semaphore(CONCURRENCY)


async def check_minecraft(ip: str):
    ip = ip.strip()
    if not ip:
        return

    async with semaphore:
        try:
            # Truy vấn máy chủ Minecraft
            server = await MinecraftServer.async_lookup(
                f"{ip}:25565", timeout=TIMEOUT
            )
            status = await server.async_status()

            # Lấy MOTD
            motd = (
                status.description
                if isinstance(status.description, str)
                else status.description.get("text", "")
            )
            motd_clean = motd.replace("\n", " ").strip()

            # Hiện trực tiếp kết quả lên Terminal
            output = f"[+] FIND: {ip}:25565 | Ver: {status.version.name} | Players: {status.players.online}/{status.players.max} | MOTD: {motd_clean}"
            print(output, flush=True)

            # Ghi vào file txt lưu trữ
            with open("mc_found.txt", "a", encoding="utf-8") as f:
                f.write(f"{output}\n")

        except Exception:
            pass


async def main():
    # Đọc danh sách IP được đẩy trực tiếp từ Masscan qua STDIN
    tasks = []
    loop = asyncio.get_event_loop()

    while True:
        line = await loop.run_in_executor(None, sys.stdin.readline)
        if not line:
            break
        ip = line.strip()
        if ip:
            tasks.append(asyncio.create_task(check_minecraft(ip)))

    if tasks:
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Đã dừng quét.")
