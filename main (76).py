print("Welcome to Dhruv's Currency Converter!")
val=str(input('Enter the output currency code:'))
if(val=='INR'):
    USD=float(input('Enter the amount in USD:'))
    INR=USD*74.24
    print('%0.3f USD is equal to %0.3f INR' %(USD, INR))
elif(val=='MXN'):
    USD=float(input('Enter the amount in USD:'))
    MXN=USD*20.02
    print('%0.3f dollars is equal to %0.3f Mexican Pesos' %(USD, MXN))
elif(val=='EUR'):
    USD=float(input('Enter the amount in USD:'))
    EUR=USD*0.85
    print('%0.3f dollars is equal to %0.3f euros' %(USD, EUR))
elif(val=='JPY'):
    USD=float(input('Enter the amount in USD:'))
    JPY=USD*110.25
    print('%0.3f dollars is equal to %0.3f Japanese Yen' %(USD, JPY))
elif(val=='AUD'):
    USD=float(input('Enter the amount in USD:'))
    AUD=USD*1.36
    print('%0.3f dollars is equal to %0.3f Australian Dollars' %(USD, AUD))
elif(val=='CAD'):
    USD=float(input('Enter the amount in USD:'))
    CAD=USD*1.25
    print('%0.3f dollars is equal to %0.3f canadian dollars' %(USD, CAD))
elif(val=='NPR'):
    USD=float(input('Enter the amount in USD:'))
    NPR=USD*118.66
    print('%0.3f dollars is equal to %0.3f Nepalese Rupees' %(USD, NPR))
elif(val=='GBP'):
    USD=float(input('Enter the amount in USD:'))
    GBP=USD*0.72
    print('%0.3f dollars is equal to %0.3f pound sterling' %(USD, GBP))
elif(val=='PKR'):
    USD=float(input('Enter the amount in USD:'))
    PKR=USD*163.10
    print('%0.3f dollars is equal to %0.3f pakistan rupees' %(USD, PKR))