# Question 3

# Loading libraries and sourcing
library(tidyverse)
library(boot)
library(kknn)

ms.train <- read.csv("ms.train.2021.csv")
ms.test <- read.csv("ms.test.2021.csv")
summary(ms.train)

## 3.1

k <- 1:25

mse.test <- as.data.frame(k)

for (i in seq(along = ks)) {
  ytest.hat <- fitted(kknn(intensity ~ ., ms.train, ms.test,
                           kernel = "gaussian", k=i))
  mse.test[i,2] <- mean((ytest.hat-ms.test$intensity)^2)
}

ggplot(mse.test, aes(x=k, y=V2)) +
  geom_point(colour = 'blue') +
  theme_bw() +
  labs(x = "K", y="Mean-squared Error")


## 3.2
mz <- as.data.frame(ms.test$MZ)
colours <- c("Training Data" = "blue", "True Spectrum" = "orange",
             "Estimated Spectrum" = "red")

### k=2

ytest.hat.2 <- as.data.frame(fitted(kknn(intensity ~ ., ms.train, ms.test,
                             kernel = "gaussian", k=2)))

ytest.hat.2 <- cbind(mz,ytest.hat.2)
names(ytest.hat.2)[1] <- 'MZ'
names(ytest.hat.2)[2] <- 'intensity'

ggplot(ms.train, aes(MZ, intensity)) +
  geom_point(aes(colour = "Training Data"), size = 1) +
  geom_line(data = ms.test, aes(colour = "True Spectrum"), size = 1) +
  geom_line(data = ytest.hat.2, aes(colour= "Estimated Spectrum")) +
  labs(x='Mass/Charge(MZ)', y='Relative Intensity', colour = "Legend") +
  scale_color_manual(values = colours) +
  theme_bw() +
  theme(
    legend.position = c(.05, .95),
    legend.justification = c("left", "top")
  )

### k=6

ytest.hat.6 <- as.data.frame(fitted(kknn(intensity ~ ., ms.train, ms.test,
                                         kernel = "gaussian", k=6)))

ytest.hat.6 <- cbind(mz,ytest.hat.6)
names(ytest.hat.6)[1] <- 'MZ'
names(ytest.hat.6)[2] <- 'intensity'

ggplot(ms.train, aes(MZ, intensity)) +
  geom_point(aes(colour = "Training Data"), size = 1) +
  geom_line(data = ms.test, aes(colour = "True Spectrum"), size = 1) +
  geom_line(data = ytest.hat.6, aes(colour= "Estimated Spectrum")) +
  labs(x='Mass/Charge(MZ)', y='Relative Intensity', colour = "Legend") +
  scale_color_manual(values = colours) +
  theme_bw() +
  theme(
    legend.position = c(.05, .95),
    legend.justification = c("left", "top")
  )

### k=12

ytest.hat.12 <- as.data.frame(fitted(kknn(intensity ~ ., ms.train, ms.test,
                                         kernel = "gaussian", k=12)))

ytest.hat.12 <- cbind(mz,ytest.hat.12)
names(ytest.hat.12)[1] <- 'MZ'
names(ytest.hat.12)[2] <- 'intensity'

ggplot(ms.train, aes(MZ, intensity)) +
  geom_point(aes(colour = "Training Data"), size = 1) +
  geom_line(data = ms.test, aes(colour = "True Spectrum"), size = 1) +
  geom_line(data = ytest.hat.12, aes(colour= "Estimated Spectrum")) +
  labs(x='Mass/Charge(MZ)', y='Relative Intensity', colour = "Legend") +
  scale_color_manual(values = colours) +
  theme_bw() +
  theme(
    legend.position = c(.05, .95),
    legend.justification = c("left", "top")
  )

### k = 25

ytest.hat.25 <- as.data.frame(fitted(kknn(intensity ~ ., ms.train, ms.test,
                                          kernel = "gaussian", k=25)))

ytest.hat.25 <- cbind(mz,ytest.hat.25)
names(ytest.hat.25)[1] <- 'MZ'
names(ytest.hat.25)[2] <- 'intensity'

ggplot(ms.train, aes(MZ, intensity)) +
  geom_point(aes(colour = "Training Data"), size = 1) +
  geom_line(data = ms.test, aes(colour = "True Spectrum"), size = 1) +
  geom_line(data = ytest.hat.25, aes(colour= "Estimated Spectrum")) +
  labs(x='Mass/Charge(MZ)', y='Relative Intensity', colour = "Legend") +
  scale_color_manual(values = colours) +
  theme_bw() +
  theme(
    legend.position = c(.05, .95),
    legend.justification = c("left", "top")
  )

## 3.4

knn = train.kknn(intensity ~ ., data=ms.train, kmax=25, kernel="gaussian")
knn$best.parameters$k

## 3.5

ytest.hat.4 <- as.data.frame(fitted(kknn(intensity ~ ., ms.train, ms.test,
                                          kernel = "gaussian", k=4)))

ytest.hat.4 <- cbind(mz,ytest.hat.4)
names(ytest.hat.4)[1] <- 'MZ'
names(ytest.hat.4)[2] <- 'intensity'

### Mean of testing data
ms.test.mean <- mean(ms.test$intensity)

### SD
sqrt(mean((ytest.hat.4$intensity - ms.test.mean)^2))

## 3.7
row <- which.max(ytest.hat.4$intensity)[1]
ytest.hat.4[row,1]

## 3.8

### k = 4 bootstrap
bs.knn.4 = boot(data = ms.train, function(data,indices,k,mz) {
  d = data[indices,]
  
  ytest.hat = fitted(kknn(intensity ~ ., d, ms.test[ms.test$MZ==mz,],
                          kernel = "gaussian", k=k))
  return(ytest.hat)
},R = 5000,k=4,mz=5789.8)

boot.ci(bs.knn.4, 0.95, type="bca")

### k = 3 bootstrap
bs.knn.3 = boot(data = ms.train, function(data,indices,k,mz) {
  d = data[indices,]
  
  ytest.hat = fitted(kknn(intensity ~ ., d, ms.test[ms.test$MZ==mz,],
                          kernel = "gaussian", k=k))
  return(ytest.hat)
},R = 5000,k=3,mz=5789.8)

boot.ci(bs.knn.3, 0.95, type="bca")

### k = 20 bootstrap
bs.knn.20 = boot(data = ms.train, function(data,indices,k,mz) {
  d = data[indices,]
  
  ytest.hat = fitted(kknn(intensity ~ ., d, ms.test[ms.test$MZ==mz,],
                          kernel = "gaussian", k=k))
  return(ytest.hat)
},R = 5000,k=20,mz=5789.8)

boot.ci(bs.knn.20, 0.95, type="bca")
