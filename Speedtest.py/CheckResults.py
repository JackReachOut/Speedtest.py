import os
import re

FILE = os.path.join(os.getcwd(), "SpeedtestLogAuswertung.log")

download_speeds = []
upload_speeds = []
zero_speed_times = []

with open('SpeedtestLog.log', 'r') as file:
    data = file.read()
    timestamps = re.findall(r"Time: (.*)\n", data)
    downloadspeeds = re.findall(r"Download speed: (\d+\.\d+) Mbits/s", data)
    uploadspeeds = re.findall(r"Upload speed: (\d+\.\d+) Mbits/s", data)
    for i in range(len(downloadspeeds)):
        download_speed = float(downloadspeeds[i])
        upload_speed = float(uploadspeeds[i])
        if download_speed == 0.0 or upload_speed == 0.0:
            zero_speed_times.append((timestamps[i], download_speed, upload_speed))
        else:
            download_speeds.append(download_speed)
            upload_speeds.append(upload_speed)

if zero_speed_times:
    with open(FILE, "a") as file:
        file.write("download/upload speed at zero:\n")
        for t in zero_speed_times:
            file.write("Timestamp: " + t[0] + ", Download speed: " + str(t[1]) + ", Upload speed: " + str(t[2]) + "\n")
        average_download_speed = sum(download_speeds)/len(download_speeds)
        min_download_speed = min(download_speeds)
        max_download_speed = max(download_speeds)
        file.write("Average Download speed: " + str(average_download_speed) + " Mbits/s\n")
        file.write("Minimum Download speed: " + str(min_download_speed) + " Mbits/s\n")
        file.write("Maximum Download speed: " + str(max_download_speed) + " Mbits/s\n")

        average_upload_speed = sum(upload_speeds)/len(upload_speeds)
        min_upload_speed = min(upload_speeds)
        max_upload_speed = max(upload_speeds)
        file.write("Average Upload speed: " + str(average_upload_speed) + " Mbits/s\n")
        file.write("Minimum Upload speed: " + str(min_upload_speed) + " Mbits/s\n")
        file.write("Maximum Upload speed: " + str(max_upload_speed) + " Mbits/s\n")
else:
    with open(FILE, "a") as file:
        average_download_speed = sum(download_speeds)/len(download_speeds)
        min_download_speed = min(download_speeds)
        max_download_speed = max(download_speeds)
        file.write("Average Download speed: " + str(average_download_speed) + " Mbits/s\n")
        file.write("Minimum Download speed: " + str(min_download_speed) + " Mbits/s\n")
        file.write("Maximum Download speed: " + str(max_download_speed) + " Mbits/s\n")

        average_upload_speed = sum(upload_speeds)/len(upload_speeds)
        min_upload_speed = min(upload_speeds)
        max_upload_speed = max(upload_speeds)
        file.write("Average Upload speed: " + str(average_upload_speed) + " Mbits/s\n")
        file.write("Minimum Upload speed: " + str(min_upload_speed) + " Mbits/s\n")
        file.write("Maximum Upload speed: " + str(max_upload_speed) + " Mbits/s\n")


