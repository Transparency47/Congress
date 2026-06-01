# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6656?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6656
- Title: Child Care Access and Affordability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6656
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-01-08T15:26:03Z
- Update date including text: 2026-01-08T15:26:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6656",
    "number": "6656",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "M001237",
        "district": "8",
        "firstName": "Kristen",
        "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
        "lastName": "McDonald Rivet",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Child Care Access and Affordability Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-08T15:26:03Z",
    "updateDateIncludingText": "2026-01-08T15:26:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6656ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6656\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Ms. McDonald Rivet (for herself and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo require the Government Accountability Office to carry out a study relating to barriers in accessing the Child Care and Development Block Grant Act of 1990 due to inflation and State eligibility standards.\n#### 1. Short title\nThis Act may be cited as the Child Care Access and Affordability Act of 2025 .\n#### 2. Required study by the Government Accountability Office\nNot latter than 18 months after the date of the enactment of this Act, the Government Accountability Office carry out a study of each of States, and report the results of such study to the appropriate committees of the Congress, to identify\u2014\n**(1)**\nthe barriers children and parents face in meeting State standards under such Act due to State median income eligibility limits,\n**(2)**\nthe extent of the wait list of applicants for child care services provided under the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ) and State-level reforms that have reduced such wait lists,\n**(3)**\nthe rates of payments made under such Act to center-based child care providers, family child care providers, and other providers of child care services for compensation under such Act, and\n**(4)**\nthe impact of inflation on child care availability and affordability under such Act, on expanding the number of families accessing such services, and improving payment rates for such services.",
      "versionDate": "2025-12-11",
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
        "name": "Families",
        "updateDate": "2026-01-08T15:26:03Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6656ih.xml"
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
      "title": "Child Care Access and Affordability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T06:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Child Care Access and Affordability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T06:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Government Accountability Office to carry out a study relating to barriers in accessing the Child Care and Development Block Grant Act of 1990 due to inflation and State eligibility standards.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T06:18:27Z"
    }
  ]
}
```
