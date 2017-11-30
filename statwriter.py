import datetime
import psutil
time = ('{:%Y%m%d%H%M%S}'.format(datetime.datetime.now()))
nsfilename = str(time) + ".txt"
nsfile = open(nsfilename, "w+") 
lget = list(psutil.win_service_iter())
for name in lget:
	sdetails = (list(psutil.win_service_get(str(name))) + sget.as_dict())
	nsfile.write(sdetails)
nsfile.close()
print (nsfile)
