import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "j)k4_c#&ue8e(e7^9+j)_x4vc5y)z+#tlai$sfzaje=gbcw1ma"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["quvonchbek.uz"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "chat",
    "ckeditor",
    "ckeditor_uploader",
]

CKEDITOR_UPLOAD_PATH = "uploads/"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "anonymus_chat.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "anonymus_chat.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tashkent"

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True


STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

MEDIA_URL = "/media/"
MEDIA_ROOT = "media/"


# CKEDITOR_CONFIGS = {
#     "default": {
#         "toolbar_Custom": [
#             {
#                 "name": "document",
#                 "items": [
#                     "Source",
#                     "-",
#                     "Save",
#                     "NewPage",
#                     "Preview",
#                     "Print",
#                     "-",
#                     "Templates",
#                 ],
#             },
#             {
#                 "name": "clipboard",
#                 "items": [
#                     "Cut",
#                     "Copy",
#                     "Paste",
#                     "PasteText",
#                     "PasteFromWord",
#                     "-",
#                     "Undo",
#                     "Redo",
#                 ],
#             },
#             {"name": "editing", "items": ["Find", "Replace", "-", "SelectAll"]},
#             {
#                 "name": "forms",
#                 "items": [
#                     "Form",
#                     "Checkbox",
#                     "Radio",
#                     "TextField",
#                     "Textarea",
#                     "Select",
#                     "Button",
#                     "ImageButton",
#                     "HiddenField",
#                 ],
#             },
#             "/",
#             {
#                 "name": "basicstyles",
#                 "items": [
#                     "Bold",
#                     "Italic",
#                     "Underline",
#                     "Strike",
#                     "Subscript",
#                     "Superscript",
#                     "-",
#                     "RemoveFormat",
#                 ],
#             },
#             {
#                 "name": "paragraph",
#                 "items": [
#                     "NumberedList",
#                     "BulletedList",
#                     "-",
#                     "Outdent",
#                     "Indent",
#                     "-",
#                     "Blockquote",
#                     "CreateDiv",
#                     "-",
#                     "JustifyLeft",
#                     "JustifyCenter",
#                     "JustifyRight",
#                     "JustifyBlock",
#                     "-",
#                     "BidiLtr",
#                     "BidiRtl",
#                     "Language",
#                 ],
#             },
#             {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
#             {
#                 "name": "insert",
#                 "items": [
#                     "Image",
#                     "Youtube",
#                     "Flash",
#                     "Table",
#                     "HorizontalRule",
#                     "Smiley",
#                     "SpecialChar",
#                     "PageBreak",
#                     "Iframe",
#                 ],
#             },
#             "/",
#             {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
#             {"name": "colors", "items": ["TextColor", "BGColor"]},
#             {"name": "tools", "items": ["Maximize", "ShowBlocks"]},
#             {"name": "about", "items": ["CodeSnippet"]},
#             {"name": "about", "items": ["About"]},
#             "/",  # put this to force next toolbar on new line
#             {
#                 "name": "yourcustomtools",
#                 "items": [
#                     # put the name of your editor.ui.addButton here
#                     "Preview",
#                     "Maximize",
#                 ],
#             },
#         ],
#         "toolbar": "Custom",  # put selected toolbar config here
#         "toolbarGroups": [
#             {"name": "document", "groups": ["mode", "document", "doctools"]}
#         ],
#         'width': '50%',
#         "height": "50%",
#         "filebrowserWindowHeight": 725,
#         "filebrowserWindowWidth": 940,
#         "toolbarCanCollapse": True,
#         "mathJaxLib": "//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML",
#         "tabSpaces": 4,
#         "extraPlugins": ",".join(
#             [
#                 "uploadimage",  # the upload image feature
#                 # your extra plugins here
#                 "div",
#                 "autolink",
#                 "autoembed",
#                 "embedsemantic",
#                 "autogrow",
#                 "devtools",
#                 "widget",
#                 "lineutils",
#                 "clipboard",
#                 "dialog",
#                 "dialogui",
#                 "elementspath",
#                 "codesnippet",
#             ]
#         ),
#     }
# }
