from Crypto.Util.number import getPrime, getRandomRange
from Crypto import Random

class PedersonCommitment:
    def __init__(self,security, message):
        self.security = security
        self.message  = message
        self.s =  None

        self.p =  None
        self.q = None
        self.g = None
        self.h =  None
        return None
    

    def pedersen_setup(self):
        self.p = getPrime(2 * self.security, Random.new().read)
        self.q = 2*self.p + 1# Choose a large prime number
        self.g = getRandomRange(1, self.q-1)
        self.s = getRandomRange(1, self.q-1)
        self.h = pow(self.g,self.s,self.q)
        return self.p, self.q, self.g, self.h
    

    def pederson_commitment(self):
        r = getRandomRange(1, self.q-1)
        c = (pow(self.g,self.message,self.q) * pow(self.h,r,self.q)) % self.q

        return c,r

    def pedersen_opening(self,*randomNumber):
        sum = 0
        for i in randomNumber:
            sum += i

        res = (pow(self.g,self.message,self.q) * pow(self.h,sum,self.q)) % self.q
        return res