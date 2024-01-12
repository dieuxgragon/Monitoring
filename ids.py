import fire

class ids(object):
    def db(self):
        f = open("/var/ids/dbjson" "a")
        f.write("ca a marcher")
        f.close()    


if __name__ == '__main__':
    fire.Fire(ids)