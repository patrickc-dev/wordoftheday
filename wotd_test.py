from wotd import WordOfTheDay


class TestWotd:

    def test_word(self):
        word = WordOfTheDay()
        assert len(word.string) > 1

    def test_url(self):
        word = WordOfTheDay()
        assert word.url[:5] == 'https'
