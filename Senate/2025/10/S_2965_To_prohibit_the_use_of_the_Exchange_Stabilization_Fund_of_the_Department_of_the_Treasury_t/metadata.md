# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2965?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2965
- Title: No Argentina Bailout Act
- Congress: 119
- Bill type: S
- Bill number: 2965
- Origin chamber: Senate
- Introduced date: 2025-10-01
- Update date: 2026-01-07T16:16:57Z
- Update date including text: 2026-01-07T16:16:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-01: Introduced in Senate
- 2025-10-01 - IntroReferral: Introduced in Senate
- 2025-10-01 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-10-01: Introduced in Senate

## Actions

- 2025-10-01 - IntroReferral: Introduced in Senate
- 2025-10-01 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-01",
    "latestAction": {
      "actionDate": "2025-10-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2965",
    "number": "2965",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "No Argentina Bailout Act",
    "type": "S",
    "updateDate": "2026-01-07T16:16:57Z",
    "updateDateIncludingText": "2026-01-07T16:16:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-01",
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
      "actionDate": "2025-10-01",
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
          "date": "2025-10-01T19:48:50Z",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-01",
      "state": "VA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-10-01",
      "state": "MD"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-10-01",
      "state": "NJ"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-10-01",
      "state": "MN"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-10-01",
      "state": "AZ"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-10-02",
      "state": "VT"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "HI"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "HI"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-10-22",
      "state": "NY"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-22",
      "state": "NJ"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-10-22",
      "state": "RI"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-10-22",
      "state": "NV"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "NM"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "MD"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "IL"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "CA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2965is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2965\nIN THE SENATE OF THE UNITED STATES\nOctober 1, 2025 Ms. Warren (for herself, Mr. Kaine , Mr. Van Hollen , Mr. Booker , Ms. Smith , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo prohibit the use of the Exchange Stabilization Fund of the Department of the Treasury to bail out Argentina's financial markets.\n#### 1. Short title\nThis Act may be cited as the No Argentina Bailout Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nworkers and families in the United States are struggling to afford basic necessities, like groceries, rent, health care, credit card bills, and other debt payments;\n**(2)**\nmany farmers in the United States, especially soybean farmers, are experiencing severe financial hardship, in large part, because of the chaotic tariffs imposed by President Donald Trump;\n**(3)**\nthe Exchange Stabilization Fund of the Department of the Treasury should be used to promote financial interests of the United States by defending jobs, wages, and financial stability from foreign currency manipulation, not to bail out foreign financial markets;\n**(4)**\nglobal investors appear to have lost confidence in the President of Argentina, Javier Milei, because of corruption scandals and his waning public popularity, causing serious disruptions in the country\u2019s financial markets;\n**(5)**\nSecretary of the Treasury Scott Bessent announced a $20,000,000,000 bailout of Argentina\u2019s financial markets to provide President Milei with a bridge to the country\u2019s October 26 midterm elections;\n**(6)**\nPresident Donald Trump and Republicans in Congress are shutting down the United States Government after ripping away health care from 15,000,000 people in the United States; and\n**(7)**\nPresident Trump should not prioritize a $20,000,000,000 bailout for his foreign political ally and global investors over health care for the people of the United States and the critical government programs that will be turned off in the Trump-Republican shutdown.\n#### 3. Prohibition on use of Exchange Stabilization Fund to bail out Argentina's financial markets\nSection 5302(b) of title 31, United States Code, is amended\u2014\n**(1)**\nby inserting (1) after (b) ; and\n**(2)**\nby adding at the end the following:\n(2) (A) The fund may not be used to provide direct or indirect financial support to the country of Argentina under paragraph (1), including through the establishment of currency swap lines, the purchase of pesos or sovereign debt of Argentina, or the extension of any credit instrument. (B) Any financial contract or instrument entered into before the date of the enactment of this paragraph that violates subparagraph (A) shall be sold or terminated not later than 7 days after such date of enactment. (C) The prohibition under subparagraph (A) terminates on December 10, 2027. .",
      "versionDate": "2025-10-01",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-01-07T16:16:57Z"
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
      "date": "2025-10-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2965is.xml"
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
      "title": "No Argentina Bailout Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-31T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Argentina Bailout Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the use of the Exchange Stabilization Fund of the Department of the Treasury to bail out Argentina's financial markets.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:03:13Z"
    }
  ]
}
```
