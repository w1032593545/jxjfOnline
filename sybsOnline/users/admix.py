import xadmin
from xadmin import views


class BaseSetting(object):
    enabel_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '即学即会IT课后台管理页面'
    site_footer = 'Powered By Bruce - 2020'

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)