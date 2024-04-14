



def calculate(h_total, t2):
    # % h_app, thickness of melted water per day with snow melting
    # % h_total is in meter
    # print(self.t2)
    # 
    h_app = h_total / 12 /t2 /100
    return h_app