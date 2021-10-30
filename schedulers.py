import schedule
import time
import get_ping

# from get_ping import  get_loss_perc, get_ping_rslt_dict

schedule.every(5).seconds.do(get_ping())


while True:
    schedule.run_pending()
    time.sleep(1)
