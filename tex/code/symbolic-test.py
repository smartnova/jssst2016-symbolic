# 視野錐台が単位立方体に射影されること
Points = Perspective * PointsCamera
for c in range(4):
    assert(Cartesian(Points[:,c])
           == Cartesian(PointsPerspective[:,c]))
