# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1237?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1237
- Title: PANELS Act
- Congress: 119
- Bill type: HR
- Bill number: 1237
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2026-03-06T09:07:16Z
- Update date including text: 2026-03-06T09:07:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1237",
    "number": "1237",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001295",
        "district": "12",
        "firstName": "Mike",
        "fullName": "Rep. Bost, Mike [R-IL-12]",
        "lastName": "Bost",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "PANELS Act",
    "type": "HR",
    "updateDate": "2026-03-06T09:07:16Z",
    "updateDateIncludingText": "2026-03-06T09:07:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:04:00Z",
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MN"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1237ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1237\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Bost (for himself and Mr. Finstad ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to deny the energy credit to property located on prime or unique farmland, as defined by the Secretary of Agriculture in part 657 of title 7, Code of Federal Regulations, if such property is used for generating solar energy.\n#### 1. Short title\nThis Act may be cited as the Protect Agriculture, Nutrients, and Essential Lands from Solar Act or the PANELS Act .\n#### 2. Credits amended to exclude property located on prime or unique farmland\n##### (a) Energy Credit\n**(1) Energy property**\nSection 48(a)(3) of the Internal Revenue Code of 1986 is amended by striking the period at the end and inserting , or property which is located on prime farmland or unique farmland if such property is used for generating solar energy.\n**(2) Qualified property**\nSection 48(a)(5)(D) of such Code is amended\u2014\n**(A)**\nin clause (iii), by striking and at the end,\n**(B)**\nin clause (iv), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following new clause:\n(v) which, in the case of property used for the purpose of generating solar energy, is not located on prime farmland or unique farmland. .\n**(3) Definitions added**\nSection 48(c) of such Code is amended by adding at the end the following new paragraph:\n(9) Prime farmland; unique farmland The terms prime farmland and unique farmland have the meaning given such terms in part 657 of title 7, Code of Federal Regulations. .\n**(4) Qualified solar and wind facility**\nSection 48(e)(2)(A) of such Code is amended\u2014\n**(A)**\nin clause (ii), by striking and at the end,\n**(B)**\nin clause (iii), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following new clause:\n(iv) which, in the case of a facility used for generating solar energy, is not located on prime farmland or unique farmland. .\n##### (b) Clean electricity production credit\nSection 45Y(b)(1) is amended\u2014\n**(1)**\nin subparagraph (A), by striking subparagraphs (B), (C), and (D), and inserting subparagraphs (B), (C), (D), and (E) , and\n**(2)**\nby adding at the end the following new subparagraph:\n(E) Prime farmland and unique farmland excluded The term qualified facility shall not include any facility used for generating solar energy if such facility is located on prime farmland or unique farmland (as such terms are defined in section 48(c)(9)). .\n##### (c) Effective date\nThe amendments made by this section shall apply to property placed in service after the date of the enactment of this Act.",
      "versionDate": "2025-02-12",
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
        "updateDate": "2025-05-05T19:56:36Z"
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
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1237ih.xml"
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
      "title": "PANELS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PANELS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Agriculture, Nutrients, and Essential Lands from Solar Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to deny the energy credit to property located on prime or unique farmland, as defined by the Secretary of Agriculture in part 657 of title 7, Code of Federal Regulations, if such property is used for generating solar energy.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:15Z"
    }
  ]
}
```
