#!/bin/bash

# Crear notebooks para DataPreparation
touch notebooks/01-DataPreparation/Load_ScanData_LQCD.ipynb

# Crear notebooks para Calculations
touch notebooks/02-Calculations/Pressure_Classical_Tsallis.ipynb
touch notebooks/02-Calculations/Quark_Gluon_Pressure_Distributions.ipynb
touch notebooks/02-Calculations/BagConstant_Models.ipynb

# Crear notebooks para FinalPlots
touch notebooks/03-Visualizations/FinalPlots/Plot1_PressureGluons.ipynb
touch notebooks/03-Visualizations/FinalPlots/Plot2_ModelVsNature.ipynb
touch notebooks/03-Visualizations/FinalPlots/Plot3_TotalVsGluons_LQCDvsModel.ipynb
touch notebooks/03-Visualizations/FinalPlots/Plot4_BagConstantSurfaces.ipynb
touch notebooks/03-Visualizations/FinalPlots/Plot5_TsallisPressure.ipynb

# Crear notebooks para Explorations
touch notebooks/04-Explorations/ParameterStudy_Mu_q.ipynb
touch notebooks/04-Explorations/qReplacingBagPressure.ipynb
touch notebooks/04-Explorations/AlternativeRadiusDependencies.ipynb

# Crear estructura en data (subcarpetas para datos)
mkdir -p data/scanit
mkdir -p data/lqcd

echo "Notebooks y estructura de datos creados exitosamente."