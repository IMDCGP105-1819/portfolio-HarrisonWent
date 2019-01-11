class Car(object):

    def __int__(self, description):
        self.colour = description["Colour"]
        self.manufacturer = description["Manufacturer"]
        self.model = description["Model"]
        self.number_of_doors = description["NumberOfDoors"]

    def _change_colour_(self, new_colour):
        self.colour = new_colour
        return

    def _change_manufacturer_(self, new_manufacturer):
        self.manufacturer = new_manufacturer

    def _change_model_(self, new_model):
        self.model = new_model

    def _change_number_of_doors_(self, new_doors):
        self.number_of_doors = new_doors

    def _change_all_(self, new_description):
        self._change_colour_(new_description["Colour"])
        self._change_manufacturer_(new_description["Manufacturer"])
        self._change_model_(new_description["Model"])
        self._change_number_of_doors_(new_description["NumberOfDoors"])
