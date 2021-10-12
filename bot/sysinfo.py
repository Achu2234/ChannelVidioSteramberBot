import platform
import re
import socket
import sys
import time
import uuid
from datetime import datetime
from os import environ, execle, path, remove

import psutil
from pyrogram import  Client, filters, __version__

# Utils Helper
def humanbytes(size):
    """Convert Bytes To Bytes So That Human Can Read It"""
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"



# FETCH SYSINFO

@Client.on_message(filters.command('sysinfo'))
async def give_sysinfo(client, message):
    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    ram = humanbytes(round(psutil.virtual_memory().total))
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    du = psutil.disk_usage(client.workdir)
    psutil.disk_io_counters()
    disk = f"{humanbytes(du.used)} / {humanbytes(du.total)} " f"({du.percent}%)"
    cpu_len = len(psutil.Process().cpu_affinity())
    somsg = f"""**System Info
    
PlatForm : {splatform}
PlatForm - Release : {platform_release}
PlatFork - Version : {platform_version}
Architecture : {architecture}
Hostname : {hostname}
IP : {ip_address}
Mac : {mac_address}
Processor : {processor}
Ram :  {ram}
CPU : {cpu_len}
CPU FREQ : {cpu_freq}
DISK : {disk}
    """
    await message.reply(somsg)
