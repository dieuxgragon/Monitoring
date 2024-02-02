import os
import json
import hashlib
import fire
import datetime

class ids(object):
    def db(self, root_directory='/', exclude_directories=None):
        if exclude_directories is None:
            exclude_directories = []

        if os.path.exists("/var/ids/db.json"):
            return
        else:
            os.makedirs("/var/ids")
            f = open("/var/ids/db.json", "a")
            f.write("ca a marcher")
            f.close()

        build_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file_data = {}

        for root, dirs, files in os.walk(root_directory):
           dirs[:] = [d for d in dirs if d not in exclude_directories]

        for db in files:
                path = os.path.abspath(os.path.join(root, db))

                md5_hash = hashlib.md5()
                sha256_hash = hashlib.sha256()
                sha512_hash = hashlib.sha512()

                with open(path, "rb") as file:
                    for chunk in iter(lambda: file.read(4096), b""):
                        md5_hash.update(chunk)
                        sha256_hash.update(chunk)
                        sha512_hash.update(chunk)

                file_data[path] = {
                    "build_date": build_date,
                    "last_modified": os.path.getmtime(path),
                    "creation_date": os.path.getctime(path),
                    "owner": os.stat(path).st_uid,
                    "group_owner": os.stat(path).st_gid,
                    "size": os.path.getsize(path),
                    "md5_hash": md5_hash.hexdigest(),
                    "sha256_hash": sha256_hash.hexdigest(),
                    "sha512_hash": sha512_hash.hexdigest()
                }

        with open("/var/ids/db.json", "w") as json_file:
            json.dump(file_data, json_file, indent=2)

if __name__ == '__main__':
    fire.Fire(ids)
