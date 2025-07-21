# KEY AUTHENTICATION TYPES:

<BR>

### >ENABLE SSH<BR>
## 1. SSH AUTHENTICATION:<BR>

### STEPS:<br>
<LI>  generate the public and private key pair of the client using (ssh-keygen)
<LI>  login into the server using password 
<LI>  go to the .ssh folder in the server if not then make one .ssh folder & in that create a file named authentication_key.
<LI>  using VIM editor paste the copied key pair into the authentication_key file
<LI>  then from the client side login to the server side using (ssh username@127.0.0.1 -p 2222)

## 2. SSH + PASSPHRASE AUTHENTICATION:<BR>
 ### STEPS:
<LI>  generate the public and private key pair of the client using (ssh-keygen)
<li>  It will ask for a passphrase then add a passphrase
<LI>  login into the server using password 
<LI>  go to the .ssh folder in the server if not then make one .ssh folder & in that create a file named authentication_key.
<LI>  using VIM editor paste the copied key pair into the authentication_key file
<li>  using (sudo nano /etc/ssh/sshd_config) edit the PasswordAuthentication to NO and PublicAuthentication to YES 
<LI>  then from the client side login to the server side using (ssh username@127.0.0.1 -p 2222)

## 3. SSH + CERTIFICATE AUTHENTICATION:<BR>
 ### STEPS:
