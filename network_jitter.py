import subprocess
import time
import statistics
from datetime import datetime
import csv

latencies = []

def get_ping_latency():
    try:
        output = subprocess.check_output(
            ["ping", "-c", "1", "8.8.8.8"],
            stderr=subprocess.DEVNULL
        ).decode()

        for line in output.split("\n"):
            if "time=" in line:
                return float(line.split("time=")[1].split(" ms")[0])
    except:
        return None

with open("network_log.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "latency_ms"])

    print("Measuring network jitter... Press Ctrl+C to stop.")

    try:
        while True:
            timestamp = datetime.now().isoformat()

            latency = get_ping_latency()

            if latency is not None:
                latencies.append(latency)
                writer.writerow([timestamp, latency])

                if len(latencies) % 10 == 0:
                    avg = statistics.mean(latencies)
                    jitter = statistics.stdev(latencies) if len(latencies) > 1 else 0
                    print(f"Avg: {avg:.2f} ms | Jitter: {jitter:.2f} ms")

                if latency > 100:
                    print("High network latency detected")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nFinal Stats:")
        if latencies:
            print(f"Avg latency: {statistics.mean(latencies):.2f} ms")
            if len(latencies) > 1:
                print(f"Jitter: {statistics.stdev(latencies):.2f} ms")
