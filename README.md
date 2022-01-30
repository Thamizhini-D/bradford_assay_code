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
Deployed on: https://bradford-data-processor.herokuapp.com/

## How to use?

Requirements:
- Download a copy of the Excel template: https://1drv.ms/x/s!Aj5GbYxiY2JqpSmA01qbYmKOFFM5?e=6cpfoA

(Check out the template containing sample data: https://1drv.ms/x/s!Aj5GbYxiY2JqpRYtWiqB6Bbzbztj?e=vZxuJA. 
This will give you an idea of how to fill the template with experimental data i.e. what to enter in each column. 
You can download a copy of this file and upload it to the application if you wanna check out how it works.
Disclaimer: data given in this template are not from any experiment. Just random numbers written to given a demo of how to enter data into the template and how the application processes and displays that data.)

- Web-application: (or) Jupyter Notebook

Instructions
1. Enter the experimental data as per the format provided in the Excel template
2. Upload the excel file onto the application using the upload button
3. Click the process button to get the processed data. This includes calculating average absorbance value (if you had replicates for a condition), calculating the concentration in your aliquot and sample, a new colum containing how much volume is required to get 100ug of a sample
4. Click the display graph to get the visualization of the standard curve, linear equation used in the calculation of proteins and the r^2 value of the model. You could also download the graph in a .png file using the download button.




