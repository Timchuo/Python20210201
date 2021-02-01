point1=int(input('math'))
point2=int(input('eng'))
if point1>100 or point1<0:
     print('亂打')
elif point2<100 or point2<0:      
     print('亂打')
if point1>=90 and point2>=90:
     print('gift')
elif point1<60 and point2<60:
     print('bednew')
elif point1 < 60 or point2 <60:       
     print('再加油') 
      