# C.A.C.T.U.S.
Compact Automated Cluster of Tactically Useful Services


Ammunitions container cluster of 3-9 Raspberry Pi nodes. 
- Pi3b+ for computing power. 
- Pi4 node for handling Pirate Box SLC network and services related (may need external wifi adapter capable of monitor-mode -- look at below link)
-- https://www.amazon.com/Alfa-Long-Range-Dual-Band-Wireless-External/dp/B00VEEBOPG/ref=pd_bxgy_img_2/144-9854697-5070115?_encoding=UTF8&pd_rd_i=B00VEEBOPG&pd_rd_r=c2ae0927-4cfd-4e3a-841b-dc763916b7ac&pd_rd_w=KNYbg&pd_rd_wg=lxsjF&pf_rd_p=ce6c479b-ef53-49a6-845b-bbbf35c28dd3&pf_rd_r=1D48KE5YCGXT0PT0S8SA&psc=1&refRID=1D48KE5YCGXT0PT0S8SA
- Pi Zero-W  

Possible network architecture:

	- Pi Cluster of computing power
		+ Functions:
			= DDoS --> Forced MITM
				- DDoS test case, they all dont have to communicate for that due to it only being a command
				- However, the computing power may be a bit off, and the heat generated will be disastrous
			= Distributed computing to possibly help with other functions
	- SLC (cluster?) of Pirate boxes
  
