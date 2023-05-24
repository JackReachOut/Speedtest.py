import os
import datetime
import time
import speedtest

i = 0

while True:
    i = i+1
    print (i)
    
    now = datetime.datetime.now()
        
    while True:
        try:
            whilecheck1 = 1
            test = speedtest.Speedtest()
                
        except:
            print ("Set_Function_Error")
            time.sleep(60)
            whilecheck1 = 0
                
        if whilecheck1 == 1 :
            break

    FILE = os.path.join(os.getcwd(), "SpeedtestLog.log")

    print ("loading server list...")

#get list of servers
    test.get_servers()

    print ("choosing best server...")
    
    while True:
        try:
            whilecheck2 = 1
            best = test.get_best_server()
            
        except:
            print ("Choose_Server_Error")
            time.sleep(60)
            whilecheck2 = 0
        
        if whilecheck2 == 1 :
            break

    print (best)

#print(best)
#print(f"Found: {best['host']} located in {best['country']})


    print("Performing download test...")
    download_result = test.download()
    print("Performing uploadtest...")
    upload_result = test.upload()
#ping_result = test.results.ping

    print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbits/s")
    print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbits/s")
#print(f"Ping: {download_results:.2f} ms")

    with open(FILE, "a") as file:
        file.write(f"Time: {str(now)} \n")
#    file.write
        file.write(f"Download speed: {download_result / 1024 / 1024:.2f} Mbits/s \n")
        file.write(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbits/s \n")

    time.sleep(1200)
        
