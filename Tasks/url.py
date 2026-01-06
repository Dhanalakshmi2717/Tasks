class URLShortener:
    def __init__(self):
        self.short_to_long = {}
        self.long_to_short = {}
        self.counter = 1

    def shorten(self, long_url):
        if long_url in self.long_to_short:
            return self.long_to_short[long_url]

        short_code = "url" + str(self.counter)
        self.counter += 1

        self.short_to_long[short_code] = long_url
        self.long_to_short[long_url] = short_code
        return short_code

    def expand(self, short_code):
        return self.short_to_long.get(short_code, "Invalid URL")


shortener = URLShortener()
short = shortener.shorten("https://example.com/page/123")

print("Short URL:", short)
print("Original URL:", shortener.expand(short))
