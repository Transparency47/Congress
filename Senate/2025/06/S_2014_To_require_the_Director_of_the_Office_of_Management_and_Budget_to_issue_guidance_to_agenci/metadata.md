# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2014?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2014
- Title: Special District Fairness and Accessibility Act
- Congress: 119
- Bill type: S
- Bill number: 2014
- Origin chamber: Senate
- Introduced date: 2025-06-10
- Update date: 2026-05-01T11:03:33Z
- Update date including text: 2026-05-01T11:03:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in Senate
- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-06-10: Introduced in Senate

## Actions

- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2014",
    "number": "2014",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Special District Fairness and Accessibility Act",
    "type": "S",
    "updateDate": "2026-05-01T11:03:33Z",
    "updateDateIncludingText": "2026-05-01T11:03:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-10",
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
        "item": [
          {
            "date": "2025-06-10T18:52:14Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-10T18:52:14Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "OR"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "OH"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "AZ"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2014is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2014\nIN THE SENATE OF THE UNITED STATES\nJune 10, 2025 Mr. Cornyn (for himself, Mr. Merkley , Mr. Moreno , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the Director of the Office of Management and Budget to issue guidance to agencies requiring special districts to be recognized as local government for the purpose of Federal financial assistance determinations.\n#### 1. Short title\nThis Act may be cited as the Special District Fairness and Accessibility Act .\n#### 2. Agency financial assistance guidance on special districts\n##### (a) Requirements for agency acknowledgment of special districts as grant recipients\n**(1) OMB guidance**\nNot later than 180 days after the date of the enactment of this Act, the Director shall issue guidance that clarifies how an agency recognizes a special district as a unit of local government for the purpose of being eligible to receive Federal financial assistance.\n**(2) Agency requirements**\nNot later than 1 year after the date on which the guidance is issued pursuant to paragraph (1), the head of each agency shall implement the requirements of such guidance and conform any policy, principle, practice, procedure, or guideline relating to the administration of the Federal financial assistance programs of the agency.\n**(3) Reporting requirement**\nNot later than 2 years after the date of the enactment of this Act, the Director shall submit to the Committee on Oversight and Government Reform of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report that evaluates agency implementation of and conformity to the guidance issued pursuant to paragraph (1).\n##### (b) Definitions\nIn this section:\n**(1) Agency**\nThe term agency has the meaning given the term in section 552 of title 5, United States Code.\n**(2) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(3) Federal financial assistance**\nThe term Federal financial assistance \u2014\n**(A)**\nmeans assistance that a non-Federal entity receives or administers in the form of a grant, loan, loan guarantee, property, cooperative agreement, interest subsidy, insurance, food commodity, direct appropriation, or other assistance; and\n**(B)**\ndoes not include an amount received as reimbursement for services rendered to an individual in accordance with guidance issued by the Director.\n**(4) Special district**\nThe term special district means a political subdivision of a State, with specified boundaries and significant budgetary autonomy or control, created by or pursuant to the laws of the State, for the purpose of performing limited and specific governmental or proprietary functions that distinguish it as a significantly separate entity from the administrative governance structure of any other form of local government unit within a State.\n**(5) State**\nThe term State means each of the several States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.",
      "versionDate": "2025-06-10",
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
        "actionDate": "2026-03-18",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 32 - 8."
      },
      "number": "2766",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Special District Fairness and Accessibility Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-04-06T17:52:25Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-06T17:52:25Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-06T17:52:25Z"
          },
          {
            "name": "Office of Management and Budget (OMB)",
            "updateDate": "2026-04-06T17:52:25Z"
          },
          {
            "name": "Political representation",
            "updateDate": "2026-04-06T17:52:25Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-04-06T17:52:25Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-07-21T20:15:26Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2014is.xml"
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
      "title": "Special District Fairness and Accessibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T11:03:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Special District Fairness and Accessibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Director of the Office of Management and Budget to issue guidance to agencies requiring special districts to be recognized as local government for the purpose of Federal financial assistance determinations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:33:21Z"
    }
  ]
}
```
