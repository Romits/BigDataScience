import sys

def pathCount(m,n):
    if m ==1 or n == 1:
        return 1
    else:
        return pathCount(m-1,n) + pathCount(m,n-1)

def main():
    count = pathCount(3,3)
    print count

if __name__== "__main__":
    main()

