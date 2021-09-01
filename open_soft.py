import os

def open_app(app_dir):
    os.startfile(app_dir)

if __name__ == "__main__":
    app_dir = r'E:\soft\WPS Office\11.8.2.10321\office6\wpspdf.exe'
    open_app(app_dir)
    app_dir = r'E:\soft\WPS Office'
    open_app(app_dir)
    app_dir = r'notepad.exe'
    open_app(app_dir)