# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/627?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/627
- Title: ENABLE Act
- Congress: 119
- Bill type: S
- Bill number: 627
- Origin chamber: Senate
- Introduced date: 2025-02-19
- Update date: 2025-12-05T21:44:54Z
- Update date including text: 2025-12-05T21:44:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-19: Introduced in Senate
- 2025-02-19 - IntroReferral: Introduced in Senate
- 2025-02-19 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-19: Introduced in Senate

## Actions

- 2025-02-19 - IntroReferral: Introduced in Senate
- 2025-02-19 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-19",
    "latestAction": {
      "actionDate": "2025-02-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/627",
    "number": "627",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "ENABLE Act",
    "type": "S",
    "updateDate": "2025-12-05T21:44:54Z",
    "updateDateIncludingText": "2025-12-05T21:44:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-19",
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
      "actionDate": "2025-02-19",
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
          "date": "2025-02-19T17:39:24Z",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "MD"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "AR"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "AL"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "VA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "AL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "MN"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "DE"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "KS"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "NC"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "PA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "GA"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "AK"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "AZ"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "UT"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "GA"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s627is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 627\nIN THE SENATE OF THE UNITED STATES\nFebruary 19, 2025 Mr. Schmitt (for himself, Mr. Van Hollen , Mr. Boozman , Mr. Tuberville , Mr. Kaine , Mrs. Britt , Ms. Klobuchar , Mr. Coons , Mr. Moran , Mr. Tillis , Mr. Fetterman , Mr. Warnock , Mr. Sullivan , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to make certain provisions with respect to qualified ABLE programs permanent.\n#### 1. Short title\nThis Act may be cited as the Ensuring Nationwide Access to a Better Life Experience Act or the ENABLE Act .\n#### 2. Permanent extension of increased contributions to ABLE accounts\n##### (a) In general\nSection 529A(b)(2)(B)(ii) of the Internal Revenue Code of 1986 is amended by striking before January 1, 2026 .\n##### (b) Allowance of savers credit\n**(1) In general**\nSection 25B(d)(1) of the Internal Revenue Code of 1986 is amended to read as follows:\n(1) In general The term qualified retirement savings contributions means, with respect to any taxable year, the sum of\u2014 (A) the amount of contributions made by the eligible individual during such taxable year to the ABLE account (within the meaning of section 529A) of which such individual is the eligible beneficiary, and (B) in the case of any taxable year beginning before January 1, 2027\u2014 (i) the amount of the qualified retirement contributions (as defined in section 219(e)) made by the eligible individual, (ii) the amount of\u2014 (I) any elective deferrals (as defined in section 402(g)(3)) of such individual, and (II) any elective deferral of compensation by such individual under an eligible deferred compensation plan (as defined in section 457(b)) of an eligible employer described in section 457(e)(1)(A), and (iii) the amount of voluntary employee contributions by such individual to any qualified retirement plan (as defined in section 4974(c)). .\n**(2) Coordination with SECURE 2.0 Act of 2022 amendment**\nParagraph (1) of section 103(e) of the SECURE 2.0 Act of 2022 is repealed, and the Internal Revenue Code of 1986 shall be applied and administered as though such paragraph were never enacted.\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years ending after the date of the enactment of this Act.\n#### 3. Permanent extension of rollovers to ABLE programs from 529 programs\n##### (a) In general\nSection 529(c)(3)(C)(i)(III) of the Internal Revenue Code of 1986 is amended by striking before January 1, 2026, .\n##### (b) Effective date\nThe amendment made by this section shall apply to distributions made after the date of the enactment of this Act.",
      "versionDate": "2025-02-19",
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
        "actionDate": "2025-02-18",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1436",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ENABLE Act",
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
        "updateDate": "2025-05-06T14:11:20Z"
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
      "date": "2025-02-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s627is.xml"
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
      "title": "ENABLE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ENABLE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Nationwide Access to a Better Life Experience Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to make certain provisions with respect to qualified ABLE programs permanent.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:21Z"
    }
  ]
}
```
