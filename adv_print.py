from log_with_path import log_with_path

@log_with_path('logs/adv_print_logs')
def adv_print(*args, **kwargs):
    source = str(args[0])
    start = kwargs.get('start')
    if kwargs.get('start') is None:
        start = '\n'
    max_line = kwargs.get('max_line')
    if kwargs.get('max_line') is None:
        max_line = 0
    def source_format(source): # на основе решения http://www.cyberforum.ru/python-beginners/thread1799717.html
        if max_line == 0:
            proxy_text = source
        else:
            proxy_text = ''
            counter = 0
            for word in source.split():
                counter += len(word)
                if counter > max_line:
                    proxy_text += '\n'
                    counter = len(word)
                elif proxy_text != '':
                    proxy_text += ' '
                    counter += 1
                proxy_text += word
        return proxy_text
    result = '' + start + '\n' + source_format(source)
    in_file = kwargs.get('in_file')
    if in_file is None:
        pass
    else:
        with open(in_file, 'wt', encoding='utf-8') as document:
            document.write(result)
    print(result)


if __name__ == '__main__':
    a = "Антиутопия (от «анти-» и «утопия»), также дистопия (" \
        "dystopia, букв. «плохое место» от греч. δυσ «отрицание» + " \
        "греч. τόπος «место») или какотопия (kakotopia или " \
        "cacotopia от греч. κακός «плохой») — изображение " \
        "общественного строя или сообщества, представляющегося " \
        "автору или критику нежелательным, отталкивающим или " \
        "пугающим. Является противоположностью утопии или её " \
        "деривацией.\n Антиутопические общества описаны во многих " \
        "художественных произведениях, действие которых в " \
        "литературе Нового времени происходит в будущем. " \
        "Антиутопия как жанр зачастую используется, чтобы обратить " \
        "внимание на реальные для автора проблемы в окружающей " \
        "среде, политике, экономике, религии, технологии и др. В " \
        "литературоведении XX—XXI веков антиутопии, как и утопии, " \
        "рассматриваются в ряду жанров научной фантастики. "

    adv_print(a, start='Тест adv_print', max_line=55,
              in_file='example.txt')

    adv_print(a)