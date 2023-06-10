""" Модуль описания функций. Работа со строками """

def hi_reg_str(any_string):
   """ Все буквы ПРОПИСНЫМИ возвращаются, без лишних пробелов """

   while "  " in any_string:
    any_string= any_string.replace("  ", " ")
   return any_string.upper()


def hi_first_letters_of_words(any_text):
 """Функция hi_first_letters_of_words(any_text) возвращает копию текста, в котором в которой все слова начинаются с заглавной буквы

Например, hi_first_letters_of_words('мама МЫЛА раму') выдаст 'Мама Мыла Раму'.
У каждого слова первый символ будет иметь верхний регистр, а остальные символы слова переводятся в нижний регистр."""

 return any_text.title()

#print(hi_reg_str("А роза упала на лапу Азора"))