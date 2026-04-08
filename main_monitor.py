import time
import subprocess
import csv
from datetime import datetime

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


interval = 0.01
prev_interrupts = get_total_interrupts() or 0

with open("system_metrics.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "timestamp",
        "latency_ms",
        "interrupts_per_sec",
        "network_latency_ms"
    ])

    print("Running unified system monitor (Mac)... Press Ctrl+C to stop.")

    try:
        while True:
            timestamp = datetime.now().isoformat()

            # latency
            start = time.perf_counter()
            time.sleep(interval)
            end = time.perf_counter()
            latency = (end - start - interval) * 1000

            if latency < 0:
                latency = 0

            # interrupts
            curr_interrupts = get_total_interrupts() or 0
            interrupt_delta = curr_interrupts - prev_interrupts
            prev_interrupts = curr_interrupts

            if interrupt_delta < 0:
                interrupt_delta = 0

            # network
            net_latency = get_ping_latency()

            writer.writerow([
                timestamp,
                latency,
                interrupt_delta,
                net_latency
            ])

            print(
                f"{timestamp} | "
                f"Lat: {latency:.3f} ms | "
                f"Int: {interrupt_delta} | "
                f"Net: {net_latency}"
            )

            if latency > 2:
                print("Latency spike detected")

            if interrupt_delta > 10000:
                print("Interrupt burst detected")

            if net_latency is not None and net_latency > 100:
                print("Network instability detected")

            if latency > 2 and interrupt_delta > 10000:
                print("Likely cause: interrupt storm affecting scheduling")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped.")
