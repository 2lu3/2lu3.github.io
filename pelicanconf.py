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

SITELOGO = "/assets/sitelogo.png"
FAVICON = "/assets/favicon.png"

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
#PATH = "content"
#PATH = "."
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
# -- プラグイン
# -------------------------------------------------------------

PLUGIN_PATHS = [
    "plugins/official",
    "plugins/custom",
]

PLUGINS = [
    "related_posts",  # 関連する記事を表示
    "tag_cloud",  # これを入れないと、タグの設定が反映されない
    #"search",  # 検索フォーム
    "filetime_from_git",  # ファイルの日時を、gitの履歴から参照する
]


# -------------------------------------------------------------
# -- その他
# -------------------------------------------------------------
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
