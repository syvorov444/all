
import telegram
from telegram  import ReplyKeyboardMarkup
from   imporgit t Updater, CommandHandler, MessageHandler, Filters
# Списки сайтов по категориям 
sites_clothing = ["https://www.yoox.com/us/", "https://usa.tommy.com/en", "https://calvinklein.com/", "https://zappos.com/", "https://www.6pm.com/", "https://www.ralphlauren.com/", "https://www.thenorthface.com/en-us", "https://www.armaniexchange.com/us", "https://www.armani.com/en-us", "https://www.hugoboss.com/us/", "https://www.gap.com/", "https://www.adidas.com/us", "https://www.farfetch.com/", "https://www.lacoste.com/us/", "https://www.levi.com/US/en_US/", "https://uspoloassn.com/"]
sites_shoes = ["https://www.newbalance.com/", "https://www.timberland.com/", "https://www.asics.com/us/en-us/", "https://www.underarmour.com/en-us/", "https://www.yoox.com/us/", "https://usa.tommy.com/en", "https://calvinklein.com/", "https://zappos.com/", "https://www.6pm.com/", "https://www.adidas.com/us", "https://www.lacoste.com/us/"]sites_accessories = ["https://www.wardow.com/it/checkout/cart/", "https://www.furla.com/it/it/", "https://www.valentino.com/it-it", "https://www.michaelkors.it/", "https://www.gucci.com/it/it/", "https://www.pinko.com/it-it/", "https://www.karl.com/it-it", "https://www.coccinelle.com/it/", "https://www.trussardi.com/it/it", "https://www.yoox.com/it/donna", "https://www.farfetch.com/"]
sites_electronics = ["https://www.ebay.com/", "https://www.mediamarkt.com.tr/?ref=logo_rh", "https://www.vatanbilgisayar.com/"]
# Функция для обработки команды /start
def start(update, context):
    reply_keyboard = [['Одежда', 'Обувь'], ['Аксессуары', 'Электроника']]    
    update.message.reply_text('Привет! Я твой личный шоппер. Выбери категорию товаров, чтобы увидеть список магазинов:',     
    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
# Функция для обработки сообщений
def echo(update, context):
    # Получаем текст сообщения   
        text = update.message.text
    # Определяем список сайтов в зависимости от категории    
        if text == 'Одежда':
            sites = sites_clothing    
        elif text == 'Обувь':
            sites = sites_shoes   
        elif text == 'Аксессуары':
            sites = sites_accessories    
        elif text == 'Электроника':
            sites = sites_electronics