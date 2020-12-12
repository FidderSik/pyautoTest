from poium import Page, NewPageElement


class BaiduPage(Page):
    search_input = NewPageElement(id_="kw", describe="搜索框")
    search_button = NewPageElement(id_="su", describe="搜索按钮")
    ##可能是编码问题，我浏览器里的“设置”和文本框中的“设置”长得不一样，所以简单修改一下
    ##settings = NewPageElement(link_text="设置", describe="设置下拉框")
    settings = NewPageElement(id_="s-usersetting-top", describe="设置下拉框")
    search_setting = NewPageElement(css=".setpref", describe="搜索设置选项")
    save_setting = NewPageElement(css=".prefpanelgo", describe="保存设置")
