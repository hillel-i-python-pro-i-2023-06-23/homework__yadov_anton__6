from app.config import FILES_INPUT_DIR

def reading_a_file():
    file=FILES_INPUT_DIR.joinpath('sample3.txt')
    with open(file) as f:
        print(f.read())