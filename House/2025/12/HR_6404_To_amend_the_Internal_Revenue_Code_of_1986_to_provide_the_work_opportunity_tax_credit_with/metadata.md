# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6404?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6404
- Title: Hire Student Veterans Act
- Congress: 119
- Bill type: HR
- Bill number: 6404
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-01-07T16:51:30Z
- Update date including text: 2026-01-07T16:51:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6404",
    "number": "6404",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000590",
        "district": "3",
        "firstName": "Susie",
        "fullName": "Rep. Lee, Susie [D-NV-3]",
        "lastName": "Lee",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Hire Student Veterans Act",
    "type": "HR",
    "updateDate": "2026-01-07T16:51:30Z",
    "updateDateIncludingText": "2026-01-07T16:51:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:00:50Z",
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
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "FL"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6404ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6404\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Ms. Lee of Nevada (for herself, Mr. Steube , and Ms. Craig ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide the work opportunity tax credit with respect to hiring veterans who are receiving educational assistance under laws administered by the Secretary of Veterans Affairs or Defense.\n#### 1. Short title\nThis Act may be cited as the Hire Student Veterans Act .\n#### 2. Work opportunity tax credit for hiring veterans receiving educational assistance under laws administered by the Secretary of Veterans Affairs or Defense\n##### (a) In general\nSection 51(d)(3)(A) of the Internal Revenue Code of 1986 is amended by striking or at the end of clause (iii), by striking the period at the end of clause (iv) and inserting , or , and by adding at the end the following new clause:\n(v) attending an educational institution by means of educational assistance provided under chapter 30, 31, 32, 33, or 34 of title 38, United States Code, or chapter 1606 or 1607 of title 10, United States Code. .\n##### (b) Modification of minimum employment period\nSection 51(i)(3)(A) of the Internal Revenue Code of 1986 is amended by inserting (other than a qualified veteran described in subsection (d)(3)(A)(v)) after In the case of an individual .\n##### (c) Effective date\nThe amendments made by this section shall apply to individuals who begin work for the employer after the date of the enactment of this Act.",
      "versionDate": "2025-12-03",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-07-29",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2494",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Hire Student Veterans Act",
      "type": "S"
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
        "updateDate": "2026-01-06T16:31:16Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6404ih.xml"
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
      "title": "Hire Student Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Hire Student Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T06:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide the work opportunity tax credit with respect to hiring veterans who are receiving educational assistance under laws administered by the Secretary of Veterans Affairs or Defense.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T06:18:23Z"
    }
  ]
}
```
