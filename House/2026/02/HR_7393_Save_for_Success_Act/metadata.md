# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7393?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7393
- Title: Save for Success Act
- Congress: 119
- Bill type: HR
- Bill number: 7393
- Origin chamber: House
- Introduced date: 2026-02-05
- Update date: 2026-03-26T08:06:36Z
- Update date including text: 2026-03-26T08:06:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-05: Introduced in House

## Actions

- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7393",
    "number": "7393",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "P000622",
        "district": "1",
        "firstName": "Jimmy",
        "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
        "lastName": "Patronis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Save for Success Act",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:36Z",
    "updateDateIncludingText": "2026-03-26T08:06:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-05",
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
          "date": "2026-02-05T15:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7393ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7393\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2026 Mr. Patronis (for himself and Mr. Bilirakis ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow distributions from qualified tuition programs for qualified housing expenses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Save for Success Act .\n#### 2. Allowance of distributions from qualified tuition programs for qualified housing expenses\n##### (a) In general\nSection 529(c)(3) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(F) Distributions for qualified housing expenses (i) In general Subparagraph (A) shall not apply to that portion of any distribution which is used to pay for a qualified housing expense of the designated beneficiary. (ii) Qualified housing expense For purposes of this subparagraph, the term qualified housing expense , with respect to a designated beneficiary, means any expense incurred by such beneficiary for the purchase of a principal residence, but only if such beneficiary is a first-time homebuyer, and includes any closing costs and mortgage payments incurred with respect to such purchase. (iii) Other definitions For purposes of this subparagraph\u2014 (I) First-time homebuyer The term first-time homebuyer means any individual if such individual (and if married, such individual\u2019s spouse) had no present ownership interest in a principal residence during the 3-year period ending on the date of the purchase of the principal residence to which this subparagraph applies. (II) Principal residence The term principal residence has the same meaning as when used in section 121. (III) Purchase The term purchase has the meaning given such term in section 36(c). .\n##### (b) Effective date\nThe amendment made by this section shall apply to distributions made after December 31, 2026.",
      "versionDate": "2026-02-05",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-02-23T16:29:00Z"
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
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7393ih.xml"
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
      "title": "Save for Success Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-20T10:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Save for Success Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T10:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow distributions from qualified tuition programs for qualified housing expenses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T10:48:21Z"
    }
  ]
}
```
