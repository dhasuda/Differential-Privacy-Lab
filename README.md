# Differential Privacy Lab
## Getting Started

If you want to get started in Differential Privacy, go to the `Getting Started` folder (https://github.com/dhasuda/Differential-Privacy-Lab/tree/master/Getting%20Started), we managed to document and explain the basics of DP there!

If you already master the basics of DP and just want to implement your own experiments using this Lab, you can follow the steps below to setup everything. I hope it is useful for you!

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

## About
This is part of the gradutaion project of Davi Grossi Hasuda about differential privacy for ITA (Instituto Tecnológico de Aeronáutica).

In this project, the Laplacian Mechanism to keep data private is implemented and analysed when using some of the most commom AI algorithms, such as Decision Tree and Machine Learning.

This project is oriented by Juliana de Melo Bezerra (http://www.comp.ita.br/~juliana/)

In this repo there is a more refined and easy to understand version of the original repo used during most of the project development, which you can find here: https://github.com/dhasuda/tg-differential-privacy
