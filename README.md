# Differential-Privacy-Lab
## Setup

There is a script `setup.sh` that can help you with that. It creates a brand new environment and install all the dependencies needed for you to run the Differential Privacy Lab. Simply run the script in the terminal

```
sh setup.sh
```

The setup only needs to be done once

## Activating environment and using notebooks

After the setup is complete at least once, you can run the following commands from the root directory of this repo:
```
source venv/bin/activate
cd code/
jupyter notebook
```

This will open a new window or tab in your browser of choice. From there, all the availabel directories to have access to all notebooks implemented!


### About
This is part of the gradutaion project of Davi Grossi Hasuda about differential privacy for ITA (Instituto Tecnológico de Aeronáutica).

In this project, the Laplacian Mechanism to keep data private is implemented and analysed when using some of the most commom AI algorithms, such as Decision Tree and Machine Learning.

This project is oriented by Juliana de Melo Bezerra (http://www.comp.ita.br/~juliana/)