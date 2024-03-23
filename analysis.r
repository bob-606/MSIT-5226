library(DBI)
library(dplyr)
library(ggplot2)
library(plotly)
library(scatterplot3d)
conn <- dbConnect(RSQLite::SQLite(), "translations.db")
data <- dbGetQuery(conn, "SELECT * FROM WordTranslations")
str(data)
summary(data)
data$timestamp <- as.POSIXct(data$timestamp)
ggplot(data, aes(x = timestamp)) + geom_line(stat = "count") +
  labs(title = "Translation Requests Over Time",
       x = "Timestamp",
       y = "Frequency")
data_aggregated <- data %>%
  mutate(hour = as.POSIXct(round(as.numeric(timestamp) / (60*60)) * (60*60), origin="2024-01-01")) %>%
  group_by(hour) %>%
  summarise(num_requests = n())
scatterplot3d(x = as.numeric(data_aggregated$hour),
              y = data_aggregated$num_requests,
              z = as.numeric(data_aggregated$hour),
              main = "Translation Requests Over Time",
              xlab = "Time", ylab = "Number of Requests",
              zlab = "Time", color = "blue", angle = 55)
dbDisconnect(conn)

