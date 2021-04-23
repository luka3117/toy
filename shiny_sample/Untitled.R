suppressMessages(library(dplyr))


n = 100000
mu1 <- 20
sigma1 <- 11
mu2 <- 10
sigma2 <- 10

data<-rnorm(n = n, mu1, sigma1) * rnorm(n = n, mu2, sigma2) 
plot(density(data), col = "red", 
     main = data %>% mean()
     )

# hist(data, probability = T, breaks = 20)

# %>% hist(.,probability = T)
