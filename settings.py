from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
TOLOKA_PARTICIPATION_FEE = environ.get('TOLOKA_PARTICIPATION_FEE', 0.25)
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=.01,
    participation_fee=0.00,
    doc="",
    use_browser_bots=False,
    toloka_participation_fee=TOLOKA_PARTICIPATION_FEE
)

SESSION_CONFIGS = [
    dict(
        name='baseline',
        num_demo_participants=2,
        app_sequence=[
            'start',
            'sorter',
            'survey_sens',
            'dg',
            'questionnaire',
            'last'
        ],
        info=False,
        baseline=True,
        toloka=True,
        toloka_sandbox=True

    ),
    dict(
        name='info_dg_first',
        num_demo_participants=2,
        app_sequence=[
            'start',
            'sorter',
            'dg',
            'survey_sens',
            'questionnaire',
            'last'
        ],
        info=True,
        toloka=True,
        dg_first=True,
        toloka_sandbox=True

    ),
    dict(
        name='info_dg',
        num_demo_participants=2,
        app_sequence=[
            'start',
            'sorter',
            'survey_sens',
            'dg',
            'questionnaire',
            'last'
        ],
        info=True,
        toloka=True,
        toloka_sandbox=True

    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_CUSTOM_NAME = '¢'

DECIMAL_SEPARATOR = '.'
FORMAT_MODULE_PATH = [
    'survey_sens.formats',
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = 'q!20%s+pfawi^l_xsrs!9=i0uf^@3huf+t^41t&+em-hp&h_ju'

INSTALLED_APPS = ['otree', 'django.contrib.admin', ]
EXTENSION_APPS = ['tolokaregister']
TOLOKA_API = environ.get('TOLOKA_API')
SANDBOX_TOLOKA_API = environ.get('SANDBOX_TOLOKA_API')
