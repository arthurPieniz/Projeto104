import cv2

img = cv2.imread("solar-system.jpg")

#Possívelmente ficaram mal colocados os textos, pois eu não consegui abrir o arquivo

cv2.putText(
    img,
    "Sol",
    (200, 80),
    cv2.FONT_HERSHEY_COMPLEX,
    2,
    (0,0,255)
)

cv2.putText(
    img,
    "Mercurio",
    (200, 185),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (255,255,255)
)

cv2.putText(
    img,
    "Venus",
    (300, 240),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (255,255,255)
)

cv2.putText(
    img,
    "Terra",
    (410, 240),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (255,255,255)
)

cv2.putText(
    img,
    "Marte",
    (480, 240),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (255,255,255)
)

cv2.putText(
    img,
    "Jupiter",
    (590, 150),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (255,255,255)
)

cv2.putText(
    img,
    "Saturno",
    (710, 190),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (255,255,255)
)

cv2.putText(
    img,
    "Urano",
    (1000, 210),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (255,255,255)
)

cv2.putText(
    img,
    "Neturno",
    (1150, 210),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (255,255,255)
)

cv2.imshow("resultado",img)
cv2.waitKey(0)