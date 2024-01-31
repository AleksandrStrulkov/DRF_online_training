import re
from rest_framework.serializers import ValidationError


class LessonVideoValidator:
	def __init__(self, field):
		self.field = field

	def __call__(self, value):
		# reg = re.compile('https://www.youtube.com')
		reg = re.compile(r'(https?://)?(www\.)?youtube\.(com)/watch\?v=([\w-]+)(&.*?)?')
		tmp_value = dict(value).get(self.field)
		if not bool(reg.match(tmp_value)):
			raise ValidationError("Загружать видео разрешено только с платформы 'youtube'!")
