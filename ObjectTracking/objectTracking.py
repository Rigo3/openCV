import numpy as np
import cv2
import matplotlib.pyplot as plt
# %matplotlib inline

corner_track_params = dict(maxCorners=10,qualityLevel=0.3,minDistance=7,blockSize=7)
lk_params=dict(winSize=(200,200), maxLevel=1, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TermCriteria_COUNT, 15, 0.8))

cap = cv2.VideoCapture(0)
ret,prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame,cv2.COLOR_BGR2GRAY)


prevPts = cv2.goodFeaturesToTrack(prev_gray,mask=None, **corner_track_params)
mask = np.zeros_like(prev_frame)
prevPts.shape


# for i in prevPts:
#     x,y = i.ravel()
#     cv2.circle(prev_frame,(x,y), 5,(255,0,0),-1)
# plt.imshow(prev_frame)

# ret, frame = cap.read()
# frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# nextPts,status, err = cv2.calcOpticalFlowPyrLK(prev_gray,frame_gray,prevPts, None, **lk_params)
# good_new = nextPts[status == 1]
# good_new.shape

while True:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    nextPts,status, err = cv2.calcOpticalFlowPyrLK(prev_gray,frame_gray,prevPts, None, **lk_params)

    #THIS 2 NEXT ARRAYS HAVE A SHAPE (10,2)
    #FILL ARRAY WITH VALUES OF THE NEXTPTS, AND PREVPTS ARRAYS. ONLY VALUES WHERE THE ALGORITHM FOUND THE POINTS
    #EACH INDEPENDENT ARRAY(nextPts, and prevPts) HAVE THEIR POINTS ALREADY FOUND. YOU ARE SELECTING WHICH INDEX POINTS TO HAVE IN THE NEW ARRAYS.
    good_new = nextPts[status == 1]
    good_prev = prevPts[status == 1]

    for i, (new,prev) in enumerate(zip(good_new,good_prev)):
        x_new, y_new = new.ravel()
        x_prev, y_prev = prev.ravel()

        mask = cv2.line(mask,(x_new,y_new),(x_prev,y_prev),(0,255,0),3)
        frame = cv2.circle(frame,(x_new,y_new), 8, (0,0,255), -1)

    img = cv2.add(frame,mask)
    cv2.imshow('tracking', img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

    prev_gray = frame_gray.copy()
    prevPts = good_new.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()