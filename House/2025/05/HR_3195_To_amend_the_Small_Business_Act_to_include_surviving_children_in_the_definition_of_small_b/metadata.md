# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3195?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3195
- Title: To amend the Small Business Act to include surviving children in the definition of small business concern owned and controlled by service-disabled veterans, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 3195
- Origin chamber: House
- Introduced date: 2025-05-05
- Update date: 2025-11-13T09:05:38Z
- Update date including text: 2025-11-13T09:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-05: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2025-05-05: Introduced in House

## Actions

- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3195",
    "number": "3195",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001212",
        "district": "1",
        "firstName": "Barry",
        "fullName": "Rep. Moore, Barry [R-AL-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "To amend the Small Business Act to include surviving children in the definition of small business concern owned and controlled by service-disabled veterans, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-11-13T09:05:38Z",
    "updateDateIncludingText": "2025-11-13T09:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-05",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T16:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "TX"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "AL"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "AL"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3195ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3195\nIN THE HOUSE OF REPRESENTATIVES\nMay 5, 2025 Mr. Moore of Alabama (for himself, Mr. Ellzey , and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Act to include surviving children in the definition of small business concern owned and controlled by service-disabled veterans, and for other purposes.\n#### 1. Inclusion of surviving children in small business concern owned and controlled by service-disabled veterans definition\nSection 3(q) of the Small Business Act ( 15 U.S.C. 632(q) ) is amended\u2014\n**(1)**\nin paragraph (2), by adding at the end the following new subparagraph:\n(D) (i) During the time period described in clause (ii), a small business concern that was a small business concern described in subparagraph (A) or (B) immediately prior to the death of a service-disabled veteran who was the owner of the concern, the death of whom causes the concern to be less than 51 percent owned by one or more service-disabled veterans, if\u2014 (I) a surviving child of the deceased veteran acquires such veteran\u2019s ownership interest in such concern; and (II) immediately prior to the death of such veteran and during the period described in clause (ii), the small business concern is included in the database described in section 36. (ii) The time period described in this clause is the time period beginning on the date of the veteran\u2019s death and ending on the earlier of\u2014 (I) the date on which the surviving child relinquishes an ownership interest in the small business concern; or (II) the date that is 3 years after the date of the veteran\u2019s death. ; and\n**(2)**\nby adding at the end the following new paragraph:\n(8) Surviving child The term surviving child means a biological or legally adopted child of a service-disabled veteran. .",
      "versionDate": "2025-05-05",
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
        "name": "Commerce",
        "updateDate": "2025-05-21T12:58:01Z"
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
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3195ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Act to include surviving children in the definition of small business concern owned and controlled by service-disabled veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:48:39Z"
    },
    {
      "title": "To amend the Small Business Act to include surviving children in the definition of small business concern owned and controlled by service-disabled veterans, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-06T08:05:38Z"
    }
  ]
}
```
