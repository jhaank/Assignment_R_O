# Python Assignment using Python 3

from abc import ABC, abstractmethod
import re


class IWordFrequencyAnalyser(ABC):
    # Abstract Class
    @abstractmethod
    def calculate_highest_frequency(self, input_text):
        """

        :type input_text: String
        """
        pass

    @abstractmethod
    def calculate_frequency_for_word(self, input_text, chars):
        """

        :param chars: String
        :type input_text: String
        """
        pass

    @abstractmethod
    def calculate_most_frequent_nwords(self, input_text, input_num):
        """

        :type input_num: String
        :type input_text: String
        """
        pass


class FrequencyAnalyser(IWordFrequencyAnalyser):
    # Class to perform all the desired operation

    def calculate_highest_frequency(self, text_input):  # Returns the highest frequency in the text
        word_frequency = {}
        for word in re.split(";|,|\\*|\\n|\\s", text_input):
            if word.isalpha():
                word = word.lower()
                word_frequency[word] = word_frequency.get(word, 0) + 1
            else:
                raise Exception('Only Alphabets(a-z and A-Z) should be part of word')
        max_frequency = [(value, key) for key, value in word_frequency.items()]
        return max(max_frequency)[0]

    def calculate_frequency_for_word(self, text_input, chars):  # Returns the frequency of the specified word
        word_frequency = {}
        chars = chars.lower()
        if (chars.isalpha()) and (chars in text_input):
            for word in re.split(";|,|\\*|\\n|\\s", text_input):
                if word.isalpha():
                    word = word.lower()
                    word_frequency[word] = word_frequency.get(word, 0) + 1
                else:
                    raise Exception('Only Alphabets(a-z and A-Z) should be part of word')
        else:
            raise Exception('Incorrect Word or Not found in text')
        return word_frequency[chars]

    def calculate_most_frequent_nwords(self, text_input,
                                       number_input):  # Returns a list of the most frequent N words in the input text
        word_frequency = {}
        if number_input.isnumeric() and (int(number_input) <= len(re.split(";|,|\\*|\\n|\\s", text_input))):
            for word in re.split(";|,|\\*|\\n|\\s", text_input):
                if word.isalpha():
                    word = word.lower()
                    word_frequency[word] = word_frequency.get(word, 0) + 1
                else:
                    raise Exception('Only Alphabets(a-z and A-Z) should be part of word')

            word_fre = sorted(word_frequency.items(), key=lambda x: (-x[1], x[0]))

            count = 0
            if int(number_input) < len(word_fre):
                count = int(number_input)
            else:
                count = len(word_fre)

            return word_fre[:int(number_input)]
        else:
            raise Exception(
                'Selected number is greater than number of words text(%d)' % (len(re.split(";|,|\\*|\\n|\\s",
                                                                                           text_input))))


if __name__ == '__main__':
    end = False
    fa = FrequencyAnalyser()
    while not end:
        print('Options Available:')
        print('Press 1 : To get maximum frequency of word in the text ')
        print('Press 2 : To get the frequency of a word in the text ')
        print('Press 3 : To get the most frequent N number of words in the text ')
        print('Press 4 : To Exit ')
        print('Option Selected: ')
        option = input()
        print('Option Selected: %s' % option)
        if int(option) not in [1, 2, 3, 4]:
            print('Incorrect Option Selected...Try again')
        elif int(option) == 2:
            print('Enter text ')
            text = input()
            print('Enter Word: ')
            word = input()
            fre = fa.calculate_frequency_for_word(text, word)
            print('Frequency of %s is %d' % (word, fre))
        elif int(option) == 3:
            print('Enter text ')
            text = input()
            print('Enter Number: ')
            num = input()
            list_of_words = fa.calculate_most_frequent_nwords(text, num)
            print('List of words and their frequencies: ')
            for key, value in list_of_words:
                print(str(key) + ": " + str(value))
        elif int(option) == 1:
            print('Enter text ')
            text = input()
            value = fa.calculate_highest_frequency(text)
            print('Maximum Frequency is: ' + str(value))
        elif int(option) == 4:
            end = True
            print("Exiting Program")
