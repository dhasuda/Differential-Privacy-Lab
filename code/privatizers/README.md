# Privatizers

The privatizer is the class responsible for actually privatizing the data. As there are many possible ways to add noise to a dataset, we implemented a privatizer abstract class (`AbstractPrivatizer`) which defines the interface for privatizers. And the one concrete privatizer we implemented is the `LaplacePrivatizer`, that gets the noise from the Laplace distribution.

## AbstractPrivatizer

This abstract class has tree methods, and we'll go through all of them one by one in this document! This class is responsible for getting the raw data, access each value and then it calls the `privatizeSingleAnswer` method, to add noise to a single value in the dataset. The `privatizeSingleAnswer` is an abstract method, and it's were you decide what is the noise you're going to add to your data.

### `def privatize`
This is a recursive method, that access all values of the dataset.
The expected input for this method is an array of arrays of real numbers (`float`) or an array of floats, or simply a float value. 

In its parameters, there are three important parameters:
- `data`: The dataset you want to privatize
- `sensitivityValue`: If it is only one value that you are going to privatize, this value will be the [sensitivity](https://github.com/dhasuda/Differential-Privacy-Lab/blob/master/Getting%20Started/3.%20Exponential%20Mechanism.md#Sensitivity) of the noise added
- `sensitivityList`: Naturally, if your `data` is an array of values, each value may have a different [sensitivity](https://github.com/dhasuda/Differential-Privacy-Lab/blob/master/Getting%20Started/3.%20Exponential%20Mechanism.md#Sensitivity). This parameter is the value of the sensitivity for each value in the array.

The user will most probably use it to privatize an entire dataset, so let's say that the parameter it receives is an array of an array of floats, or a matrix of floats, if you will.

In this scenario, it enters the first `if` and it also makes a little check to validate the input data:
```
if (type(data) == list): // True
  if (len(data) == 0): // False, in this example
    return []
```
The user has the option to not give us a [sensitivity](https://github.com/dhasuda/Differential-Privacy-Lab/blob/master/Getting%20Started/3.%20Exponential%20Mechanism.md#Sensitivity) value, in this case we are going to estimate it based on the entire dataset. This is this part of the code:
```
if (type(data[0]) == list and sensitivityList == None):
  sensitivityList = self.getSensitivityList(data)
```

After that, we are just iterating through the `data` array and calling this same function recursively.
```
counter = 0 // Aux value to help with the sensitivity array
for value in data: // `value` can be a list or a real number
  if (type(value) == list):
    sensitivity = sensitivityList
  else:
    // Here is assumed that there is a sensitivityValue
    if (type(sensitivityValue) == float):
      sensitivity = sensitivityValue
    else:
      sensitivity = sensitivityValue[counter]

  privatizedData.append(self.privatize(value, sensitivity))
  counter += 1
```

But if the first `if` of this method is not satisfied, then you assume that `data` is a `float` value and we simply add the noise to it:
```
else:
  return self.privatizeSingleAnswer(data, sensitivityValue)
```

### def getSensitivityList
For more info about sensitivity, [click here](https://github.com/dhasuda/Differential-Privacy-Lab/blob/master/Getting%20Started/3.%20Exponential%20Mechanism.md#Sensitivity). But this method estimates the sensitivity of a column in the dataset simply by getting the difference between the maximum and the minimum value in the dataset in that column.


### def privatizeSingleAnswer
This method is the one that actually implements the noise addition to a single value. Since there are many different noises you can use to privatize your dataset, this is an abstract method, and must be implemented in a concrete privatizer. For an example of that, check the [`LaplacePrivatizer`](https://github.com/dhasuda/Differential-Privacy-Lab/blob/master/code/privatizers/laplacePrivatizer.py)

## LaplacePrivatizer
This implements the Laplace mechanism for privatizing a dataset. There are only two simple methods in this class: the constructor, and `privatizeSingleAnswer`.

### Constructor
For the constructor you only receive the epsilon value, which is a measurement of the privacy you want to add to your data. You can see the theory for it clicking [here](https://github.com/dhasuda/Differential-Privacy-Lab/blob/master/Getting%20Started/1.%20What's%20Differential%20Privacy%3F.md)

### `privatizeSingleAnswer`
Gets a value and a sensitivity for it and, based on that, draws a value from a Laplace distribution to add it to the original value. The implementation of the Laplace distribution comes from [numpy](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.laplace.html). Furthermore, we know from the [Laplace Mechanism](https://github.com/dhasuda/Differential-Privacy-Lab/blob/master/Getting%20Started/4.%20Laplace%20Mechanism.md) that the scale of the distribution is the epsilon divided by the sensitivity.
To avoid some problems with divisions by zero, we forced a minimum value for the sensitivity:
```
sensitivityValue = max(0.00001, sensitivityValue)
```

Hopefully you are now more confident to implement your own privatizer and to explore changes in the already implemented ones!