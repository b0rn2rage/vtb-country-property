import os
from pages.base_page import BasePage
from .ba_locators import BaCountryPropertyPhotosAndDocsPageLocators


class BaCountryPropertyPhotosAndDocsPage(BasePage):
    """Заполнение раздела 'Фото и документы' в новом отчете по ЖД."""

    def attach_photos(self):
        """Приложить фотографии в разделе 'Фото и документы'."""
        assert self.is_element_presence(*BaCountryPropertyPhotosAndDocsPageLocators.INPUT_PHOTO), \
            'Раздел с фото не успел прогрузиться'
        photos = ["\\samples\\test jpg.jpg"]
        for photo in photos:
            input_new_photo = self.browser.find_element(*BaCountryPropertyPhotosAndDocsPageLocators.INPUT_PHOTO)
            input_new_photo.send_keys(os.getcwd() + photo)
            assert self.is_element_presence(
                *BaCountryPropertyPhotosAndDocsPageLocators.UPLOAD_PROGRESS_BAR_FOR_PHOTO, timeout=30), \
                f"Фото {photo} не загрузилось"

    def attach_documents(self):
        """Приложить документы в разделе 'Фото и документы'."""
        document = "\\samples\\test jpeg.jpeg"
        input_new_photo = self.browser.find_element(*BaCountryPropertyPhotosAndDocsPageLocators.INPUT_DOCUMENT)
        input_new_photo.send_keys(os.getcwd() + document)
        assert self.is_element_presence(
            *BaCountryPropertyPhotosAndDocsPageLocators.UPLOAD_PROGRESS_BAR_FOR_DOCUMENT, timeout=30), \
            f'Документ {document} не загрузился'

