install.packages("ggmap")
install.packages("httr")
install.packages("jsonlite")

library(ggmap)
library(httr)
library(jsonlite)

# Chave do Google Maps
register_google(key = "AIzaSyB9TXaizU5FuAH6NBEFucBWogY9bRr3hCE")

# Obter latitude e longitude de um endereço
localizacao <- geocode("Barra da Tijuca, Rio de Janeiro")

# latitude e longitude de um endereço
longitude <- localizacao$lon
latitude <- localizacao$lat

# Chave da API de Meterologia
api_key <- '111e062e7460ad3455ee894eeff4ec41'

# Método que busca dados por latitude e longitude da API de Meterologia
url <- paste0("https://api.openweathermap.org/data/2.5/weather?",
              "lat=", latitude, 
              "&lon=", longitude, 
              "&appid=", api_key,
              "&units=metric")

# Resposta do Método 
response <- GET(url)
content(response, "text")
data <- fromJSON(content(response, "text", encoding = "UTF-8"))

data <- content(response, "parsed")

names(data)  

# Pegando a Descrição do Clima
descricao <- data$weather[[1]]$description

# Pegando Temperatura, Sensação Térmica e Umidade
temperatura <- data$main$temp
sensacao_termica <- data$main$feels_like
umidade <- data$main$humidity

# Pegando Velocidade e Direção do Vento
velocidade_vento <- data$wind$speed
direcao_vento <- data$wind$deg

# Pegando Nome da Cidade e País
cidade <- data$name
pais <- data$sys$country

print(descricao)
print(temperatura)
print(sensacao_termica)
print(umidade)
print(velocidade_vento)
print(direcao_vento)
print(cidade)
print(pais)


