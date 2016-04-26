# Rescaling-StandartDev
Two normalization methods implemented

# What is Normalization

Normalization is a method used to standardize the range of independent variables or features of data. 
In data processing, it is also known as “Feature Scaling” and is generally performed during the data 
preprocessing step. Since the range of values of raw data varies widely, in some machine learning algorithms,
objective functions will not work properly without normalization. For example, the majority of classifiers
calculate the distance between two points by the distance. If one of the features has a broad range of values, 
the distance will be governed by this particular feature. Therefore, the range of all features should be normalized
so that each feature contributes approximately proportionately to the final distance.

# Methods

# Rescaling

The simplest method is rescaling the range of features to scale the range in [0, 1] or [−1, 1]. Selecting the target range 
depends on the nature of the data. The general formula is given as:
$$x=={x-min(x)}/{max(x)-min(x)}$$                    


where x is an original value, x’ is the normalized value. For example, suppose that we have the students’ weight data, 
and the students’ weights span [160 pounds, 200 pounds]. To rescale this data, we first subtract 160 from each student’s 
weight and divide the result by 40 (the difference between the maximum and minimum weights).

#Standardization

In machine learning, we can handle various types of data, e.g. audio signals and pixel values for image data. Feature
standardization makes the values of each feature in the data have zero-mean (when subtracting the mean in the enumerator) 
and unit-variance. This method is widely used for normalization in many machine learning algorithms (e.g., support vector 
machines, logistic regression, and neural networks). This is typically done by calculating standard scores. The general 
method of calculation is to determine the distribution mean and standard deviation for each feature. Next we subtract the
mean from each feature. Then we divide the values (mean is already subtracted) of each feature by its standard deviation.

$$z={x-μ}/{σ}$$

where:

μ is the mean of the population,
σ is the standard deviation of the population.



