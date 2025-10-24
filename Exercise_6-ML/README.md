
# Exercise Sheet 6 - Machine Learning Classification and Cross-Validation

## Overview

This exercise focuses on implementing and analyzing different classification techniques and cross-validation methods using Python. The assignment covers K-Nearest Neighbors (KNN) classification, Logistic Regression, and Cross-Validation techniques.

## Prerequisites

Required Python Libraries:

- numpy
- matplotlib
- scikit-learn
- seaborn
- scipy

## Project Structure

The exercise is divided into two main parts:

### Exercise 1: K-Nearest-Neighbours/Logistic-Regression (45%)

#### a. Data Visualization (5%)

- Loaded 'samples.npy' and 'labels.npy'
- Created scatter plot using custom colors
- Implemented visualization of binary classification data

#### b. KNN Implementation (5%)

- Implemented KNeighborsClassifier with k=2
- Calculated and displayed classification accuracy
- Code demonstrated proper use of scikit-learn's KNN implementation

#### c. Classification Boundaries (15%)

- Created visualization of decision boundaries
- Used meshgrid for boundary visualization
- Implemented custom colormap for clear visualization
- Showed classification regions with proper transparency

#### d. KNN Parameter Analysis (5%)

- Analyzed impact of different k values
- Identified smallest k value where classification islands disappear
- Found optimal k value for accuracy
- Created visualizations for multiple k values

#### e. Test Data Evaluation (5%)

- Loaded and evaluated test data
- Calculated test accuracy
- Compared training vs test performance

#### f. Logistic Regression Comparison (10%)

- Implemented Logistic Regression classifier
- Created visualizations showing:
  - Continuous classification probabilities
  - Hard decision boundaries
- Compared performance with KNN classifier

### Exercise 2: Cross Validation (55%)

#### a. Data Transformation (10%)

- Loaded and visualized non-linearly separable data
- Implemented data transformation function
- Created visualization of transformed data
- Demonstrated improvement in classification potential

#### b. KNN Parameter Study (10%)

- Implemented k-parameter study
- Created training/test accuracy plots
- Analyzed impact of k on model performance
- Visualized accuracy trends

#### c. Cross-Validation Implementation (30%)

- Implemented k-fold cross-validation
- Analyzed model performance across folds
- Found optimal k value using cross-validation
- Created visualization of cross-validation results

#### d. Error Analysis (5%)

- Created error bar plots for cross-validation
- Compared best k values from different methods
- Analyzed consistency between methods
- Provided interpretation of results

## Technical Implementation Details

### Data Processing

- Custom data transformation for non-linear classification
- Proper train-test splitting
- Implementation of cross-validation

### Visualization Techniques

- Scatter plots for data visualization
- Decision boundary plotting
- Error bar plots for accuracy analysis
- Cross-validation result visualization

### Model Implementation

- KNN classifier with various k values
- Logistic Regression classifier
- Cross-validation implementation
- Parameter optimization

## Key Findings

- KNN performed well with optimal k value determined through cross-validation
- Logistic Regression provided linear decision boundaries, showing different characteristics from KNN
- Cross-validation helped in finding robust k values and avoiding overfitting
- Data transformation significantly improved classification of non-linear data
