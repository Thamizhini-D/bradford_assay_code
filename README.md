# Data Processor
#### Developed for the Bradford Assay

#### Update 18/6/23
This app does not run on web anymore, at least not on Heroku. Should you need it for data analysis, feel free to download the source code and run it on your Jupyter Notebook. However, it is highly recommended to try out ProteoMetrics, a revamped version of the same tool: https://github.com/Thamizhini-D/ProteoMetHub

## Introduction
This is an interative web-application developed for visualizing and processing experimental data from the Bradford Assay - a widely used assay for protein quantitation in biochemical research.


## Technologies
- Python - 3.8.8
- Jupyter Notebook - 6.3.0
- Pandas - 1.2.4
- Matplotlib - 3.3.4
- NumPy - 1.20.1
- ipywidgets - 7.6.5
- Voila - 0.2.16
- Heroku

## Launch
Deployed on: https://bradford-data-processor.herokuapp.com/

## How to use?

Requirements:
- Download a copy of the Excel template: https://1drv.ms/x/s!Aj5GbYxiY2JqpSmA01qbYmKOFFM5?e=6cpfoA

(Check out the template containing sample data: https://1drv.ms/x/s!Aj5GbYxiY2JqpRYtWiqB6Bbzbztj?e=vZxuJA. 
This will give you an idea of how to fill the template with experimental data i.e. what to enter in each column. 
You can download a copy of this file and upload it to the application if you wanna check out how it works.
Disclaimer: data given in this template are not from any experiment. Just random numbers written to provide a demo of how to enter data into the template and how the application processes and displays that data.)

- Web-application: (or) Jupyter Notebook

Instructions
1. Enter the experimental data as per the format provided in the Excel template
2. Upload the excel file onto the application using the upload button
3. Click the process button to get the processed data. This includes calculating average absorbance value (if you had replicates for a condition), calculating the concentration in your aliquot and sample, a new colum containing how much volume is required to get 100ug of a sample
4. Click the display graph to get the visualization of the standard curve, linear equation used in the calculation of proteins and the r^2 value of the model. You could also download the graph in a .png file using the download button.




