def encrypt(msg,shift):
 enc_msg=''
 for i in msg:
  if ord(i) in range(ord('a'),ord('z')+1):
   if ord(i)+shift>ord('z'):
    enc_msg+=chr(ord('a')+((ord(i)+shift)-ord('z')))
   elif ord(i)+shift<ord('a'):
    enc_msg+=chr(ord('z')-(ord('a')-(ord(i)+shift)))
   else:    
    enc_msg+=chr(ord(i)+shift)
  else:
   enc_msg+=chr(ord(i))
 return enc_msg
 
def decrypt(msg,shift):
 dec_msg=encrypt(msg,-shift)
 return dec_msg
 
msg=raw_input('Enter message: ')
shift=input('Shift value: ')
shift%=26
print 'Encrpted message: ',encrypt(msg,shift)
print 'Plain text: ',decrypt(encrypt(msg,shift),shift)
