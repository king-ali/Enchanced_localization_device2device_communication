class Device:
    def __init__(self, ID, gps_x, gps_y, org_x, org_y):
        self.ID = ID
        self.gps_x = gps_x
        self.gps_y = gps_y
        self.org_x = org_x
        self.org_y = org_y


    def set_GPS(self, gps_x, gps_y):
        self.gps_x = gps_x
        self.gps_y = gps_y

    def get_GPS(self):
        if self.gps_x is not None and self.gps_y is not None:
            return (self.gps_x, self.gps_y)
        else:
            print('error. Nothing set.')

    def get_org(self):
        if self.org_x is not None and self.org_y is not None:
            return (self.org_x, self.org_y)
        else:
            print('error. Nothing set.')

    def set_box(self, x, y):
        self.box_x = x
        self.box_y = y


    def get_box(self):
        if self.box_x is not None and self.box_y is not None:
            return (self.box_x, self.box_y)
        else:
            print('error. Nothing set.')

    def set_color(self,color):
        self.color = color

    def get_color(self,color):
        if self.color is not None:
            return self.color
        else:
            print("error. Nothing yet")