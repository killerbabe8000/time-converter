def calculate_time (duration):
        hms_hours, remainder_seconds = divmod(duration,3600)
        hms_minutes, hms_seconds = divmod(remainder_seconds,60)
        in_minutes = round((duration) / 60, 5)
        in_hours = round((duration) / 3600, 5)
        return hms_hours, hms_minutes, hms_seconds,in_hours, in_minutes


def input_request (): 
        input_value = (input("\nEnter number of seconds that you want to convert:   "))
        input_value = input_value.replace (',','.')
        
        try:
            input_value = float(input_value)
            duration = int(round(input_value))
            negative_error = False
            number_error = False
    
            if duration <= 0:
                negative_error = True
                number_error = False
                duration = 0

        except:
            number_error = True
            negative_error = False
            duration = 0

        return (duration, negative_error, number_error)
        
        
def try_again (negative_error, error):
    repeat_input = input("\n\nDo you want to try again (y/n)? ")
    if repeat_input == "y":
        close = False
    elif repeat_input == "n":
        close = True

    else:
        close = try_again_invalid()

    return close
        
        
def try_again_invalid():
    eingabe = input("\nInvalid input, please press (y) to try again. Press (n) to close the window.  ")
    if eingabe == "y":
        close = False
    elif eingabe == "n":
        close = True
    else:
        close = try_again_invalid()
             
    return (close)
        
        
negative_error = False
number_error = False
close = False

while close != True:
    duration, negative_error, number_error = input_request()
    
    if not negative_error and not number_error:
        hms_hours, hms_minutes, hms_seconds, in_hours, in_minutes = calculate_time(duration)
        output = (f"\nt in seconds: {duration}\n-----------------------------\nin hours:      {in_hours} h\nin minutes:    {in_minutes} min\n-----------------------------\nt in hms-format: {hms_hours}h {hms_minutes}m {hms_seconds}s")
        print(str(output))
        close = try_again(negative_error, number_error)
    
    elif negative_error == True:
            error = True
            print("\nInput can't be a negative number!")
            close = try_again(negative_error, error)

    elif number_error == True:
            error = True
            print("\nValue is not a valid number!")
            close = try_again(negative_error, error)