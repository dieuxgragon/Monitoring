import os
import fire

class ids(object):
    def db(self):
        if os.path.exists("var/ids/db.json"):
            return 
        else:
            os.mkdir("var/ids")
        f = open("/var/ids/db.json" "a")
        f.write("ca a marcher")
        f.close()    


if __name__ == '__main__':
    fire.Fire(ids)