
from constant import Constant


def calculate(h_total, t1):

    # % M_app, the quantity of deicing salts applied on a roadway per day during the winter season
    # % W_lane is the lane width in meter, take as 3.75
    # % Salt_application_rate is taken as 0.07
    M_app = Constant.salt_application_rate * h_total / (Constant.W_lane*t1);
    return M_app
    # print(self.M_app)

