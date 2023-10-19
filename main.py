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


if __name__ == '__main__':
    vectorizer = CountVectorizer()
    print(vectorizer.fit_transform(corpus))
    print(vectorizer.get_feature_names())
