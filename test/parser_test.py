import unittest
import sys
sys.path
sys.path.append('../ocr')
from parser import Parser
import json



TEST_FILE_SAMPLE = 'data/ocr_sample.json'

class ParserTest(unittest.TestCase):

    def json(self, filepath):
        with open(filepath, 'r') as file:
            data = json.load(file)
            file.close()
        return data

    def test_total_words_single_page(self):
        total_total_words_expected = 84
        data = self.json(TEST_FILE_SAMPLE)
        ocrParser = Parser()
        pageWords = ocrParser.all_words_single_page(data)
        self.assertEqual(len(pageWords['words']), total_total_words_expected)

    def test_size_single_page(self):
        page_height_expected = 733
        page_width_expected = 550
        data = self.json(TEST_FILE_SAMPLE)
        ocrParser = Parser()
        page = ocrParser.all_words_single_page(data)
        width = page['width']
        height = page['height']
        self.assertEqual(width, page_width_expected)
        self.assertEqual(height, page_height_expected)

    def test_first_word_confidence(self):            
        first_word_confidence_expected = 0.8666607737541199  
        data = self.json(TEST_FILE_SAMPLE)  
        ocrParser = Parser()
        page = ocrParser.all_words_single_page(data)
        first_word = page['words'][0]
        self.assertEqual(first_word['confidence'], first_word_confidence_expected)

    def test_first_word_geometry(self):
        first_word_geometry_expected = [[0.1904296875, 0.2470703125], [0.40234375, 0.275390625]]
        data = self.json(TEST_FILE_SAMPLE)
        ocrParser = Parser()
        page = ocrParser.all_words_single_page(data)
        first_word = page['words'][0]
        self.assertEqual(first_word['geometry'], first_word_geometry_expected)

    def test_first_word_value(self):
        first_word_value_expected = "EAX-COMERCIO"
        data = self.json(TEST_FILE_SAMPLE)
        ocrParser = Parser()
        page = ocrParser.all_words_single_page(data)
        first_word = page['words'][0]
        self.assertEqual(first_word['value'], first_word_value_expected)

    def test_first_and_second_word_id(self):            
        first_word_id_expected = 0  
        second_word_id_expected = 1
        data = self.json(TEST_FILE_SAMPLE)
        ocrParser = Parser()
        page = ocrParser.all_words_single_page(data)
        first_word = page['words'][0]
        second_word = page['words'][1]
        self.assertEqual(first_word['id'], first_word_id_expected)
        self.assertEqual(second_word['id'], second_word_id_expected)

if __name__ == '__main__':
    unittest.main()