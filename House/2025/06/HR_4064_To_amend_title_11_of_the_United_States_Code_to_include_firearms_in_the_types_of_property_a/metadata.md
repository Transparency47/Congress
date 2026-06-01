# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4064?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4064
- Title: Protecting Gun Owners in Bankruptcy Act
- Congress: 119
- Bill type: HR
- Bill number: 4064
- Origin chamber: House
- Introduced date: 2025-06-20
- Update date: 2025-09-17T15:09:50Z
- Update date including text: 2025-09-17T15:09:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-20: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-20: Introduced in House

## Actions

- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-20",
    "latestAction": {
      "actionDate": "2025-06-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4064",
    "number": "4064",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Protecting Gun Owners in Bankruptcy Act",
    "type": "HR",
    "updateDate": "2025-09-17T15:09:50Z",
    "updateDateIncludingText": "2025-09-17T15:09:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-20",
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
          "date": "2025-06-20T15:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "GA"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "UT"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "TX"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4064ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4064\nIN THE HOUSE OF REPRESENTATIVES\nJune 20, 2025 Ms. Tenney (for herself, Mr. Collins , Mr. Owens , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 11 of the United States Code to include firearms in the types of property allowable under the alternative provision for exempting property from the estate.\n#### 1. Short title\nThis Act may be cited as the Protecting Gun Owners in Bankruptcy Act .\n#### 2. Exemptions\nSection 522 of title 11, United States Code, is amended\u2014\n**(1)**\nin subsection (d) by adding at the end the following:\n(13) The debtor's aggregate interest, not to exceed $3,000 in value, in a single firearm or firearms. ; and\n**(2)**\nin subsection (f)(4)(A)\u2014\n**(A)**\nin clause (xiv) by striking and at the end;\n**(B)**\nin clause (xv) by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(xvi) The debtor's aggregate interest, not to exceed $3,000 in value, in a single firearm or firearms. .\n#### 3. Effective date; application of amendments\n##### (a) Effective date\nExcept as provided in subsection (b), this Act and the amendments made by this Act shall take effect on the date of the enactment of this Act.\n##### (b) Application of amendments\nThe amendments made by this Act shall apply only with respect to cases commenced under title 11 of the United States Code on or after the date of the enactment of this Act.",
      "versionDate": "2025-06-20",
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
        "updateDate": "2025-09-17T15:09:50Z"
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
      "date": "2025-06-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4064ih.xml"
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
      "title": "Protecting Gun Owners in Bankruptcy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Gun Owners in Bankruptcy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 11 of the United States Code to include firearms in the types of property allowable under the alternative provision for exempting property from the estate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T05:18:50Z"
    }
  ]
}
```
