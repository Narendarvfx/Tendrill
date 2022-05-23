import shutil
from multiprocessing.pool import ThreadPool


class MultithreadedCopier:
    def __init__(self, max_threads):
        self.pool = ThreadPool(max_threads)

    def copy(self, source, dest):
        self.pool.apply_async(shutil.copy2, args=(source, dest))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pool.close()
        self.pool.join()


src_dir = r"I:\Projects\KT\2020\SEP\20200901\PAINT\BK\BK109_031_035_fg01_v002"
dest_dir = r"D:\Test\copy"


with MultithreadedCopier(max_threads=16) as copier:
    shutil.copytree(src_dir, dest_dir, copy_function=copier.copy)