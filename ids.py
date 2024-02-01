import os
import json
import hashlib
import fire
import datetime

class ids(object):
    def db(self):
        if os.path.exists("var/ids/db.json"):
            return 
        else:
            os.mkdir("var/ids")
        f = open("/var/ids/db.json" "a")
        f.write("ca a marcher")
        f.close()

        build_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        files_to_watch = [f for f in os.listdir('.') if os.path.isfile(f)]

        file_data = {}

        for file_name in files_to_watch:
            file_path = os.path.abspath(file_name)

            md5_hash = hashlib.md5()
            sha256_hash = hashlib.sha256()
            sha512_hash = hashlib.sha512()

            with open(file_path, "rb") as file:
                for chunk in iter(lambda: file.read(4096), b""):
                    md5_hash.update(chunk)
                    sha256_hash.update(chunk)
                    sha512_hash.update(chunk)

            file_data[file_name] = {
                "build_date": build_date,
                "last_modified": os.path.getmtime(file_path),
                "creation_date": os.path.getctime(file_path),
                "owner": os.stat(file_path).st_uid,
                "group_owner": os.stat(file_path).st_gid,
                "size": os.path.getsize(file_path),
                "md5_hash": md5_hash.hexdigest(),
                "sha256_hash": sha256_hash.hexdigest(),
                "sha512_hash": sha512_hash.hexdigest()
            }

        with open("/var/ids/db.json", "w") as json_file:
            json.dump(file_data, json_file, indent=2)

if __name__ == '__main__':
    fire.Fire(ids)