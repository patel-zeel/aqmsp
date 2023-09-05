# Air Quality Modeling and Sensor Placement (AQMSP)

## Install 
To install this package and all submodules within it, first clone the repo recursively:
```
git clone --recursive https://github.com/patel-zeel/aqmsp.git
```

Then, install the package. This command will install all submodules as well.
```
cd aqmsp
pip install -e .
```

## Submodules Guidelines
Whenever edits are made in a submodule:
* Commit changes in the submodule
* Commit changes in the main repo
* If you first push changes in the main repo, it'll not fail, but it has updated the commit number of the submodule, which is not yet pushed to the remote. So, clicking on the submodule folder in the remote will throw a 404 error.
* To avoid this, first push changes in the submodule and then push changes in the main repo.