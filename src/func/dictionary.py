def create_val_dictionary(known_vals,known_years):
    if known_vals is None :
        val_dictionay = {0 for y in years_world}
    else  :
        # Linear interpolation to get vals for all years
        interpolated_vals = np.interp(list(years_world), known_years, known_vals)
        # Create the dictionary
        val_dictionary = dict(zip(list(years_world), interpolated_vals))
        return val_dictionary