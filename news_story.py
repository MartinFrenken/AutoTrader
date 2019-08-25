class NewsStory:
    text = ""
    source = ""
    time_posted = 0
    def set_text(self,input_text):
        global text
        text=input_text
    def set_news_source(self, news_source):
        global text
        global source
        source = news_source
