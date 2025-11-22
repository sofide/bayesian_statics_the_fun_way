from scipy.stats import beta


if __name__ == "__main__":
    # get params from inputs
    a = float(input("a: "))
    b = float(input("b: "))
    
    # get distribution floor and ceil from inputs
    floor = float(input("floor: "))
    ceil = float(input("ceil: "))
    
    prob = beta.cdf(ceil, a, b) - beta.cdf(floor, a, b)
    print(f"prob: {prob}")
    