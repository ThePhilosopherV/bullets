![alt text](https://wp-media.patheos.com/blogs/sites/766/2017/03/the-four-horsemen.jpg)

       Bullets => A General internet scanner
       Usage:

      ./bullets.py <networkAddress/CIDR>/<Country code> <Port> <NumberOfThreads> [browser]

      <Country code> : Country code represented in two alphabets,type ./sniper --countries for more info

      [browser] :browser name is optinal, it activates IPs browsing; make sure [browser] is callable from any directory.
      
      Examples: ./bullets.py 196.217.254.0/24 8080 200 firefox
                ./bullets.py us 8080 200 firefox 
                ./bullets.py  196.217.254.0/24 80 100
                ./bullets.py us 8080 200
        

