---

# Quantum Computing Project

## Overview

This project implements various functions to analyze quantum systems using principles of quantum mechanics. The functionalities include calculating transition probabilities, measuring observables, and analyzing system dynamics.

## Author

Sofia Vizcaya Ardila  
Escuela Colombiana de Ingeniería Julio Garavito

## Table of Contents

1. [Functions](#functions)
   - [Probability_at_State](#probabilityatstate)
   - [Probability_one_state_to_other](#probabilityonestatetooner)
   - [amplitud_vector](#amplitudvector)
   - [MeanandVariance](#meanandvariance)
   - [EigenValuesProbability](#eigenvaluesprobability)
   - [FinalState](#finalstate)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Functions

### Probability_at_State
Calculates the probability of finding a quantum system at a given position/state. This function takes 2 parameters. The first is an array and the second one is the  position where it´s at. 

**Usage:**
```python
probability = Probability_at_State(state_vector)
```

### Probability_one_state_to_other
Calculates the probability of transitioning from one state vector (ket) to another. The function takes 2 arrays. It will tell the probability of transitining in all of the states to the others.

**Usage:**
```python
probability = Probability_one_state_to_other(initial_state, target_state)
```

### amplitud_vector
Computes the probability of transitioning between two vectors after an observation. It takes 2 arrays. It will give you the amplitud after an observable. 

**Usage:**
```python
transition_probability = amplitud_vector(state_vector1, state_vector2)
```

### MeanandVariance
Given a Hermitian matrix (observable) and a ket vector, calculates the mean and variance of the observable in the specified state.It takes 2 arrays.

**Usage:**
```python
mean, variance = MeanandVariance(observable_matrix, ket_vector)
```

### EigenValuesProbability
Calculates the eigenvalues of an observable and the probability that the system transitions to one of the eigenvectors after observation.It takes two arguments.

**Usage:**
```python
eigenvalues, probabilities = EigenValuesProbability(observable_matrix)
```

### FinalState
Computes the final state of the quantum system based on a series of matrices (U_n) from an initial state.

**Usage:**
```python
final_state = FinalState(initial_state, transformation_matrices)
```

## Installation

To use this project, clone the repository and install the required packages:
```bash
git clone <repository-url>
cd <project-directory>
pip install -r requirements.txt
```

## Usage

Import the functions in your Python script:
```python
from quantum_functions import Probability_at_State, Probability_one_state_to_other, ...
```

Then you can call the functions as shown in the usage examples.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please feel free to create an issue or submit a pull request.



---
