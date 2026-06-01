# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3611?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3611
- Title: Blockchain Regulatory Certainty Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3611
- Origin chamber: Senate
- Introduced date: 2026-01-12
- Update date: 2026-02-05T16:27:28Z
- Update date including text: 2026-02-05T16:27:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-12: Introduced in Senate
- 2026-01-12 - IntroReferral: Introduced in Senate
- 2026-01-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-01-12: Introduced in Senate

## Actions

- 2026-01-12 - IntroReferral: Introduced in Senate
- 2026-01-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-12",
    "latestAction": {
      "actionDate": "2026-01-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3611",
    "number": "3611",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Blockchain Regulatory Certainty Act of 2026",
    "type": "S",
    "updateDate": "2026-02-05T16:27:28Z",
    "updateDateIncludingText": "2026-02-05T16:27:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-12",
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
      "actionDate": "2026-01-12",
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
          "date": "2026-01-12T21:17:15Z",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3611is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3611\nIN THE SENATE OF THE UNITED STATES\nJanuary 12, 2026 Ms. Lummis (for herself and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo clarify the treatment of certain non-controlling developers or providers of distributed ledger services involved in digital assets with respect to money transmission laws, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Blockchain Regulatory Certainty Act of 2026 .\n#### 2. Treatment of certain non-controlling developers with respect to money transmission laws\n##### (a) Definitions\nIn this section:\n**(1) Developer or provider**\nThe term developer or provider means any person or business that creates or publishes software to facilitate the creation of, or provide maintenance to, a distributed ledger, or a service associated with a distributed ledger.\n**(2) Digital asset**\nThe term digital asset means any digital representation of value which is recorded on a cryptographically secured distributed ledger.\n**(3) Distributed ledger**\nThe term distributed ledger means technology in which data is shared across a network that\u2014\n**(A)**\ncreates a public digital ledger of verified transactions or information among network participants; and\n**(B)**\nuses cryptography to link the data to maintain the integrity of the public ledger and execute other functions.\n**(4) Distributed ledger service**\nThe term distributed ledger service means any information, transaction, or computing service or system that provides or enables access to a distributed ledger system by multiple users, including a service or system that enables users to send, receive, exchange, or store digital assets described by distributed ledger systems.\n**(5) Non-controlling developer or provider**\nThe term non-controlling developer or provider means a developer or provider of a distributed ledger service that, in the regular course of operations, does not have the legal right or the unilateral and independent ability to control, initiate upon demand, or effectuate transactions involving digital assets to which users are entitled, without the approval, consent, or direction of any other third party.\n##### (b) Treatment\nNotwithstanding any other provision of law, a non-controlling developer or provider\u2014\n**(1)**\nshall not be treated as\u2014\n**(A)**\na money transmitting business, as defined in section 5330 of title 31, United States Code, and the regulations promulgated under that section; or\n**(B)**\nengaged in money transmitting, as defined in section 1960 of title 18, United States Code, as amended by this Act; and\n**(2)**\non or after the date of enactment of this Act, shall not be otherwise subject to any registration requirement that is substantially similar to a requirement (as in effect on the day before the date of enactment of this Act) that applies to an entity described in subparagraph (A) or (B) of paragraph (1), solely on the basis of\u2014\n**(A)**\ncreating or publishing software to facilitate the creation of, or providing maintenance services to, a distributed ledger or a service associated with a distributed ledger;\n**(B)**\nproviding hardware or software to facilitate a customer\u2019s own custody or safekeeping of the digital assets of the customer; or\n**(C)**\nproviding infrastructure support to maintain a distributed ledger service.\n##### (c) Rules of construction\nNothing in this section may be construed\u2014\n**(1)**\nto affect whether a developer or provider of a blockchain service is otherwise subject to classification or treatment as a money transmitter, or as engaged in money transmitting, under applicable Federal or State law, including laws relating to anti-money laundering or countering the financing of terrorism, based on conduct outside the scope of subsection (b);\n**(2)**\nto affect whether a developer or provider is otherwise subject to classification or treatment as a financial institution under subchapter II of chapter 53 of title 31, United States Code, this Act, any amendment made by this Act, or any Act enacted after the date of enactment of this Act;\n**(3)**\nto limit or expand any law pertaining to intellectual property;\n**(4)**\nto prevent any State from enforcing any State law that is consistent with this section; or\n**(5)**\nto create a cause of action or impose liability under any State or local law that is inconsistent with this section.",
      "versionDate": "2026-01-12",
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
        "updateDate": "2026-02-05T16:27:28Z"
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
      "date": "2026-01-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3611is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to clarify the treatment of certain non-controlling developers or providers of distributed ledger services involved in digital assets with respect to money transmission laws, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:49Z"
    },
    {
      "title": "Blockchain Regulatory Certainty Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T10:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Blockchain Regulatory Certainty Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T10:53:15Z"
    }
  ]
}
```
