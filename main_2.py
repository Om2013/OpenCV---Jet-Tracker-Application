import cv2 

video=r"C:\Users\omrad\OneDrive\Desktop\Jet Tracker Application - OpenCV\Jet Fight1.mp4"
cap=cv2.VideoCapture(video)
tracker=cv2.TrackerCSRT_create()
ret,frame = cap.read()
Bbox=cv2.selectROI("Select the Jet to Track",frame,False)
tracker.init(frame,Bbox)

while True:
    ret,frame = cap.read()
    if not ret:
        break 
    

    #cv2.rectangle(frame,(int(Bbox[0]),int(Bbox[1])),(int(Bbox[0] + Bbox[2]), int(Bbox[1] + Bbox[3])),(255,0,0),2)
   
    success,box = tracker.update(frame)
    if success:
        x,y,w,h=[int(i) for i in box]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        cv2.putText(frame,"Tracking",(30,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),3)
        cv2.putText(frame,f"X:{x}, Y:{y}, Width: {w}, Height: {h}",(30,200),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
        
    else:
        cv2.putText(frame,"Tracking Lost",(30,20),(0,0,0),cv2.FONT_HERSHEY_PLAIN,3)

    cv2.imshow("Tracker Initialized",frame)
    
    if cv2.waitKey(20) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()


    
