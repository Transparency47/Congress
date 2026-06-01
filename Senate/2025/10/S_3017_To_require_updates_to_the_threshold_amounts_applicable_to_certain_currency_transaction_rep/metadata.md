# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3017?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3017
- Title: STREAMLINE Act
- Congress: 119
- Bill type: S
- Bill number: 3017
- Origin chamber: Senate
- Introduced date: 2025-10-20
- Update date: 2025-12-08T15:45:57Z
- Update date including text: 2025-12-08T15:45:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-20: Introduced in Senate
- 2025-10-20 - IntroReferral: Introduced in Senate
- 2025-10-20 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-10-20: Introduced in Senate

## Actions

- 2025-10-20 - IntroReferral: Introduced in Senate
- 2025-10-20 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-20",
    "latestAction": {
      "actionDate": "2025-10-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3017",
    "number": "3017",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "STREAMLINE Act",
    "type": "S",
    "updateDate": "2025-12-08T15:45:57Z",
    "updateDateIncludingText": "2025-12-08T15:45:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-20",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-10-20T20:13:36Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "SC"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "SD"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "AL"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "WY"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "TN"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "ID"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "OH"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3017is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3017\nIN THE SENATE OF THE UNITED STATES\nOctober 20, 2025 Mr. Kennedy (for himself, Mr. Scott of South Carolina , Mr. Rounds , Mrs. Britt , Ms. Lummis , Mr. Hagerty , Mr. Crapo , Mr. Moreno , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require updates to the threshold amounts applicable to certain currency transaction reports, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Streamlining Transaction Reporting and Ensuring Anti-Money Laundering Improvements for a New Era Act or the STREAMLINE Act .\n#### 2. Treasury reports\n##### (a) Thresholds for currency transaction reports\n**(1) Currency transaction reports**\n**(A) Initial updated threshold**\nNot later than 180 days after the date of enactment of this Act, the Secretary of the Treasury shall issue regulations pursuant to sections 5313 and 5315 of title 31, United States Code, to update each threshold amount under such regulations that is $10,000 to be $30,000.\n**(B) Inflation adjustment**\n**(i) In general**\nNot later that 5 years after the date on which the Secretary of the Treasury updates regulations under subparagraph (A), and every 5 years thereafter, the Secretary of the Treasury shall issue regulations pursuant to sections 5313 and 5315 of title 31, United States Code, to update each threshold amount under such regulations required to be updated under subparagraph (A) to reflect the change during the applicable 5-year period in the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor, which shall be rounded to the nearest multiple of $1,000.\n**(ii) Effective date**\nEach adjustment under clause (i) shall take effect on the first January 1 occurring after the date on which the Secretary of the Treasury publishes the adjustment.\n**(2) Reports relating to coins and currency received in nonfinancial trade or business**\nSection 5331 of title 31, United States Code, is amended\u2014\n**(A)**\nby striking $10,000 each place it appears in a heading or the text and inserting $30,000 ; and\n**(B)**\nby adding at the end the following:\n(e) Updates for inflation (1) In general Not later than 5 years after the date of enactment of this subsection, and every 5 years thereafter, the Secretary of the Treasury shall update each dollar figure under this section to reflect the change during the applicable 5-year period in the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor, which shall be rounded to the nearest multiple of $1,000. (2) Effective date Each adjustment under paragraph (1) shall take effect on the first January 1 occurring after the date on which the Secretary of the Treasury publishes the adjustment. .\n##### (b) Thresholds for suspicious activity reports\nNot later than 180 days after the date of enactment of this Act, the head of each Federal agency that issues regulations with respect to reports on suspicious transactions described under section 5318(g) of title 31, United States Code, shall update each threshold amount under such regulations that is $2,000 to be $3,000 and each threshold amount under such regulations that is $5,000 to be $10,000.\n##### (c) Review and report\nNot later than 360 days after the date of enactment of this Act, the Secretary of the Treasury shall\u2014\n**(1)**\nreview the forms and reporting and recordkeeping requirements issued pursuant to sections 5313, 5315, and 5318 of title 31, United States Code, which shall include an analysis on the aggregation, prioritization, and automation of those forms and requirements, to ensure that such forms and reporting requirements are effective and efficient in identifying illicit finance activity;\n**(2)**\nupdate the forms and requirements described in paragraph (1) as the Secretary of the Treasury determines necessary and consistent with section 5318(g)(5) of title 31, United States Code;\n**(3)**\nconduct the reviews and submit the reports required under sections 6204, 6205, and 6216 of the Anti-Money Laundering Act of 2020 (division F of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021; 134 Stat. 4569; 31 U.S.C. 5313 note, 31 U.S.C. 5311 note); and\n**(4)**\nsubmit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report that\u2014\n**(A)**\nsummarizes the results of the review conducted under paragraph (1); and\n**(B)**\nincludes recommendations for updating the forms and requirements described in paragraph (1).\n##### (d) Rule of construction\nNothing in this section shall be construed to\u2014\n**(1)**\nalter the ability of the Secretary of the Treasury to issue geographic targeting orders pursuant to section 5326 of title 31, United States Code;\n**(2)**\nalter any legal grounds for any geographic targeting order issued on or before the date of enactment of this Act; or\n**(3)**\nalter the ability of the Secretary of the Treasury to reduce reporting thresholds when consistent with all applicable law.",
      "versionDate": "2025-10-20",
      "versionType": "Introduced in Senate"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-08T15:45:57Z"
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
      "date": "2025-10-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3017is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "STREAMLINE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-24T02:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STREAMLINE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-24T02:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Streamlining Transaction Reporting and Ensuring Anti-Money Laundering Improvements for a New Era Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-24T02:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require updates to the threshold amounts applicable to certain currency transaction reports, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-24T02:18:19Z"
    }
  ]
}
```
