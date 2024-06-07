while true:    
    username = input('enter a number')
    password = input('enter password')
    if username == 'admin' and password == 'password':
        print('login successful')
        break 
    else:
        print('login failed')