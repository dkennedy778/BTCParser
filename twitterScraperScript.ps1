Set-Location -Path "Your_Path"
$startDate = Get-Date "1/12/2018"
$currentDate = Get-Date
$temp = $currentDate.ToShortDateString

$ts = New-TimeSpan -Start $startDate -End $currentDate
$DayCount = $ts.Days
$DayCount
$parseDate = $startDate
For ($i = 0; $i -lt $DayCount; $i++){ #I miss you already python
    $twitterScraperString = $parseDate + "BTCtweets.json"
    twitterscraper "Bitcoin OR BTC " -l 2000000 -o =$twitterScraperString
    $parseDate = $parseDate.AddDays(1)
    $twitterScraperString = $parseDate + "BTCtweets.json"
    twitterscraper "Bitcoin OR BTC " -l 2000000 -o =$twitterScraperString
    $parseDate = $parseDate.AddDays(1)
    $twitterScraperString = $parseDate + "BTCtweets.json"
    twitterscraper "Bitcoin OR BTC " -l 2000000 -o =$twitterScraperString
    $parseDate = $parseDate.AddDays(1)
    $twitterScraperString = $parseDate + "BTCtweets.json"
    twitterscraper "Bitcoin OR BTC " -l 2000000 -o =$twitterScraperString
    $parseDate = $parseDate.AddDays(1)
    $twitterScraperString = $parseDate + "BTCtweets.json"
    twitterscraper "Bitcoin OR BTC " -l 2000000 -o =$twitterScraperString
    $parseDate = $parseDate.AddDays(1)
    $twitterScraperString = $parseDate + "BTCtweets.json"
    twitterscraper "Bitcoin OR BTC " -l 2000000 -o =$twitterScraperString
    $parseDate = $parseDate.AddDays(1)
    $parseDate.Date 
}
