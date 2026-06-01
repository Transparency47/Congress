# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5407?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5407
- Title: Climate Resilient Elections Act
- Congress: 119
- Bill type: HR
- Bill number: 5407
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2025-09-26T15:32:55Z
- Update date including text: 2025-09-26T15:32:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5407",
    "number": "5407",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001206",
        "district": "25",
        "firstName": "Joseph",
        "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
        "lastName": "Morelle",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Climate Resilient Elections Act",
    "type": "HR",
    "updateDate": "2025-09-26T15:32:55Z",
    "updateDateIncludingText": "2025-09-26T15:32:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-16",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-09-16T14:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "AL"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5407ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5407\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Mr. Morelle (for himself, Ms. Sewell , Mrs. Torres of California , and Ms. Johnson of Texas ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo require certain States to submit a continuity of operations plan for elections in the event of a major disaster, to require the Comptroller General of the United States to report on assistance for election administration in the event of a major disaster, and to require the Election Assistance Commission to award grants to strengthen elections against climate change-driven disasters, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Climate Resilient Elections Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nIn January 2017, the Department of Homeland Security determined that the Nation\u2019s election infrastructure qualifies as critical infrastructure for national security purposes.\n**(2)**\nAccording to the Department of Homeland Security, [t]his designation recognizes that the United States\u2019 election infrastructure is of such vital importance to the American way of life that its incapacitation or destruction would have a devastating effect on the country .\n**(3)**\nElection administration consistently faces substantial threats because of severe natural disasters. Delayed elections or damaged or destroyed polling places, voting machines, ballots, or transportation and utility infrastructure may disenfranchise voters, undermine confidence in elections, or even alter election outcomes.\n**(4)**\nHurricane Sandy made landfall in New York and New Jersey just days before the 2012 presidential election, displacing as many as 776,000 residents and causing unprecedented election administration challenges. The jurisdictions most affected by Hurricane Sandy saw significantly worse voter turnout in the 2012 presidential election than those unaffected by the storm.\n**(5)**\nIn 2016, California experienced 12 major fires in the three months leading up to Election Day. In 2018, the State experienced 15 major fires leading up to Election Day. These fires displaced voters, burned residences, and damaged polling stations. Climate change has extended wildfire season in the American west into the late Fall: On November 8, 2018, just two days after Election Day, the Camp Fire ignited, eventually claiming 85 lives and destroying over 18,000 structures\u2014the deadliest fire in California history. Evacuation orders because of wildfires displace hundreds of thousands of voters each year, well into the days leading up to the election.\n**(6)**\nIn 2018, Hurricane Michael hit the Florida panhandle just 27 days before the midterm elections, causing at least 16 deaths, damaging or destroying an estimated 40,000 homes, and resulting in approximately $25 billion in damages. The destruction displaced tens of thousands of voters and forced the closure of polling places, significantly depressing turnout amongst voters recovering from the hurricane who were forced to travel longer distances to cast a ballot.\n**(7)**\nIn 2021, Hurricane Ida forced the Governor of Louisiana to delay several elections, scheduled for October, and relocate and consolidate polling places due to devastating damage. In the hardest hit parts of the State, some voters had to cast their ballots in large tents because of the significant damage.\n**(8)**\nIn 2022, voters in Kentucky displaced by tornadoes that ravaged the State in the months leading up to the primary election had to vote absentee in order to cast a ballot in their home counties.\n**(9)**\nHurricane Helene caused significant damage and devastation throughout the southeastern United States\u2014particularly in Florida, Georgia, North Carolina, South Carolina, Tennessee, and Virginia\u2014when it made landfall in September 2024. The hurricane\u2019s destruction was extreme, occurring during the early and mail voting period for the November 2024 elections and displacing thousands while disrupting mail services for countless voters who rely on the United States Postal Service to cast a ballot.\n**(10)**\nHurricane Milton caused billions of dollars in damage, spawned numerous deadly tornadoes, and displaced countless voters less than a month before the November 2024 elections.\n**(11)**\nThe United States Election Assistance Commission has published a web page on contingency planning to help election officials prepare for unexpected circumstances, including natural and other disasters.\n**(12)**\nThe United States Forest Service has declared that [i]n the past 20 years, many States have had record catastrophic wildfires, harming people, communities and natural resources and causing billions of dollars in damage. In running 5-year average number of structures destroyed by wildfires each year rose from 2,873 in 2014 to 12,255 in 2020\u2014a fourfold increase in just six years . As these trends continue, the impacts of climate change on American lives and American infrastructure will grow.\n**(13)**\nThe National Oceanic and Atmospheric Administration has cautioned that extreme weather events [caused by climate change] that bring heavy rains, floods, wind, snow, or temperature changes can stress existing structures and facilities. Increased temperatures require more indoor cooling, which can put stress on an energy grid. Sudden heavy rainfall can lead to flooding that shuts down highways and major business areas . Each of these factors may strain election infrastructure if they occur during a voting period.\n**(14)**\nThe Department of Defense has declared that [r]ising temperatures, changing precipitation patterns, and more frequent, extreme, and unpredictable weather conditions caused by climate change are worsening existing security risks and creating new challenges for the United States . These security risks and challenges are amplified when they threaten the elections that form the bedrock of our Republic.\n**(15)**\nThe Department of Energy has noted that severe weather\u2014the leading cause of power outages and fuel supply disruption in the United States\u2014is projected to worsen, with eight of the 10 most destructive hurricanes of all time having happened in the last 10 years . The catastrophic effects of severe weather threaten the sanctity of American elections, and we must ensure that our election systems are prepared for worsening climate change-based weather events.\n**(16)**\nThe Department of the Interior has clarified that the climate crisis disproportionately affects underserved communities . These communities already face significant barriers to the ballot.\n**(17)**\nPresident Trump\u2019s budget request proposes the elimination of the Election Security Grants funding program that supports State and local election administration, in addition to drastic cuts to the Election Assistance Commission\u2014cuts that would harm States\u2019 ability to conduct secure, safe, and fair elections in the face of natural disasters.\n**(18)**\nIt is incumbent upon election administrators nationwide to ensure the resiliency of our elections\u2014and through our elections, our very democracy\u2014in the face of the worsening climate crisis.\n#### 3. Ensuring election administrators prepare and retain continuity of operations plans for use in the event of disaster\n##### (a) Requirement\nTitle IX of the Help America Vote Act of 2002 ( 52 U.S.C. 21141 et seq. ) is amended by adding at the end the following:\n907. Continuity of operations plan requirement (a) In general Each State that receives a grant or other payment under this Act after the date of the enactment of this section\u2014 (1) shall, not later than September 30, 2028, submit to the Commission a continuity of operations plan to ensure the successful administration of elections in the event of disaster, accounting for the disasters most likely to occur in the jurisdiction of such recipient, including a major disaster (as defined in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 )); (2) shall, not later than September 30, 2033, and not less frequently than every 5 years thereafter until September 30, 2043, update such plan to reflect evolving risks or changing conditions and promptly submit the updated version of such plan to the Commission; (3) may, after September 30, 2043, update such plan to reflect evolving risks or changing conditions and submit the updated version of such plan to the Commission; (4) shall retain each plan submitted under paragraph (1), (2), or (3) until the date that is 5 years after the date such plan was submitted to the Commission; and (5) may coordinate with the Commission, other States, Tribal governments, units of local government, or other resources or entities when preparing such plan. (b) Publication The Commission shall disseminate to the public (through the internet, published reports, and other methods the Commission considers appropriate) any continuity of operations plan received pursuant to this section, except that no information so disseminated may expose personally identifiable information or endanger national security, public infrastructure, or public safety. .\n##### (b) Clerical amendment\nThe table of contents of such Act is amended by inserting after the item relating to section 906 the following new item:\nSec. 907. Continuity of operations plan requirement. .\n#### 4. Report on voter registration and Federal assistance for election administration in the event of a major disaster\n##### (a) In general\nThe Comptroller General of the United States shall conduct\u2014\n**(1)**\nan analysis of the effect of natural disasters on voter registration rates in areas affected by such disasters;\n**(2)**\nan analysis of ways that the Federal Government may better assist States and units of local government in the administration of elections in the event of a covered major disaster, including the ways existing Federal resources in regions potentially affected by such a covered major disaster that are not allocated to life-saving or national security measures should be engaged to support election infrastructure; and\n**(3)**\na study of legislative authorizations, if any are needed, that Congress may consider to ensure the efficient and effective deployment of emergency resources to support election infrastructure in the event that the President declares a covered major disaster.\n##### (b) Report\nNot later than September 30, 2026, the Comptroller General shall submit to the Committee on House Administration of the House of Representatives and the Committee on Rules and Administration of the Senate a report on the analysis and study required under subsection (a).\n##### (c) Limitation on authority\nNo provision of this Act may be construed to authorize any power of the Federal Government to seize or hold any ballot or voting machine.\n#### 5. Grants for strengthening American elections against climate change-driven disasters\n##### (a) In general\nThe Election Assistance Commission shall make grants to assist States in strengthening the resiliency of State voting systems against potential covered major disasters to improve the quality, reliability, accuracy, accessibility, affordability, and security of voting equipment, election systems, and voting technology.\n##### (b) Use of funds\nA State shall use the funds provided under a grant made under this section to carry out one or more of the following activities:\n**(1)**\nImproving the administration of elections for Federal office with specific regard to disaster preparedness.\n**(2)**\nEducating voters concerning State plans for election administration during or immediately after a covered major disaster.\n**(3)**\nTraining election officials, poll workers, and election volunteers with respect to disaster preparedness.\n**(4)**\nDeveloping or publishing the continuity of operation plan required by section 3 of this Act.\n**(5)**\nImproving, acquiring, leasing, modifying, or replacing voting systems and technology and methods for casting and counting votes, provided that such improvements, acquisitions, leases, modifications, or replacements will enhance the resiliency of a Federal election in the State.\n**(6)**\nEstablishing or modifying a toll-free hotline that voters may use to obtain information on how and where to vote in the event of a covered major disaster.\n##### (c) Limitation\nA State may not use the funds provided under a grant made under this section\u2014\n**(1)**\nto pay the costs associated with any litigation, except to the extend that such costs otherwise constitute permitted uses of a grant under this section;\n**(2)**\nfor the payment of any judgment; or\n**(3)**\nfor any use that would violate a State or Federal court order.\n##### (d) Authorization of appropriations\nThere are authorized to be appropriated for grants under this section\u2014\n**(1)**\n$20,000,000 for fiscal year 2026;\n**(2)**\n$20,000,000 for fiscal year 2027;\n**(3)**\n$20,000,000 for fiscal year 2028;\n**(4)**\n$20,000,000 for fiscal year 2029; and\n**(5)**\n$20,000,000 for fiscal year 2030.\n#### 6. Definitions\nIn this Act:\n**(1) Covered major disaster**\nThe term covered major disaster means a major disaster declared by the President during the voting period of a Federal election pursuant to section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ) in response to\u2014\n**(A)**\na natural catastrophe, including hurricane, tornado, storm, high water, wind-driven water, tidal wave, tsunami, earthquake, volcanic eruption, landslide, mudslide, snowstorm, extreme heat, and drought;\n**(B)**\na fire, flood, or explosion, regardless of cause; or\n**(C)**\nan act of terrorism.\n**(2) State**\nThe term State has the meaning given such term in section 901 of the Help America Vote Act of 2002 ( 52 U.S.C. 21141 ).",
      "versionDate": "2025-09-16",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-26T15:32:55Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5407ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Climate Resilient Elections Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-26T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Climate Resilient Elections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-26T05:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require certain States to submit a continuity of operations plan for elections in the event of a major disaster, to require the Comptroller General of the United States to report on assistance for election administration in the event of a major disaster, and to require the Election Assistance Commission to award grants to strengthen elections against climate change-driven disasters, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-26T05:33:22Z"
    }
  ]
}
```
