# Rename regions in  leica .rgn files

## The problem:

When setting up multi-well acquisitions in the LAS X navigator, the regions are created named e.g. 'A/1/R1'. When exporting .ptu files, they are only exported with the name (here 'R1') as a filename. This results in all the .ptu files being overwritten while exporting.

## The workaround:

* Before acquisition, export the generated regions as .rgn files (right-click on the regions in the lower right panel of the navigator and export as .rgn).
* Save it somewhwere accessible from a VM
* Log into a VM (any of them should do)
* Start 'Anaconda Powershell Prompt (Miniconda ZMB)'
* Change to the folder where 'rename.py' is stored, e.g.:  
`cd D:\path\to\21_BOYMAN\rename_LASX-regions`
* execute the script, giving the input .rgn file, and an optional output file, e.g.:  
`python .\rename.py D:\path\to\96-well.rgn`  
(this will overwrite '96-well.rgn') or:  
`python .\rename.py D:\path\to\96-well.rgn D:\path\to\96-well_output.rgn`  
(this will create a new file '96-well_output.rgn')
* Go back to navigator in LAS X
* Delete all created regions
* Reimport altered regions (right-click in the lower rigth panel of the navigator)
* Continue with the acquisition