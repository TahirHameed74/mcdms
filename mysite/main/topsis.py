import numpy as np
import operator

from .serializers import carParametersSerializer, houseParametersSerializer
from .models import carParameters, houseParameters

towns = [
    'johar town',
    'faisal town',
    'model town',
    'garden town',
    'wapda town',
    'township'
]
brands = [
    'toyota',
    'honda',
    'suzuki',
    'mercedes',
    'audi',
    'kia',
    'hyundai'
]
cities = [
    'lahore'
]
assembly_types = [
    'local',
    'imported'
]

colors = [
    'red',
    'green',
    'black',
    'white',
    'yellow',
    'blue',
    'pink'
]
eng_choice = [
    'automatic',
    'manual'
]
year_choice = [
    '2020',
    '2019',
    '2018',
    '2017',
    '2016',
    '2015',
    '2014',
    '2013',
    '2012',
    '2011',
    '2010',
    '2009',
    '2008',
    '2007',
    '2006',
    '2005',
    '2004',
    '2003',
    '2002',
    '2001',
    '2000'
]


class topsis:
    """ Define a TOPSIS decision making process
    TOPSIS (Technique for Order Preference by Similarity to an Ideal Solution)
    chooses and ranks alternatives of shortest distance from the ideal solution
    """
    C = None
    optimum_choice = None

    def __init__(self, a, w, I):
        """ Initialise topsis object with alternatives (a), weighting (w),
        and benefit/cost indicator (i). Validate the user input for correct
        dimensions etc.

        :param np.ndarray a: A 2D array of shape (J,n)
        :param np.ndarray w: A 1D array of shape (J)
        :param np.ndarray I: A 1D array of shape (n)
        """
        # Decision Matrix
        self.a = np.array(a, dtype=np.float).T
        assert len(self.a.shape) == 2, "Decision matrix a must be 2D"

        # Number of alternatives, aspects
        (self.n, self.J) = self.a.shape

        # Weight matrix
        self.w = np.array(w, dtype=np.float)
        assert len(self.w.shape) == 1, "Weights array must be 1D"
        assert self.w.size == self.n, "Weights array wrong length, " + \
                                      "should be of length {}".format(self.n)

        # Normalise weights to 1
        self.w = self.w / sum(self.w)

        # Benefit (True) or Cost (False) criteria?
        self.I = np.array(I, dtype=np.int8)
        assert len(self.I.shape) == 1, "Criterion array must be 1D"
        assert len(self.I) == self.n, "Criterion array wrong length, " + \
                                      "should be of length {}".format(self.n)

        # Initialise best/worst alternatives lists
        ab, aw = np.zeros(self.n), np.zeros(self.n)

    def __repr__(self):
        """ What to print when the object is called?
        """
        # If optimum choice not yet calculated, start the calculation!
        if self.optimum_choice == None:
            self.calc()
        opt_idx = self.optimum_choice
        return 'Best alternative\na[{}]: {}'.format(opt_idx, self.a[:, opt_idx])

    def step1(self):
        """ TOPSIS Step 1
        Calculate the normalised decision matrix (self.r)
        """
        self.r = self.a / np.array(np.linalg.norm(self.a, axis=1)[:, np.newaxis])
        return

    def step2(self):
        """ TOPSIS Step 2
        Calculate the weighted normalised decision matrix
        Two transposes required so that indices are multiplied correctly:
        """
        self.v = (self.w * self.r.T).T
        return

    def step3(self):
        """ TOPSIS Step 3
        Determine the ideal and negative-ideal solutions
        I[i] defines i as a member of the benefit criteria (True) or the cost
        criteria (False)
        """
        # Calcualte ideal/negative ideals
        self.ab = np.max(self.v, axis=1) * self.I + \
                  np.min(self.v, axis=1) * (1 - self.I)
        self.aw = np.max(self.v, axis=1) * (1 - self.I) + \
                  np.min(self.v, axis=1) * self.I
        return

    def step4(self):
        """ TOPSIS Step 4
        Calculate the separation measures, n-dimensional Euclidean distance
        """
        # Create two n long arrays containing Eculidean distances
        # Save the ideal and negative-ideal solutions
        self.db = np.linalg.norm(self.v - self.ab[:, np.newaxis], axis=0)
        self.dw = np.linalg.norm(self.v - self.aw[:, np.newaxis], axis=0)
        return

    def step5(self):
        """ TOPSIS Step 5 & 6
        Calculate the relative closeness to the ideal solution, then rank the
        preference order
        """
        # Ignore division by zero errors
        # np.seterr(all='ignore')
        # Find relative closeness
        self.C = self.dw / (self.dw + self.db)
        self.optimum_choice = self.C.argsort()[-1]
        return

    def calc(self):
        """ TOPSIS Calculations
        This can be called once the object is initialised, and is
        automatically called when a representation of topsis is
        needed (eg. print(topsis(matrix, weights, I)). This calls each step in
        TOPSIS algorithm and stores calcultions in self.

        The optimum alternatives index (starting at 0) is saved in
        self.optimum_choice
        """
        self.step1()
        self.step2()
        self.step3()
        self.step4()
        self.step5()
        return


def add_new_prop(prop):
    if prop[3].lower() in towns:
        prop[3] = towns.index(prop[3].lower())
        prop[2] = cities.index(prop[2].lower())
        return prop
    else:
        towns.append(prop[3].lower())
        return add_new_prop(prop)


def add_new_car(cars):
    if cars[0].lower() in brands:
        cars[0] = brands.index(cars[0].lower())
        cars[1] = cities.index(cars[1].lower())
        cars[2] = assembly_types.index(cars[2].lower())
        cars[3] = int(cars[3])
        cars[4] = int(cars[4])
        cars[5] = cities.index(cars[5].lower())
        cars[6] = int(cars[6])
        cars[7] = int(cars[7])
        if cars[8].lower() == 'automatic':
            cars[8] = 1
        else:
            cars[8] = 0
        cars[9] = colors.index(cars[9])
        cars[10] = int(cars[10])
        cars[11] = int(cars[11])
        return cars
    else:
        brands.append(cars[0])
        return add_new_car(cars)


# def decode_car(prop):
#     prop[3] = towns[prop[3]]
#     prop[2] = cities[prop[2]]
#     return prop



def prop_recom(inputArr):
    # size(marla), price, city, town, old, floors, basement?, garden? room for servants, beds, bathrooms, park dist
    # mosque dist, school dist, market dist, hospital dist
    # a = []

    data = houseParameters.objects.all()
    serializer = houseParametersSerializer(data,many=True)
    # print(serializer.data)

    arr = []
    for item in serializer.data:

        tmp = []
        tmp.append(item['houseSize'])
        tmp.append(item['price'])
        if item['city'] =="Lahore":
            tmp.append(1)
        if item['town'] == "Model Town":
            tmp.append(0)
        elif item['town'] == "Johar Town":
            tmp.append(0)
        elif item['town'] == "gulberg":
            tmp.append(0)
        elif item['town'] == "defence":
            tmp.append(0)
        elif item['town'] == "Faisal Town":
            tmp.append(0)
        elif item['town'] == "barkat market":
            tmp.append(0)
        tmp.append(item['age'])
        tmp.append(item['floor'])
        if item['isBasement'] == True:
            tmp.append(1)
        else:
            tmp.append(0)

        if item['isGarden'] == True:
            tmp.append(1)
        else:
            tmp.append(0)

        tmp.append(item['servantRooms'])
        tmp.append(item['numberOfBeds'])
        tmp.append(item['bathroom'])
        tmp.append(item['distanceFromPark'])
        tmp.append(item['distanceFromMosque'])
        tmp.append(item['distanceFromSchool'])
        tmp.append(item['distanceFromMarket'])
        tmp.append(item['distanceFromHospital'])
        arr.append(tmp)

    print(arr)
    a = arr
    w = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    w = convert_weight(w)
    I = inputArr
    # print(a)
    decision = topsis(a, w, I)
    print(decision)
    # print(decision.C)
    i = 0
    result_dict = {}
    for rank in list(decision.C):
        result_dict[i] = rank
        i += 1
    return_dict = dict(sorted(result_dict.items(), key=operator.itemgetter(1), reverse=True))
    final_result = []
    for key in return_dict.keys():
        final_result.append(a[key])
    return final_result


def convert_weight(w):
    sum = 0
    for i in w:
        sum = sum + i
    new_w = []
    for i in w:
        new_w.append(i / sum)
    return new_w


def car_recom(inputArr):
    # brand, city, assembly type, price, engine cap, reg city, yearly model, brand model, automatic or manual, color
    # engine, mileage

    data = carParameters.objects.all()
    serializer = carParametersSerializer(data,many=True)
    print(serializer.data)

    # brand, city, assembly type, price, engine cap, reg city, yearly model, brand model, automatic or manual, color
    # engine, mileage
    arr = []
    for item in serializer.data:
        tmp = []
        if item['brandType'] == "Toyota":
            tmp.append(1)
        elif item['brandType'] == "Honda":
            tmp.append(2)
        elif item['brandType'] == "bmw":
            tmp.append(3)
        elif item['brandType'] == "Suzuki":
            tmp.append(4)
        elif item['brandType'] == "Mercedes":
            tmp.append(5)
        elif item['brandType'] == "Audi":
            tmp.append(6)
        else:
            tmp.append(1)

        if item['city'] =='Lahore':
            tmp.append(1)
        else:
            tmp.append(1)


        if item['assemblyType'] == "Local":
            tmp.append(1)
        else:
            tmp.append(0)
        tmp.append(item['price'])
        tmp.append(item['engineCapacity'])
        if item['registrationCity'] =="Lahore":
            tmp.append(1)
        else:
            tmp.append(1)


        if item['yearlyModel'] == "Yearly Model":
            tmp.append(1)
        elif item['yearlyModel'] == "2020":
            tmp.append(1)
        elif item['yearlyModel'] == "2019":
            tmp.append(2)
        elif item['yearlyModel'] == "2018":
            tmp.append(3)
        elif item['yearlyModel'] == "2017":
            tmp.append(4)
        elif item['yearlyModel'] == "2016":
            tmp.append(5)
        elif item['yearlyModel'] == "2015":
            tmp.append(6)
        elif item['yearlyModel'] == "2014":
            tmp.append(7)
        elif item['yearlyModel'] == "2013":
            tmp.append(8)
        elif item['yearlyModel'] == "2012":
            tmp.append(9)
        elif item['yearlyModel'] == "2011":
            tmp.append(10)
        elif item['yearlyModel'] == "2010":
            tmp.append(11)
        elif item['yearlyModel'] == "2009":
            tmp.append(12)
        elif item['yearlyModel'] == "2008":
            tmp.append(13)
        elif item['yearlyModel'] == "2007":
            tmp.append(14)
        elif item['yearlyModel'] == "2006":
            tmp.append(15)
        elif item['yearlyModel'] == "2005":
            tmp.append(16)
        elif item['yearlyModel'] == "2004":
            tmp.append(17)
        elif item['yearlyModel'] == "2003":
            tmp.append(18)
        elif item['yearlyModel'] == "2002":
            tmp.append(19)
        elif item['yearlyModel'] == "2001":
            tmp.append(20)
        elif item['yearlyModel'] == "2000":
            tmp.append(21)
        else:
            tmp.append(1)



        if item['brandModel'] == "GLI":
            tmp.append(1)
        elif item['brandModel'] == "XLI":
            tmp.append(2)
        elif item['brandModel'] == "Mehran":
            tmp.append(3)
        elif item['brandModel'] == "Alto":
            tmp.append(4)
        else:
            tmp.append(1)


        if item['engineType'] == 'Manual':
            tmp.append(1)
        elif item['engineType'] == 'Automatic':
            tmp.append(2)
        else:
            tmp.append(3)


        if item['color'] == 'red':
            tmp.append(1)
        elif item['color'] == 'green':
            tmp.append(2)
        elif item['color'] == 'black':
            tmp.append(3)
        elif item['color'] == 'white':
            tmp.append(4)
        elif item['color'] == 'yellow':
            tmp.append(5)
        elif item['color'] == 'blue':
            tmp.append(6)
        elif item['color'] == 'pink':
            tmp.append(7)
        else:
            tmp.append(1)



        if item['engineDetail'] == 'Diesel':
            tmp.append(1)
        elif item['engineDetail'] == 'Petrol':
            tmp.append(2)
        elif item['engineDetail'] == 'LPG':
            tmp.append(3)
        elif item['engineDetail'] == 'CNG':
            tmp.append(4)
        elif item['engineDetail'] == 'Hybrid':
            tmp.append(5)
        else:
            tmp.append(1)


        tmp.append(item['Mileage'])
        arr.append(tmp)

    print("topsis arrrrrr")
    print(arr)
    a = arr
    w = [0.0833, 0.0833, 0.0833, 0.0833, 0.0833, 0.0833, 0.0833, 0.0833, 0.0833, 0.0833, 0.0833, 0.0833]
    I = inputArr

    decision = topsis(a, w, I)
    print(decision)
    i = 0
    result_dict = {}
    for rank in list(decision.C):
        result_dict[i] = rank
        i += 1
    return_dict = dict(sorted(result_dict.items(), key=operator.itemgetter(1), reverse=True))
    final_result = []
    for key in return_dict.keys():
        final_result.append(a[key])



    return final_result


if __name__ == '__main__':
    car_recom()
