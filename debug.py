import json

class Debug:
    def save_list(content):
        with open('pagedump.json', 'w') as file:
            json.dump(content, file)

    def save_html(content):
        with open('page.html', 'w', encoding='utf-8') as file:
            file.write(content)

    