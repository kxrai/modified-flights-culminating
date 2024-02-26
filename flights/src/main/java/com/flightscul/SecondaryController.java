package com.flightscul;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.text.Text;
//fxml secondary controller
public class SecondaryController {

    @FXML
    private Text PTFtitle;

    @FXML
    private Button backbutton;

    @FXML
    private Text depdat;

    @FXML
    private Text econTitle;

    @FXML
    private Text genflightTitle;

    @FXML
    private Text locatoloca;

    @FXML
    private TextField opt1;

    @FXML
    private TextField opt2;

    @FXML
    private TextField opt3;

    @FXML
    private TextField opt4;

    @FXML
    private Text repdat;

    @FXML
    void switchToSecondary(ActionEvent event) {

    }
    
    /**
    *Takes the info gathered by data that's in the array
    *displays each prices onto GUI
    *https://stackoverflow.com/questions/34091561/javafx-setting-label-text-from-an-array 
    **/
    /**
    public void start(Stage secondaryStage) throws Exception {
        
    
    label.setText(text[0]);
    label.setTranslateX(200);


    Stage stage = new Stage();
    Pane pane = new Pane();
    Scene scene = new Scene(pane, 800, 500);
    stage.setScene(scene);
    stage.show();

    pane.getChildren().addAll(label);

    }
/**
*
*
**
public void makeLabel() {

    for(int i=0; i<text.length; i++) {

        label.setText(text[i]);

          }

       }
  **/

}

/**
prices_list variable in order to get price data plugged into javafx GUI
 */