import glob
import pickle

import cv2


class PickleEncoding:
    def __init__(self, maxsize, out_dir, save_file):
        self.maxsize = maxsize
        self.out_dir = out_dir
        self.save_file = out_dir + save_file

    def resize_encoding(self, size):
        result = []
        fs = glob.glob(self.out_dir+"/*")
        for i,labeldir in enumerate(fs):
            print("i=",i)
            print("labeldir=",labeldir)
            fs0 = glob.glob(labeldir+"/*")
            for j,f in enumerate(fs0):
                if j>=self.maxsize:
                    break
                img = cv2.imread(f)
                if img is not None:
                    img = cv2.resize(img, dsize=(size, size))
                    result.append([i, img])
                else:
                    print("Failed to load image:", f)

        pickle.dump(result, open(self.save_file, "wb"))
        print("done!")

    def encoding(self):
        result = []
        fs = glob.glob(self.out_dir+"/*")
        for i,labeldir in enumerate(fs):
            print("i=",i)
            print("labeldir=",labeldir)
            fs0 = glob.glob(labeldir+"/*")
            for j,f in enumerate(fs0):
                if j>=self.maxsize:
                    break
                img = cv2.imread(f)
                if img is not None:
                    result.append([i, img])
                else:
                    print("Failed to load image:", f)

        pickle.dump(result, open(self.save_file, "wb"))
        print("done!")

