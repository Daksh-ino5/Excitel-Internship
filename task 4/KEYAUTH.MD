# KEY AUTHENTICATION TYPES:

<BR>

### ENABLE SSH<BR>
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
# SSH Certificate Authentication Setup Guide

This guide provides the complete, step-by-step process for configuring SSH certificate-based authentication.

---

### **Phase 1: On Your Windows PC (Client + CA)**

These steps create the necessary keys and the certificate on your local machine.

1.  **Create the Certificate Authority (CA) Key Pair**
    *This creates the master key pair that will be used to sign user keys.*
    ```bash
    ssh-keygen -t rsa -b 4096 -f ca_key -C "My Personal CA"
    ```

2.  **Create the User Key Pair**
    *This creates the standard SSH key pair you will use to log in.*
    ```bash
    ssh-keygen -t rsa -b 4096 -f user_key
    ```

3.  **Create the User Certificate**
    *This uses the CA's private key to sign your user's public key. The certificate is only valid for the specified user (`-n daksh`) and for a limited time (`-V +8h`).*
    ```bash
    ssh-keygen -s ca_key -I user_cert -n daksh -V +8h user_key.pub
    ```

4.  **Upload the CA Public Key to the Server**
    *This securely copies the CA's public key to the server so the server can learn to trust it. You will be prompted for your password.*
    ```bash
    scp -P 2222 ca_key.pub daksh@127.0.0.1:/tmp/ca_key.pub
    ```

---

### **Phase 2: On the Server**

These steps configure the server to trust your CA and accept the certificate for login.

1.  **Log In to the Server**
    *Connect to your server using your password for this one-time setup.*
    ```bash
    ssh -p 2222 daksh@127.0.0.1
    ```

2.  **Move the CA Key to the SSH Directory**
    *This moves the key from the temporary folder to its permanent location.*
    ```bash
    sudo mv /tmp/ca_key.pub /etc/ssh/ca_key.pub
    ```

3.  **Configure the SSH Server**
    *This command adds a line to the SSH server's configuration file, telling it to trust your CA.*
    ```bash
    echo "TrustedUserCAKeys /etc/ssh/ca_key.pub" | sudo tee -a /etc/ssh/sshd_config
    ```

4.  **Restart the SSH Service**
    *This applies the new configuration settings.*
    ```bash
    sudo systemctl restart sshd
    ```

5.  **Log Out of the Server**
    *The server setup is complete.*
    ```bash
    exit
    ```

---

### **Phase 3: Final Connection from Windows PC**

This is the final step where you connect using your new certificate.

1.  **Connect Without a Password**
    *This command uses your user key (`user_key`). The SSH client will automatically find and present the associated certificate (`user_key-cert.pub`). If successful, you will be logged in immediately without a password prompt.*
    ```bash
    ssh -p 2222 -i user_key daksh@127.0.0.1
    ```

