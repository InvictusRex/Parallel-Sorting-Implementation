import numpy as np
import time
import sys
from multiprocessing import Pool, cpu_count
from memory_profiler import profile
import psutil

class ParallelSorting:
    def __init__(self, input_file="input_data.txt", num_threads=None, size=50000):
        self.input_file = input_file
        self.num_threads = num_threads if num_threads else cpu_count()
        self.size = size
        self.data = None
        
    def generate_dataset(self):
        """Generate random dataset and save to file"""
        print(f"Generating dataset of size {self.size}...")
        data = np.random.randint(1, 100000, size=self.size)
        np.savetxt(self.input_file, data, fmt='%d')
        print(f"Dataset saved to {self.input_file}")
        return data
    
    def load_dataset(self):
        """Load dataset from file"""
        try:
            self.data = np.loadtxt(self.input_file, dtype=int)
            print(f"Loaded {len(self.data)} elements from {self.input_file}")
            return self.data
        except Exception as e:
            print(f"Error loading data: {e}")
            sys.exit(1)
    
    def merge_sort(self, arr):
        """Sequential merge sort for individual chunks"""
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        """Merge two sorted arrays"""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def parallel_merge_sort(self, data):
        """Parallel merge sort implementation"""
        chunk_size = len(data) // self.num_threads
        chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
        
        with Pool(processes=self.num_threads) as pool:
            sorted_chunks = pool.map(self.merge_sort, chunks)
        
        while len(sorted_chunks) > 1:
            pairs = [(sorted_chunks[i], sorted_chunks[i + 1]) 
                    for i in range(0, len(sorted_chunks) - 1, 2)]
            if len(sorted_chunks) % 2 == 1:
                pairs.append((sorted_chunks[-1], []))
            
            sorted_chunks = [self.merge(left, right) for left, right in pairs]
        
        return sorted_chunks[0]
    
    def get_system_info(self):
        """Get system information for performance analysis"""
        return {
            'physical_cores': psutil.cpu_count(logical=False),
            'total_cores': psutil.cpu_count(logical=True),
            'cpu_freq': psutil.cpu_freq().current,
            'memory_used': psutil.Process().memory_info().rss / 1024 / 1024  # MB
        }
    
    @profile
    def run_sorting(self):
        """Execute parallel sorting and measure performance"""
        if self.data is None:
            self.load_dataset()
            
        print(f"\nStarting parallel merge sort with {self.num_threads} threads...")
        start_time = time.time()
        
        sorted_data = self.parallel_merge_sort(self.data.tolist())
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        is_sorted = all(sorted_data[i] <= sorted_data[i+1] for i in range(len(sorted_data)-1))
        sys_info = self.get_system_info()
        
        print(f"\nExecution Results:")
        print(f"{'='*50}")
        print(f"Dataset size: {self.size}")
        print(f"Number of threads: {self.num_threads}")
        print(f"Physical cores: {sys_info['physical_cores']}")
        print(f"Total cores: {sys_info['total_cores']}")
        print(f"CPU frequency: {sys_info['cpu_freq']:.2f} MHz")
        print(f"Memory used: {sys_info['memory_used']:.2f} MB")
        print(f"Execution time: {execution_time:.4f} seconds")
        print(f"Sorting verified: {is_sorted}")
        print(f"{'='*50}")
        
        return execution_time, is_sorted

if __name__ == "__main__":
    sizes = [50000, 75000, 100000]  # Updated dataset sizes
    thread_counts = [2, 4, 6, 8]
    results = {}
    
    for size in sizes:
        for threads in thread_counts:
            sorter = ParallelSorting(num_threads=threads, size=size)
            sorter.generate_dataset()
            execution_time, is_sorted = sorter.run_sorting()
            results[(size, threads)] = execution_time
            
    print("\nComparative Results:")
    print(f"{'='*50}")
    for (size, threads), time in results.items():
        print(f"Size {size}, Threads {threads}: {time:.4f} seconds")