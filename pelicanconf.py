# -------------------------------------------------------------
# -- 基本設定
# -------------------------------------------------------------
SITENAME = "2lu3"
SITEURL = ""
TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "ja"

# -------------------------------------------------------------
# -- プロフィール
# -------------------------------------------------------------
AUTHOR = "2lu3"

SITELOGO="/assets/sitelogo.png"
FAVICON='/assets/favicon.png'

# Blogroll
# LINKS = (('github', 'https://github.com/2lu3'),)

# Social widget
SOCIAL = (
    ("twitter", "https://twitter.com/hi2lu3"),
    ("github", "https://github.com/2lu3"),
)

# -------------------------------------------------------------
# -- ディレクトリ関連
# -------------------------------------------------------------
PATH = "content"
ARTICLE_PATHS = ["articles"]
STATIC_PATHS = ["assets", "articles"]


# -------------------------------------------------------------
# -- 見た目
# -------------------------------------------------------------
THEME = "./themes/Flex"



DEFAULT_PAGINATION = 20

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# -------------------------------------------------------------
# -- その他
# -------------------------------------------------------------
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
