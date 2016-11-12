
urlString <- "http://www.omdbapi.com/?i=tt9999999"
json_file <- urlString
json_data <- fromJSON(file=json_file)
json_data$Response

json_data$Poster

df <- data.frame()
df$Title = 'd'

vecTitle <- c()
vecPoster <- c()

vecTitle <- "Carmencita"
vecPoster <- "http://ia.media-imdb.com/images/M/MV5BMjAzNDEwMzk3OV5BMl5BanBnXkFtZTcwOTk4OTM5Ng@@._V1_SX300.jpg"
vecIMDB <- "5.9"

vecTitle <- c(vecTitle, "http://www.omdbapi.com/?i=tt2")

colnames(df) <- c("Title","Poster", "Metarating", "IMDB")


for (i in 400000:500000) {
  s <- toString(i)
  s <- str_pad(s, 7, pad = "0")
  urlString <- paste("http://www.omdbapi.com/?i=tt", s, sep="")
  json_file <- urlString
  json_data <- fromJSON(file = json_file)
  if (json_data$Response == "True" && json_data$Title != "N/A" && json_data$Poster != "N/A" && json_data$imdbRating != "N/A") {
    vecTitle <- c(vecTitle, json_data$Title)
    vecPoster <- c(vecPoster, json_data$Poster)
    vecIMDB <- c(vecIMDB, json_data$imdbRating)
  }
}

df <- data.frame(vecTitle, vecPoster, vecIMDB)
colnames(df) <- c("Title","Poster", "IMDB")
write.table(df, "C:/Users/Dell/Documents/hackprinceton/movieData.txt", sep=",", row.names = FALSE)



