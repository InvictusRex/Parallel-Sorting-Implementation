import matplotlib.pyplot as plt
import numpy as np
from sequential_sort import SequentialSorting
from parallel_sort import ParallelSorting
import pandas as pd

def run_performance_analysis(sizes=[50000, 75000, 100000], thread_counts=[2, 4, 6, 8]):
    results = []
    
    # Run tests for each size
    for size in sizes:
        # Generate dataset
        seq_sorter = SequentialSorting(size=size)
        seq_sorter.generate_dataset()
        
        # Sequential execution
        seq_time, _ = seq_sorter.run_sorting()
        
        # Parallel execution with different thread counts
        for threads in thread_counts:
            par_sorter = ParallelSorting(num_threads=threads)
            par_sorter.load_dataset()
            par_time, _ = par_sorter.run_sorting()
            
            speedup = seq_time / par_time
            efficiency = speedup / threads
            
            results.append({
                'Size': size,
                'Threads': threads,
                'Sequential_Time': seq_time,
                'Parallel_Time': par_time,
                'Speedup': speedup,
                'Efficiency': efficiency
            })
    
    return pd.DataFrame(results)

def plot_results(df):
    # Create subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Execution Time Comparison
    for size in df['Size'].unique():
        size_data = df[df['Size'] == size]
        axes[0,0].plot(size_data['Threads'], size_data['Parallel_Time'], 
                      marker='o', label=f'Size {size}')
    axes[0,0].set_xlabel('Number of Threads')
    axes[0,0].set_ylabel('Execution Time (s)')
    axes[0,0].set_title('Parallel Execution Time vs Threads')
    axes[0,0].legend()
    
    # Speedup Analysis
    for size in df['Size'].unique():
        size_data = df[df['Size'] == size]
        axes[0,1].plot(size_data['Threads'], size_data['Speedup'], 
                      marker='o', label=f'Size {size}')
    axes[0,1].plot([1, max(df['Threads'])], [1, max(df['Threads'])], 
                   'k--', label='Linear Speedup')
    axes[0,1].set_xlabel('Number of Threads')
    axes[0,1].set_ylabel('Speedup')
    axes[0,1].set_title('Speedup vs Threads')
    axes[0,1].legend()
    
    # Efficiency Analysis
    for size in df['Size'].unique():
        size_data = df[df['Size'] == size]
        axes[1,0].plot(size_data['Threads'], size_data['Efficiency'], 
                      marker='o', label=f'Size {size}')
    axes[1,0].set_xlabel('Number of Threads')
    axes[1,0].set_ylabel('Efficiency')
    axes[1,0].set_title('Efficiency vs Threads')
    axes[1,0].legend()
    
    # Size vs Time for different thread counts
    for threads in df['Threads'].unique():
        thread_data = df[df['Threads'] == threads]
        axes[1,1].plot(thread_data['Size'], thread_data['Parallel_Time'], 
                      marker='o', label=f'{threads} Threads')
    axes[1,1].set_xlabel('Problem Size')
    axes[1,1].set_ylabel('Execution Time (s)')
    axes[1,1].set_title('Execution Time vs Problem Size')
    axes[1,1].legend()
    
    plt.tight_layout()
    plt.savefig('performance_analysis.png')
    plt.close()

if __name__ == "__main__":
    # Run analysis
    results_df = run_performance_analysis()
    
    # Save results to CSV
    results_df.to_csv('performance_results.csv', index=False)
    
    # Plot results
    plot_results(results_df)
    
    # Print summary table
    print("\nPerformance Summary:")
    print("="*80)
    print(results_df.to_string(index=False))