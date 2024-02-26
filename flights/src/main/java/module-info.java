module com.flightscul {
    requires javafx.controls;
    requires javafx.fxml;

    opens com.flightscul to javafx.fxml;
    exports com.flightscul;
}
