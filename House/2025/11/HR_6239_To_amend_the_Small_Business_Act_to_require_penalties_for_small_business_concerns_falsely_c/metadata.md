# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6239?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6239
- Title: Made in America Integrity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6239
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2025-12-15T16:26:20Z
- Update date including text: 2025-12-15T16:26:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6239",
    "number": "6239",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "V000134",
        "district": "24",
        "firstName": "Beth",
        "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
        "lastName": "Van Duyne",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Made in America Integrity Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-15T16:26:20Z",
    "updateDateIncludingText": "2025-12-15T16:26:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:07:10Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6239ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6239\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Ms. Van Duyne introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Act to require penalties for small business concerns falsely claiming goods or services are Made in America, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Made in America Integrity Act of 2025 .\n#### 2. Penalties for small business concerns falsely claiming goods or services are Made in America\nSection 16 of the Small Business Act ( 15 U.S.C. 645 ) is amended by adding at the end the following new subsection:\n(h) False claims of Made in America In addition to any other applicable penalties, a small business concern that is awarded a Federal contract in part or in whole because the concern falsely claims the goods or services that are the subject of the contract are made or produced in the United States shall be subject to the penalties and remedies described in subsection (d)(2), except that subparagraph (D) of such subsection shall be applied to such concern by substituting 5 years for 3 years . .",
      "versionDate": "2025-11-20",
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
        "updateDate": "2025-12-15T16:26:19Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6239ih.xml"
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
      "title": "To amend the Small Business Act to require penalties for small business concerns falsely claiming goods or services are Made in America, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-12T17:24:37Z"
    },
    {
      "title": "Made in America Integrity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-12T14:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Made in America Integrity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-12T14:23:19Z"
    }
  ]
}
```
