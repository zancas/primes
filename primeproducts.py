#! /usr/bin/env python

def primalitycheck(x, printout=False):
    innernaturals = range(2,x)
    for y in innernaturals:
        if x%y == 0: #x not prime
            if printout:
                print "%s is not prime. It is evenly divisible by: %s" % (x,y)
                print "%s / %s = %s" % (x, y, x/y)
            return False
    return True    

def main():
    import sys    
    naturals = range(2,int(sys.argv[1]))
    primes = []

    for x in naturals:
        prime = primalitycheck(x)
        if prime:
            primes.append(x)

    #print "primes: %s" % primes

    Ns = []

    for index in range(len(primes)):
        firstprimes = primes[:index+1]
        primeprod = reduce(lambda x,y: x*y, firstprimes)
        #print "firstprimes: %s and their primeprod is: %s " % (firstprimes, primeprod)
        N = primeprod+1
        Ns.append(N)

    print "Ns are %s." % Ns

    for N in Ns:
        Nprime = primalitycheck(N)
        if not Nprime:
            print "N: %s is not prime!!!" % N
            primalitycheck(N, True)

if __name__ == '__main__':
    main()
