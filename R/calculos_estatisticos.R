install.packages('DescTools')
library(DescTools)
#base de dados: consumo de água por mês por hectare em m³
consumo.mensal.agua=data.frame(
  cana=c(265,240,265,257,265,257,265,265,257,265,257,265),
  tomate=c(201,181,201,194,201,194,201,201,194,201,194,201))

#calculadora dos principais cálculos estatísticos

#aplicando a média
apply(consumo.mensal.agua,2,mean)

#aplicando a mediana
apply(consumo.mensal.agua,2,median)

#aplicando a variância
apply(consumo.mensal.agua,2,var)

#aplicando o desvio padrão
apply(consumo.mensal.agua,2,sd)

#aplicando o valor máximo
apply(consumo.mensal.agua,2,max)

#aplicando o valor mínimo
apply(consumo.mensal.agua,2,min)

#aplicando a moda
apply(consumo.mensal.agua,2,Mode)
