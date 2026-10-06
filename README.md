# CMPSC 202 - Midterm Programming Assignment

Name: Marshall Obeng Benne

**Instructions**: Complete the exercise below. Open book, open notes, any tools allowed (except submitting another student's work). Due tonight (10/6) at 11:59pm.

**Submission**: Fork this repository and invite your professor (username: bcmullins) to the repository. To submit, push your code to your forked repository. Make sure to include your name in the README file.

You have been provided with a starter Python file (`midterm_starter.py`). This file contains two fully implemented algorithms that solve the exact same problem: finding if an array contains duplicate values.

The file also contains a `flawed_benchmark()` function. The developer who wrote this benchmark made several severe methodological errors, making the printed timing results completely unreliable for comparing the asymptotic growth of these two algorithms.

**Your tasks**: 

1. Rewrite the `flawed_benchmark()` function to provide a robust empirical comparison of the two algorithms. List the methodological errors in the original benchmark and explain how you fixed them. Your benchmark should demonstrate the scaling behavior of the two algorithms across multiple input sizes.

Methodological errors in the original benchmark and fixes:
- The benchmark timed data generation together with the algorithm. Fix: generate the input list before the timed section, and time only the actual duplicate check.
- Each algorithm used a different random input array. Fix: use the same exact test data for both algorithms in each trial.
- The benchmark used only one input size, so it could not show scaling behavior. Fix: test several input sizes and compare the timings across the range.
- A single timing run is noisy and unstable. Fix: repeat each timing several times and use the median runtime to reduce noise.
- The original code did not control for early exits. Fix: use duplicate values placed near the end so both algorithms must traverse nearly the full array in each trial, which better reflects the algorithmic behavior.

2. Run the empirical comparion and plot the results using a plotting library of your choice (e.g., `matplotlib`, `seaborn`, etc.). Include the plot in your submission called `results.png`. Be sure to label your axes and include a legend.



