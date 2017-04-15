#######
#author : wangsonghe
#date: 2017.01.18
#######

#pw: 736973636f

import argparse
import app_event
import os
import redis
from droidbot import DroidBot

app_path = "/home/user/retest/"
device_serial = "08fd8e5ba2439881"
output_dir = "/home/user/result3/"
#event_interval = 5
#event_duration = 5

def main():
    """
    the main function
    it starts a droidbot according to the arguments given in cmd line
    """
    '''
    apknames = os.listdir(app_path)
    print apknames
    for apkname in apknames:
        print len(apkname)
        if apkname == '.DS_Store':
            continue
        else:
            name = apkname[0: len(apkname) - 4]
            print name
            try:
                droidbot = DroidBot(app_path + apkname,
                                    device_serial,
                                    output_dir + name,
                                    env_policy="static",
                                    event_policy="utg_dynamic",
                                    with_droidbox=False,
                                    event_interval=None,
                                    event_duration=3,
                                    event_count=20,
                                    quiet=False,
                                    use_hierarchy_viewer=True)
                # droidbot.setRedis(r2)
                droidbot.start()
            except:
                droidbot.stop()
                continue
    return

    '''
    pool1 = redis.ConnectionPool(host='192.168.3.70', port=6379, db=5)
    pool2 = redis.ConnectionPool(host='192.168.3.70', port=6379, db=6)
    r1 = redis.Redis(connection_pool=pool1)
    r2 = redis.Redis(connection_pool=pool2)
    res_db0 = r1.lrange('apk_name', 0, -1)
    res_db1 = r2.lrange('apk_name', 0, -1)

    for apkname in res_db1:
        if apkname in res_db0:
            res_db0.remove(apkname)

    for apkname in res_db0:
        if not os.path.exists(app_path + apkname + ".apk"):
            print app_path + apkname + ".apk not exists"
            continue

        try:
            print apkname
            droidbot = DroidBot(app_path + apkname + ".apk",
                                device_serial,
                                output_dir + apkname,
                                env_policy="static",
                                event_policy="utg_dynamic",
                                with_droidbox=None,
                                event_interval=None,
                                event_duration=3,
                                event_count=15,
                                quiet=False,
                                use_hierarchy_viewer=True)

            droidbot.start()

            if r2 is not None:
                r2.lpush('apk_name', apkname)
        except:
            droidbot.stop()
            if r2 is not None:
                r2.lpush('apk_name', apkname)

            print apkname + " can not use! Continue!"
            import traceback
            traceback.print_exc()
    return

if __name__ == "__main__":
    main()