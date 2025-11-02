presents = open('day2.txt', 'r').read()

def organize_presents(input: str):
    '''
    Organizes presents consistent with the format of that found in AOC 2015 day 2 and returns a list of dimension lists.
    '''

    presents = input.splitlines()
    present_list = []

    for present in presents:
        dimensions = present.split(sep='x')
        dimensions = [int(dim) for dim in dimensions]
        present_list.append(dimensions)
    
    return present_list

def calculate_square_footage(dimensions: list):
    '''
    Takes `dimensions`, a list assumed to be of size 3 (since we live in 3D), and returns the `surface_area` plus the area of the smallest side, denoted `smallest`.
    '''

    lw = dimensions[0] * dimensions[1]
    wh = dimensions[1] * dimensions[2]
    hl = dimensions[2] * dimensions[0]

    smallest = min([lw, wh, hl])
    surface_area = 2 * (lw + wh + hl)
    
    return surface_area + smallest

def ribbon_and_bow(dimensions: list):

    sorted_dims = sorted(dimensions)
    ribbon = 2 * (sorted_dims[0] + sorted_dims[1])
    bow = sorted_dims[0] * sorted_dims[1] * sorted_dims[2]

    return ribbon + bow

if __name__ == '__main__':

    pres_list = organize_presents(presents)
    total_wrap = 0
    total_ribbon = 0
    for dim_list in pres_list:
        total_wrap += calculate_square_footage(dim_list)
        total_ribbon += ribbon_and_bow(dim_list)

    print(f'Total square feet of wrapping paper required:\t{total_wrap} sqft.')
    print(f'Total length (ft) of ribbon required:\t\t{total_ribbon} ft.')