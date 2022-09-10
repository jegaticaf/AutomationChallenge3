from libraries.common import log_message, capture_page_screenshot, browser
from config import OUTPUT_FOLDER, tabs_dict
from libraries.searchpe.searchpe import Searchpe

class Process():
    
    def __init__(self, credentials: dict):
        log_message("Initialization")

        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_popups": 0,
            "directory_upgrade": True,
            "download.default_directory": OUTPUT_FOLDER,
            "plugins.always_open_pdf_externally": True,
            "download.prompt_for_download": False
        }

        browser.open_available_browser(preferences = prefs)
        browser.set_window_size(1920, 1080)
        browser.maximize_browser_window()

        searchpe = Searchpe(browser, {"url": "https://www.gob.pe/busquedas"})
        searchpe.access_searchpe()
        self.searchpe = searchpe

    def start(self):
        """
        main
        """

        self.searchpe.initial_search()
        self.searchpe.filter_page()
        self.searchpe.find_articles()
        self.searchpe.create_excel()

    
    def finish(self):
        log_message("DW Process Finished")
        browser.close_browser()