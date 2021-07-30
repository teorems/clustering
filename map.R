

plot_map <- function(data, map.clusters){

library(maps)
library(ggplot2)
library(dplyr)

world_map <- map_data("world")
groupes <- read.csv("FAO/groupes_pays_7-19-2021.csv", encoding = 'UTF-8')
monde <- groupes[groupes$Groupe.de.pays == 'Monde',]

data %>% mutate(Pays = rownames(data)) %>% 
   left_join(monde[,c('Pays','Code.ISO3')], by="Pays") %>% 
   mutate(Code.ISO3 = if_else(Pays == 'Chine, continentale', 'CHN', Code.ISO3)) %>% 
   mutate(country= iso.expand(Code.ISO3)) %>% 
   mutate(country = if_else(Pays=='Chine, continentale', 'China', country)) %>% 
   mutate(country = case_when(str_detect(country, "France") ~ "France",
                              str_detect(country,"Spain") ~ "Spain",
                              str_detect(country,"Portugal") ~ "Portugal",
                              str_detect(country, "Norway") ~  "Norway",
                              str_detect(country, "UK") ~ "UK",
                              TRUE ~ country)) %>% 
   cbind(cluster = map.clusters) -> map.data

clusters_map <- merge(world_map, map.data, by.x = "region", by.y = "country",all.x = TRUE, )

clusters_map <- arrange(clusters_map, group, order)

ggplot(clusters_map, aes(x = long, y = lat, group = group, fill = as.factor(cluster), label = region)) +
   geom_polygon(colour = "black") + theme_minimal() + labs(fill = "Cluster")
}