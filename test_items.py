import sys
import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'

languages = [
    ('ar', 'العربيّة', 'أضف الى سلة التسوق'),
    ('ca', 'català', 'Afegeix a la cistella'),
    ("cs", 'česky', 'Vložit do košíku'),
    ("da", 'dansk', 'Læg i kurv'),
    ('de', 'Deutsch', 'In Warenkorb legen'),
    ("en-gb", 'English', 'Add to basket'),
    ("el", 'Ελληνικά', 'Προσθήκη στο καλάθι'),
    ("es", 'español', 'Añadir al carrito'),
    ("fi", 'suomi', 'Lisää koriin'),
    ("fr", 'français', 'Ajouter au panier'),
    ("it", 'italiano', 'Aggiungi al carrello'),
    ("ko", '한국어', '장바구니 담기'),
    ("nl", 'Nederlands', 'Voeg aan winkelmand toe'),
    ("pl", 'polski', 'Dodaj do koszyka'),
    ("pt", 'Português', 'Adicionar ao carrinho'),
    ("pt-br", 'Português Brasileiro', 'Adicionar à cesta'),
    ("ro", 'Română', 'Adauga in cos'),
    ("ru", 'Русский', 'Добавить в корзину'),
    ("sk", 'Slovensky', 'Pridať do košíka'),
    ("uk", 'Українська', 'Додати в кошик'),
    ("zh-hans", '简体中文', 'Add to basket'),
]
# Language to cmd
for i in sys.argv:
    if i.split('=')[0] == '--language':
        lang = i.split('=')[1]
        print()

def test_get_item(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element(By.CSS_SELECTOR, "a[href$='/catalogue/']").click()  
    browser.implicitly_wait(10)    
    browser.find_element(By.CSS_SELECTOR, "a[title='Coders at Work']").click()      
    time.sleep(5)
    # Button "Add to basket"
    btn = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").text

    for i in languages:
        if lang == i[0]:
            assert btn == i[2], "OK"
            print(f'Language of button "Add to basket" is - {i[1]}')

# ====================================================================

# pytest -s -v --language=es test_items.py    
# pytest -s -v --language=ko test_items.py     
# pytest -s -v --language=ro test_items.py       
# pytest -s -v --browser_name=firefox --language=sk test_items.py    
# pytest -s -v --browser_name=firefox --language=el test_items.py  
# pytest -s -v --browser_name=firefox --language=de test_items.py    
# pytest -s -v --browser_name=firefox --language=ru test_items.py      
