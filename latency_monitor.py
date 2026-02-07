import time
import statistics
latencies=[]
interval=0.01;
print("Measuring scheduling latency... Press Ctrl+C to stop.")
try:
    while True:
        start=time.perf_counter()
        time.sleep(interval)
        end=time.perf_counter()
        latency=(end-start)-interval
        latencies.append(latency)

        if len(latencies)%100==0:
            print(f"Avg latency: {statistics.mean(latencies)*1000:.3f} ms | "
                  f"Max latency: {max(latencies)*1000:.3f} ms")
except KeyboardInterrupt:
    print("\nFinal Stats:")
    print(f"Average latency: {statistics.mean(latencies)*1000:.3f} ms")
    print(f"Max latency: {max(latencies)*1000:.3f} ms")