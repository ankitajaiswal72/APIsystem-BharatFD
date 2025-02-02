from django.db import models
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    question_hi = models.TextField(null=True, blank=True)  # Hindi
    question_bn = models.TextField(null=True, blank=True)  # Bengali

    def save(self, *args, **kwargs):
        translator = Translator()

        if not self.question_hi:  # Auto-translate to Hindi
            self.question_hi = translator.translate(self.question, dest='hi').text
        
        if not self.question_bn:  # Auto-translate to Bengali
            self.question_bn = translator.translate(self.question, dest='bn').text

        super().save(*args, **kwargs)

    def get_translation(self, lang='en'):
        if lang == 'hi' and self.question_hi:
            return {'question': self.question_hi, 'answer': self.answer}
        if lang == 'bn' and self.question_bn:
            return {'question': self.question_bn, 'answer': self.answer}
        
        return {'question': self.question, 'answer': self.answer}
