import subprocess
import time
import statistics

latencies = []

print("Measuring network jitter (ping)... Press Ctrl+C to stop.")

try:
    while True:
        output = subprocess.check_output(
            ["ping", "-c", "1", "8.8.8.8"],
            stderr=subprocess.DEVNULL
        ).decode()

        for line in output.split("\n"):
            if "time=" in line:
                latency = float(line.split("time=")[1].split(" ms")[0])
                latencies.append(latency)

        if len(latencies) % 10 == 0:
            print(f"Avg: {statistics.mean(latencies):.2f} ms | "
                  f"Jitter: {statistics.stdev(latencies):.2f} ms")

        time.sleep(1)

except KeyboardInterrupt:
    print("Final stats:")
    print(f"Avg latency: {statistics.mean(latencies):.2f} ms")
    print(f"Jitter: {statistics.stdev(latencies):.2f} ms")
