# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4298?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4298
- Title: Stop CHEATERS Act
- Congress: 119
- Bill type: S
- Bill number: 4298
- Origin chamber: Senate
- Introduced date: 2026-04-15
- Update date: 2026-05-07T12:23:49Z
- Update date including text: 2026-05-07T12:23:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in Senate
- 2026-04-15 - IntroReferral: Introduced in Senate
- 2026-04-15 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-04-15: Introduced in Senate

## Actions

- 2026-04-15 - IntroReferral: Introduced in Senate
- 2026-04-15 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4298",
    "number": "4298",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "Stop CHEATERS Act",
    "type": "S",
    "updateDate": "2026-05-07T12:23:49Z",
    "updateDateIncludingText": "2026-05-07T12:23:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T15:43:02Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "VA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "RI"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "OR"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NJ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "DE"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "PA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "AZ"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "CO"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NJ"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NM"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "OR"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-04-15",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "HI"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NH"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MD"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "VA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "VT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MN"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4298is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4298\nIN THE SENATE OF THE UNITED STATES\nApril 15 (legislative day, April 14), 2026 Mr. King (for himself, Ms. Warren , Mr. Kaine , Mr. Whitehouse , Mr. Schumer , Mr. Wyden , Mr. Bennet , Mr. Blumenthal , Ms. Blunt Rochester , Mr. Booker , Mr. Coons , Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mr. Gallego , Mr. Heinrich , Mr. Hickenlooper , Mr. Kim , Mr. Luj\u00e1n , Mr. Merkley , Mr. Peters , Mr. Sanders , Mr. Schatz , Mrs. Shaheen , Mr. Van Hollen , Mr. Warner , Mr. Welch , Ms. Smith , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide appropriations for the Internal Revenue Service to overhaul technology and strengthen enforcement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Corporations and High Earners from Avoiding Taxes and Enforce the Rules Strictly Act or the Stop CHEATERS Act .\n#### 2. Additional appropriations for the Internal Revenue Service\n##### (a) Enforcement\nIn addition to other amounts, there is appropriated the following amounts for necessary expenses for tax enforcement activities of the Internal Revenue Service to pursue the objectives described in section 3(a)(1), including to determine and collect owed taxes, to provide legal and litigation support, to conduct criminal investigations, to enforce criminal statutes related to violations of internal revenue laws and other financial crimes, to purchase and hire passenger motor vehicles ( 31 U.S.C. 1343(b) ), and to provide other services as authorized by 5 U.S.C. 3109 , at such rates as may be determined by the Commissioner:\n**(1)**\nFor fiscal year 2026, $3,600,000,000.\n**(2)**\nFor fiscal year 2027, $5,000,000,000.\n**(3)**\nFor fiscal year 2028, $6,500,000,000.\n**(4)**\nFor fiscal year 2029, $8,200,000,000.\n**(5)**\nFor fiscal year 2030, $10,100,000,000.\n**(6)**\nFor fiscal year 2031, $12,200,000,000.\n##### (b) Taxpayer services\nIn addition to other amounts, there are appropriated the following amounts to provide taxpayer services, including pre-filing assistance and education, filing and account services, and taxpayer advocacy services:\n**(1)**\nFor fiscal year 2026, $1,400,000,000.\n**(2)**\nFor fiscal year 2027, $1,600,000,000.\n**(3)**\nFor fiscal year 2028, $1,600,000,000.\n**(4)**\nFor fiscal year 2029, $1,600,000,000.\n**(5)**\nFor fiscal year 2030, $1,700,000,000.\n**(6)**\nFor fiscal year 2031, $1,700,000,000.\n##### (c) Technology and operations support\nThere are appropriated the following additional amounts for the Department of the Treasury\u2014Internal Revenue Service\u2014Operations Support account to overhaul outdated technology of the Internal Revenue Service and improve the capacity of the Internal Revenue Service to detect fraud and noncompliance:\n**(1)**\nFor fiscal year 2026, $900,000,000.\n**(2)**\nFor fiscal year 2027, $4,500,000,000.\n**(3)**\nFor fiscal year 2028, $4,500,000,000.\n**(4)**\nFor fiscal year 2029, $4,800,000,000.\n**(5)**\nFor fiscal year 2030, $4,800,000,000.\n**(6)**\nFor fiscal year 2031, $5,900,000,000.\n##### (d) Business systems modernization\nThere are appropriated the following additional amounts for necessary expenses of the Internal Revenue Service\u2019s business systems modernization program, but not including the operation and maintenance of legacy systems:\n**(1)**\nFor fiscal year 2026, $1,000,000,000.\n**(2)**\nFor fiscal year 2027, $900,000,000.\n**(3)**\nFor fiscal year 2028, $300,000,000.\n**(4)**\nFor fiscal year 2029, $300,000,000.\n**(5)**\nFor fiscal year 2030, $300,000,000.\n**(6)**\nFor fiscal year 2031, $300,000,000.\n##### (e) Availability\nEach additional amount appropriated by this section shall remain available until expended.\n#### 3. Reports to Congress\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act and every 2 years thereafter, the Commissioner of Internal Revenue shall submit to Congress a report containing\u2014\n**(1)**\na comprehensive description of\u2014\n**(A)**\na plan to\u2014\n**(i)**\nshift more of the auditing and enforcement assets of the Internal Revenue Service toward high-income individuals and large corporations,\n**(ii)**\nrecruit and retain auditors with the skills essential to audit high-income individuals and large corporations, and\n**(iii)**\nincrease voluntary compliance among high-income individuals and large corporations, and\n**(B)**\nthe progress made in implementing such plan, and\n**(2)**\nan analysis of how much of the difference between tax liabilities owed to the United States under the Internal Revenue Code of 1986 and those liabilities actually collected by the Internal Revenue Service are attributable to taxpayers at different income levels, including high-income individuals and large corporations.\n##### (b) Inspector general\nNot later than 1 year after the first report is submitted under subsection (a) and every 2 years thereafter, the Treasury Inspector General for Tax Administration shall submit to Congress a report evaluating the plan described in subsection (a)(1) and the progress made by the Internal Revenue Service in implementing such plan.",
      "versionDate": "2026-04-15",
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
        "name": "Taxation",
        "updateDate": "2026-05-07T12:23:49Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4298is.xml"
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
      "title": "Stop CHEATERS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop CHEATERS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Corporations and High Earners from Avoiding Taxes and Enforce the Rules Strictly Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide appropriations for the Internal Revenue Service to overhaul technology and strengthen enforcement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:46Z"
    }
  ]
}
```
