install.packages("skimr")
install.packages("DataExplorer")




DataExplorer
DataExplorer::create_report(iris)

system("open .")


help(package = "skimr")
help(package = "DataExplorer")
library()

library()


skimr::skim(iris) %>% knitr::kable()
