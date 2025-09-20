class MeteorDataEntry:
    def __init__(self, nme, ident, nmetyp, rclass, m, fll, yr, rlat, rlong, gloc, st, ct):
        self.name = nme
        self.id = ident
        self.nametype = nmetyp
        self.recclass = rclass
        self.mass = m
        self.fall = fll
        self.year = yr
        self.reclat = rlat
        self.reclong = rlong
        self.GeoLocation = gloc
        self.States = st
        self.Counties = ct

    def get_sep_data(self):
        return f'{self.name}\t{self.mass}\t{self.year}\t'
