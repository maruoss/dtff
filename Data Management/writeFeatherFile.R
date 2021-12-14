library(feather)

researchPath <- Sys.getenv("RESEARCH_PATH")
featherPath <- paste0(researchPath, "\\4-Data Management\\test.feather")
df <- data.frame(replicate(10,sample(0:1,1000,rep=TRUE)))
write_feather(df, featherPath)

