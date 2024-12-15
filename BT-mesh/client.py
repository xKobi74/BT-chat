import asyncio
from bleak import BleakScanner, BleakClient, BleakError

# Обработчик получения уведомлений
def notification_handler(sender: int, data: bytearray):
    print(f"Received notification from {sender}: {data.decode()}")

# Функция для сканирования доступных Bluetooth-устройств
async def scan_devices():
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Found device: {device.name}, Address: {device.address}")

# Функция для отправки сообщения
async def send_message(device_address, message):
    async with BleakClient(device_address) as client:
        if await client.is_connected():
            print(f"Sending message: {message}")
            await client.write_gatt_char('characteristic_uuid', message.encode())

# Функция для приема сообщений
async def receive_messages(device_address):
    async with BleakClient(device_address) as client:
        if await client.is_connected():
            print("Connected to device. Waiting for notifications...")
            # Установите UUID характеристики, к которой необходимо подписаться для получения уведомлений
            char_uuid = 'characteristic_uuid'  # Замените на нужный UUID
            await client.start_notify(char_uuid, notification_handler)

            # Ожидаем в фоновом режиме, чтобы получать уведомления
            await asyncio.sleep(30)  # Например, слушаем 30 секунд

            # Останавливаем получение уведомлений после времени ожидания
            await client.stop_notify(char_uuid)
            print("Stopped listening for notifications.")

# Основная функция
async def main():
    await scan_devices()
    device_address = "a0:b3:39:5d:b2:35"  # Замените на MAC-адрес устройства

    # Запуск приема сообщений в фоновом режиме
    asyncio.create_task(receive_messages(device_address))
    
    # Отправка сообщения
    await send_message(device_address, "Hello from Bluetooth")

# Запуск программы
asyncio.run(main())
