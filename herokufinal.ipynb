{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b3619076",
   "metadata": {
    "extensions": {
     "jupyter_dashboards": {
      "version": 1,
      "views": {
       "default_view": {
        "col": 0,
        "height": 4,
        "row": 0,
        "width": 12
       }
      }
     }
    }
   },
   "source": [
    "# <span style='font-family:rockwell'>  <span style='color:black'> ***Bradford Assay***\n",
    "### <span style='font-family:rockwell'>  <span style='color:black'> **Data Processor**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a8acb79",
   "metadata": {
    "extensions": {
     "jupyter_dashboards": {
      "version": 1,
      "views": {
       "default_view": {
        "col": 0,
        "height": 27,
        "row": 4,
        "width": 12
       }
      }
     }
    }
   },
   "outputs": [],
   "source": [
    "%matplotlib widget\n",
    "import matplotlib.pyplot as plt\n",
    "import ipywidgets as widgets\n",
    "import pandas as pd\n",
    "import io \n",
    "from IPython.display import display, HTML, clear_output\n",
    "import numpy as np\n",
    "import scipy.stats as stats\n",
    "import warnings\n",
    "import base64\n",
    "\n",
    "#Eliminate warnings\n",
    "warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')\n",
    "warnings.simplefilter(action='ignore', category=FutureWarning)\n",
    "\n",
    "out = widgets.Output()\n",
    "display(out)\n",
    "\n",
    "uploader = widgets.FileUpload(description = \"Upload your file: xlsx/xls/csv\", multiple=False, button_style = 'info')\n",
    "uploader.layout.width = '300px'\n",
    "display(uploader)\n",
    "\n",
    "\n",
    "def on_upload_change(self):\n",
    "    global content, file_title_csv\n",
    "    with out:   \n",
    "        for file_name in uploader.value:\n",
    "            extension = file_name.split('.')[1]\n",
    "            file_title_csv = file_name.split('.')[0] + ' - processed_data' + '.csv'\n",
    "            content = uploader.value[file_name]['content']\n",
    "\n",
    "        if(extension == 'xlsx' or extension == 'xls'):\n",
    "            uploader.close()\n",
    "            content = pd.read_excel(io.BytesIO(content))\n",
    "            return display(Header_text), display(content), display(process_btn)\n",
    "        \n",
    "        elif(extension == 'csv'):\n",
    "            uploader.close()\n",
    "            content = pd.read_csv(io.BytesIO(content))\n",
    "            return display(Header_text), display(content), display(process_btn)\n",
    "\n",
    "        else:\n",
    "            uploader._counter = 0\n",
    "            display(widgets.HTML(\n",
    "    value=\"<H4><b> File not accepted: Only xlsx/xls/csv </b> </H4>\"))\n",
    "    \n",
    "\n",
    "\n",
    "uploader.observe(on_upload_change, names='value') \n",
    "\n",
    "Header_text = widgets.HTML(\n",
    "    value=\"<H1><b> File Contents </b> </H1>\"\n",
    ")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df61ffc4",
   "metadata": {
    "extensions": {
     "jupyter_dashboards": {
      "version": 1,
      "views": {
       "default_view": {
        "col": 0,
        "height": 14,
        "row": 31,
        "width": 12
       }
      }
     }
    }
   },
   "outputs": [],
   "source": [
    "out_2 = widgets.Output()\n",
    "display(out_2)\n",
    "\n",
    "process_btn = widgets.Button(description = \"Process data\", button_style='success')\n",
    "    \n",
    "# calculates the concentration using the absorbance_value, m & c values  \n",
    "def calconc (gradient, intercept, absorbance):\n",
    "    concentration = (absorbance - intercept) / gradient\n",
    "    return round(concentration, 3)\n",
    "        \n",
    "# calculates required volume to get the the desired amount of proteins from a sample under a particular condition\n",
    "def calcvol (Protein_μg_aliquot, Aliquot_volume_μl, desired_protein_μg):\n",
    "    required_volume = (desired_protein_μg*Aliquot_volume_μl)/Protein_μg_aliquot    \n",
    "    return round(required_volume, 3)\n",
    "\n",
    "# calculates the amount of proteins in the entire sample using aliquot amounts\n",
    "def calcsampleconc (Protein_μg_aliquot, ALiquot_volume_μl, Sample_volume_ml):\n",
    "    Sample_volume_μl = Sample_volume_ml*1000\n",
    "    Protein_μg_sample = (Sample_volume_μl*Protein_μg_aliquot)/ALiquot_volume_μl\n",
    "    return Protein_μg_sample\n",
    "\n",
    "def data_processing(on_upload_change):\n",
    "        global conc, abso, m, c, content_2\n",
    "        with out_2:\n",
    "            \n",
    "            process_btn.close()\n",
    "            display(Header1_text)\n",
    "            \n",
    "            content['Condition_name'] = content['Condition_name'].str.lower()\n",
    "            content['Standard_Unknown'] = content['Standard_Unknown'].str.lower()\n",
    "            \n",
    "            #reading data from the columns\n",
    "            conc = content[content.Standard_Unknown =='s']['Protein_μg_sample']\n",
    "            abso = content[content.Standard_Unknown =='s']['Absorbance_nm']\n",
    "            \n",
    "            #line of best fit using polyfit function\n",
    "            m, c = np.polyfit(conc, abso, 1)\n",
    "                        \n",
    "            #group by Condition num/name, avg the abso values, name the new columns, round the avg values\n",
    "            content_mean = content.groupby(['Condition_number'])['Absorbance_nm'].mean().round(3).rename('Average_absorbance_nm').reset_index()\n",
    "\n",
    "            #merge the new column with the main index\n",
    "            content_1 = content.merge(content_mean)\n",
    "            \n",
    "            #calculate the amount of proteins using the absorbance values\n",
    "            content_1.loc[content_1.Standard_Unknown =='u','Protein_μg_aliquot'] = calconc(m, c, content_1['Average_absorbance_nm'])\n",
    "            \n",
    "            #drop unnecessary columns\n",
    "            content_2 = content_1.drop(['Absorbance_nm', 'Replicate_number'], 1)\n",
    "\n",
    "            #drop repetetive rows\n",
    "            content_2.drop_duplicates(['Condition_number', 'Condition_name'], keep='first', inplace=True)\n",
    "            content_2.reset_index(drop=True, inplace=True)\n",
    "            \n",
    "            #calculate volume to get desired amount of proteins. Default set to 100μg\n",
    "            content_2.loc[content_2.Standard_Unknown =='u', ['Volume_(μl)_for_100μg']] = calcvol (content_2['Protein_μg_aliquot'], content_2['Aliquot_volume_μl'], 100)\n",
    "            #calculate the amount of protein in entire sample based on amounts in aliquot \n",
    "            content_2.loc[content_2.Standard_Unknown =='u','Protein_μg_sample'] = calcsampleconc(content_2['Protein_μg_aliquot'], content_2['Aliquot_volume_μl'], content_2['Sample_volume_ml'])\n",
    "            \n",
    "            return display(content_2), display(widgets.HBox([graph_btn, download_btn]))\n",
    "            \n",
    "\n",
    "process_btn.on_click(data_processing)\n",
    "Header1_text = widgets.HTML(\n",
    "    value=\"<H1><b> Processed Data </b> </H1>\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2408c087",
   "metadata": {
    "extensions": {
     "jupyter_dashboards": {
      "version": 1,
      "views": {
       "default_view": {
        "col": 0,
        "height": 14,
        "row": 45,
        "width": 12
       }
      }
     }
    }
   },
   "outputs": [],
   "source": [
    "out_3 = widgets.Output()\n",
    "display(out_3)\n",
    "\n",
    "graph_btn = widgets.Button(description = \"Display graph\", button_style='info')\n",
    "\n",
    "def graph_creator(self):\n",
    "        with out_3:\n",
    "            #layout of the graph\n",
    "            plt.ylabel('Absorbance at 595nm')\n",
    "            plt.xlabel('Amount of proteins (μg)')\n",
    "            plt.title('Graph of the standard curve')\n",
    "            \n",
    "            #plot the data points,   # plot the line of best fit\n",
    "            plt.plot(conc, abso, 'o')\n",
    "            plt.plot(conc, m*conc+c, 'g-')\n",
    "\n",
    "            plt.legend(['Standards', 'Line of best fit'])\n",
    "            plt.text(-1, .28, r\"y = {}x + {}\".format(round(m, 4), round(c, 4)), color=\"k\", fontsize=10)\n",
    "            \n",
    "            res = stats.linregress(conc, abso)\n",
    "            plt.text(-1, .24, f\"R-squared: {res.rvalue**2:.6f}\", color=\"k\", fontsize=10)\n",
    "            return plt.show()\n",
    "        \n",
    "graph_btn.on_click(graph_creator)\n",
    "\n",
    "out_4 = widgets.Output()\n",
    "display(out_4)\n",
    "\n",
    "def trigger_download(text, filename, kind='text/json'):\n",
    "    \n",
    "    testt=content_2.to_csv(index = False)\n",
    "    content_b64 = base64.b64encode(testt.encode()).decode()\n",
    "    data_url = f'data:{kind};charset=utf-8;base64,{content_b64}'\n",
    "    js_code = f\"\"\"\n",
    "        var a = document.createElement('a');\n",
    "        a.setAttribute('download', '{filename}');\n",
    "        a.setAttribute('href', '{data_url}');\n",
    "        a.click()\n",
    "    \"\"\"\n",
    "    with out_4:\n",
    "        clear_output()\n",
    "        display(HTML(f'<script>{js_code}</script>'))\n",
    "\n",
    "download_btn = widgets.Button(description='Download processed data', button_style = 'warning')\n",
    "download_btn.layout.width = '200px'\n",
    "\n",
    "\n",
    "def download_file(e=None):\n",
    "    trigger_download(content_2, file_title_csv, kind='text/plain')\n",
    "\n",
    "download_btn.on_click(download_file)"
   ]
  }
 ],
 "metadata": {
  "extensions": {
   "jupyter_dashboards": {
    "activeView": "default_view",
    "version": 1,
    "views": {
     "default_view": {
      "cellMargin": 10,
      "defaultCellHeight": 40,
      "maxColumns": 12,
      "name": "active_view",
      "type": "grid"
     }
    }
   }
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
