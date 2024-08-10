class Solution(object):
    def addBinary(self, a, b):
        def decimalConveration(x):
            val =1
            x=x[::-1]
            decimal=0
            for i in range(len(x)):
                if x[i] =='1':
                    decimal+=val
                val=val*2
            return decimal

        if a=='0' and b=='0':
            return '0'

        a_decimal = decimalConveration(a)
        b_decimal = decimalConveration(b)
        
        required_sum = a_decimal+b_decimal
        print(a_decimal,b_decimal,required_sum)
        required_number =''

        while required_sum > 0:
            rem = required_sum%2
            required_number+=str(rem)
            required_sum=required_sum//2

        return required_number[::-1]


        
