# Proton Bag Model - Refactor

This repository contains a **refactored and organized version** of the calculations and simulations used in my thesis on the **MIT Bag Model applied to the quark-gluon plasma (QGP)** and **non-extensive Tsallis statistics**.

## 📂 Project Structure

```bash
ProtonBagModel-Refactor/
├── data                    # Experimental data, pressure profiles, uncertainties
├── environment.yml         # Conda environment file
├── images                  # Figures used in the thesis
├── notebooks               # Refactored Jupyter notebooks with step-by-step calculations and 
├── README.md               # Project description
└── src                      # Modular Python scripts (formulas, plotting utilities)
    ├── plot_utils.py
    └── pressure_models.py
```

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ProtonBagModel-Refactor.git
   cd ProtonBagModel-Refactor
   ```

2.	**Create the environment**:
    ```
    conda env create -f environment.yml
    conda activate proton-bag-model
    ```
3.	Launch JupyterLab:

    ```
    jupyter lab
    ```

## 🧮 Contents
- Pressure calculations: Symbolic derivations for gluons and quarks within the MIT Bag Model, both classical and using Tsallis statistics.
- Data visualizations: Consistent plots for pressure distributions, comparisons with Lattice QCD results.
- Modular code: Separated scripts for formulas and plotting utilities.

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for details.

--- 

*Developed as part of my PhD research.*