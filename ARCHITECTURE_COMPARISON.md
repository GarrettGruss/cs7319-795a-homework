# Architecture Comparison: Single-Program vs MapReduce

This document compares single-program architecture and MapReduce distributed processing for sentiment analysis. 

## Implementation Files

- **Single-Program**: `part_a_sentiment_single_program.ipynb`
- **MapReduce**: `sentiment_mapreduce_starter.ipynb`
- **Advanced MapReduce**: `part_a_sentiment_mapreduce.ipynb`

## Architectural Comparison

| Aspect | Single-Program | MapReduce |
|--------|---------------|-----------|
| **Processing Model** | Sequential | Parallel |
| **Data Flow** | Stream-based | Batch-based |
| **CPU Utilization** | Single core | Multi-core |


## Time Complexity Analysis

### Single-Program Architecture
```
Time Complexity: O(N)
- N = number of posts
- Each post processed sequentially
- Constant time per post: O(k) where k = average words per post
- Total: O(N × k) ≈ O(N)

Space Complexity: O(1)
- Processes one post at a time
- Constant memory footprint
- Only stores final counters
```

### MapReduce Architecture
```
Time Complexity: O(N/P) + overhead
- N = number of posts
- P = number of parallel workers
- Theoretical speedup: P times faster
- Overhead: data chunking, process creation, result aggregation

Practical Time: O(N/P + C)
- C = constant overhead for parallelization
- C becomes significant for small datasets

Space Complexity: O(N)
- Must load entire dataset for chunking
- Each worker processes chunk in memory
- Higher memory requirements
```

### Choose Single-Program When:
- Simplicity is prioritized
- Real-time streaming processing needed
- Development/testing phase

### Choose MapReduce When:
- Fault tolerance is important
- Processing time is critical
- Production environment with large datasets