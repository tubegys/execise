import datetime

today = datetime.date.today()


class JenkinCrawler(object):
    def __init__(self, date=today, mode="SAN"):
        self._url = None
        self._build_number = None
        self.date = date
        self.mode = mode

    @property
    def url(self):
        self._url = "111"
        return self._url


if __name__ == "__main__":
    j = JenkinCrawler()
    print(j.url)