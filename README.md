# Vector Simulation Tool for A-Level Mathematics

An interactive Python simulation for visualizing and manipulating vectors in 1D, 2D, and 3D space. This tool helps A-level mathematics students understand vector operations through graphical programming using matplotlib and numpy.

> **Note:** This teaching resource is hosted in the 'Stacks' repository as part of a collection of educational Python simulations.

## 🎯 Learning Objectives

After using this tool, students will be able to:

- **Understand vectors geometrically** - See vectors as arrows with magnitude and direction
- **Visualize scalar multiplication** - Observe how multiplying by a scalar stretches, shrinks, or reverses vectors
- **Understand vector addition** - See how vectors combine component-wise and geometrically
- **Explore convex combinations** - Learn how weighted averages of vectors work when weights sum to 1
- **Apply numpy and matplotlib** - Gain practical experience with Python's key scientific libraries

## 📋 System Requirements

- **Python 3.7 or higher** (Python 3.8+ recommended)
- **Operating System:** Windows, macOS, or Linux
- **Display:** A graphical display is required for the matplotlib plots

## 🚀 Installation Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/ljmgodalming/Stacks.git
cd Stacks
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- **numpy** - For numerical operations on vectors
- **matplotlib** - For creating graphical visualizations

### Step 3: Run the Simulation

```bash
python vector_simulation.py
```

## 📖 How to Use

When you run the simulation, you'll see an interactive menu:

```
============================================================
       VECTOR SIMULATION - A-Level Mathematics
============================================================

Select an operation:
  1. Scalar Multiplication (scale a vector)
  2. Vector Addition (add two vectors)
  3. Convex Combination (weighted average of vectors)
  4. Change Dimension (currently: 2)
  5. Clear Plot
  6. Exit
------------------------------------------------------------
```

### Operations Available

#### 1. Scalar Multiplication
Multiply a vector by a number (scalar):
- Enter a vector (e.g., x=3, y=2 for 2D)
- Enter a scalar (e.g., 2)
- See the original vector and the scaled result plotted together
- **Key insight:** Scalar > 1 makes vectors longer; 0 < scalar < 1 makes them shorter; negative scalars reverse direction

#### 2. Vector Addition
Add two vectors together:
- Enter two vectors
- See both input vectors and their sum plotted
- **Key insight:** Vector addition is component-wise (x₁+x₂, y₁+y₂, z₁+z₂)

#### 3. Convex Combination
Create a weighted average of vectors:
- Enter 2-4 vectors
- Enter weights (λ₁, λ₂, ...) that sum to 1 and are non-negative
- See how the result lies "between" the input vectors
- **Key insight:** The result is always within the convex hull of the input vectors

#### 4. Change Dimension
Switch between:
- **1D:** Vectors on a number line (just x)
- **2D:** Vectors in a plane (x, y)
- **3D:** Vectors in space (x, y, z)

## 🎨 Visual Features

- **Color-coded vectors:** Input vectors are blue/orange/green; results are red
- **Grid lines:** Help identify coordinates
- **Axis labels:** Clear x, y, z labeling
- **Legend:** Shows vector names and values
- **Dynamic updates:** Plots refresh as you perform operations

## 📝 Mathematical Background

### Scalar Multiplication
For a vector **v** and scalar k:
```
k × v = k × (x, y, z) = (kx, ky, kz)
```

### Vector Addition
For vectors **v₁** and **v₂**:
```
v₁ + v₂ = (x₁, y₁, z₁) + (x₂, y₂, z₂) = (x₁+x₂, y₁+y₂, z₁+z₂)
```

### Convex Combination
For vectors **v₁**, **v₂**, ..., **vₙ** with weights λ₁, λ₂, ..., λₙ:
```
v = λ₁v₁ + λ₂v₂ + ... + λₙvₙ

where: λᵢ ≥ 0 for all i, and λ₁ + λ₂ + ... + λₙ = 1
```

## 🔧 Troubleshooting

### "numpy is not installed" or "matplotlib is not installed"
Run:
```bash
pip install -r requirements.txt
```

### Plot window doesn't appear
- Ensure you have a graphical display connected
- On some systems, you may need to install a matplotlib backend:
  ```bash
  pip install pyqt5
  ```

### Python not found
- Make sure Python 3.7+ is installed
- Try using `python3` instead of `python`:
  ```bash
  python3 vector_simulation.py
  ```

## 📚 For Teachers

This tool is designed for A-level mathematics lessons on vectors. Suggested activities:

1. **Introduction to Vectors:** Start in 2D mode, show how vectors are arrows from origin
2. **Scalar Multiplication Exploration:** Try scalars like 2, 0.5, -1, 0 and observe effects
3. **Vector Addition:** Show both algebraic and geometric interpretations
4. **Convex Combinations:** Demonstrate with weights (0.5, 0.5) to show midpoint
5. **3D Extension:** Once 2D is understood, explore 3D to build spatial intuition

## 📄 Files in This Repository

- `vector_simulation.py` - Main Python script with the interactive simulation
- `requirements.txt` - Python package dependencies
- `README.md` - This documentation file

## 🤝 Contributing

This is an educational resource. Feel free to fork and adapt for your classroom needs!

## 📜 License

This educational resource is provided for teaching purposes.
