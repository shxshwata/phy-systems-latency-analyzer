import time
import statistics
from datetime import datetime
import csv

latencies = []
interval = 0.01

with open("latency_log.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "latency_ms"])

    print("Measuring scheduling latency... Press Ctrl+C to stop.")

    try:
        while True:
            timestamp = datetime.now().isoformat()

            start = time.perf_counter()
            time.sleep(interval)
            end = time.perf_counter()

            latency = (end - start - interval) * 1000

            if latency < 0:
                latency = 0

            latencies.append(latency)
            writer.writerow([timestamp, latency])

            if len(latencies) % 100 == 0:
                avg = statistics.mean(latencies)
                mx = max(latencies)
                print(f"Avg latency: {avg:.3f} ms | Max latency: {mx:.3f} ms")

            if latency > 2:
                print(f"Latency spike: {latency:.3f} ms")

    except KeyboardInterrupt:
        print("\nFinal Stats:")
        print(f"Average latency: {statistics.mean(latencies):.3f} ms")
        print(f"Max latency: {max(latencies):.3f} ms")
