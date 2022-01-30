# Data processor for the Bradford Assay

## Introduction
This is an interative web-application developed for visualizing and processing experimental data from the Bradford Assay - a widely used assay for protein quantitation in biochemical research.


## Technologies
- Python
- Jupyter Notebook
- Pandas
- Matplotlib
- NumPy
- ipywidgets
- Voila
- Heroku

## Launch
Deployed on: bradford-data-processor.herokuapp.com/

## How to use?

Requirements:
- Copy of the Excel template: 
- Web-application: (or) Jupyter Notebook

Instructions
1. Enter the experimental data as per the format provided in the Excel template
2. Upload the excel file onto the application using the upload button
3. Click the process button to get the processed data. This includes calculating average absorbance value (if you had replicates for a condition), calculating the concentration in your aliquot and sample
4. Click the display graph to get the visualization of the standard curve, linear equation used in the calculation of proteins and the r^2 value of the model. You could also download the graph in a .png file using the download button.
