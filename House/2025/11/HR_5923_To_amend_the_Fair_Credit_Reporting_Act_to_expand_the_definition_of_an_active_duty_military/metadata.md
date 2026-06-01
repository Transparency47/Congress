# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5923?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5923
- Title: Servicemember Credit Monitoring Enhancement Act
- Congress: 119
- Bill type: HR
- Bill number: 5923
- Origin chamber: House
- Introduced date: 2025-11-04
- Update date: 2025-11-25T18:51:42Z
- Update date including text: 2025-11-25T18:51:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-04: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-11-04: Introduced in House

## Actions

- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-04",
    "latestAction": {
      "actionDate": "2025-11-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5923",
    "number": "5923",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001196",
        "district": "21",
        "firstName": "Elise",
        "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
        "lastName": "Stefanik",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Servicemember Credit Monitoring Enhancement Act",
    "type": "HR",
    "updateDate": "2025-11-25T18:51:42Z",
    "updateDateIncludingText": "2025-11-25T18:51:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-04",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-04",
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
          "date": "2025-11-04T19:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "OR"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5923ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5923\nIN THE HOUSE OF REPRESENTATIVES\nNovember 4, 2025 Ms. Stefanik (for herself and Ms. Bynum ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Fair Credit Reporting Act to expand the definition of an active duty military consumer for purposes of certain credit monitoring requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Servicemember Credit Monitoring Enhancement Act .\n#### 2. Credit monitoring\nSection 605A(k) of the Fair Credit Reporting Act ( 15 U.S.C. 1681c\u20131(k) ) is amended\u2014\n**(1)**\nby amending paragraph (1) to read as follows:\n(1) Uniformed services member consumer defined In this subsection, the term uniformed services member consumer means a consumer who is a member of the uniformed services (as such term is defined under section 101(a) of title 10, United States Code). ; and\n**(2)**\nin paragraph (2)(A), by striking active duty military consumer and inserting uniformed services member consumer .",
      "versionDate": "2025-11-04",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-11-25T18:51:42Z"
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
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5923ih.xml"
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
      "title": "Servicemember Credit Monitoring Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Servicemember Credit Monitoring Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Fair Credit Reporting Act to expand the definition of an active duty military consumer for purposes of certain credit monitoring requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-07T12:18:15Z"
    }
  ]
}
```
