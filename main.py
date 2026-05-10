class ArxitektorDasturchi:
    def __init__(self, ismi, tajriba):
        self.ismi = ismi
        self.tajriba = tajriba

    def google_tajribasi(self):
        return self.tajriba.get('Google', None)

    def meta_tajribasi(self):
        return self.tajriba.get('Meta', None)

    def is_tajribali(self):
        return self.tajriba.get('Google', None) is not None and self.tajriba.get('Meta', None) is not None

    def is_100_percent_shartlarga_javob(self):
        google_tajriba = self.google_tajribasi()
        meta_tajriba = self.meta_tajribasi()
        return google_tajriba == 100 and meta_tajriba == 100

    def is_arxitektor_dasturchi(self):
        return self.is_100_percent_shartlarga_javob() and self.is_tajribali()

arxitektor_dasturchi = ArxitektorDasturchi('Ismi', {'Google': 100, 'Meta': 100})

print(arxitektor_dasturchi.is_arxitektor_dasturchi())
