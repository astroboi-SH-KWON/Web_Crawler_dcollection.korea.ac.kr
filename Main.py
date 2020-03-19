from selenium import webdriver
import time

import Utils
import Process
############### start to set env ################
#  webdriver path
WEB_DRV_PATH = "C:/Users/terry/chromedriver.exe"

TARGET_URL = "http://dcollection.korea.ac.kr/"
SUB_TARGET_URL = "/browse/broDeptItemList/"
DEPT_ID = "000000003554"
# DEPT_ID = "000000003219"
TARGET_PAGE_URL = "/browse/broDeptItemList/"+ DEPT_ID +"?navigationSize=10&query=%28dept_id%3A" + DEPT_ID + "%29+AND+%28item_type_code%3ADissertation%29&locale=ko&pageSize=10&insCode=211009&sortDir=desc&searchTotalCount=0&mode=item&rows=10&searthTotalPage=0&treePageNum=1&sortField=pub_year&start=0&ajax=false&deptId=" + DEPT_ID

RESULT_PATH = "F:/Downloads/thesis"

############### end setting env ################
WEB_DRV = webdriver.Chrome(WEB_DRV_PATH)

def main():
    p = Process.Process(WEB_DRV,TARGET_URL)
    p.go_to_url(TARGET_URL + SUB_TARGET_URL + DEPT_ID)
    # get pages as list
    pages = list(p.get_one_by_xpath("//ul[@class='paging']").text.split(" "))

    thesis_url_list = []
    for page_num in pages:
        # move to target page
        p.go_to_url(TARGET_URL + TARGET_PAGE_URL + "&pageNum=" + page_num)
        # get list of thesis in current page
        thesis_list = p.get_multi_by_xpath("//form[@id='itemList']/ul/li//p[@class='title']/a")
        # get detail page url of each thesis
        for item in thesis_list:
            thesis_url_list.append(item.get_attribute("href"))

    data_list = p.get_detail_data(thesis_url_list)
    util = Utils.Utils()
    util.make_excel([RESULT_PATH, data_list])






# print("Find by key_word = [ "+ KEY_WORD +" ], OPT_NUM = [ "+ str(OPT_NUM) +" ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>")
main()




