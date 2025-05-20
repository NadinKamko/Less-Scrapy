import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")
        return None

def word_game():
    print("Добро пожаловать в игру")

    while True:
        word_dict = get_english_words()
        word = word_dict.get('english_words')
        word_definition = word_dict.get('word_definition')

        # Перевод слова и определения
        word_ru = GoogleTranslator(source='auto', target='ru').translate(word)
        definition_ru = GoogleTranslator(source='auto', target='ru').translate(word_definition)

        print(f'Слово - {word_ru}')
        print(f'Значение - {definition_ru}')

        user = input('Что это за слово? ')
        if user.strip().lower() == word.lower():
            print('Все верно!')
        else:
            print(f'Ответ неверный, было загадано - {word}')

        play_again = input('хотите сыграть еще раз? (y/n): ')
        if play_again.strip().lower() != 'y':
            print('Спасибо за игру!')
            break

word_game()






