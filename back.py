import sqlite3



class ParkedVehicle:
    def __init__(self,vehicleno,fourwheeler,hour,valetparking,pstatus):
        self.vehicleno=vehicleno
        self.fourwheeler=fourwheeler
        self.hour=hour
        self.valetparking=valetparking
        self.pstatus=pstatus

class ParkingLot:
    def __init__(self,vehicleinfo):
        self.vehicleinfo=vehicleinfo

    def updatepstatus(self,lotno):
        o=self.vehicleinfo
        for i in o.keys():
            if i==lotno:
                o[i].pstatus="Cleared"
                print(i,o[i].vehicleno,o[i].pstatus)

    def parkingcharge(self,lotno):
        charge=0
        ob=self.vehicleinfo[lotno]
        if ob.fourwheeler=="Yes":
            charge=50*ob.hour
        else:
            charge=30*ob.hour
        if ob.valetparking=="Yes":
            charge=charge+10
        return charge
            
if __name__=="__main__":

    conn = sqlite3.connect('parkinglot.sqlite')
    cur = conn.cursor()


    vehicleno=input("vehicleno: ")
    fourwheeler=input("fourwheeler: ")
    hour=float(input("hour: "))
    valetparking=input("valetparking: ")
    pstatus="Parked"
    lotno=int(input("lotno: "))
    v=ParkedVehicle(vehicleno,fourwheeler,hour,valetparking,pstatus)
    
    vdict={}
    vdict[lotno]=v

    cur.execute(''' INSERT INTO vehicledetails(vehicleno,fourwheeler,hour,valetparking,pstatus) VALUES(?,?,?,?,?)''',(vehicleno,fourwheeler,hour,valetparking,pstatus,))
    cur.execute('SELECT vehicleid FROM vehicledetails WHERE vehicleno = ? ', (vehicleno, ))
    vehicleid = cur.fetchone()[0]

    cur.execute(''' INSERT INTO lotdetails(lotno,vehicleid) VALUES(?,?)''',(lotno,vehicleid))


    s=ParkingLot(vdict)
    srchlot=int(input("Search lotno: "))
    s.updatepstatus(srchlot)
    charge=s.parkingcharge(srchlot)
    print(charge)

    cur.execute(''' INSERT INTO parkingdetails(vehicleno,charge) VALUES(?,?)''',(vehicleno,charge))

    conn.commit()
    cur.close()


