# PHY Systems Latency & Interrupt Analyzer

A lightweight system profiling tool to analyze how low-level OS behavior (scheduling, interrupts, and network variability) impacts application-level performance.

---

## Overview

This project explores system-level performance by monitoring:

- CPU scheduling latency  
- Interrupt activity  
- Network latency and jitter  

The goal is to understand how low-level OS events manifest as real-world performance issues, even when traditional metrics like CPU utilization appear normal.

---

## Motivation

Modern systems often experience performance degradation due to:

- Interrupt storms  
- Scheduler delays  
- Network instability  

These issues are not always visible through standard monitoring tools.

This project focuses on measuring, correlating, and analyzing these hidden performance factors.

---

## Components

### 1. Scheduling Latency Monitor
Measures OS scheduling delays by comparing expected sleep duration with actual wake-up time using high-resolution timers.

- Captures scheduler jitter and timing deviations  
- Helps identify latency spikes due to context switching or CPU contention  

---

### 2. Interrupt Activity Monitor
Tracks system activity using OS-level statistics:

- On Linux: `/proc/interrupts`  
- On macOS: approximated using `vm_stat`  

- Detects sudden spikes in system activity  
- Useful for identifying interrupt bursts and system disturbances  

---

### 3. Network Jitter Monitor
Measures network latency using ICMP (ping):

- Computes average latency and jitter (standard deviation)  
- Identifies instability even when average latency is low  

---

### 4. Unified System Monitor
Combines all signals into a single time-aligned stream:

- Scheduling latency  
- Interrupt rate  
- Network latency  

Includes:

- Real-time logging  
- Spike detection  
- Basic correlation between system events  

---

## Data Collection

All metrics are logged into:

system_metrics.csv

Format:

timestamp, latency_ms, interrupts_per_sec, network_latency_ms

This enables offline analysis and visualization.

---

## Visualization

The project includes plotting scripts to analyze:

- Latency over time  
- Interrupt activity over time  
- Network latency trends  
- Correlation between interrupts and latency  

Example insight:

Latency spikes often align with bursts in system activity, indicating scheduler disruption due to underlying OS events.

---

## Key Learnings

- CPU utilization alone is insufficient to diagnose performance issues  
- Interrupt bursts can significantly impact scheduling latency  
- Network jitter can indicate deeper system instability  
- Time-aligned metrics are essential for root-cause analysis  

---

## Environment

- macOS (development using vm_stat)  
- Linux (recommended for full functionality using /proc/interrupts)  
- Python 3.x  

Dependencies:

pip install pandas matplotlib

---

## Usage

Run unified monitor:

python3 main_monitor.py

Generate plots:

python3 plot_metrics.py

---

## Future Improvements

- Real-time visualization dashboard  
- More accurate interrupt tracking on macOS  
- Integration with system tracing tools (e.g., perf, eBPF)  
- Automated anomaly detection  

---

## Author

Shashwata Ghosh
