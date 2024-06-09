import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:
    @staticmethod
    def get_Admin_Url():
        Url = config.get('Admin Login Info', 'Admin_Page_Url')
        return Url

    @staticmethod
    def get_Username():
        username = config.get('Admin Login Info', 'username')
        return username

    @staticmethod
    def get_Password():
        password = config.get('Admin Login Info', 'password')
        return password

    @staticmethod
    def get_Invalid_username():
        Invalid_username = config.get('Admin Login Info', 'Invalid_Username')
        return Invalid_username


