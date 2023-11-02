from math import log

corpus = [
 'Crock Pot Pasta Never boil pasta again',
 'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]


class CountVectorizer:
    def __init__(self, vocabulary: list[str] = None):
        self.vocabulary = vocabulary

    def fit_transform(self, lines: list[str]) -> list[list]:
        self.vocabulary = []
        for word in ' '.join(lines).lower().split(' '):
            if word not in self.vocabulary:
                self.vocabulary.append(word)
        count_matrix = [
            [line.lower().count(word) for word in self.vocabulary]
            for line in lines
        ]
        return count_matrix

    def get_feature_names(self):
        return self.vocabulary


class TfidfTransformer:
    def __init__(self):
        pass

    def tf_matrix(self, cm: list[list[int | float]]) -> list[list[float]]:
        tf = [[round(i/sum(row), 2) for i in row] for row in cm]
        return tf

    def idf_matrix(self, cm: list[list[int | float]]) -> list[float]:
        n = len(cm[0])
        idf = [sum([1 if row[i] else 0 for row in cm]) for i in range(n)]
        idf = [
            round(log((len(cm)+1)/(el+1))+1, 2) for el in idf
        ]
        return idf

    def fit_transform(self, cm: list[list[int | float]]) -> list[list[float]]:
        tf = self.tf_matrix(cm)
        idf = self.idf_matrix(cm)
        return [
            [round(row[i] * idf[i], 2) for i in range(len(row))] for row in tf
        ]


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, lines: list[str]) -> list[list[float]]:
        cm = super().fit_transform(lines)
        return self.transformer.fit_transform(cm)


if __name__ == '__main__':
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.fit_transform(corpus))
    print(vectorizer.get_feature_names())
    transformer = TfidfTransformer()
    print(transformer.tf_matrix(count_matrix))
    print(transformer.idf_matrix(count_matrix))
    print(transformer.fit_transform(count_matrix))
    vect = TfidfVectorizer()
    print(vect.fit_transform(corpus))
    print(vect.get_feature_names())
