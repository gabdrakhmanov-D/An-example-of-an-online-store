import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class ForbiddenWordsValidator(RegexValidator):
    FORBIDDEN_WORDS: list[str] # список запрещенных слов

    FORBIDDEN_WORDS = ['казино',
                       'биржа',
                       'обман',
                       'криптовалюта',
                       'дешево',
                       'полиция',
                       'крипта',
                       'бесплатно',
                       'радар',
                       ]
    inverse_match = True

    def __call__(self, value):
        for word in self.FORBIDDEN_WORDS:
            self.regex = re.compile(rf'({word})', re.IGNORECASE)
            regex_matches = self.regex.search(value)
            invalid_input = regex_matches if self.inverse_match else not regex_matches
            if invalid_input:
                self.message = 'Слово "%(value)s", нельзя использовать при заполнении формы.'
                raise ValidationError(self.message, code=self.code, params={"value": word})