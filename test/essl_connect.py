from zk import ZK, const

conn = None
# create ZK instance
zk = ZK('192.168.10.201', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)

try:
    # connect to device
    conn = zk.connect()
    print(conn.test_voice(index=1))
    attendances = conn.get_attendance()
    for att in attendances:
        # print(att)
        if att.user_id == "427":
            print(att)
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()