# Genetic Algorithm for Traveling Salesman Problem (TSP)

This project is a continuation of the previous **Basic Database Project**, whose repository is also available.

![Python](https://img.shields.io/badge/Python-v3.12+-brightgreen) ![Status](https://img.shields.io/badge/Status-Complete-green)

## 📖 Project Overview
This project implements a **Genetic Algorithm (GA)** to solve the **Traveling Salesman Problem (TSP)** efficiently. The algorithm optimizes the shortest possible route for visiting multiple cities, considering different selection, crossover, and mutation techniques.

### ✨ Key Features:
- **Random population generation** for diverse solutions.
- **Selection methods** like tournament and roulette wheel.
- **Crossover operations** to generate new individuals.
- **Mutation strategies** to enhance diversity.
- **Fitness evaluation** to guide evolution.
- **Convergence criteria** for terminating the algorithm.
- **Data visualization** for route optimization results.

---

## 🗂️ Project Structure
The project includes the following key files:

| File | Description |
|------|-------------|
| `dataset_preparation.py` | Reads and prepares the dataset for TSP |
| `individual.py` | Defines the structure of an individual solution |
| `evaluation.py` | Implements the fitness function |
| `selection.py` | Implements selection techniques |
| `crossover.py` | Performs crossover operations |
| `mutation.py` | Handles mutation operations |
| `termination_condition.py` | Defines termination criteria |
| `optimizer.py` | Runs the genetic algorithm |
| `main.ipynb` | Jupyter Notebook for running the algorithm |

---

## 🛠️ Setup Instructions

### Prerequisites:
- Python 3.12+
- Required Python packages: `numpy`, `matplotlib`

### Installation:
1. Clone this repository:
   ```bash
   git clone https://github.com/mohammad8186/Evolutionary-Algorithm-Project-of-Traveling-Salesman-Computational-Intelligence-Course.git
   
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the algorithm:
   ```bash
   python optimizer.py
   ```

4. Visualize results:
   - Open `main.ipynb` in Jupyter Notebook.

---

## 🚀 How the Algorithm Works

1️⃣ **Dataset Preparation:**
- Reads city coordinates from `tsp.txt`.
- Constructs a graph representation of cities.

2️⃣ **Population Initialization:**
- Randomly generates a set of possible solutions.

3️⃣ **Fitness Evaluation:**
- Computes total travel distance for each individual.

4️⃣ **Selection:**
- Chooses parents based on fitness using selection techniques.

5️⃣ **Crossover & Mutation:**
- Applies genetic operations to generate offspring.

6️⃣ **Termination Check:**
- Stops when a defined fitness threshold is met or iterations are exhausted.

---

## 📊 Performance Visualization
The project includes graphical representations of:
- **Fitness improvement over generations** 📈
- **Best route visualization** 🗺️

---

## 💡 Future Enhancements
- Implement **parallel processing** for faster execution.
- Add **hybrid optimization** with local search techniques.
- Improve **mutation and crossover diversity** for better convergence.


