![alt text](https://wp-media.patheos.com/blogs/sites/766/2017/03/the-four-horsemen.jpg)

       # Bullets => A General internet scanner
       Usage:

      ./sniper <networkAddress/CIDR>/<Country code> <Port> <NumberOfThreads> [browser]

      <Country code> : Country code represented in two alphabets,type ./sniper --countries for more info

      [browser] :browser name is optinal, it activates IPs browsing; make sure [browser] is callable from any directory.
      
      Examples: ./sniper.py 196.217.254.0/24 8080 200 firefox
                ./sniper.py us 8080 200 firefox 
                ./sniper.py  196.217.254.0/24 80 100
        

