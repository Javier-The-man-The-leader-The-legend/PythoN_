import time
seconds = time.time()
local_time = time.ctime(seconds)
passprint("Local time:", local_time)
time.time() = round(time(), 3)