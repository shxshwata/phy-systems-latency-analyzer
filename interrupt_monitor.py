import time
from datetime import datetime
import csv
import subprocess

def get_total_interrupts():
    try:
        output = subprocess.check_output(["vm_stat"]).decode()
        total = 0

        for line in output.split("\n"):
            parts = line.split(":")
            if len(parts) == 2:
                value = parts[1].strip().replace(".", "")
                if value.isdigit():
                    total += int(value)

        return total

    except:
        return 0


with open("interrupt_log.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "interrupts_per_sec"])

    print("Monitoring interrupt rate (Mac)... Press Ctrl+C to stop.")

    prev = get_total_interrupts() or 0

    try:
        while True:
            time.sleep(1)
            timestamp = datetime.now().isoformat()

            curr = get_total_interrupts() or 0
            delta = curr - prev
            prev = curr

            if delta < 0:
                delta = 0

            writer.writerow([timestamp, delta])

            print(f"{timestamp} | Interrupts/sec: {delta}")

            if delta > 10000:
                print("Interrupt burst detected")

    except KeyboardInterrupt:
        print("Stopped.")
