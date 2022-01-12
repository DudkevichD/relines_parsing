import argparse

from rbk.parser_content_rbk import parse_urls_rbk

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', action='store_true')
    parser.add_argument('--img', '-i', action='store_true')
    parser.add_argument('--length', '-l', type=int, default=100)

    args = parser.parse_args()
    if args.length < 25:
        args.length = 25

    print(args)

    news = parse_urls_rbk(file=args.file, img=args.img, length=args.length)

    for news_number, news_body in news.items():
        print(f'Статья № {news_number}')
        for key, content in news_body.items():
            print(key.upper(), ':')
            if key == "foto":
                for k, v in content.items():
                    print(k, v)
                continue

            if len(content) < args.length:
                print(content)
            else:
                content = content.split(' ')
                str_user_size = ''
                for word in content:
                    if len(str_user_size + word) < args.length:
                        str_user_size += word
                        str_user_size += ' '
                        if word == content[-1]:
                            print(str_user_size)
                    else:
                        print(str_user_size)
                        str_user_size = ''
        print('-' * args.length)
