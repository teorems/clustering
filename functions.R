
plot_wss <- function(data) {
tot.wss <-0
for (i in 1:10) {
  km <- kmeans(data, centers = i, nstart = 50)
  tot.wss[i] <- km$tot.withinss
}
plot(tot.wss, type ='b', main = 'total within sum of squares', xlab = "Number of Clusters", 
     ylab = "Within groups sum of squares")
}


plot_dendrograms <- function(data) {
  
  methods <- c("ward.D", "ward.D2", "single", "complete", "average", "mcquitty" , "median","centroid")
  for (m in methods) {
    data <- scale(data)
    data.hclust <- hclust(dist(data), method = m)
    plot(data.hclust, cex=0.5)
  }
  
}