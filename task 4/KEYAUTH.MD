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

## 3. SSH + CERTIFICATE AUTHENTICATION(USING 3 SERVERS):<BR>
 ### STEPS:
# SSH Certificate Authority Setup Guide

This guide provides all the steps to set up SSH authentication using a Certificate Authority (CA).

**Roles:**
* **CA Server (`chirag`):** Signs keys.
* **Main Server (`voldemort`):** The server you want to log into.
* **Client PC (`Daksh`):** The machine you are connecting from.

---

### ## 1. Configure the CA Server (`chirag`)

* **Goal:** Create the master Certificate Authority keys.

* **Commands (run on `chirag`):**
    ```bash
    # Create a dedicated directory
    mkdir ~/ssh-ca
    cd ~/ssh-ca

    # Generate the CA's private and public keys
    ssh-keygen -t rsa -b 4096 -f ca_key -C "SSH CA Key"
    ```

---

### ## 2. Configure the Main Server (`voldemort`)

* **Goal:** Tell the server to trust user keys signed by the CA.

* **Commands:**

    1.  **From `chirag`**, copy the CA's public key to `voldemort`:
        ```bash
        # Replace [IP_OF_VOLDEMORT] with the server's IP
        scp ~/ssh-ca/ca_key.pub voldemort@[IP_OF_VOLDEMORT]:/tmp/
        ```

    2.  **On `voldemort`**, move the key and configure SSH:
        ```bash
        # Move the key to the SSH directory
        sudo mv /tmp/ca_key.pub /etc/ssh/

        # Edit the SSH config file
        sudo nano /etc/ssh/sshd_config
        ```
        Add this line to the file, then save and exit:
        ```
        TrustedUserCAKeys /etc/ssh/ca_key.pub
        ```

    3.  **On `voldemort`**, restart the SSH service:
        ```bash
        sudo systemctl restart sshd
        ```

---

### ## 3. Configure the Client PC (`Daksh`)

* **Goal:** Generate a personal key, get it signed by the CA, and use it to connect.

* **Commands:**

    1.  **On `Daksh` (Windows PowerShell)**, create a personal SSH key pair (if you don't have one):
        ```powershell
        ssh-keygen -t rsa -b 4096
        ```

    2.  **On `Daksh`**, copy your public key to the CA for signing:
        ```powershell
        # Replace [IP_OF_CHIRAG] with the CA's IP
        scp $HOME/.ssh/id_rsa.pub chirag@[IP_OF_CHIRAG]:~/
        ```

    3.  **On `chirag`**, sign the client's key:
        ```bash
        # The client key is now in chirag's home directory
        ssh-keygen -s ~/ssh-ca/ca_key -I voldemort -n voldemort -V +52w ~/id_rsa.pub
        ```
        This creates the signed certificate: `~/id_rsa-cert.pub`.

    4.  **On `Daksh`**, copy the new signed certificate from the CA:
        ```powershell
        # Replace [IP_OF_CHIRAG] with the CA's IP
        scp chirag@[IP_OF_CHIRAG]:~/id_rsa-cert.pub $HOME/.ssh/
        ```
### ## 4. Final Connection

* **Goal:** Log into `voldemort` from `Daksh` using the certificate.

* **Command (run on `Daksh`):**
    ```powershell
    # Replace [IP_OF_VOLDEMORT] with the server's IP
    ssh voldemort@[IP_OF_VOLDEMORT]
    ```
