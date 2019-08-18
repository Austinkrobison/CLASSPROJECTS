# p8_FunctionCall.py
i_prompt = 'Enter C to calculate wind chill or Q to quit: '
t_prompt = 'Temperature in Fahrenheit: '
w_prompt = 'Wind speed in mph: '
def calc_wind_chill(f_temp, wind_speed):
    velocity = wind_speed ** 0.16
    chill = 35.74 + (0.6215 * f_temp) - \
            (35.75 * velocity) + (0.4275 * f_temp * velocity)
    return chill
i_inp = input(i_prompt).lower()
while i_inp !='q':
    if i_inp == 'c':
        t_inp = float(input(t_prompt))
        w_inp = float(input(w_prompt))
        wind_chill = round(calc_wind_chill(t_inp, w_inp), 1)
        wind_chill2 = round(calc_wind_chill(t_inp, w_inp + 10), 1)
        print('\nWind chill is', wind_chill,
              'degrees F when:\n The temperature is: ', t_inp, 'F\n'
              , 'The wind speed is', w_inp, 'mph\n')
        print('\nWind chill is', wind_chill2,
              'degrees F when:\n The temperature is: ', t_inp, 'F\n'
              , 'The wind speed is', w_inp, 'mph\n')

        
        i_inp = input(i_prompt).lower()
        
