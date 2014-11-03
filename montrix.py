def between(a,b,c):
    return a<=b and b<=c

class Zone:
    def __init__(self, row0, col0, row1, col1, value):
        self.row0 = row0
        self.col0 = col0
        self.row1 = row1
        self.col1 = col1
        self.value = value

    def __cmp__(self, other):
        return cmp(
            (self.row0, self.col0, self.row1, self.col1, self.value),
            (other.row0, other.col0, other.row1, other.col1, other.value)
            )

    def __eq__(self, zone):
        a = self.row0 == zone.row0
        b = self.col0 == zone.col0
        c = self.row1 == zone.row1
        d = self.col1 == zone.col1
        e = self.value == zone.value
        
        return a and b and c and d and e

    def aspect_ratio(self):
        ratio = 1.0*(self.row1 -self.row0)/(self.col1 - self.col0)
        if ratio>1: return 1.0/ratio
        else: return ratio


    def __repr__(self):
        return "Zone(%s,%s,%s,%s,%s)"%(self.row0, self.col0, self.row1, self.col1, self.value)

    def is_void(self):
        if self.row0 >= self.row1: return True
        if self.col0 >= self.col1: return True

    def intersects(self, zone):
        a = (self.row0 > zone.row0 and self.row1 > zone.row1)
        b = (self.row0 < zone.row0 and self.row1 < zone.row1)
        c = (self.col0 > zone.col0 and self.col1 > zone.col1)
        d = (self.col0 < zone.col0 and self.col1 < zone.col1)
        return not(a or b or c or d)

    def fragment_and_set_minusfive(self, zone):
        return self.fragment_and_apply_minusfive(zone, lambda x,y:y)

    def fragment_and_set_five(self, zone):
        return self.fragment_and_apply_five(zone, lambda x,y:y)
    
    def fragment_and_set_nine(self, zone):
        return self.fragment_and_apply_nine(zone, lambda x,y:y)

    def fragment_and_set(self, zone, layout = None):
        return self.fragment_and_apply(zone,layout,lambda x,y:y)

    def fragment_and_apply(self, zone, layout, fn):
        if layout == "nine": return self.fragment_and_apply_nine(zone, fn)
        if layout == "five": return self.fragment_and_apply_five(zone, fn)
        if layout == "minusfive": return self.fragment_and_apply_minusfive(zone, fn)

        a = self.fragment_and_apply_five(zone, fn)
        b = self.fragment_and_apply_minusfive(zone, fn)
        
        ratio_a = sum(map(lambda x:x.aspect_ratio(),a))/len(a)
        ratio_b = sum(map(lambda x:x.aspect_ratio(),a))/len(a)
        
        if ratio_a >= ratio_b: return a
        else: return b


    def fragment_and_apply_five(self, zone, fn): # untested
        """
        
        interesting only if they intersect
        
        fragments current zone, according to intersection with new zone
        returns all new zones
        
        p       b              a       q
      u ################################
        #                      #       #
        #                      #       #
        #             z[1]     #       #
        #                      #       #
        #                      #       #
      r ########################       #
        #       #              #       #
        #  z[2] #     z[0]     # z[4]  #
        #       #              #       #
      s #       ########################
        #       #                      #
        #       #     z[3]             #
        #       #                      #
      v ################################
        
        """

        p = self.col0
        q = self.col1
        u = self.row0
        v = self.row1
        
        a=min(q, zone.col1)
        b=max(p, zone.col0)

        r=max(u, zone.row0)
        s=min(v, zone.row1)

        z=range(5)

        z[0] = Zone(r,b,s,a, fn(self.value,zone.value))
        z[1] = Zone(u,p,r,a, self.value)
        z[2] = Zone(r,p,v,b, self.value)
        z[3] = Zone(s,b,v,q, self.value)
        z[4] = Zone(u,a,s,q, self.value)
        
        return [x for x in z if not x.is_void()]
        



    def fragment_and_apply_minusfive(self, zone, fn):
        """
        
        interesting only if they intersect
        
        fragments current zone, according to intersection with new zone
        returns all new zones
        
        p       b              a       q
      u ################################
        #       #                      #
        #       #                      #
        #       #     z[2]             #
        #       #                      #
        #       #                      #
      r #       ########################
        #       #              #       #
        #  z[1] #     z[0]     # z[3]  #
        #       #              #       #
      s ########################       #
        #                      #       #
        #             z[4]     #       #
        #                      #       #
      v ################################
        
        """

        p = self.col0
        q = self.col1
        u = self.row0
        v = self.row1
        
        a=min(q, zone.col1)
        b=max(p, zone.col0)

        r=max(u, zone.row0)
        s=min(v, zone.row1)

        z=range(5)

        z[0] = Zone(r,b,s,a, fn(self.value,zone.value))
        z[1] = Zone(u,p,s,b, self.value)
        z[2] = Zone(u,b,r,q, self.value)
        z[3] = Zone(r,a,v,q, self.value)
        z[4] = Zone(s,p,v,a, self.value)
        
        return [x for x in z if not x.is_void()]
        

    def fragment_and_apply_nine(self, zone, fn):
        """
        
        interesting only if they intersect
        
        fragments current zone, according to intersection with new zone
        returns all new zones
        
        p       b              a       q
      u ################################
        #       #              #       #
        #       #              #       #
        #  z[0] #     z[1]     # z[2]  #
        #       #              #       #
        #       #              #       #
      r ################################
        #       #              #       #
        #  z[3] #     z[4]     # z[5]  #
        #       #              #       #
      s ################################
        #       #              #       #
        #  z[6] #     z[7]     # z[8]  #
        #       #              #       #
      v ################################
        
        """

        p = self.col0
        q = self.col1
        u = self.row0
        v = self.row1
        
        a=min(q, zone.col1)
        b=max(p, zone.col0)

        r=max(u, zone.row0)
        s=min(v, zone.row1)

        z=range(9)

        z[0] = Zone(u,p,r,b, self.value)
        z[1] = Zone(u,b,r,a, self.value)
        z[2] = Zone(u,a,r,q, self.value)
        z[3] = Zone(r,p,s,b, self.value)
        z[4] = Zone(r,b,s,a, fn(self.value,zone.value))
        z[5] = Zone(r,a,s,q, self.value)
        z[6] = Zone(s,p,v,b, self.value)
        z[7] = Zone(s,b,v,a, self.value)
        z[8] = Zone(s,a,v,q, self.value)
        
        return [x for x in z if not x.is_void()]
        


class Montrix:

    def __init__(self, rows, cols, value=None):
        self.zones=[]
        self.rows=rows
        self.cols=cols
        z = Zone(0,0,self.rows,self.cols, value)
        self.zones.append(z)

    def get_max(self):
        if self.zones==[]: return None, None
        max_zone=self.zones[0]
        max_value=max_zone.value

        for z in self.zones[1:]:
            if z.value>max_value:
                max_zone=z
                max_value=max_zone.value
        
        return max_value, (max_zone.row0,max_zone.col0)

    def get_min(self):
        if self.zones==[]: return None, None
        min_zone=self.zones[0]
        min_value=min_zone.value

        for z in self.zones[1:]:
            if z.value<min_value:
                min_zone=z
                min_value=min_zone.value
        
        return min_value, (min_zone.row0,min_zone.col0)

    def set_zone(self, zone):
        self.apply_zone(zone,lambda x,y:y)
    
    def apply_zone(self, zone, fn):
        aux = []
        for z in self.zones:
            if not z.intersects(zone=zone): aux.append(z)
            else:
                aux+=z.fragment_and_apply(zone, layout=None, fn=fn)
        self.zones=aux

    def select_intersecting_zones(self, mzones):
    #TODO: this could be very fast using indexing of zones
    #recommended: use a SegmentTree: http://liangsun.org/posts/a-python-implementation-of-segment-tree/
    
        aux = []
        for z in self.zones:
            for mz in mzones:
                if z.intersects(mz): aux.append(mz)
        return aux

    def apply(self, montrix, fn):
        for mz in self.select_intersecting_zones(montrix.zones):
            self.apply_zone(mz,fn)

    def to_list(self):
        aux = []
        for x in range(self.rows):
            aux.append([None]*self.cols)
        for z in self.zones:
            for r in range(z.row0, z.row1):
                for c in range(z.col0, z.col1):
                    aux[r][c]=z.value

        return aux

    
    def print_repr(self,stream):
        aux = []
        for x in range(self.rows):
            aux.append([None]*self.cols)
        for z in self.zones:
            for r in range(z.row0, z.row1):
                for c in range(z.col0, z.col1):
                    aux[r][c]=z.value
        
        stream.write("[\n")
        for x in aux:
            stream.write("\t%s\n"%x)
        stream.write("]\n")
            