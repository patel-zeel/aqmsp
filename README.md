# Air Quality Modeling and Sensor Placement (AQMSP)

## Install 
To install this package and all submodules within it, run:
```
pip install git+https://github.com/patel-zeel/aqmsp.git --recursive
```

## Edit files
Whenever edits are made in submodule:
* Commit changes in submodule
* Commit changes in main repo
* If you first push changes in the main repo, it'll not fail but it has updated the commit number of submodule which is not yet pushed, so when clicked on submodule folder in the remote, it'll throw 404.
* To avoid this, first push changes in submodule and then push changes in main repo.