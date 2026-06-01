# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5570?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5570
- Title: Rail Passenger Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 5570
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2025-12-16T18:53:16Z
- Update date including text: 2025-12-16T18:53:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-26 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-01 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-26 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-01 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5570",
    "number": "5570",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000530",
        "district": "17",
        "firstName": "Christopher",
        "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
        "lastName": "Deluzio",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Rail Passenger Fairness Act",
    "type": "HR",
    "updateDate": "2025-12-16T18:53:16Z",
    "updateDateIncludingText": "2025-12-16T18:53:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-01T19:23:04Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-26T14:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "PA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5570ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5570\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Deluzio (for himself, Mr. Boyle of Pennsylvania , and Mrs. McIver ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo permit Amtrak to bring civil actions in Federal district court to enforce the right set forth in section 24308(c) of title 49, United States Code, which gives intercity and commuter rail passenger transportation preference over freight transportation in using a rail line, junction, or crossing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rail Passenger Fairness Act .\n#### 2. Findings\n**(1)**\nCongress created Amtrak under the Rail Passenger Service Act of 1970 ( Public Law 91\u2013158 ).\n**(2)**\nAmtrak began serving customers on May 1, 1971, taking over the operation of most intercity passenger trains that private, freight railroads were previously required to operate. In exchange for assuming these passenger rail operations, Amtrak was given access to the national rail network.\n**(3)**\nIn return for relief from the obligation to provide intercity passenger service, railroads over which Amtrak operated (referred to in this section as host railroads ) were expected to give Amtrak passenger trains preference over freight trains when using the national rail network.\n**(4)**\nIn 1973, Congress passed the Amtrak Improvement Act of 1973 ( Public Law 93\u2013146 ), which gives intercity and commuter rail passenger transportation preference over freight transportation in using a rail line, junction, or crossing. This right, which is now codified as section 24308(c) of title 49, United States Code, states, Except in an emergency, intercity and commuter rail passenger transportation provided by or for Amtrak has preference over freight transportation in using a rail line, junction, or crossing unless the Board orders otherwise under this subsection. A rail carrier affected by this subsection may apply to the Board for relief. If the Board, after an opportunity for a hearing under section 553 of title 5, decides that preference for intercity and commuter rail passenger transportation materially will lessen the quality of freight transportation provided to shippers, the Board shall establish the rights of the carrier and Amtrak on reasonable terms. .\n**(5)**\nMany host railroads have ignored the law referred to in paragraph (4) by refusing to give passenger rail the priority to which it is statutorily entitled and giving freight transportation the higher priority. As a result, Amtrak\u2019s on time performance on most host railroads is poor, has declined between 2014 through 2019, and continues to decline.\n**(6)**\nAccording to Amtrak, 6,500,000 customers on State-supported and long-distance trains arrived at their destination late during fiscal year 2019. Nearly 70 percent of these delays were caused by host railroads, amounting to a total of 3,200,000 minutes. The largest cause of these delays was freight train interference, which accounted for more than 1,000,000 minutes of delay for Amtrak passengers, or approximately 2 years, because host railroads chose to give freight trains priority.\n**(7)**\nPoor on-time performance wastes taxpayer dollars. According to a 2019 report by Amtrak\u2019s Office of Inspector General, a 5 percent improvement of on-time performance on all Amtrak routes would result in $12,100,000 in cost savings to Amtrak in the first year. If on-time performance on long-distance routes reached 75 percent for a year, Amtrak would realize an estimated $41,900,000 in operating cost savings, with a one-time savings of $336,000,000 due to a reduction in equipment replacement needs.\n**(8)**\nHistorical data suggests that on-time performance on host railroads is driven by the existence of an effective means to enforce Amtrak\u2019s preference rights:\n**(A)**\nTwo months after the date of the enactment of the Passenger Rail Investment and Improvement Act of 2008 (division B of Public Law 110\u2013432 ), which included provisions for the enforcement of these preference rights, was enacted, the on-time performance of long-distance trains improved from 56 percent to 77 percent and class I freight train interference delays across all routes declined by 40 percent.\n**(B)**\nOne year after such date of enactment, freight train interference delays had declined by 54 percent and the on-time performance of long-distance trains reached 85 percent.\n**(C)**\nIn 2014, after some of the provisions in the Passenger Rail Investment and Improvement Act of 2008 related to enforcement of preference were ruled unconstitutional by a D.C. Circuit Court, long-distance train on-time performance declined from 72 percent to 50 percent, and freight train interference delays increased 59 percent.\n**(D)**\nThe last time long-distance trains achieved an on-time rate of more than 80 percent in a given month was February 2012.\n**(9)**\nAs a result of violations of Amtrak\u2019s right to preference, Amtrak has been consistently unable on host railroad networks to meet its congressionally mandated mission and goals, which are codified in section 24101 of title 49, United States Code (relating to providing on-time and trip-time competitive service to its passengers).\n**(10)**\nAmtrak does not have an effective mechanism to enforce its statutory preference right in order to fulfill its mission and goals. Only the Attorney General can bring a civil action for equitable relief in a district court of the United States to enforce Amtrak\u2019s preference rights.\n**(11)**\nIn Amtrak\u2019s entire history, the only enforcement action initiated by the Attorney General was against the Southern Pacific Transportation Company in 1979.\n**(12)**\nCongress supports continued authority for the Attorney General to initiate an action, but Amtrak should also be entitled to bring a civil action before a Federal district court to enforce its statutory preference rights.\n#### 3. Authorize Amtrak to bring a civil action to enforce it preference rights\n##### (a) In general\nSection 24308(c) of title 49, United States Code, is amended, by adding at the end the following: Notwithstanding sections 24103(a) and 24308(f), Amtrak shall have the right to bring an action for equitable or other relief in the United States District Court for the District of Columbia to enforce the preference rights granted under this subsection. .\n##### (b) Conforming amendment\nSection 24103 of title 49, United States Code, is amended by inserting and section 24308(c) before , only the Attorney General .",
      "versionDate": "2025-09-26",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-16T18:53:16Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5570ih.xml"
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
      "title": "Rail Passenger Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T07:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rail Passenger Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T07:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To permit Amtrak to bring civil actions in Federal district court to enforce the right set forth in section 24308(c) of title 49, United States Code, which gives intercity and commuter rail passenger transportation preference over freight transportation in using a rail line, junction, or crossing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T07:33:27Z"
    }
  ]
}
```
