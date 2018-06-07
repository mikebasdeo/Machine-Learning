# Data Preprocessing

# import the dataset
dataset = read.csv("Data.csv")

dataset = dataset[, 2:3]

# take care of missing data
# dataset$Age = ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x) mean(x, na.rm =TRUE)),   dataset$Age)
# dataset$Salary = ifelse(is.na(dataset$Salary), ave(dataset$Salary, FUN = function(x) mean(x, na.rm =TRUE)),    dataset$Salary)


# # Dummy encoding for MOF
# dataset$Country = factor(dataset$Country, levels=c('France', 'Spain', 'Germany'), labels=c(1,2,3))
# 
# 
# # Dummy encoding for DVV
# dataset$Purchased = factor(dataset$Purchased, levels=c('Yes', 'No'), labels=c(1,0))

# Split data into training set and test set
library(caTools)
set.seed(123)

split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set[,2:3] = scale(training_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])

