# Question 2

# Loading libraries and sourcing
rm(list=ls())
source("my.prediction.stats.R")
source("wrappers.R")
library(glmnet)
library(rpart)
library(boot)

heart.train <- read.csv("heart.train.ass3.2021.csv", stringsAsFactors = T)
heart.test <- read.csv("heart.test.ass3.2021.csv", stringsAsFactors = T)
summary(heart.train)

# 2.1

cv = learn.tree.cv(HD ~ .,data=heart.train, nfolds=10,m=5000)
cv$best.tree

# 2.2
plot(cv$best.tree)
text(cv$best.tree, pretty=12)

# 2.5
fullmod = glm(HD ~ ., data=heart.train, family="binomial")
step.fit.bic = step(fullmod, k=log(nrow(heart.train)),direction="both",trace=0)
summary(step.fit.bic)
# 2.7

my.pred.stats(predict(cv$best.tree, heart.test)[,2], heart.test$HD)
my.pred.stats(predict(step.fit.bic, heart.test, type="response"), heart.test$HD)

# 2.8

patient62 <- data.frame(heart.test[62,])

## a.
tree_pred = predict(cv$best.tree, patient62)
tree_pred

## b.
regress_prob = predict(step.fit.bic, patient62,type="response")
regress_prob
       
# 2.9

## Confidence interval for 65th patient
bs.65 = boot(data = heart.test, function(formula,data,indices) {
  # Create a bootstrapped version of data
  d = data[indices,]
  
  # Fit a logistic regression to the bootstrapped data
  fit = glm(formula, d, family="binomial")
  
  # Compute the probability of HD and return it
  return(predict(fit, newdata=d[65,], type="response"))
},R = 5000, formula = HD ~ EXANG + OLDPEAK + CA + THAL)

boot.ci(bs.65, 0.95, type="bca")


## Confidence interval for 66th patient
bs.66 = boot(data = heart.test, function(formula,data,indices) {
  # Create a bootstrapped version of data
  d = data[indices,]
  
  # Fit a logistic regression to the bootstrapped data
  fit = glm(formula, d, family="binomial")
  
  # Compute the probability of HD and return it
  return(predict(fit, newdata=d[66,], type="response"))
},R = 5000, formula = HD ~ EXANG + OLDPEAK + CA + THAL)

boot.ci(bs.66, 0.95, type="bca")
