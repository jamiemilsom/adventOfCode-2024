# Advent of Code 2024  

Welcome to my **Advent of Code 2024** repository! 🎄  

## Purpose  
I’m using this years advent of code to improve my software development skills, with a particular focus on **Test-Driven Development (TDD)** aswell as a general fun challenge. All solutions are implemented using Python, and tests are written and executed with **pytest**.  
I’ve kept library usage to a minimum in this project because I believe implementing most of the puzzles from scratch is the best way to learn. That said, I’ve made an exception for **NumPy**, as practicing data manipulation with it is invaluable given its importance in machine learning.

## Structure  
Each day of the challenge has its own folder containing:  
- `dayX.py`: The implementation for that day's puzzle.  
- `test_dayX.py`: Unit tests written in pytest, following the TDD approach.
- `task.txt`: The task description from https://adventofcode.com/
- `input.txt`: The provided puzzle input from https://adventofcode.com/

Example folder structure:  
```
day1/  
  ├── day1.py  
  ├── test_day1.py
  ├── task.txt
  ├── input.txt

day2/  
  ├── day2.py  
  ├── test_day2.py
  ├── task.txt
  ├── input.txt
...  
```  

## Goals  
- Practice **TDD principles**: Write tests before implementing functionality.  
- Reinforce Python fundamentals and problem-solving skills.  
- Stay consistent and complete all 25 days of the challenge.  

## How to Run  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/jamiemilsom/adventOfCode-2024.git  
   cd adventOfCode-2024  
   ```  

2. Install dependencies:  
   ```bash  
   pip install pytest
   pip install numpy
   ```  

3. Run tests for a specific day:  
   ```bash  
   pytest dayXX/test_solution.py  
   ```  

4. (Optional) Run all tests in the repository:  
   ```bash  
   pytest  
   ```  

## Contributions  
This repository is primarily for personal learning, so contributions aren’t expected. However, feel free to fork it or share ideas if you’d like!  
