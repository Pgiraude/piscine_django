import antigravity
import sys

def geohashing():
    if len(sys.argv) != 4:
        print("inputs: latitude(float) longitude(float) date(YYYY-MM-DD)")
        return
    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
    except:
        return print("latitude and longitude should be float")
    date = sys.argv[3].encode('utf-8')

    if len(date) != 10 or (sys.argv[3][4] != "-") or (sys.argv[3][7] != "-"):
        return print('date format: YYYY-MM-DD')
    if not (date[:4].isdigit() and date[5:7].isdigit() and date[8:].isdigit()):
         return print('date format: YYYY-MM-DD ffff')

    try:
        antigravity.geohash(latitude, longitude, date)
    except:
        return print('geohash error')



if __name__ == '__main__':
    geohashing()