import logging,time,os.path

class Logger(object):

    def __init__(self, logger):
        # 创建logger对象
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        rq = time.strftime('%Y%m%d%H%M', time.localtime())
        log_path = os.path.dirname(os.path.abspath('.')) + '/Test_Selenium_Auto/logs/'
        log_name = log_path + rq + '.log'

        # 日志文件的输出路径
        ch = logging.StreamHandler()  # 输出到控制台
        ch.setLevel(logging.INFO)
        fh = logging.FileHandler(log_name)  # 输出到文件
        fh.setLevel(logging.INFO)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

        # 设置日志文件的输出格式
        formatter = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s -%(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

    def getlog(self):
        return self.logger
