# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1636?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1636
- Title: Securing our Radioactive Materials Act
- Congress: 119
- Bill type: HR
- Bill number: 1636
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2025-05-07T08:06:08Z
- Update date including text: 2025-05-07T08:06:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1636",
    "number": "1636",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Securing our Radioactive Materials Act",
    "type": "HR",
    "updateDate": "2025-05-07T08:06:08Z",
    "updateDateIncludingText": "2025-05-07T08:06:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1636ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1636\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mr. Torres of New York introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Nuclear Regulatory Commission to take certain actions relating to security measures for radioactive materials, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing our Radioactive Materials Act .\n#### 2. NRC actions to address certain radiological security risks\n##### (a) Actions To be taken by NRC\nThe Nuclear Regulatory Commission shall take the following actions, as described in the Government Accountability Office report titled Preventing a Dirty Bomb: Nuclear Regulatory Commission Has Not Taken Steps to Address Certain Radiological Security Risks (GAO\u201324\u2013107014; published September 30, 2024):\n**(1)**\nThe Nuclear Regulatory Commission shall incorporate socioeconomic consequences into the Nuclear Regulatory Commission\u2019s decision-making for setting security measures for radioactive materials.\n**(2)**\nThe Nuclear Regulatory Commission shall immediately require that\u2014\n**(A)**\nall category 3 licenses be added to the Web-based Licensing System;\n**(B)**\nall category 3 sources be included and tracked in the National Source Tracking System; and\n**(C)**\nall vendors verify the legitimacy of would-be purchasers\u2019 category 3 licenses with the appropriate regulator.\n##### (b) Revision of regulations\nNot later than 1 year after the date of enactment of this Act, the Nuclear Regulatory Commission shall revise any applicable guidelines, policies, and regulations as necessary to carry out subsection (a).",
      "versionDate": "2025-02-26",
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
        "name": "Energy",
        "updateDate": "2025-03-21T14:26:57Z"
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
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1636ih.xml"
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
      "title": "Securing our Radioactive Materials Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T07:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing our Radioactive Materials Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T07:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Nuclear Regulatory Commission to take certain actions relating to security measures for radioactive materials, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T07:03:33Z"
    }
  ]
}
```
