import numpy as np
import time
import sys
from memory_profiler import profile

class SequentialSorting:
    def __init__(self, input_file="input_data.txt", size=50000):
        self.input_file = input_file
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
        """Recursive merge sort implementation"""
        if len(arr) <= 1:
            return arr
            
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # Recursive sorting of left and right halves
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        
        # Merge sorted halves
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
        
        # Add remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    @profile
    def run_sorting(self):
        """Execute sorting and measure performance"""
        if self.data is None:
            self.load_dataset()
            
        print("\nStarting sequential merge sort...")
        start_time = time.time()
        
        # Convert to list for sorting
        data_list = self.data.tolist()
        sorted_data = self.merge_sort(data_list)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Verify sorting
        is_sorted = all(sorted_data[i] <= sorted_data[i+1] for i in range(len(sorted_data)-1))
        
        print(f"\nExecution Results:")
        print(f"{'='*50}")
        print(f"Dataset size: {self.size}")
        print(f"Execution time: {execution_time:.4f} seconds")
        print(f"Sorting verified: {is_sorted}")
        print(f"{'='*50}")
        
        return execution_time, is_sorted

if __name__ == "__main__":
    # Test with larger dataset sizes
    sizes = [50000, 75000, 100000]
    results = {}
    
    for size in sizes:
        sorter = SequentialSorting(size=size)
        sorter.generate_dataset()
        execution_time, is_sorted = sorter.run_sorting()
        results[size] = execution_time
        
    print("\nComparative Results:")
    print(f"{'='*50}")
    for size, time in results.items():
        print(f"Size {size}: {time:.4f} seconds")