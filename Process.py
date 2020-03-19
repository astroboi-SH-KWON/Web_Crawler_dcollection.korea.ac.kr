import time

class Process:
    def __init__(self, web_drv, url):
        self.web_drv = web_drv
        self.url = url

    def go_to_url(self, url):
        self.web_drv.get(url)

    def click_by_id(self,id):
        self.web_drv.find_element_by_id(id).click()

    def get_one_by_xpath(self,ml_path):
        return self.web_drv.find_element_by_xpath(ml_path)

    def get_multi_by_xpath(self,ml_path):
        return self.web_drv.find_elements_by_xpath(ml_path)

    def get_one_by_css(self,css_tag):
        return self.web_drv.find_element_by_css_selector(css_tag)

    def get_detail_data(self, thesis_url_list):
        data_list = []
        # crawling detail
        for item in thesis_url_list:
            tmp_data = {
                "제목": ""
                , "저자": ""
                , "주제(키워드)": ""
                , "지도교수": ""
                , "실제URI": ""
                , "학위구분": ""
                , "발행년도": ""
            }
            # print(item)
            self.go_to_url(item)
            title = self.get_one_by_css("h3").text
            tmp_data["제목"] = title
            writer = self.get_one_by_xpath("//p[@class='writer']").text
            tmp_data["저자"] = writer
            detail_titles = self.get_multi_by_xpath("//ul/li/span[@class='eleName']")
            detail_values = self.get_multi_by_xpath("//ul/li/span[@class='eleMeta']")
            idx = 0
            for title in detail_titles:
                for tmp_key in tmp_data:
                    if title.text == tmp_key:
                        tmp_data[tmp_key] = detail_values[idx].text
                idx = idx + 1
            data_list.append(tmp_data)
        return data_list
