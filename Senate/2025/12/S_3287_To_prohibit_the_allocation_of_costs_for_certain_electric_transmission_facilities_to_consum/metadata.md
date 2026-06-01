# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3287?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3287
- Title: Fair Allocation of Interstate Rates Act
- Congress: 119
- Bill type: S
- Bill number: 3287
- Origin chamber: Senate
- Introduced date: 2025-12-01
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in Senate
- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-12-01: Introduced in Senate

## Actions

- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3287",
    "number": "3287",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Fair Allocation of Interstate Rates Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:45Z"
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
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-01",
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
            "date": "2025-12-01T23:33:11Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-01T23:33:11Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "ND"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3287is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3287\nIN THE SENATE OF THE UNITED STATES\nDecember 1, 2025 Mr. Cramer (for himself and Mr. Hoeven ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo prohibit the allocation of costs for certain electric transmission facilities to consumers in a State the public officials of which did not expressly consent to the transmission facility, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Allocation of Interstate Rates Act .\n#### 2. Rates and charges\nSection 205 of the Federal Power Act ( 16 U.S.C. 824d ) is amended by adding at the end the following:\n(h) Prohibition on allocation of certain costs (1) Definitions In this subsection: (A) Covered policy The term covered policy means a policy of a State, including any policy of a local political entity of a State. (B) Covered transmission facility The term covered transmission facility means any facility, line, equipment, or system used for the transmission of electric energy in interstate commerce that is planned, constructed, or operated in whole or in part to implement a covered policy. (2) Prohibition Except as provided in paragraph (3), a transmission provider providing electric service to consumers in 2 or more States may not allocate costs for a covered transmission facility to a consumer served by that transmission provider if\u2014 (A) the basis for construction or implementation of the covered transmission facility is, in whole or in part, to implement a covered policy of a State; and (B) the consumer is not a resident of the State the covered policy of which is the basis for constructing or implementing the covered transmission facility. (3) Exception A transmission provider providing electric service to consumers in 2 or more States may allocate costs for a covered transmission facility to a consumer described in paragraph (2)(B) if the State in which that consumer is a resident, or a designated public official of that State, expressly consents to such allocation of costs. (4) Presumptions It shall be presumed that\u2014 (A) the benefits of a covered transmission facility accrue solely to the cost causers of that covered transmission facility; (B) any consumer who is a resident of a State that implements a covered policy that is, in whole or in part, the basis for constructing or implementing a covered transmission facility is a cost causer for purposes of subparagraph (A); and (C) any consumer that does not reside in the State described in subparagraph (B) is not a cost causer for purposes of subparagraph (A). (5) Implementation Not later than 180 days after the date of enactment of this subsection, the Commission shall issue such rules and regulations as are necessary to implement this subsection. .",
      "versionDate": "2025-12-01",
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
        "name": "Energy",
        "updateDate": "2025-12-18T17:07:29Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3287is.xml"
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
      "title": "Fair Allocation of Interstate Rates Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Allocation of Interstate Rates Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T06:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the allocation of costs for certain electric transmission facilities to consumers in a State the public officials of which did not expressly consent to the transmission facility, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T06:18:34Z"
    }
  ]
}
```
