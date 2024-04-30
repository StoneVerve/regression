class SimpleLinearModel:

    # We create a new simple linear regression model with slope m and intercept b
    def __init__(self, m, b):
        self.m = m
        self.b = b

    # The model makes a prection, given a value x
    def make_prediction(self, x):
        return self.m * x + self.b

    # Updates the model's intercept parameter
    def update_intercept(self, new_b):
        self.b = new_b

    # Updates the model's slope parameter
    def update_slope(self, new_slope):
        self.m = new_slope

    # Returns the model's intercept parameter
    def get_intercept(self):
        return self.b

    # Returns the model's slope parameter
    def get_slope(self):
        return self.m

    # Returns both the intercept and slope in an array
    def get_params(self):
        return [self.m, self.b]