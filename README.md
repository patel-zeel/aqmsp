[![Coverage](https://coveralls.io/repos/github/patel-zeel/aqmsp/badge.svg?branch=main)](https://coveralls.io/github/patel-zeel/aqmsp?branch=main)

[**Tutorials and Documentation**](https://patel-zeel.github.io/aqmsp/) | [**AQMSP Data**](https://github.com/patel-zeel/aqmsp_data)

# Air Quality Modeling and Sensor Placement (AQMSP)

## Install 
To install this package, run the following command:

```bash
pip install git+https://github.com/patel-zeel/aqmsp
```

To install the submodules, run the above command for that submodule. For example, to install the `aqmsp_data` submodule, run the following command:

```bash
pip install git+https://github.com/patel-zeel/aqmsp_data
```


## Submodules Guidelines for Contributors
Whenever edits are made in a submodule:
* Commit changes in the submodule
* Commit changes in the main repo
* If you first push changes in the main repo, it'll not fail, but it has updated the commit number of the submodule, which is not yet pushed to the remote. So, clicking on the submodule folder in the remote will throw a 404 error.
* To avoid this, first push changes in the submodule and then push changes in the main repo.