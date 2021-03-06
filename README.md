# Python Data Vizualization   <a href="https://doi.org/10.5281/zenodo.4292484"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.4292484.svg" alt="DOI"></a>


Aifi Store is autonomus store for cashierless shopping experience this is achieved by multi modal sensing (Vision modality, weight modality and location modality).
<br />

This repository helps you plot and vizualize the weight sensor data and moving average from csv files from the AiFi store.
### Note:
For complete dataset click on the DOI batch at the top to download from <strong>Zenodo</strong> open source dataset repository.
<br />

<p align="center">
<img src="images/plates.png" width="500" class="center">
  </br>
  <em>AIFI Nano store layout</em>
  </p>

  <p align="center">
  <em>Image Credits <a href="https://dl.acm.org/doi/10.1145/3360322.3361018" target="_blank">AIM3S paper</a></em>
  </p>
  
### Overview

<p>The store is organised in the gondola's and each gondola has shelfs that holds the products and each shelf has weight sensor plates. These weight sensor plates data is used to find the event trigger (pick up, put down or no event) from which we can find the weight of the product picked.</p>
 <p>Gondola is similar to vertical fixture consisting of horizontal shelfs in any normal store and in this case there are 5 to 6 shelfs in a Gondola. 
  Every shelf again is composed of weight sensing plates, weight sensing modalities, there are around 12 plates on each shelf.</p>
  <p>Every plate has a sampling rate of **60Hz**, so there are 60 samples collected every second from each plate </p>
  <p>The pick up event on the plate can be observed and marked when the weight sensor reading decreases with time and increases with time when the put down event happens.</p>
  
  ### Event Detection
  <p>The event is said to be detected if the moving varience calculated from the raw weight sensor reading exceeds a set threshold of (10000gm^2 or 0.01kg^2) over the siliding window length of 0.5 seconds, which is half of the sampling rate of sensors, i.e 1 second </p>
  
  
  Pick Up Event = Object being taken from the particular gondola and shelf from the customer</br>
  <p align="center">
      <img src="images/1,3.png" class="center">
      </br>
      <em>Example Pick Up Event Graph</em>
      </br>
  </p>
  
Put Down Event = Object being placed back from the customer on that particular gondola and shelf </br>
<p align="center">
    <img src="images/1,5.png" class="center">. 
    </br>
    <em>Example Put Down Event Graph</em>
    </br>
</p>
 
NO Event = No object being picked up from that shelf </br>
<p align="center">
    <img src="images/1,1.png" class="center">
    </br>
    <em>Example No Event Graph</em>
    </br>
</p>
  

### NOTE: 
1.The python script must be in the same folder as of the weight.csv files and .csv files should not be placed in other subdirectories. <br />
2.The videos for the corresponding weight sensor data can be found in the <b>"Videos folder"</b> in the repository and are named similar to their corresponding <b>".csv"</b> files.<br />
3.Each video files consists of video data from 13 different camera angles.<br />

### Details of the weight sensor files:
<p>
These weight.csv (Baseline cases) files are from the AIFI CPS IoT 2020 week.There are over 50 cases in total and each file has 5 columns (timestamp,reading(in       grams),gondola,shelf,plate number)
</p>
  
 <p align="center">
      <img src="images/weight_file.png" height="250" width="500" class="center">
      </br>
      <em>Snapshot of weight.csv file</em>
      </br>
 </p>

<p>
Each of these files have data of around 2 minutes or 120 seconds in the form of timestamp. In order to unpack date and time from timestamp use datetime module from python.
</p>

# Instruction to run the script 

To start analysing the weigh.csv files using the python script and plot the timeseries plot for corresponding files.
1. Clone the repository<br />
`$ git clone https://github.com/Rahul664/Analysis_plots.git`<br />
2. Change the directory to cloned repository<br/>
`$ cd Analysis_plots`<br />
3. Install the requirements <br/>
`$ pip3 install -r requirements.txt`<br/>
4. Run the python script Plot.py<br />
`$ python3 Plot.py`<br />

After the script has run successfully you will find the corresponding folders of weight.csv files which contain the figures (weight vs timestamp) in the format<br/> 

# Instruction to run the Jupyter Notebook

Run the Plot.ipynb file using Jupyter Notebook by placing .csv files in the same directory as the Plot.ipynb script.<br/>
--------------------------------- --------------------------------- --------------------------------- ------ <br />

<p align="center">
gondola_number,shelf_number.png   <br />
</p>

<p align="center">
    Ex: 1,1.png<br/>
</p>
<p align="center">
    <img src="images/1,1.png" class="center">
    </br>
    <em>Timeseries Graph</em>
    </br>
</p>

--------------------------------- --------------------------------- --------------------------------- ------ <br />
