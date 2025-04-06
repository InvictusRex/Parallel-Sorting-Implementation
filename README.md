# Parallel Sorting Implementation

This project implements **Merge Sort** in both **sequential** and **parallel** forms using Python. The parallel implementation leverages Python's `multiprocessing` module to speed up sorting of large datasets by distributing the workload across multiple CPU cores. The project also includes performance monitoring tools, scalability analysis, and visualization capabilities.

---

## 🚀 Overview

**Merge Sort** is a classic divide-and-conquer algorithm that recursively splits an array into smaller subarrays, sorts them individually, and merges them back together to form the final sorted array.

This implementation supports:

- **Sequential Merge Sort** (single-threaded)
- **Parallel Merge Sort** (multi-threaded using `multiprocessing`)
- Performance comparison between sequential and parallel executions
- Visualization of speedup, efficiency, and resource usage

---

## 🧠 Algorithm Description

- **Merge Sort** is a divide-and-conquer algorithm:

  - Divides the array into halves
  - Recursively sorts each half
  - Merges the sorted halves to produce a fully sorted array

- **Parallel Merge Sort**:
  - Divides the input into subarrays
  - Sorts each subarray in parallel using multiple processes
  - Merges the results concurrently for faster overall execution

---

## 🔧 Implementation Features

### ✅ Sequential Implementation

- Pure Python implementation of Merge Sort
- Tracks memory usage and execution time
- Automatically generates random datasets
- Verifies sorted results for correctness

### ⚙️ Parallel Implementation

- Utilizes Python’s `multiprocessing` module
- Configurable number of parallel processes/threads
- Includes system resource monitoring during execution
- Collects detailed performance metrics
- Supports scalability analysis on various dataset sizes

### 📈 Analysis Tools

- Performance metrics (execution time, memory usage, CPU load)
- Speedup and efficiency calculations
- Graphical visualization using `matplotlib`
- Exportable CSV logs for further analysis
- System resource tracking and visualization

---

## 📊 Dataset Information

- Randomly generated numeric datasets
- Sizes ranging from **1000** to **5000** elements
- Customizable for larger datasets if needed

---

## 🖥️ System Requirements

- Python 3.8+
- Recommended: Multi-core CPU
- Dependencies:
  ```bash
  pip install psutil matplotlib
  ```

---

## 📂 Project Structure

```bash
.
├── sequential_merge_sort.py        # Sequential merge sort implementation
├── parallel_merge_sort.py          # Parallel merge sort with multiprocessing
├── dataset_generator.py            # Random dataset generator
├── performance_analyzer.py         # Execution time, memory, CPU tracking
├── plotter.py                      # Visualizes performance metrics
├── results/                        # Saved plots and CSV files
└── README.md                       # You're reading it!
```

---

## 🧪 How to Run

### Sequential:

```bash
python sequential_merge_sort.py
```

### Parallel:

```bash
python parallel_merge_sort.py --threads 4
```

> Use `--threads` to define the number of parallel processes.

---

## 📈 Sample Output (Visualizations)

- Execution time comparison between sequential and parallel sort
- Speedup and efficiency graphs
- CPU and memory usage over time

---

## 📌 Key Takeaways

- Parallel processing offers significant performance gains for larger datasets
- Optimal speedup is limited by system resources and multiprocessing overhead
- Visualization and analysis help understand performance trade-offs

---

## 📚 References

- [Merge Sort - Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)
- [Python multiprocessing docs](https://docs.python.org/3/library/multiprocessing.html)
