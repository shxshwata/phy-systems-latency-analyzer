import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("system_metrics.csv")

# convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# -------- PLOT 1: Latency over time --------
plt.figure()
plt.plot(df["timestamp"], df["latency_ms"])
plt.xlabel("Time")
plt.ylabel("Latency (ms)")
plt.title("Scheduling Latency Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -------- PLOT 2: Interrupts over time --------
plt.figure()
plt.plot(df["timestamp"], df["interrupts_per_sec"])
plt.xlabel("Time")
plt.ylabel("Interrupts/sec")
plt.title("Interrupt Activity Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -------- PLOT 3: Network latency --------
plt.figure()
plt.plot(df["timestamp"], df["network_latency_ms"])
plt.xlabel("Time")
plt.ylabel("Network Latency (ms)")
plt.title("Network Latency Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -------- PLOT 4: Correlation (Latency vs Interrupts) --------
plt.figure()
plt.scatter(df["interrupts_per_sec"], df["latency_ms"])
plt.xlabel("Interrupts/sec")
plt.ylabel("Latency (ms)")
plt.title("Latency vs Interrupt Activity")
plt.tight_layout()
plt.show()
