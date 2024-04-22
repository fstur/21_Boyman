# 21_Boyman
FLIM: STAT-5 dimerization project with Roman and Thi

## Installation:
Note: These steps work on the ZMB-VMs. Please adapt accordingly if used somewhere else.

* Open 'Anaconda Powershell Prompt (MinicondaZMB)'
* When logging into a VM, the necessary conda-environment might not be installed. To list all installed environments, execute:  
  `conda env list`
* If 'zmb_21' is listed, you can skip ahead to 'Start Jupyter'. Otherwise continue with the installation steps:
* Create conda environment and install packages:  
```
conda create -n zmb_21 -c conda-forge python=3.11 -y
conda activate zmb_21
conda install -y -c conda-forge jupyterlab
conda install -y -c conda-forge nb_conda_kernels
conda install -y -c conda-forge numpy pandas matplotlib tifffile
pip install "napari[all]"
pip install torch --index-url https://download.pytorch.org/whl/cu118
pip install cellpose
```

## Start Jupyter:

* Open 'Anaconda Powershell Prompt (MinicondaZMB)'
* Activate the conda environment:  
  `conda activate zmb_21`
* Change to directory, where jupyter-notebook is:  
  e.g.: `cd Z:\home\u.sername\notebooks`
* Start jupyter-lab:  
  `jupyter-lab --browser='C:/Program Files/Mozilla Firefox/firefox.exe %s'`

