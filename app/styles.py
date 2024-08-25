class Styles:
    @staticmethod
    def button():
        return """
        QPushButton {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
        """

    @staticmethod
    def label():
        return """
        QLabel {
            font: 14pt "MS Shell Dlg 2";
        }
        """

    @staticmethod
    def header():
        return """
        QLabel {
            font: 18pt "MS Shell Dlg 2";
        }
        """

    @staticmethod
    def bg_transparent():
        return """
        background-color: transparent;
        """

    @staticmethod
    def btn_back():
        return """
        QPushButton {
            text-align: left;
            background-color: transparent;
            border: 2px solid gray;
            padding: 8px;
            border-radius: 40%;
        }
        """

    @staticmethod
    def home_page_others_button():
        return """
        QPushButton {
            background-color: #BFBFBF;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            margin-left: 80px;
            border-radius: 10px;
            font: 16pt "MS Shell Dlg 2";            
        }
        """

    @staticmethod
    def btn_main():
        return """
            background-color: #4CAF50;
            border-radius: 10px;
            padding: 10px;
            color: white;
            margin-left: 20px;
            margin-right: 20px;
        """

    @staticmethod
    def btn_main_clicked():
        return """
            background-color: #45a049;
            border-radius: 10px;
            padding: 10px;
            color: white;
            margin-left: 20px;
            margin-right: 20px;
        """

    @staticmethod
    def otp_input():
        return """
        QLineEdit {
            background-color: lightgray;
            border: 0px;
            border-radius: 5px;
            padding: 10px;
            color: black;
            font-size: 16px;
            margin: 0px;
            font: 16pt "MS Shell Dlg 2";
        }
        """

    @staticmethod
    def btn_success():
        return """
        QPushButton {
            background-color: #4CAF50;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 10px;
        }
        """

    @staticmethod
    def btn_danger():
        return """
        QPushButton {
            background-color: #f44336;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 10px;
        }
        """

    @staticmethod
    def btn_numeric_keyboard():
        return """
        QPushButton {
            background-color: lightgray;
            color: black;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            font-size: 25px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 10px;
        }
        """

