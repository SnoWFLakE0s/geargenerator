#Variable Input
toothCount = 2*float(input("Enter number of gear teeth:\n"))
toothSize = float(input("Enter gear tooth base size, in fuselage units:\n"))
toothHeight = float(input("Enter gear tooth height, in fuselage units:\n"))
gearThickness = float(input("Enter gear thickness, in fuselage units:\n"))
color = input("Please specify the color id (0~12) that you want on the system: \n")

import math
#The size of the gear is determined by the apothem when determining the gear as a polygon. The diameter should be twice the apothem.
gearDiameter = 2*(toothSize / (2*math.tan(math.pi / toothCount)))
#gearDiameter is the size of the base fuselage piece
yOffset = gearDiameter / 4
#yoffset is the apothem, in meters, which is also the correct y-offset for the hemisphere part
angleOffset = 2*math.pi / toothCount

output1 = '''<?xml version="1.0" encoding="utf-8"?>
<Aircraft name="GeneratedObject" url="" theme="Default" xmlVersion="6">
  <Assembly>
    <Parts>
      <Part id="0" partType="Cockpit-1" position="0,0,0" rotation="0,0,0" drag="0,0,0,0,0,0" materials="{0}" scale="1,1,1" massScale="0" calculateDrag="false" dragScale="0" partCollisionResponse="Default">
        <Cockpit.State primaryCockpit="True" lookBackTranslation="0,0" />
      </Part>
      <Part id="1" partType="Fuselage-Body-1" position="0,0,0" rotation="0,0,0" drag="0,0,0,0,0,0" materials="{0}" scale="1,1,1" massScale="1" calculateDrag="false" disableAircraftCollisions="true" dragScale="0">
        <FuelTank.State fuel="0" capacity="0" />
        <Fuselage.State frontScale="{1},{1}" rearScale="{1},{1}" offset="0,0,{2}" deadWeight="0" buoyancy="0" fuelPercentage="0" cornerTypes="3,3,3,3,3,3,3,3" />
      </Part>'''.format(color, gearDiameter, gearThickness)
print(output1)

partId = 2
#The first gear tooth will be the third part in the craft, so start part id at 2. While loop the tooth generation bit until partId is 2 more than the tooth count.
initialAngle = 0
#initial angle to drive trig calculations
offsetMultiplier = 0
#how many angleOffsets to use
while partId < toothCount + 2:
  positionX = yOffset * math.sin(angleOffset * offsetMultiplier)
  positionY = yOffset * math.cos(angleOffset * offsetMultiplier)
  rotationAngle = math.degrees(angleOffset * offsetMultiplier)
  output2 = '''\t\t<Part id="{0}" partType="Hemisphere-1" position="{1},{2},0" rotation="0,0,{3}" drag="0,0,0,0,0,0" materials="{4}" disableAircraftCollisions="false" scale="{5},{6},{7}" massScale="0" calculateDrag="false" dragScale="0" partCollisionResponse="Default">
    <ResizableShape.State size="1" bounciness="0" friction="0" attachPointPosition="0,0,0" />
        </Part>'''.format(partId, positionX, positionY, -rotationAngle, color, toothSize, toothHeight, gearThickness)
  print(output2)
  partId += 2
  offsetMultiplier += 2
  
output3 = '''\t\t</Parts>
      <Connections>'''
print(output3)

#connections
connectId = 2
while connectId - 2 < toothCount:
  output4 = '''\t\t\t<Connection partA="1" partB="{0}" attachPointsA="0" attachPointsB="0" />'''.format(connectId)
  print(output4)
  connectId += 1

output5 = '''\t</Connections>
      <Bodies>'''
print(output5)

bodyId = 2
bodyList = []
while bodyId - 2 < toothCount:
  bodyList.append(str(bodyId))
  bodyId += 1

bodyListStr = ", ".join(bodyList)

output6 = '''\t\t\t<Body partIds="1, {0}" position="0,0,0" rotation="0,0,0" velocity="0,0,0" angularVelocity="0,0,0" />'''.format(bodyListStr)
print(output6)

output7 = '''\t</Bodies>
  </Assembly>
</Aircraft>'''
print(output7)