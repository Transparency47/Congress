# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1335?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1335
- Title: Secure Family Futures Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1335
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2026-02-05T12:03:16Z
- Update date including text: 2026-02-05T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1335",
    "number": "1335",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Secure Family Futures Act of 2025",
    "type": "S",
    "updateDate": "2026-02-05T12:03:16Z",
    "updateDateIncludingText": "2026-02-05T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
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
            "date": "2025-04-08T17:21:18Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-08T17:21:18Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "GA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "TN"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "VA"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "IA"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "IN"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "IN"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1335is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1335\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. Tillis (for himself and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude debt held by certain insurance companies from capital assets and to extend capital loss carryovers for such companies from 5 years to 10 years.\n#### 1. Short title\nThis Act may be cited as the Secure Family Futures Act of 2025 .\n#### 2. Debt not treated as capital asset for applicable insurance companies\n##### (a) Exclusion from capital assets\nSection 1221(a) of the Internal Revenue Code of 1986 is amended by striking or at the end of paragraph (7), by striking the period at the end of paragraph (8) and inserting ; or , and by adding at the end the following new paragraph:\n(9) any note, bond, debenture, or other evidence of indebtedness held by an applicable insurance company. .\n##### (b) Applicable insurance company defined\nSection 1221(b) of such Code is amended by redesignating paragraph (4) as paragraph (5) and by inserting after paragraph (3) the following new paragraph:\n(4) Applicable insurance company For purposes of subsection (a)(9), the term applicable insurance company means, with respect to any taxable year\u2014 (A) any insurance company other than an insurance company\u2014 (i) with respect to which an election is in effect under section 831(b)(2)(A)(iii) or 835(a) for such taxable year, (ii) which is a foreign corporation described in section 842, or (iii) which is an organization to which section 833 applies for such taxable year, or (B) a face-amount certificate company registered under the Investment Company Act of 1940. .\n##### (c) Effective date\nThe amendments made by this section shall apply to notes, bonds, debentures, or other evidence of indebtedness acquired by an applicable insurance company (as defined in section 1221(b)(4)) of such Code after December 31, 2025.\n#### 3. Capital loss carryovers incurred by applicable insurance companies allowed for 10 years\n##### (a) In general\nSection 1212(a)(1)(C) of the Internal Revenue Code of 1986 is amended to read as follows:\n(C) a capital loss carryover to each of the 10 taxable years succeeding the loss year, but only to the extent such loss\u2014 (i) is attributable to a foreign expropriation loss, or (ii) was incurred by an applicable insurance company (as defined in section 1221(b)(4)). .\n##### (b) Effective date\nThe amendment made by this section shall apply to net capital losses arising in taxable years beginning after December 31, 2025.",
      "versionDate": "2025-04-08",
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
        "actionDate": "2025-04-01",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2547",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Secure Family Futures Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-05-09T17:44:53Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1335is.xml"
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
      "title": "Secure Family Futures Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Secure Family Futures Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude debt held by certain insurance companies from capital assets and to extend capital loss carryovers for such companies from 5 years to 10 years.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:18Z"
    }
  ]
}
```
