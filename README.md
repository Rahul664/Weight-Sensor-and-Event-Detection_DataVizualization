# Analyse_Weight_Sensor_Plots
This repository helps you plot the weight sensor data and moving average from csv files from the AiFi store.

To start analysing the weigh.csv files using the python script and plot the timeseries plot for corresponding files.
1. Clone the repository<br />
`$ git clone https://github.com/Rahul664/Analysis_plots.git`<br />
2. Change the directory to cloned repository<br/>
`$ cd Analysis_plots`<br />
3.Install the requirements<br/>
`$ pip3 install -r requirements.txt`<br/>
4. Run the python script Plot.py<br />
`$ python3 Plot.py`<br />
<br />
After the script has run successfully you will find the corresponding folders of weight.csv files which contain the figures (weight vs timestamp) in the format<br /> 
--------------------------------- <br />
gondola_number,shelf_number.png   <br />
--------------------------------- <br />
