#!/usr/bin/env python3
"""
Vector Simulation Tool for A-Level Mathematics Students

This interactive simulation helps students visualize and understand vector operations
in 1D, 2D, and 3D space using matplotlib for graphics and numpy for calculations.

Learning Objectives:
- Understand vectors as arrows with magnitude and direction
- Visualize scalar multiplication (scaling vectors)
- Understand vector addition geometrically
- Explore convex combinations and their geometric meaning

Author: A-Level Mathematics Teaching Resource
"""

# ============================================================================
# DEPENDENCY CHECKING
# ============================================================================
# First, we check if the required libraries are installed.
# This provides helpful error messages for students who haven't set up their environment.

try:
    import numpy as np  # numpy is used for numerical operations on arrays/vectors
except ImportError:
    print("=" * 60)
    print("ERROR: numpy is not installed!")
    print("Please run: pip install -r requirements.txt")
    print("Or: pip install numpy")
    print("=" * 60)
    exit(1)

try:
    import matplotlib.pyplot as plt  # matplotlib is used for creating plots/graphs
    from mpl_toolkits.mplot3d import Axes3D  # Axes3D enables 3D plotting
except ImportError:
    print("=" * 60)
    print("ERROR: matplotlib is not installed!")
    print("Please run: pip install -r requirements.txt")
    print("Or: pip install matplotlib")
    print("=" * 60)
    exit(1)


# ============================================================================
# GLOBAL CONFIGURATION
# ============================================================================
# Colors for different vectors - using colorblind-friendly palette
COLORS = {
    'vector1': '#1f77b4',      # Blue - first input vector
    'vector2': '#ff7f0e',      # Orange - second input vector
    'vector3': '#2ca02c',      # Green - third input vector
    'result': '#d62728',       # Red - result vector (stands out)
    'convex_region': '#9467bd'  # Purple - for convex combination region
}


# ============================================================================
# VECTOR VISUALIZATION FUNCTIONS
# ============================================================================

def plot_1d_vectors(vectors, labels, title="1D Vector Visualization"):
    """
    Plot vectors in 1D (on a number line).
    
    In 1D, vectors are just numbers (scalars), displayed as arrows on a line.
    
    Parameters:
    -----------
    vectors : list of array-like or float
        The 1D vectors to plot. Can be 1-element arrays [x] or scalar floats.
    labels : list of str
        Labels for each vector
    title : str
        Title for the plot
    """
    # plt.clf() clears the current figure to start fresh
    plt.clf()
    
    # Create a figure and axis with appropriate size
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Convert vectors to scalar values (handles both arrays and floats)
    # This ensures consistent handling of 1D vectors whether passed as [x] or x
    scalar_values = []
    for v in vectors:
        if hasattr(v, '__len__'):  # If it's an array-like
            scalar_values.append(float(v[0]))
        else:  # If it's already a scalar
            scalar_values.append(float(v))
    
    # Find the range needed for our vectors
    all_values = [0] + scalar_values  # Include 0 as the origin
    min_val = min(all_values) - 1
    max_val = max(all_values) + 1
    
    # Draw the number line (x-axis)
    ax.axhline(y=0, color='black', linewidth=1)
    ax.set_xlim(min_val, max_val)
    ax.set_ylim(-1, len(scalar_values) + 1)
    
    # Plot each vector as an arrow from the origin
    color_keys = ['vector1', 'vector2', 'vector3', 'result']
    for i, (vec, label) in enumerate(zip(scalar_values, labels)):
        color = COLORS.get(color_keys[i % len(color_keys)], COLORS['vector1'])
        
        # Draw arrow from origin (0) to the vector value
        # We offset vertically so arrows don't overlap
        y_offset = 0.3 * (i + 1)
        ax.annotate('', 
                    xy=(vec, y_offset),     # Arrow tip
                    xytext=(0, y_offset),   # Arrow start
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))
        
        # Add label with the vector value
        ax.text(vec, y_offset + 0.2, f'{label} = {vec:.2f}', 
                ha='center', fontsize=10, color=color)
    
    # Add grid and labels
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Value', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_yticks([])  # Hide y-axis ticks since 1D only uses x
    
    # Draw origin marker
    ax.plot(0, 0, 'ko', markersize=8)  # 'ko' = black circle
    ax.text(0, -0.3, 'Origin (0)', ha='center', fontsize=9)
    
    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)  # Small pause to update display


def plot_2d_vectors(vectors, labels, title="2D Vector Visualization"):
    """
    Plot vectors in 2D (on a plane).
    
    Vectors are displayed as arrows from the origin to their (x, y) coordinates.
    
    Parameters:
    -----------
    vectors : list of array-like
        Each vector should be [x, y]
    labels : list of str
        Labels for each vector
    title : str
        Title for the plot
    """
    plt.clf()
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Calculate plot limits based on all vectors
    all_x = [0] + [v[0] for v in vectors]
    all_y = [0] + [v[1] for v in vectors]
    
    margin = 1
    x_min, x_max = min(all_x) - margin, max(all_x) + margin
    y_min, y_max = min(all_y) - margin, max(all_y) + margin
    
    # Make the plot square for better visualization
    max_range = max(x_max - x_min, y_max - y_min) / 2
    x_mid = (x_max + x_min) / 2
    y_mid = (y_max + y_min) / 2
    
    ax.set_xlim(x_mid - max_range, x_mid + max_range)
    ax.set_ylim(y_mid - max_range, y_mid + max_range)
    
    # Draw coordinate axes through origin
    ax.axhline(y=0, color='gray', linewidth=0.5)
    ax.axvline(x=0, color='gray', linewidth=0.5)
    
    # Plot each vector using quiver()
    # quiver(X, Y, U, V) draws arrows from (X, Y) with components (U, V)
    color_keys = ['vector1', 'vector2', 'vector3', 'result']
    for i, (vec, label) in enumerate(zip(vectors, labels)):
        color = COLORS.get(color_keys[i % len(color_keys)], COLORS['vector1'])
        
        # quiver parameters: X, Y = start position; U, V = vector components
        ax.quiver(0, 0, vec[0], vec[1], 
                  angles='xy',           # Use x-y coordinate system
                  scale_units='xy',      # Scale relative to data
                  scale=1,               # 1:1 scaling
                  color=color,
                  width=0.02,            # Arrow width
                  label=f'{label} = ({vec[0]:.2f}, {vec[1]:.2f})')
    
    # Add grid, labels, legend
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(loc='best', fontsize=10)
    ax.set_aspect('equal')  # Equal aspect ratio for accurate representation
    
    # Mark the origin
    ax.plot(0, 0, 'ko', markersize=6)
    
    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)


def plot_3d_vectors(vectors, labels, title="3D Vector Visualization"):
    """
    Plot vectors in 3D (in space).
    
    Vectors are displayed as arrows from the origin to their (x, y, z) coordinates.
    
    Parameters:
    -----------
    vectors : list of array-like
        Each vector should be [x, y, z]
    labels : list of str
        Labels for each vector
    title : str
        Title for the plot
    """
    plt.clf()
    fig = plt.figure(figsize=(10, 8))
    
    # Create 3D axes - this is where we use Axes3D
    ax = fig.add_subplot(111, projection='3d')
    
    # Calculate plot limits
    all_coords = [[0, 0, 0]] + [list(v) for v in vectors]
    all_x = [c[0] for c in all_coords]
    all_y = [c[1] for c in all_coords]
    all_z = [c[2] for c in all_coords]
    
    margin = 1
    max_range = max(
        max(all_x) - min(all_x),
        max(all_y) - min(all_y),
        max(all_z) - min(all_z)
    ) / 2 + margin
    
    mid_x = (max(all_x) + min(all_x)) / 2
    mid_y = (max(all_y) + min(all_y)) / 2
    mid_z = (max(all_z) + min(all_z)) / 2
    
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    
    # Plot each vector using 3D quiver
    color_keys = ['vector1', 'vector2', 'vector3', 'result']
    for i, (vec, label) in enumerate(zip(vectors, labels)):
        color = COLORS.get(color_keys[i % len(color_keys)], COLORS['vector1'])
        
        # 3D quiver: ax.quiver(x, y, z, u, v, w)
        # (x, y, z) = start point, (u, v, w) = vector components
        ax.quiver(0, 0, 0, vec[0], vec[1], vec[2],
                  color=color,
                  arrow_length_ratio=0.1,
                  linewidth=2,
                  label=f'{label} = ({vec[0]:.2f}, {vec[1]:.2f}, {vec[2]:.2f})')
    
    # Add labels and legend
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_zlabel('z', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(loc='best', fontsize=9)
    
    # Mark the origin
    ax.scatter([0], [0], [0], color='black', s=50)
    
    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)


# ============================================================================
# VECTOR OPERATIONS
# ============================================================================

def scalar_multiply(vector, scalar):
    """
    Multiply a vector by a scalar.
    
    Scalar multiplication stretches or shrinks a vector:
    - scalar > 1: vector gets longer
    - 0 < scalar < 1: vector gets shorter
    - scalar < 0: vector reverses direction
    
    Parameters:
    -----------
    vector : numpy array
        The vector to scale
    scalar : float
        The scalar multiplier
    
    Returns:
    --------
    numpy array
        The scaled vector
    """
    # numpy allows easy multiplication of arrays by scalars
    return np.array(vector) * scalar


def vector_add(vector1, vector2):
    """
    Add two vectors together.
    
    Vector addition is component-wise:
    [a, b] + [c, d] = [a+c, b+d]
    
    Geometrically, it's like placing the second vector at the tip of the first.
    
    Parameters:
    -----------
    vector1, vector2 : numpy arrays
        The vectors to add
    
    Returns:
    --------
    numpy array
        The sum of the two vectors
    """
    return np.array(vector1) + np.array(vector2)


def convex_combination(vectors, weights):
    """
    Calculate the convex combination of vectors.
    
    A convex combination is: v = λ₁v₁ + λ₂v₂ + ... + λₙvₙ
    where all λᵢ ≥ 0 and Σλᵢ = 1
    
    This gives a point "inside" the convex hull of the input vectors.
    
    Parameters:
    -----------
    vectors : list of numpy arrays
        The vectors to combine
    weights : list of float
        The weights (must be non-negative and sum to 1)
    
    Returns:
    --------
    numpy array
        The convex combination
    """
    result = np.zeros_like(vectors[0], dtype=float)
    for vector, weight in zip(vectors, weights):
        result += weight * np.array(vector)
    return result


# ============================================================================
# INPUT HANDLING FUNCTIONS
# ============================================================================

def get_float_input(prompt, default=None):
    """
    Get a float input from the user with error handling.
    
    Parameters:
    -----------
    prompt : str
        The prompt to display
    default : float, optional
        Default value if user enters nothing
    
    Returns:
    --------
    float
        The user's input as a float
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if user_input == '' and default is not None:
                return default
            return float(user_input)
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_vector_input(dimension):
    """
    Get a vector from user input.
    
    Parameters:
    -----------
    dimension : int
        The dimension of the vector (1, 2, or 3)
    
    Returns:
    --------
    numpy array
        The input vector
    """
    components = []
    labels = ['x', 'y', 'z'][:dimension]
    
    print(f"\nEnter the {dimension}D vector components:")
    for i, label in enumerate(labels):
        value = get_float_input(f"  {label} = ")
        components.append(value)
    
    return np.array(components)


def get_weights_input(n_vectors):
    """
    Get weights for convex combination from user.
    
    The weights must be non-negative and sum to 1.
    
    Parameters:
    -----------
    n_vectors : int
        Number of vectors (and weights needed)
    
    Returns:
    --------
    list of float
        The weights for each vector
    """
    while True:
        print(f"\nEnter {n_vectors} weights (must be ≥ 0 and sum to 1):")
        weights = []
        for i in range(n_vectors):
            w = get_float_input(f"  λ{i+1} = ")
            weights.append(w)
        
        # Validate: all non-negative
        if any(w < 0 for w in weights):
            print("Error: All weights must be non-negative (≥ 0)!")
            continue
        
        # Validate: sum to 1
        weight_sum = sum(weights)
        if abs(weight_sum - 1.0) > 0.0001:
            print(f"Error: Weights must sum to 1! Your weights sum to {weight_sum:.4f}")
            continue
        
        return weights


# ============================================================================
# MAIN MENU AND OPERATIONS
# ============================================================================

def display_main_menu():
    """Display the main menu and get user's choice."""
    print("\n" + "=" * 60)
    print("       VECTOR SIMULATION - A-Level Mathematics")
    print("=" * 60)
    print("\nSelect an operation:")
    print("  1. Scalar Multiplication (scale a vector)")
    print("  2. Vector Addition (add two vectors)")
    print("  3. Convex Combination (weighted average of vectors)")
    print("  4. Change Dimension (currently: {})".format(
        getattr(display_main_menu, 'current_dim', 2)))
    print("  5. Clear Plot")
    print("  6. Exit")
    print("-" * 60)
    
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def select_dimension():
    """Let user select the dimension for vectors."""
    print("\n" + "-" * 40)
    print("Select dimension:")
    print("  1. 1D (vectors on a line)")
    print("  2. 2D (vectors in a plane)")
    print("  3. 3D (vectors in space)")
    print("-" * 40)
    
    while True:
        try:
            choice = int(input("Enter dimension (1, 2, or 3): "))
            if choice in [1, 2, 3]:
                return choice
            print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter 1, 2, or 3.")


def scalar_multiplication_demo(dimension):
    """
    Demonstrate scalar multiplication interactively.
    
    Shows the original vector and the scaled result side by side.
    """
    print("\n" + "=" * 50)
    print("SCALAR MULTIPLICATION")
    print("Multiply a vector by a scalar (number)")
    print("=" * 50)
    
    # Get the vector
    vector = get_vector_input(dimension)
    print(f"\nYour vector: {vector}")
    
    # Get the scalar
    scalar = get_float_input("\nEnter the scalar (number to multiply by): ")
    
    # Calculate result
    result = scalar_multiply(vector, scalar)
    
    # Display the mathematics
    print("\n" + "-" * 40)
    print(f"Calculation: {scalar} × {vector}")
    print(f"Result: {result}")
    print("-" * 40)
    
    # Visualize
    vectors_to_plot = [vector, result]
    labels = ['Original (v)', f'Result ({scalar}v)']
    title = f"Scalar Multiplication: {scalar} × v"
    
    # plot_1d_vectors now handles arrays directly
    if dimension == 1:
        plot_1d_vectors(vectors_to_plot, labels, title)
    elif dimension == 2:
        plot_2d_vectors(vectors_to_plot, labels, title)
    else:
        plot_3d_vectors(vectors_to_plot, labels, title)
    
    return result


def vector_addition_demo(dimension):
    """
    Demonstrate vector addition interactively.
    
    Shows both input vectors and their sum.
    """
    print("\n" + "=" * 50)
    print("VECTOR ADDITION")
    print("Add two vectors together (component-wise)")
    print("=" * 50)
    
    # Get first vector
    print("\nFirst vector (v₁):")
    vector1 = get_vector_input(dimension)
    
    # Get second vector
    print("\nSecond vector (v₂):")
    vector2 = get_vector_input(dimension)
    
    # Calculate result
    result = vector_add(vector1, vector2)
    
    # Display the mathematics
    print("\n" + "-" * 40)
    print(f"v₁ = {vector1}")
    print(f"v₂ = {vector2}")
    print(f"v₁ + v₂ = {result}")
    print("-" * 40)
    
    # Visualize
    vectors_to_plot = [vector1, vector2, result]
    labels = ['v₁', 'v₂', 'v₁ + v₂']
    title = "Vector Addition: v₁ + v₂"
    
    # plot_1d_vectors now handles arrays directly
    if dimension == 1:
        plot_1d_vectors(vectors_to_plot, labels, title)
    elif dimension == 2:
        plot_2d_vectors(vectors_to_plot, labels, title)
    else:
        plot_3d_vectors(vectors_to_plot, labels, title)
    
    return result


def convex_combination_demo(dimension):
    """
    Demonstrate convex combinations interactively.
    
    A convex combination uses weights that sum to 1, showing
    how the result lies "between" or "inside" the input vectors.
    """
    print("\n" + "=" * 50)
    print("CONVEX COMBINATION")
    print("Weighted average: v = λ₁v₁ + λ₂v₂ + ...")
    print("Weights must be ≥ 0 and sum to 1")
    print("=" * 50)
    
    # Get number of vectors
    while True:
        try:
            n = int(input("\nHow many vectors? (2-4): "))
            if 2 <= n <= 4:
                break
            print("Please enter a number between 2 and 4.")
        except ValueError:
            print("Invalid input!")
    
    # Get the vectors
    vectors = []
    for i in range(n):
        print(f"\nVector {i+1} (v{i+1}):")
        vectors.append(get_vector_input(dimension))
    
    # Get the weights
    weights = get_weights_input(n)
    
    # Calculate result
    result = convex_combination(vectors, weights)
    
    # Display the mathematics
    print("\n" + "-" * 40)
    print("Calculation:")
    terms = [f"{w}×{v}" for w, v in zip(weights, vectors)]
    print(" + ".join(terms))
    print(f"Result: {result}")
    print("-" * 40)
    
    # Visualize
    vectors_to_plot = vectors + [result]
    labels = [f'v{i+1}' for i in range(n)] + ['Result']
    
    # Create title showing the combination
    weight_str = " + ".join([f"{w}v{i+1}" for i, w in enumerate(weights)])
    title = f"Convex Combination: {weight_str}"
    
    # plot_1d_vectors now handles arrays directly
    if dimension == 1:
        plot_1d_vectors(vectors_to_plot, labels, title)
    elif dimension == 2:
        plot_2d_vectors(vectors_to_plot, labels, title)
    else:
        plot_3d_vectors(vectors_to_plot, labels, title)
    
    return result


def run_simulation():
    """
    Main function to run the interactive vector simulation.
    
    Uses matplotlib's interactive mode for dynamic updates.
    """
    print("\n" + "=" * 60)
    print("  Welcome to the Vector Simulation Tool!")
    print("  A-Level Mathematics - Learning Vectors Graphically")
    print("=" * 60)
    print("\nThis tool helps you visualize vector operations:")
    print("• Scalar multiplication (stretching/shrinking)")
    print("• Vector addition (combining vectors)")
    print("• Convex combinations (weighted averages)")
    
    # Enable interactive mode for dynamic plotting
    # plt.ion() = "interactive on" - allows plots to update without blocking
    plt.ion()
    
    # Create initial figure
    fig = plt.figure(figsize=(10, 8))
    plt.title("Vector Simulation - Ready", fontsize=14)
    plt.show(block=False)
    
    # Default dimension is 2D (most intuitive for students)
    current_dimension = 2
    display_main_menu.current_dim = current_dimension
    
    print(f"\nStarting in {current_dimension}D mode.")
    print("A plot window should have opened - keep it visible!")
    
    while True:
        choice = display_main_menu()
        
        if choice == 1:
            # Scalar Multiplication
            scalar_multiplication_demo(current_dimension)
            
        elif choice == 2:
            # Vector Addition
            vector_addition_demo(current_dimension)
            
        elif choice == 3:
            # Convex Combination
            convex_combination_demo(current_dimension)
            
        elif choice == 4:
            # Change Dimension
            current_dimension = select_dimension()
            display_main_menu.current_dim = current_dimension
            print(f"\nSwitched to {current_dimension}D mode.")
            
        elif choice == 5:
            # Clear Plot
            plt.clf()
            plt.title("Vector Simulation - Cleared", fontsize=14)
            plt.draw()
            print("\nPlot cleared.")
            
        elif choice == 6:
            # Exit
            print("\n" + "=" * 50)
            print("Thank you for using the Vector Simulation Tool!")
            print("Keep practicing - vectors are everywhere in maths!")
            print("=" * 50)
            plt.close('all')
            break
        
        # Pause to let user see the plot
        input("\nPress Enter to continue...")


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    """
    Entry point for the script.
    
    When you run 'python vector_simulation.py', Python looks for this
    block and executes it. This is a standard Python convention for
    making scripts that can be both imported and run directly.
    """
    try:
        run_simulation()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\nSimulation interrupted. Goodbye!")
        plt.close('all')
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("If you're having trouble, check that matplotlib and numpy are installed:")
        print("  pip install -r requirements.txt")
        raise
