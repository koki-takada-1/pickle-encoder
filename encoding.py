from pickle_encoder import PickleEncoding

maxsize = 600
out_dir = "data"
save_file = "/yen.pickle"
size = 200 

pe = PickleEncoding(maxsize, out_dir, save_file)
pe.resize_encoding(size)
