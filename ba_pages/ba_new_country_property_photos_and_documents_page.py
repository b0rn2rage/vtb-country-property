import os
from pages.base_page import BasePage
from .ba_locators import BaNewCountryPropertyPhotosAndDocumentsPageLocators


class BaNewCountryPropertyPhotosAndDocumentsPage(BasePage):
    """ Заполнение раздела 'Фото и документы' в новом отчете по ЖД """

    def attach_photos_in_photos_and_documents_tab(self):
        """ Приложить фотографии в разделе 'Фото и документы' """
        assert self.is_element_presence(*BaNewCountryPropertyPhotosAndDocumentsPageLocators.INPUT_PHOTO), \
            'Раздел с фото не успел прогрузиться'
        '''
        photos = [
            "\\samples\\test jpeg.jpeg", "\\samples\\test jpg.jpg", "\\samples\\test png.png",
            "\\samples\\test bmp.bmp"]
        '''
        photos = ["\\samples\\test jpg.jpg"]
        for photo in photos:
            input_new_photo = self.browser.find_element(*BaNewCountryPropertyPhotosAndDocumentsPageLocators.INPUT_PHOTO)
            input_new_photo.send_keys(os.getcwd() + photo)
            assert self.is_element_presence(
                *BaNewCountryPropertyPhotosAndDocumentsPageLocators.UPLOAD_PROGRESS_BAR_FOR_PHOTO, timeout=30), \
                f"Фото {photo} не загрузилось"

    def attach_documents_in_photos_and_documents_tab(self):
        """ Приложить документы в разделе 'Фото и документы' """
        assert self.is_element_presence(*BaNewCountryPropertyPhotosAndDocumentsPageLocators.INPUT_DOCUMENT), \
            'Раздел с документами не успел прогрузиться'
        '''
        documents = ["\\samples\\test jpeg.jpeg", "\\samples\\test jpg.jpg", "\\samples\\test png.png",
                     "\\samples\\test bmp.bmp", "\\samples\\test doc.doc",
                     "\\samples\\test docx.docx", "\\samples\\test pdf.pdf", "\\samples\\test tiff.tiff"]
        '''
        document = "\\samples\\test jpeg.jpeg"
        input_new_photo = self.browser.find_element(
            *BaNewCountryPropertyPhotosAndDocumentsPageLocators.INPUT_DOCUMENT)
        input_new_photo.send_keys(os.getcwd() + document)
        assert self.is_element_presence(
            *BaNewCountryPropertyPhotosAndDocumentsPageLocators.UPLOAD_PROGRESS_BAR_FOR_DOCUMENT, timeout=30), \
            f'Документ {document} не загрузился'
