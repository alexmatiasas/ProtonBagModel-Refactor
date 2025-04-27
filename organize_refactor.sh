#!/bin/bash

# Define carpetas base
mkdir -p notebooks/{01-DataPreparation,02-Calculations,03-Visualizations/FinalPlots,04-Explorations}
mkdir -p src

# Crear archivos en src si no existen
touch src/pressure_models.py
touch src/bag_profiles.py
touch src/plot_utils.py

# Mensajes finales
echo "Estructura refinada creada:"
echo " - notebooks/ con subcarpetas:"
echo "    - 01-DataPreparation/"
echo "    - 02-Calculations/"
echo "    - 03-Visualizations/FinalPlots/"
echo "    - 04-Explorations/"
echo " - src/ con archivos base para modularización"