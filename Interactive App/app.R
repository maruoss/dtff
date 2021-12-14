library(shiny)
library(quantmod)

server = function(input, output, session) {
  output$plot <- renderPlot({
    data <- getSymbols(input$stocks,  
                       from = input$date[1],
                       to = input$date[2],
                       auto.assign = FALSE  
    )
    chartSeries(data, theme = chartTheme("white"),
                type = "line", log.scale = input$log, TA = NULL)
  })
} 

ui = basicPage(
  h1("Stock Price Chart"),
  textInput("stocks", "Ticker symbol for stock of interest", "AMZN"),   # default stock
  dateRangeInput("date", "Time range of interest", start = "2018-01-01", end = toString(Sys.Date()),min = "2007-01-01", max = toString(Sys.Date()),format = "yyyy-mm-dd" ),
  checkboxInput(inputId = "log", label = "log y axis", value = FALSE),  # added "log" input
  plotOutput("plot")
) 

shinyApp(ui = ui, server = server) # perform app launch