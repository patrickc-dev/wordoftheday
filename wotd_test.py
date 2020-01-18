import wordoftheday


class TestWotd:
    
    def test_today_word(self):
        word = wordoftheday.load()
        assert len(word.string) > 1
        assert word.url[:5] == 'https'

    def test_past_word(self):
        word = wordoftheday.load(date='2020-01-01')
        assert word.string == 'redux'
        assert word.url[:5] == 'https'

