# PHY Systems Latency & Interrupt Analyzer

## Overview
This project explores system-level performance behavior by monitoring
CPU scheduling latency, interrupt activity, and network jitter on Linux.

The goal is to understand how low-level events (interrupt bursts,
PHY-level instability, and OS scheduling delays) manifest as
application-level performance issues.

This project is focused on **system analysis and root cause reasoning**
rather than application development.

---

## Motivation
Real-time applications often suffer from performance degradation even
when CPU utilization appears low. Such issues are frequently caused by
interrupt storms, scheduling delays, or PHY/network instability.

This project helps visualize and correlate these effects over time.

---

## Components

### 1. Scheduling Latency Monitor
Measures OS scheduling jitter by observing deviations from expected
sleep intervals. Useful for identifying latency spikes caused by
interrupt pressure or context switching.

### 2. Interrupt Activity Monitor
Tracks changes in `/proc/interrupts` to detect abnormal interrupt rates
that may indicate hardware or PHY-level issues.

### 3. Network Jitter Monitor
Uses ICMP echo requests to measure latency variation and jitter, helping
identify timing instability even when average bandwidth remains high.

---

## Usage

Run each script independently on a Linux system:

```bash
python3 latency_monitor.py
python3 interrupt_monitor.py
python3 network_jitter.py
