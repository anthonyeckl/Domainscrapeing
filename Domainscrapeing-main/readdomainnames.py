
class FileReader():

    def __init__(self, name):
        self.name = name
        self.domains = []

    def readFile(self):
        fname = self.name + ".txt"
        f = open(fname, "r")
        #print(type(f.read()))
        for x in f:
            if x.find(".") != -1:
                self.domains.append(x[:x.find(".")])
            else:
                self.domains.append(x)

        #print(self.domains)
        return self.domains


def main():
    print(FileReader("testtxt").readFile())
if __name__ == "__main__":
   main()