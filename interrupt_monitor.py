import time
def read_interrupts():
    with open("/proc/interrupts") as f:
        return f.readlines()
prev=read_interrupts()
time.sleep(1)
print("Monitoring interrupt rate... Press Ctrl+C to stop.")
try:
    while True:
        curr=read_interrupts()
        print("---- Interrupt snapshot ----")
        for p,c in zip (prev, curr):
            if p!=c:
                print(c.strip())
        prev=curr
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped.")