"""
Various utility classes and structures
"""

from __future__ import division, print_function, absolute_import

resanallib = {
    "me" : {
        'VAL' : [('CB','CG1'),('CB','CG2')],
        'THR' : [('CB','CG2')],
        'ILE' : [('CB','CG2'),('CG1','CD1')],
        'LEU' : [('CG','CD1'),('CG','CD2')],
        'MET' : [('SD','CE')],
        'ALA' : [('CA','CB')]
    },
    "dict" : {
        'VAL' : [("CB","CG1"),("CB","CG2")],
        'SER' : [("CB","HB2"),("CB","HB3")],
        'THR' : [("CB","CG2")],
        'ILE' : [("CG1","CD1")],
        'LEU' : [("CG","CD1"),("CG","CD2")],
        'MET' : [("SD","CE")],
        'ASN' : [("ND2","HD21"),("ND2","HD22")],
        'GLN' : [("NE2","HE21"),("NE2","HE22")],
        'PHE' : [("CD1","HD1")],
        'HID' : [("CD2","HD2")],
        'HIE' : [("CD2","HD2")],
        'HIP' : [("CD2","HD2")],
        'TYR' : [ ("CD1","HD1")],
        'PRO' : [("CG","HG2"),("CG","HG3")],
        'LYS' : [("CB","HB2"),("CB","HB3"),("CG","HG2"),("CG","HG3"),("CD","HD2"),("CD","HD3"),("CE","HE2"),("CE","HE3")],
        'ARG' : [("CB","HB2"),("CB","HB3"),("CG","HG2"),("CG","HG3"),("CD","HD2"),("CD","HD3"),("NE","HE")],
        'ASP' : [("CB","HB2"),("CB","HB3")],
        'GLU' : [("CG","HG2"),("CG","HG3")],
    }
}



class AnalysisGrid(object) :

    """
    Class to store a 2D grid for analysis

    Attributes
    ----------
    count : NdArray
        the number of times the accumulate function has been called
    edgesx : NdArray
        the edges along the x-dimension
    edgesy : NdArray
        the edges along the y-dimension
    matrix : NdArray
        the discretised data
    resolution : float
        the resolution, i.e. the size of each pixel
    """
    def __init__(self, xyz, resolution=1.0) :
        xyz_shift = xyz - xyz.mean(axis=0)

        self.edgesx = np.arange(xyz_shift[:,0].min(),
                                    xyz_shift[:,0].max()+resolution, resolution)
        self.edgesy = np.arange(xyz_shift[:,1].min(),
                                    xyz_shift[:,1].max()+resolution, resolution)
        self.resolution = resolution
        self.matrix = np.zeros([self.edgesx.shape[0]+1, self.edgesy.shape[0]+1])
        self.count = np.zeros([self.edgesx.shape[0]+1, self.edgesy.shape[0]+1])

    def accumulate(self, positions, data) :

        idx = self.indices(positions)
        self.matrix[idx[0], idx[1]] += data
        self.count[idx[0], idx[1]] += 1.0

    def average(self, func=None) :

        sel = self.count > 0.0
        self.matrix[sel] /= self.count[sel]
        if func is not None :
            self.matrix[sel] = func(self.matrix[sel])

    def indices(self, positions) :
        """
        Returns the grid coordinates for a set of Cartesian coordinates
        """
        xidx = np.digitize(positions[:,0], self.edgesx)
        yidx = np.digitize(positions[:,1], self.edgesy)
        return xidx, yidx

    def write(self, filename) :

        with open(filename, "w") as f :
            for i in range(self.matrix.shape[0]) :
                for j in range(self.matrix.shape[1]) :
                    f.write("%.3f\t"%self.matrix[i,j])
                f.write("\n")
