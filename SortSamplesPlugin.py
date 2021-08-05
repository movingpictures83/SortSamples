import PyPluMA
class SortSamplesPlugin:
    def input(self, filename):
       infile = open(filename, 'r')
       self.parameters = dict()
       for line in infile:
           contents = line.strip().split('\t')
           self.parameters[contents[0]] = contents[1]
       self.otufile = open(PyPluMA.prefix()+"/"+self.parameters["otufile"], 'r')
       self.metadata = open(PyPluMA.prefix()+"/"+self.parameters["metadata"], 'r')
       self.orderby = self.parameters["orderby"]

    def run(self):
        # Assumption: First column contains row names
        # Samples are rest of columns

        # Parse metadata first
        meta = self.metadata.readline().strip()
        metaheader = meta.split(',')
        samplecol = metaheader.index('\"Sample\"')
        ordercol = metaheader.index(self.orderby)
        orderhelper = []
        for line in self.metadata:
            contents = line.strip().split(',')
            orderhelper.append((float(contents[ordercol]), contents[samplecol]))
        orderhelper.sort()
        sortedsamples = []
        for i in range(len(orderhelper)):
           sortedsamples.append(orderhelper[i][1])

        # Parse otu
        self.otuheader = self.otufile.readline().strip().split(',')
        self.sortedidx = [0] # First col
        for i in range(len(sortedsamples)):
           self.sortedidx.append(self.otuheader.index(sortedsamples[i]))

        

    def output(self, filename):
        outfile = open(filename, 'w')
        for i in range(len(self.sortedidx)):
            outfile.write(self.otuheader[self.sortedidx[i]])
            if (i != len(self.sortedidx)-1):
                outfile.write(',')
            else:
                outfile.write('\n')
        for line in self.otufile:
            contents = line.strip().split(',')
            for i in range(len(self.sortedidx)):
               outfile.write(contents[self.sortedidx[i]])
               if (i != len(self.sortedidx)-1):
                   outfile.write(',')
               else:
                   outfile.write('\n')
