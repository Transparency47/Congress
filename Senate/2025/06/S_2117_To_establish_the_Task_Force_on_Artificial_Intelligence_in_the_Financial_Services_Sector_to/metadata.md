# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2117?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2117
- Title: Preventing Deep Fake Scams Act
- Congress: 119
- Bill type: S
- Bill number: 2117
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2025-12-05T22:52:41Z
- Update date including text: 2025-12-05T22:52:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2117",
    "number": "2117",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Preventing Deep Fake Scams Act",
    "type": "S",
    "updateDate": "2025-12-05T22:52:41Z",
    "updateDateIncludingText": "2025-12-05T22:52:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
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
      "actionDate": "2025-06-18",
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
          "date": "2025-06-18T16:47:35Z",
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
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2117is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2117\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Husted (for himself and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo establish the Task Force on Artificial Intelligence in the Financial Services Sector to report to Congress on issues related to artificial intelligence in the financial services sector, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Deep Fake Scams Act .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nArtificial intelligence is being used in new and innovative ways by the financial services sector.\n**(2)**\nArtificial intelligence may provide benefits to banks, credit unions, and banking consumers.\n**(3)**\nArtificial intelligence poses unique threats to the safety and security of customer accounts.\n**(4)**\nVoice banking is offered by many banks for security and convenience reasons.\n**(5)**\nThe popularity of social media has made video and audio of potential targets easier to obtain for bad actors. These materials can be exploited to replicate the voices and appearances of other people in pursuit of data theft, identity theft, or fraud.\n**(6)**\nBad actors could utilize deep fakes, including voice and audio manipulation, to compromise and access the financial accounts of a consumer.\n#### 3. Task Force on Artificial Intelligence in the Financial Services Sector\n##### (a) Establishment\nThere is established a Task Force on Artificial Intelligence in the Financial Services Sector (in this section referred to as the Task Force ).\n##### (b) Membership\nThe Task Force shall consist of the following:\n**(1)**\nThe Secretary of the Treasury, or a designee, who shall serve as Chair of the Task Force.\n**(2)**\nThe Comptroller of the Currency, or a designee.\n**(3)**\nThe Chairman of the Board of Governors of the Federal Reserve System, or a designee.\n**(4)**\nThe Chairperson of the Federal Deposit Insurance Corporation, or a designee.\n**(5)**\nThe Director of the Bureau of Consumer Financial Protection, or a designee.\n**(6)**\nThe Chairman of the National Credit Union Administration, or a designee.\n**(7)**\nThe Director of the Financial Crimes Enforcement Network, or a designee.\n##### (c) Report\n**(1) In general**\nNot later than the end of the 1-year period beginning on the date of enactment of this Act, the Task Force shall submit to Congress a report containing the contents described in paragraph (3).\n**(2) Consultation**\n**(A) Request for Information**\nNot later than 90 days after the date of enactment of this Act, the Task Force shall solicit public feedback on the report required under paragraph (1).\n**(B) Industry and expert stakeholders**\nIn developing the report required under paragraph (1), the Task Force shall seek out and consult with industry and expert stakeholders, including\u2014\n**(i)**\ndepository institutions of varying asset sizes;\n**(ii)**\ncredit unions of varying asset sizes;\n**(iii)**\nthird-party vendors who use artificial intelligence when providing services to depository institutions and credit unions; and\n**(iv)**\nartificial intelligence experts.\n**(3) Contents**\nThe contents of the report described in this paragraph are as follows:\n**(A)**\nA description of how banks and credit unions proactively protect themselves and consumers from fraud utilizing artificial intelligence.\n**(B)**\nA list of standard definitions for the different manners in which artificial intelligence is used, including terms like generative AI , machine learning , natural language processing , algorithmic AI , and deep fakes .\n**(C)**\nA description of potential risks that could result from the use of artificial intelligence by bad actors to steal data and identities of consumers and commit fraud.\n**(D)**\nA list of best practices for financial institutions to protect their customers from attempts to steal data and identities of consumers or commit fraud.\n**(E)**\nLegislative and regulatory recommendations for the regulation of artificial intelligence and to protect consumers from data theft, identity theft, and fraud.\n##### (d) Termination\nThe Task Force shall terminate on the date that is 90 days after the date on which the final report is issued pursuant to subsection (c).",
      "versionDate": "2025-06-18",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-02-27",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "1734",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Preventing Deep Fake Scams Act",
      "type": "HR"
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
        "updateDate": "2025-07-14T14:15:10Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2117is.xml"
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
      "title": "Preventing Deep Fake Scams Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-02T01:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing Deep Fake Scams Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Task Force on Artificial Intelligence in the Financial Services Sector to report to Congress on issues related to artificial intelligence in the financial services sector, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:34:10Z"
    }
  ]
}
```
