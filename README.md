![alt text](https://wp-media.patheos.com/blogs/sites/766/2017/03/the-four-horsemen.jpg)

       Bullets => A General internet scanner
       Usage:

       ./bullets <networkAddress/CIDR>/<Country code> <Port> <NumberOfThreads> [browser/brute]

       <Country code> : Country code represented in two alphabets,type ./sniper --countries for more info

       [browser] :browser name is optional, it activates IPs browsing; make sure [browser] is callable from any directory.
       [brute]   :ssh dictionary attack

       Examples: ./bullets.py 196.217.254.0/24 8080 200 firefox
                 ./bullets.py 196.217.254.0/24 22 500 brute
                 ./bullets.py us 8080 200 firefox 
                 ./bullets.py  196.217.254.0/24 80 100
                 ./bullets.py us 8080 200
        

