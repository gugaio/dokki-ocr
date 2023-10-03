class Parser:

    def all_words_single_page(self, data):
        words = []
        first_page = data['pages'][0]
        for block in first_page['blocks']:
            for line in block['lines']:
                for word in line['words']:   
                    word['id'] = len(words)                 
                    words.append(word)
        height = first_page['dimensions'][0]
        width = first_page['dimensions'][1]
        page = {}
        page['words'] = words
        page['height'] = height
        page['width'] = width
        return page

   

    