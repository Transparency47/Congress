# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4157?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4157
- Title: No Bailout for Crypto Act
- Congress: 119
- Bill type: S
- Bill number: 4157
- Origin chamber: Senate
- Introduced date: 2026-03-19
- Update date: 2026-04-01T15:51:57Z
- Update date including text: 2026-04-01T15:51:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in Senate
- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S1380)
- Latest action: 2026-03-19: Introduced in Senate

## Actions

- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S1380)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4157",
    "number": "4157",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "No Bailout for Crypto Act",
    "type": "S",
    "updateDate": "2026-04-01T15:51:57Z",
    "updateDateIncludingText": "2026-04-01T15:51:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S1380)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-20T00:05:24Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "VT"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-03-19",
      "state": "VT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MN"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "HI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-20",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4157is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4157\nIN THE SENATE OF THE UNITED STATES\nMarch 19, 2026 Mr. Durbin (for himself, Ms. Warren , Mr. Welch , Mr. Sanders , Ms. Smith , and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo prohibit bailouts of digital asset market participants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Bailout for Crypto Act .\n#### 2. Prohibition on bailouts of digital asset market participants\n##### (a) Definitions\nIn this section:\n**(1) Blockchain**\nThe term blockchain means technology\u2014\n**(A)**\nthrough which data is shared across a network that creates a public blockchain of verified transactions or information among network participants; and\n**(B)**\nin which cryptography is used to link the data described in subparagraph (A)\u2014\n**(i)**\nto maintain the integrity of the blockchain described in that subparagraph; and\n**(ii)**\nto execute other functions.\n**(2) Decentralized finance trading protocol**\nThe term decentralized finance trading protocol means a blockchain system through which multiple participants can execute a financial transaction\u2014\n**(A)**\nin accordance with an automated rule or algorithm that is predetermined and non-discretionary; and\n**(B)**\nwithout reliance on any other person to maintain control of the digital assets of the user during any part of the financial transaction.\n**(3) Digital asset intermediary**\nThe term digital asset intermediary means any person that provides services that are financial in nature, as defined in section 4(k)(4) of the Bank Holding Company Act ( 12 U.S.C. 1843(k)(4) ), with respect to any digital asset.\n**(4) Financial service provider**\nThe term financial service provider means a financial service provider that is regulated by a Federal banking agency, as defined in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ).\n**(5) GENIUS Act terms**\nThe terms digital asset , digital asset service provider , and distributed ledger protocol have the meanings given those terms, respectively, in section 2 of the GENIUS Act ( 12 U.S.C. 5901 ).\n##### (b) Prohibition on financial assistance\nA Federal agency may not provide financial assistance to a digital asset intermediary, digital asset service provider, distributed ledger protocol, decentralized finance trading protocol, or financial service provider with respect to digital asset activities, to prevent the failure or bankruptcy of the digital asset commodity intermediary.\n##### (c) Emergency liquidity facilities\nA digital asset intermediary, digital asset service provider, distributed ledger protocol, decentralized finance trading protocol, or financial service provider with respect to digital asset activities may not have access to any emergency liquidity facility established under section 13(3) of the Federal Reserve Act ( 12 U.S.C. 343 ).\n##### (d) Exchange Stabilization Fund\nThe Secretary of the Treasury may not use any amounts in the Exchange Stabilization Fund established under section 5302 of title 31, United States Code, for the benefit of any digital asset intermediary, digital asset service provider, distributed ledger protocol, decentralized finance trading protocol or financial service provider with respect to digital asset activities.\n##### (e) Rule of construction\nThe prohibition under subsection (b) shall not alter the Federal Reserve\u2019s authority to lend to depository institutions under section 10B of the Federal Reserve Act ( 12 U.S.C. 347b ).",
      "versionDate": "2026-03-19",
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
        "updateDate": "2026-04-01T15:51:56Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4157is.xml"
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
      "title": "No Bailout for Crypto Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T02:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Bailout for Crypto Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-27T02:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit bailouts of digital asset market participants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-27T02:48:23Z"
    }
  ]
}
```
