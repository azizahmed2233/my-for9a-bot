nity"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        first_opp = soup.find('div', class_='opportunity-card')
        
        title = first_opp.find('h3').text.strip()
        link = first_opp.find('a')['href']
        
        token = os.environ.get("TELEGRAM_TOKEN")
        chat_id = os.environ.get("CHAT_ID")
        
        message = f"📢 فرصة جديدة:\n\n{title}\n\nالرابط: {link}"
        requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}")
        
        return {"statusCode": 200, "body": "Success"}
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
