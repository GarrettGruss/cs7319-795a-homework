# CS 7319 Homework 2: Sentiment Analysis in Two Architectures

This project implements sentiment analysis using two different software architectures to demonstrate architectural trade-offs and design patterns.

## Project Overview

The goal is to analyze text datasets and classify posts based on sentiment using keyword-based rules, implementing the same functionality in two distinct architectural styles:

- **Part A**: Single-program architecture
- **Part B**: MapReduce-style pipeline architecture

## Problem Statement

Given a text dataset (one post per line), classify posts based on sentiment keywords:

### Keywords
- **Positive**: happy, excited, thrilled, love
- **Negative**: sad, depressed, angry, upset

### Classification Rules
- **Positive**: contains e1 positive keyword and no negative keyword
- **Negative**: contains e1 negative keyword and no positive keyword  
- **Mixed**: contains both positive and negative keywords
- **Neutral**: otherwise

## Data

The project includes datasets in the `data/` folder:
- `sample_us_posts.txt` - starter dataset
- `sample_us_posts_mixed.txt` - dataset with mixed sentiments
- Keywords are defined in `keywords.csv`

## Architecture Implementations

### Part A - Single-Program Architecture
A straightforward, single-process program that:
1. Reads the dataset sequentially
2. Tokenizes and classifies each line
3. Aggregates totals
4. Outputs summary and verdict

**Key characteristics**: Simple, monolithic, direct data flow

### Part B - MapReduce-Style Architecture  
A distributed processing simulation using Map ’ Shuffle/Group ’ Reduce pattern:
1. **Map**: Process each line and emit (label, 1) pairs
2. **Shuffle/Group**: Group values by sentiment label
3. **Reduce**: Sum values per label for final totals

**Key characteristics**: Parallel processing model, data partitioning, scalable design

## Expected Output Format

```
Positive=123 Negative=95 Mixed=17 Neutral=64
Verdict: Happier
```

**Verdict Rules**:
- "Happier": Positive > Negative
- "Sadder": Negative > Positive  
- "Tied": Positive = Negative

## Learning Outcomes

- Experience two distinct architectural patterns
- Understand trade-offs between simplicity and scalability
- Compare code structure, data flow, and complexity
- Analyze scalability implications for large datasets

## Course Information

**Course**: CS 7319 Software Architecture  
**Instructor**: Dr. Isaac Chow  
**Term**: Fall 2025