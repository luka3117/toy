library(shiny)



ui<-fluidPage(
  
  titlePanel("updateSelectInput"),
  
  radioButtons("input_radio_button", "Input radioButtons",
               c("Gumma","Tokyo",  "Ibaraki")
  ),
  selectInput("choices", "Select input",
              choices = c("Tokyo", "Gumma", "Ibaraki"), 
              ),
  radioButtons("data", "select data",
               c("iris","mtcars")
               # , selected = "Tokyo"
  )
)


server<-function(input, output, session) {
  observe({
    if (input$input_radio_button == "Tokyo") {
      choiceList = c("Shinjuku", "Shibuya", "Shinagawa")
    } else if (input$input_radio_button == "Gumma") {
      choiceList = c("Maebashi", "Takasaki", "Kiryu")
    } else {
      choiceList = c("Mito", "Tsuchiura", "Tsukuba")
    }
    
    # updateSelectInput(
    #   session, 
    #                   "choices", label = "Select input label",
    #                   choices = choiceList)
  })
}


shinyApp(ui = ui, server = server)