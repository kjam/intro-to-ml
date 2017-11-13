## Introduction to Machine Learning with Python 

A workshop designed by [Katharine Jarmul](https://kjamistan.com) for learning Machine Learning with Python. Designed for a one-day training.

### Installation

These lessons has been tested for Python 3.6 and primarily uses the latest release of each library, except where versions are pinned. You likely can run most of the code with older releases, but if you run into an issue, try upgrading the library in question first. 

First you will need to [install Conda for your OS](https://conda.io/docs/installation.html) or use a [virtual environment with pip](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Then, to install all the requirements, we will setup a conda environment. You can do so and install all the requirements like so:

```
conda create -n py3data --copy python=3.6
source activate py3data
pip install -r requirements.txt
```
or do so within your virtualenv.

Then, when you want to run code you will need to make sure you are in your environment. To do so, you will type:

```
source activate py3data
```

In addition, you will need to install [sqlite3](https://www.sqlite.org/) or make changes to the second day case study with a connection string to your database of choice. [more info](https://dataset.readthedocs.io/en/latest/quickstart.html#connecting-to-a-database)

### Repository structure

We will be using the notebooks folder for sharing our work. 

We also have a folder for data and a solutions folder (for taking a peek at the challenge solutions).

### Python2 v. Python3

This repository has been built with Python 3. If you are using Python 2 and need help porting some logic or finding alternatives, please let me know and I will try and help. :)

### Corrections?

If you find any issues in these code examples, feel free to submit an Issue or Pull Request. I appreciate your input!

### Questions?

Reach out to @kjam on Twitter or GitHub or via [Kjamistan UG website](https://kjamistan.com). 
