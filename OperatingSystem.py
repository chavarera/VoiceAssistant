import psutil
import datetime
class OpeartingSystem:
    def __init__(self):
        print("initialization")
    def GetBattery(self):
        resp={}
        try:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = str(battery.percent)
            if plugged==False:
                plugged="Not Plugged In"
            else:
                plugged="Plugged In"
            resp['status']=True
            resp['percent']=percent
            resp['plugged']=plugged
        except Exception as e:
            resp['status']=False
            resp['message']=str(e)
        return resp 
    def CurrentTime(self):
        try:
            tme=datetime.datetime.now()
            return "Current Time hours {} Minutes {} Seconds {}".format(tme.hour,tme.minute,tme.second)
        except:
            return "Something Went Wrong"
