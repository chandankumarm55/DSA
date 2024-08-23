"""
Example 2:
Input: expression = "-1/2+1/2+1/3"
Output: "1/3"

solution:
so we need to add and subtract the nominator and denominator and if the out is full number we need to add 1 as its denominator

step1 : we used reg for separting the the each item with its operation so we can use of re libraray and findall library 
re.findall(r'[+-]?\d+/\d+',expression)

step2 : so next we need to assign the nominto and denominator for calucting , initially we assign it as 0 as nominator because
ir can be 0 or dull number  and denominator as 1 because it should be always 1 and initially we will make a multification 

step3 : so next we need to iterate over the fractions array and we store the current element in fraction element and 
and also current nominator and denominator as num and den 

next we will make the operation of adding and substring of numninator and denominator and to simplify it we will find the 
commonDivisor of the nominator and denominator and devide the both by common devisor .

 for fraction in fractions:
            num , den = map(int , fraction.split('/'))
            nominator = nominator*den + num * denominator
            denominator*=den

            commonDivisor = gcd(abs(nominator), denominator)
            nominator//=commonDivisor
            denominator//=commonDivisor

step 4 : next we will return the obtain nominator and denominator by formating it 

return "{}/{}".format(nominator , denominator)
"""
class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = re.findall(r'[+-]?\d+/\d+',expression)
        print(fractions)
        nominator = 0
        denominator = 1
        for fraction in fractions:
            num , den = map(int , fraction.split('/'))
            nominator = nominator*den + num * denominator
            denominator*=den

            commonDivisor = gcd(abs(nominator), denominator)
            nominator//=commonDivisor
            denominator//=commonDivisor
    
        return "{}/{}".format(nominator , denominator)
