import requests, sys, time

def main():
	global auth, api
	api = 'kitkabackend.eastus.cloudapp.azure.com:5010'
	auth = str(input("\nAuth Code: "))
	print("_"*59)
	c = 0
	x = 1
	while c < x:
		dupe()
	
def dupe():
        while True:
                try:
                        headers = {
                            'authorization': auth,
                            'use_response_compression': 'true',
                            'Accept-Encoding': 'gzip',
                            'Host': api,
                            'Connection': None,
                            'User-Agent': None,
                        }
                        response = requests.get(f'http://{api}/round/finishv2/3', headers=headers)
                        if response.status_code == 200:
                                trof = response.text.split('"SkillRating":')[1].split(',')[0]
                                cro = response.text.split('"Crowns":')[1].split(',')[0]
                                sys.stdout.write(f"\rSuccess !! | {trof} | {cro}")
                                time.sleep(1)           
                        elif response.status_code == 403 and response.text == "BANNED":
                                print(f"\nBanned!")
                                break              
                except:
                    continue

if __name__ == "__main__":
	main()