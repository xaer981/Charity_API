# Enpoints prefixes
AUTH_PREFIX = '/auth'
CHARITY_PROJECT_PREFIX = '/charity_project'
DONATION_PREFIX = '/donation'
JWT_PREFIX = '/auth/jwt'
USERS_PREFIX = '/users'

# Endpoints tags
AUTH_TAG = 'auth'
CHARITY_PROJECT_TAG = 'Charity Projects'
DONATION_TAG = 'Donations'
USERS_TAG = 'users'

# Messages for errors
DELETE_NOT_ALLOWED_MESSAGE = 'Удаление пользователей запрещено!'
DUPLICATE_PROJECT_MESSAGE = 'Проект с таким именем уже существует!'
EMAIL_IN_PASSWORD_MESSAGE = 'Password should not contain e-mail'
PROJECT_AMOUNT_LESS_INVESTED_MESSAGE = ('Нельзя установить требуемую сумму '
                                        'меньше уже вложенной')
PROJECT_CLOSED_CANT_EDIT_MESSAGE = 'Закрытый проект нельзя редактировать!'
PROJECT_INVESTED_CANT_REMOVE_MESSAGE = ('В проект были внесены средства, '
                                        'не подлежит удалению!')
PROJECT_NOT_FOUND_MESSAGE = 'Проект не найден'
SHORT_PASSWORD_MESSAGE = 'Password should be at least 3 characters'

USER_REGISTRED_INFO_MESSAGE = 'Пользователь {email} зарегистрирован.'

# AUTH constants
BACKEND_NAME = 'jwt'
JWT_LIFETIME = 3600
TOKEN_URL = 'auth/jwt/login'

# Models fields
DESCRIPTION_MIN_LENGTH = 1
INVESTED_AMOUNT_DEFAULT = 0
NAME_MAX_LENGTH = 100
NAME_MIN_LENGTH = 1

# Validators constants
MIN_AMOUNT_TO_CHECK_INVESTED = 0

# Google table constants
SHEET_COLUMN_COUNT = 11
SHEET_DATETIME_FORMAT = '%Y/%m/%d %H:%M:%S'
SHEET_ID = 0
SHEET_LOCALE = 'ru_RU'
SHEET_NAME = 'Отчет на {now}'
SHEET_ROW_COUNT = 100
SHEET_TITLE = 'Лист1'
SHEET_TYPE = 'GRID'
