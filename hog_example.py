import numba
import numpy as np
from collections import Counter, defaultdict
class hogImg():
    """example usage:
    hog = hogImg(arr=np.random.randint(1, 101, size=(19,19)))
    f = hog.do_work()"""
    def __init__(self, arr, oriens=6, ppc=(3, 3), cpc=(6, 6)):
        self.arr = arr
        self.oriens = oriens
        self.ppc = ppc
        self.cpc = cpc
        if int(self.arr.shape[0]/self.ppc[0])-(self.cpc[0]+1) < 0:
            raise(ValueError("wrong dimensions - ensure array is larger or change cpc to a smaller number!"))
        
    def hog_normalize_block(self, blk, eps=1e-6):
        norma = blk/np.sqrt(np.sum(blk ** 2) + eps ** 2)
        return norma
    
    def hog_gradients(self, arr):
        g_row = np.zeros(arr.shape, dtype=arr.dtype)
        g_row[1:-1, ...] = arr[2:, ...] - arr[:-2, ...]
        g_col = np.zeros(arr.shape, dtype=arr.dtype)
        g_col[..., 1:-1] = arr[..., 2:] - arr[..., :-2]
        return g_row, g_col

    @numba.jit
    def make_hog_histogram_numba(self, arr):
        bins = list(range(0, 380, 20))
        hist = {}
        sum_values = sum(arr.ravel())
        for val in arr.ravel():
            if bins[0] < val <= bins[1]:
                if val not in hist:
                    hist[0] = 1
                else:
                    hist[0] += 1
            elif bins[1] < val <= bins[2]:
                if val not in hist:
                    hist[1] = 1
                else:
                    hist[1] += 1
            elif bins[2] < val <= bins[3]:
                if val not in hist:
                    hist[2] = 1
                else:
                    hist[2] += 1
            elif bins[3] < val <= bins[4]:
                if val not in hist:
                    hist[3] = 1
                else:
                    hist[3] += 1
            elif bins[4] < val <= bins[5]:
                if val not in hist:
                    hist[4] = 1
                else:
                    hist[4] += 1
            elif bins[5] < val <= bins[6]:
                if val not in hist:
                    hist[5] = 1
                else:
                    hist[5] += 1
            elif bins[6] < val <= bins[7]:
                if val not in hist:
                    hist[6] = 1
                else:
                    hist[6] += 1
            elif bins[7] < val <= bins[8]:
                if val not in hist:
                    hist[7] = 1
                else:
                    hist[7] += 1
            elif bins[8] < val <= bins[9]:
                if val not in hist:
                    hist[8] = 1
                else:
                    hist[8] += 1
            elif bins[9] < val <= bins[10]:
                if val not in hist:
                    hist[9] = 1
                else:
                    hist[9] += 1
            elif bins[10] < val <= bins[11]:
                if val not in hist:
                    hist[10] = 1
                else:
                    hist[10] += 1
            elif bins[11] < val <= bins[12]:
                if val not in hist:
                    hist[11] = 1
                else:
                    hist[11] += 1
            elif bins[12] < val <= bins[13]:
                if val not in hist:
                    hist[12] = 1
                else:
                    hist[12] += 1
            elif bins[13] < val <= bins[14]:
                if val not in hist:
                    hist[13] = 1
                else:
                    hist[13] += 1
            elif bins[14] < val <= bins[15]:
                if val not in hist:
                    hist[14] = 1
                else:
                    hist[14] += 1
            elif bins[15] < val <= bins[16]:
                if val not in hist:
                    hist[15] = 1
                else:
                    hist[15] += 1
            elif bins[16] < val <= bins[17]:
                if val not in hist:
                    hist[16] = 1
                else:
                    hist[16] += 1
            elif bins[17] < val <= bins[18]:
                if val not in hist:
                    hist[17] = 1
                else:
                    hist[17] += 1
        new_dict = {}
        for key, val in hist.items():
            new_dict[key] = val/sum_values
        return new_dict
        
    def make_hog_histogram(self, arr):
        bins = np.arange(0, 380, 20, dtype=float)
        hist = defaultdict(int)
        for val in arr.ravel():
            if bins[0] < val <= bins[1]:
                hist[0] += 1
            elif bins[1] < val <= bins[2]:
                hist[1] += 1 
            elif bins[2] < val <= bins[3]:
                hist[2] += 1 
            elif bins[3] < val <= bins[4]:
                hist[3] += 1
            elif bins[4] < val <= bins[5]:
                hist[4] += 1 
            elif bins[5] < val <= bins[6]:
                hist[5] += 1 
            elif bins[6] < val <= bins[7]:
                hist[6] += 1
            elif bins[7] < val <= bins[8]:
                hist[7] += 1
            elif bins[8] < val <= bins[9]:
                hist[8] += 1
            elif bins[9] < val <= bins[10]:
                hist[9] += 1 
            elif bins[10] < val <= bins[11]:
                hist[10] += 1
            elif bins[11] < val <= bins[12]:
                hist[11] += 1
            elif bins[12] < val <= bins[13]:
                hist[12] += 1 
            elif bins[13] < val <= bins[14]:
                hist[13] += 1
            elif bins[14] < val <= bins[15]:
                hist[14] += 1
            elif bins[15] < val <= bins[16]:
                hist[15] += 1 
            elif bins[16] < val <= bins[17]:
                hist[16] += 1 
            elif bins[17] < val <= bins[18]:
                hist[17] += 1
            return {key: val/sum(hist.values()) for key, val in hist.items()}
                
    def faster_hog_histogram(self, arr):
        ctr = np.unique(np.digitize(arr, bins=np.arange(0, 380, 20), right=True).ravel(), return_counts=True)
        return np.vstack((ctr[0], ctr[1]/sum(ctr[1])))
    
    def fastest_hog_histogram(self, arr):
        ctr = Counter(np.digitize(arr, bins=np.arange(0, 380, 20), right=True).ravel())
        return {key: val/sum(ctr.values()) for key, val in ctr.items()}

    def make_angles(self, row, col, eps=1e-6):
        return np.round(2*np.rad2deg(np.arctan(row/(col+eps)))+180, 2)
        
    def do_work(self):
        self.g_row, self.g_col = self.hog_gradients(self.arr)
        split_cells = np.split(self.arr, self.ppc[0])
        split_grads_rows = np.split(self.g_row, self.ppc[0])
        split_grads_cols = np.split(self.g_col, self.ppc[0])
        final = np.zeros((self.cpc[0], self.arr.shape[1], self.ppc[0]))
        hist_final = []
        for idx, (row, col) in enumerate(zip(split_grads_rows, split_grads_cols)):
            norm_row = self.hog_normalize_block(row)
            norm_col = self.hog_normalize_block(col)
            angs = self.make_angles(row, col)
            hist = self.make_hog_histogram(angs)
            hist_final.append(hist)
            final[:angs.shape[0], :angs.shape[1], idx] = angs
        return final, hist_final
