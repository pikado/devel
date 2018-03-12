def disp(s,a,d):
 print "source:",s
 print "aux:",a
 print "destination:",d
 print

def shift_left_ar(ar):
 for i in range(0,len(ar)-1):
  tmp=ar[i+1]
  ar[i]=tmp
 ar[len(ar)-1]=0
 
def shift_right_ar(ar,elt):
 for i in range(len(ar)-1,0,-1):
  tmp=ar[i-1]
  ar[i]=tmp
 ar[0]=elt
 	
def check_shift(beg_a,end_a):
 if end_a[0]==0:
  end_a[0]=beg_a[0]
 else:
  shift_right_ar(end_a,beg_a[0])
 shift_left_ar(beg_a)
 
def init_stack(s,n):
 for i in range(1,n+1):
  s.append(10*i)
 
def move_disk(s,a,d,n):
 if n==0:
  n+1
 if n==1:
  d.insert(0,s[0])
  s.remove(s[0])
 else:
  move_disk(s,d,a,n-1)
  move_disk(s,a,d,1)
  move_disk(a,s,d,n-1)
  
src=[]
aux=[]
dest=[]

init_stack(src,10)

disp(src,aux,dest)
move_disk(src,aux,dest,len(src))
disp(src,aux,dest)