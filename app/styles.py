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
        }
        """

    @staticmethod
    def label(font_size: int = 14):
        return f"QLabel {{ font: {font_size}pt \"MS Shell Dlg 2\"; }}"

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
            border-radius: 32%;
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
    def btn_main(padding: str = "10px"):
        return f"""
            background-color: #60892E;
            border-radius: 10px;
            padding: {padding};
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
            font: 20pt "MS Shell Dlg 2";
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
                border-radius: 10px;
                width: {width};
            }}
        '''

    @staticmethod
    def btn_keyboard(bg_color: str = "black"):
        return f"""
            QPushButton {{
                background-color: {bg_color};
                color: white;
                padding: 15px 32px;
                border-radius: 10px;
                font-weight: bold;
                width: auto;
                font: 20pt "Segoe UI";
            }}
        """

    @staticmethod
    def btn_keyboard_hover():
        return """
            QPushButton {
                background-color: #BFBFBF;
                color: black;
                padding: 15px 32px;
                border-radius: 10px;
                font-weight: bold;
                width: auto;
                font: 20pt "Segoe UI";
            }
        """

    @staticmethod
    def btn_numeric_keyboard():
        return """
        QPushButton {
            background-color: lightgray;
            color: black;
            padding: 15px;
            text-align: center;
            text-decoration: none;
            font-size: 25px;
            margin: 4px 2px;
            border-radius: 10%;
            font: 20pt "Segoe UI";
        }
        """

    @staticmethod
    def btn_numeric_keyboard_hover():
        return """
        QPushButton {
            background-color: #BFBFBF;
            color: black;
            padding: 15px;
            text-align: center;
            text-decoration: none;
            font-size: 25px;
            margin: 4px 2px;
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
        return "font-size: 20pt; padding: 10px; border: 1px solid #000; border-radius: 5px; background-color: transparent;"

    @staticmethod
    def bg_gray_input(padding=10):
        return f"font-size: 20pt; padding: {padding}px; border: 1px solid transparent; border-radius: 5px; background-color: #D9D9D9;"

    @staticmethod
    def get_green_color():
        return "#60892E"

    @staticmethod
    def get_gray_color():
        return "#BFBFBF"

    @staticmethod
    def get_red_color():
        return "#f44336"

    @staticmethod
    def badge_green():
        return """
        QLabel {
            background-color: #60892E;
            color: white;
            padding: 5px;
            border-radius: 5px;
            font: 12pt "MS Shell Dlg 2";
        }
        """

    @staticmethod
    def badge_gray():
        return """
        QLabel {
            background-color: #BFBFBF;
            color: white;
            padding: 5px;
            border-radius: 5px;
            font: 12pt "MS Shell Dlg 2";
        }
        """
