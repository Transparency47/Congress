# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7737?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7737
- Title: SEEDS Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7737
- Origin chamber: House
- Introduced date: 2026-02-26
- Update date: 2026-03-24T01:38:13Z
- Update date including text: 2026-03-24T01:38:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-26: Introduced in House

## Actions

- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7737",
    "number": "7737",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "SEEDS Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-24T01:38:13Z",
    "updateDateIncludingText": "2026-03-24T01:38:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-26",
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
      "actionDate": "2026-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T14:33:00Z",
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
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "SC"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7737ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7737\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2026 Mrs. Kim (for herself, Mr. Timmons , and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to treat digital asset indexes as eligible investments for purposes of Trump accounts.\n#### 1. Short title\nThis Act may be cited as the Savings and Early Exposure to Diversified Securities Act of 2026 or the SEEDS Act of 2026 .\n#### 2. Making digital asset indexes eligible investments for purposes of Trump accounts\n##### (a) In general\nSection 530A(b)(3)(B) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin clause (i), by striking or at the end,\n**(2)**\nby redesignating clause (ii) as clause (iii), and\n**(3)**\nby inserting after clause (i) the following new clause:\n(ii) an index comprised of digital assets, .\n##### (b) Effective date\nThe amendments made by this section shall apply to investments made after the date of the enactment of this Act.\n#### 3. Trump accounts contribution pilot program made permanent\n##### (a) In general\nSection 6434 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin the heading, by striking pilot , and\n**(2)**\nin subsection (c)(1), by striking and before January 1, 2029, .\n##### (b) Conforming amendments\n**(1)**\nSection 6213(g)(2)(AA) of such Code is amended by striking pilot .\n**(2)**\nThe item relating to section 6434 in the table of sections for subchapter B of chapter 65 of such Code is amended by striking pilot .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2026-02-26",
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
        "updateDate": "2026-03-24T01:38:13Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7737ih.xml"
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
      "title": "SEEDS Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SEEDS Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Savings and Early Exposure to Diversified Securities Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to treat digital asset indexes as eligible investments for purposes of Trump accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T03:48:20Z"
    }
  ]
}
```
