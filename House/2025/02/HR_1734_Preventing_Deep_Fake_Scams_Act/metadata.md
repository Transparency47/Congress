# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1734?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1734
- Title: Preventing Deep Fake Scams Act
- Congress: 119
- Bill type: HR
- Bill number: 1734
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-04-14T08:05:37Z
- Update date including text: 2026-04-14T08:05:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1734",
    "number": "1734",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "P000620",
        "district": "7",
        "firstName": "Brittany",
        "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
        "lastName": "Pettersen",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Preventing Deep Fake Scams Act",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:37Z",
    "updateDateIncludingText": "2026-04-14T08:05:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "NE"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "OR"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "PA"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NY"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "NY"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "IA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NJ"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "PA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1734ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1734\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Ms. Pettersen (for herself, Mr. Flood , Ms. Bonamici , Mr. Fitzpatrick , Ms. Ocasio-Cortez , and Mr. Harder of California ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo establish the Task Force on Artificial Intelligence in the Financial Services Sector to report to Congress on issues related to artificial intelligence in the financial services sector, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Deep Fake Scams Act .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nArtificial intelligence is being used in new and innovative ways by the financial services sector.\n**(2)**\nArtificial intelligence may provide benefits to banks, credit unions, and banking consumers.\n**(3)**\nArtificial intelligence poses unique threats to the safety and security of customer accounts.\n**(4)**\nVoice banking is offered by many banks for security and convenience reasons.\n**(5)**\nThe popularity of social media has made video and audio of potential targets easier to obtain for bad actors. These materials can be exploited to replicate the voices and appearances of other people in pursuit of data theft, identity theft, or fraud.\n**(6)**\nBad actors could utilize deep fakes , including voice and audio manipulation, to compromise and access a consumer\u2019s financial accounts.\n#### 3. Task Force on Artificial Intelligence in the Financial Services Sector\n##### (a) Establishment\nThere is established a Task Force on Artificial Intelligence in the Financial Services Sector (in this section referred to as the Task Force ).\n##### (b) Membership\nThe Task Force shall consist of the following:\n**(1)**\nThe Secretary of the Treasury, or a designee, who shall serve as Chair of the Task Force.\n**(2)**\nThe Comptroller of the Currency, or a designee.\n**(3)**\nThe Chairman of the Board of Governors of the Federal Reserve System, or a designee.\n**(4)**\nThe Chairperson of the Federal Deposit Insurance Corporation, or a designee.\n**(5)**\nThe Director of the Bureau of Consumer Financial Protection, or a designee.\n**(6)**\nThe Chairman of the National Credit Union Administration, or a designee.\n**(7)**\nThe Director of the Financial Crimes Enforcement Network, or a designee.\n##### (c) Report\n**(1) In general**\nNot later than the end of the 1-year period beginning on the date of enactment of this Act, the Task Force shall issue a report to Congress containing the contents described in paragraph (3).\n**(2) Consultation**\n**(A) Request for Information**\nNot later than 90 days after the date of enactment of this Act, the Task Force shall solicit public feedback on the report required under paragraph (1).\n**(B) Industry and expert stakeholders**\nIn developing the report required under paragraph (1), the Task Force shall seek out and consult with industry and expert stakeholders, including\u2014\n**(i)**\ndepository institutions of varying asset sizes;\n**(ii)**\ncredit unions of varying asset sizes;\n**(iii)**\nthird-party vendors who use artificial intelligence when providing services to depository institutions and credit unions; and\n**(iv)**\nartificial intelligence experts.\n**(3) Contents**\nThe contents of the report are the following:\n**(A)**\nA description of how banks and credit unions proactively protect themselves and consumers from fraud utilizing artificial intelligence.\n**(B)**\nA list of standard definitions for the different manners in which artificial intelligence is used, including terms like generative AI , machine learning , natural language processing , algorithmic AI , and deep fakes .\n**(C)**\nA description of potential risks that could result from the use of artificial intelligence by bad actors to steal consumers\u2019 data, steal consumers\u2019 identities, and commit fraud.\n**(D)**\nA list of best practices for financial institutions to protect their customers from attempts to steal consumer data, steal consumers\u2019 identities, or commit fraud.\n**(E)**\nLegislative and regulatory recommendations for the regulation of artificial intelligence and to protect consumers from data theft, identity theft, and fraud.\n##### (d) Termination\nThe Task Force shall terminate 90 days after the final report is issued pursuant to subsection (c).",
      "versionDate": "2025-02-27",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-18",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2117",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Preventing Deep Fake Scams Act",
      "type": "S"
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
        "updateDate": "2025-03-21T15:53:56Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1734ih.xml"
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
      "title": "Preventing Deep Fake Scams Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:11Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Deep Fake Scams Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Task Force on Artificial Intelligence in the Financial Services Sector to report to Congress on issues related to artificial intelligence in the financial services sector, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T03:48:19Z"
    }
  ]
}
```
