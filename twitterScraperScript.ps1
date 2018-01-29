Set-Location -Path "D:/Users/Derek/PostGrad/BTCParser"
$startDate = Get-Date "1/12/2018"
$currentDate = Get-Date
$temp = $currentDate.ToShortDateString

$ts = New-TimeSpan -Start $startDate -End $currentDate
$DayCount = $ts.Days
$parseDate = $startDate
$dateList = New-Object System.Collections.ArrayList($null)
For ($i = 0; $i -lt $DayCount; $i++){ #I miss you already python
    $dateList.Add($parseDate)
    $parseDate = $parseDate.AddDays(1)
}
$DayCount
scraper($dateList)


Workflow scraper{

    param(
    [Parameter (Mandatory = $true)]
    [System.Collections.ArrayList]$dateList
  )

        #I used those ugly ifs to avoid a situation where the script was trying to parse a date in the future (i.e. outside the boundaries of the array).
        #Please PM me if you have a more elegant solution 
        ForEach -Parallel ($date in $dateList)
        {      
              $endDate = $date.AddDays(1)
              $startDateString = $date.ToString("yyyy-MM-dd")
              $endDateString = $endDate.ToString("yyyy-MM-dd")
              $twitterScraperString = $startDateString + "BTCtweets.json"
              
              twitterscraper "Bitcoin OR BTC " -begindate $startDateString -enddate $endDateString --"limit" 20 -o =$twitterScraperString  
        }

    }
