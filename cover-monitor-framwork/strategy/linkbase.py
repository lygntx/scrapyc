# -*- coding: utf-8 -*-
from .strategy import Strategy
from utils.url import get_url_site

class Linkbase(Strategy):
    """docstring for Linkbase"""
    name = "linkbase"

    def is_pc(self,site):
        PC_SITE = self.settings["PC_SITE"]
        PC_DOMAIN = self.settings["PC_DOMAIN"]
        if site in PC_SITE: return True
        for domain in PC_DOMAIN:
            if site.endswith(domain):
                return True
        return False

    def run(self,data):
        
        for case in data:
            if case.close:
                continue
            ld = case.get_data("linkbase")
            l2patch = case.get_data("l2patch")
            l2base = case.get_data("l2base")
            site = get_url_site(case.target)

            if ld and l2patch and l2base and ld.get("urlnew") == "-" and  l2patch.get("urlnew") == "-" and  l2base.get("urlnew") == "-":
                    case.set_result("conclusion","notFound")
                    case.set_result("owner","zhangzhenhu@baidu.com")
                    case.close = True
                    continue
            if ld:
                #import pdb
                #pdb.set_trace()
                urlnew = ld.get("urlnew")
                try:
                    weight = int(ld.get("weight"))
                except:
                    weight = 0
                try:
                    wise = int(ld.get("Wise"))
                except:
                    wise = -1
                if urlnew == "CHK":
                    if  weight == 9 or wise >0  or (weight >10 and self.is_pc(site) ) :
                        case.set_result("conclusion","noProblem")
                        case.set_result("reason","wise=%d&&weight=%d"%(wise,weight))
                        #case.set_result("additional","pcccdb")
                        case.close = True
                        case.ok = True
                    elif weight >10 :
                        case.set_result("conclusion","wiseEorr")
                        case.set_result("reason","wise=%d&&weight=%d"%(wise,weight))
                        #case.set_result("additional","pcccdb")
                        case.close = True

                    else:
                        case.set_result("conclusion","weight%d"%weight)
                        case.set_result("reason","wise=%d&&weight=%d"%(wise,weight))
                        #case.set_result("additional","pcccdb")
                        case.close = True                                               
                    # case.set_result("conclusion","lcDiff")
                    # case.close = True
                    continue
                elif urlnew == "GET":
                    url_level  = ld.get("url_level")
                    forceGET  = ld.get("forceGET")
                    crawl_fail = ld.get("crawl_fail")
                    del_reason = ld.get("del_reason")
                    if crawl_fail == True:
                        case.set_result("conclusion","crawlFail")
                        case.set_result("reason","crawl_total:%d&&crawl_fail:%d"%(ld.get("craw_count"),ld.get("fail_count")))
                        case.close = True

                    elif url_level in ["1","0"]:
                        case.set_result("conclusion","lowLevel")
                        case.set_result("reason","url_level=%s"%url_level)
                        case.close = True
                    elif del_reason == "0" :
                        case.set_result("reason","urlnew=GET&&url_level=%s&&forceGET=%s"%(url_level,forceGET))
                        case.set_result("conclusion","unCrawl")
                        #case.set_result("owner","wangyifang@baidu.com")
                        case.close = True
                        continue
                    elif del_reason != "0" :
                        case.set_result("reason","del_reason=%s"%del_reason)
                        case.set_result("conclusion","del_reason=%s"%del_reason)       
                        #case.set_result("owner","zhongxiande@baidu.com")

                        case.close = True
                        continue
        
                    #continue
            if case.close == True:continue
            if l2patch and "del_reason" in l2patch and l2patch["del_reason"] != "-" :
                case.set_result("conclusion","del_reason="+l2patch["del_reason"])
                case.set_result("reason","del_reason="+l2patch["del_reason"])
                case.set_result("owner","zhongxiande@baidu.com") 
                case.close = True
                continue
            
            if l2base and "del_reason" in l2base and l2base["del_reason"] != "-" :
                case.set_result("conclusion","del_reason="+l2base["del_reason"])
                case.set_result("reason",l2base["del_reason"])
                case.set_result("owner","zhongxiande@baidu.com") 
                case.close = True
                continue



        pass
