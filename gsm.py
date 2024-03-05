
import serial

Serial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=2)
data=""

def serialEvent():
    data = Serial.read(20)
    #if data != '\0':
    print (data)
    data=""

def gsmInit():

    while 1:
        data=""
        Serial.write(b"AT\r");
        data=Serial.read(10)
        print (data)
        r=data.find(b"OK")
        if r>=0:
            break
        time.sleep(0.5)
        
    while 1:
        data=""
        Serial.write(b"AT+CLIP=1\r");
        data=Serial.read(10)
        print (data)
        r=data.find("OK")
        if r>=0:
            break
        time.sleep(0.5)
        
    while 1:
        data=""
        Serial.flush()
        Serial.write(b"AT+CPIN?\r");
        data=Serial.read(30)
        print (data)
        r=data.find(b"READY")
        if r>=0:
            break
        time.sleep(0.5)
    
    while 1:
        data=""
        Serial.flush()
        Serial.read(20)
        Serial.write(b"AT+COPS?\r");
        data=Serial.read(40)
        #print data
        r=data.find(b"+COPS:")
        if r>=0:
            l1=data.find(b",\"")+2
            l2=data.find(b"\"\r")
            operator=data[l1:l2]
            time.sleep(3)
            print (operator)
            break;
        time.sleep(0.5)
    Serial.writeb(b"AT+CMGF=1\r");
    time.sleep(0.5)
   # Serial.write("AT+CNMI=2,2,0,0,0\r");
   # time.sleep(0.5)
    Serial.write(b"AT+CSMP=17,167,0,0\r");
    time.sleep(0.5)

def receiveSMS(data):
    print (data)
    r=data.find(b"\",")
    print (r)
gsmInit()

