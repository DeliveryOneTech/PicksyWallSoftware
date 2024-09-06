class Styles:
    @staticmethod
    def button():
        return """
        QPushButton {
            background-color: #60892E;
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
    def home_secondary_button():
        return """
        QPushButton {
            background-color: #BFBFBF;
            color: white;
            padding: 15px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            border-radius: 10px;
            font: 16pt "MS Shell Dlg 2";
        }
        """

    @staticmethod
    def btn_main():
        return """
            background-color: #60892E;
            border-radius: 10px;
            padding: 10px;
            color: white;
            margin-left: 20px;
            margin-right: 20px;
        """

    @staticmethod
    def btn_main_clicked():
        return """
            background-color: #BFBFBF;
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
    def btn_success(width: str = "auto", padding: str = "15px 32px"):
        return f"""
            QPushButton {{
                background-color: #60892E;
                color: white;
                padding: {padding};
                text-align: center;
                text-decoration: none;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 10px;
                width: {width};
            }}
        """

    @staticmethod
    def btn_danger(width: str = "auto", padding: str = "15px 32px"):
        return f'''
            QPushButton {{
                background-color: #f44336;
                color: white;
                padding: {padding};
                text-align: center;
                text-decoration: none;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 10px;
                width: {width};
            }}
        '''

    @staticmethod
    def btn_numeric_keyboard():
        return """
        QPushButton {
            background-color: lightgray;
            color: black;
            padding-right: 30%;
            padding-left: 30%;
            padding-top: 25%;
            padding-bottom: 25%;
            text-align: center;
            text-decoration: none;
            font-size: 25px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 10%;
            font: 20pt "Segoe UI";
        }
        """

    @staticmethod
    def green_box():
        return """
        background-color: #60892E;
        border: 1px solid gray;
        border-radius: 20px;
        padding: 10px;
        color: white;
        font: 14pt "MS Shell Dlg 2";
        """

    @staticmethod
    def gray_box():
        return """
        background-color: #BFBFBF;
        border: 1px solid #60892E;
        border-radius: 20px;
        padding: 10px;
        color: white;
        font: 14pt "MS Shell Dlg 2";
        """

    @staticmethod
    def lg_checkbox():
        return """
            QCheckBox::indicator {
                width: 40px;
                height: 40px;
            }
            QCheckBox {
                font-size: 16px;
                padding: 5px;
                margin-right: 10px;
            }
        """

    @staticmethod
    def bordered_input():
        return "font-size: 25px; padding: 10px; border: 1px solid #000; border-radius: 5px; background-color: transparent;"

    @staticmethod
    def bg_gray_input(padding=10):
        return f"font-size:25px; padding: {padding}px; border: 1px solid transparent; border-radius: 5px; background-color: #D9D9D9;"

    @staticmethod
    def get_green_color():
        return "#60892E"

    @staticmethod
    def get_gray_color():
        return "#BFBFBF"

    @staticmethod
    def get_red_color():
        return "#f44336"
