from zk import ZK, const

conn = None
# create ZK instance
zk = ZK('192.168.10.202', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)

# connect to device
conn = zk.connect()
print(conn.live_capture())
# live capture! (timeout at 10s)
for attendance in conn.live_capture(new_timeout=2):
    if attendance is None:
        # implement here timeout logic
        print("None")
        pass
    else:
        print("Live")
        print (attendance) # Attendance object