# relines_parsing
Программа работает в режиме скрипта.
Функционал:
  parser_urls_rbk.py - заходит на клавную страницу сайта https://www.rbc.ru/, собирает актуальные ссылки категории ГЛАВНОЕ
  parser_content_rbk.py - получает ссылки главных новосте, структура страница немного разница.
  run_parser.py - запускает работу пакета rbk, так же скрипт принимает 3 различных параметра 
    parser.add_argument('--file', '-f', action='store_true') - если флаг установлен то собранные данные будут записаны в файл формата csv
    parser.add_argument('--img', '-i', action='store_true') - если флаг установлен то собранные данные будут иметь ссылку на картинку и описание картинки
    parser.add_argument('--length', '-l', type=int, default=100) - данный флаг задает длину в символах (перенос по словам) выводимого на экран текста, за исключением ссылок на изображение, чтобы ссылка оставалась кликабельной


Для запуска программы необходимо клонировать данные в нужный репозиторий https://github.com/DudkevichD/relines_parsing.git
- $docker build -t relines .
- $docker run relines
После чего откроется командная строка python в которую необходимо передать следующее
- $run_parser.py -l 50 -f -i (флаги передаем согласно предпочтению)
