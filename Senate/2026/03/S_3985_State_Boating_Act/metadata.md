# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3985?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3985
- Title: State Boating Act
- Congress: 119
- Bill type: S
- Bill number: 3985
- Origin chamber: Senate
- Introduced date: 2026-03-04
- Update date: 2026-05-08T20:39:39Z
- Update date including text: 2026-05-08T20:39:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in Senate
- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-03-04: Introduced in Senate

## Actions

- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3985",
    "number": "3985",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C000880",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Crapo, Mike [R-ID]",
        "lastName": "Crapo",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "State Boating Act",
    "type": "S",
    "updateDate": "2026-05-08T20:39:39Z",
    "updateDateIncludingText": "2026-05-08T20:39:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T17:38:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "VT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-03-10",
      "state": "ID"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3985is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3985\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2026 Mr. Crapo (for himself and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo allow States to require payment of State fees related to boating as a condition for issuance of a vessel number and to collect such fees in conjunction with other fees related to vessel numbering.\n#### 1. Short title\nThis Act may be cited as the State Boating Act .\n#### 2. Collection of state fees related to boating\nSection 12307 of title 46, United States Code, is amended\u2014\n**(1)**\nin the matter preceding paragraph (1)\u2014\n**(A)**\nby striking The authority and inserting (a) In general.\u2014 The authority ; and\n**(B)**\nby striking that are\u2014 and inserting that\u2014 ;\n**(2)**\nin paragraph (1)\u2014\n**(A)**\nby inserting are before prescribed ; and\n**(B)**\nby striking ; or and inserting a semicolon;\n**(3)**\nin paragraph (2)\u2014\n**(A)**\nby inserting are before related ; and\n**(B)**\nby striking the period and inserting ; or ; and\n**(4)**\nby adding at the end the following:\n(3) require the payment of State fees related to boating, which may include fees for search and rescue operations, boating safety measures, or efforts to address aquatic invasive species. (b) State fees related to boating A State issuing authority may collect a fee described in subsection (a)(3) in conjunction with the collection of any other fee established under this section. (c) Use of fees Fees collected by States under the authority of this section may only be used to fund activities directly related to improving recreational boating, boater safety, boater access, use of waterways by recreational boaters, and aquatic invasive species mitigation. .",
      "versionDate": "2026-03-04",
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
        "actionDate": "2026-04-28",
        "text": "Referred to the House Committee on Transportation and Infrastructure."
      },
      "number": "8550",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To allow States to require payment of State fees related to boating as a condition for issuance of a vessel number and to collect such fees in conjunction with other fees related to vessel numbering.",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-03-20T15:19:49Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3985is.xml"
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
      "title": "State Boating Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "State Boating Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to allow States to require payment of State fees related to boating as a condition for issuance of a vessel number and to collect such fees in conjunction with other fees related to vessel numbering.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:30Z"
    }
  ]
}
```
