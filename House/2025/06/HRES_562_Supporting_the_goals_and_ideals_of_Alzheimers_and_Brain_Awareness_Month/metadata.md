# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/562?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/562
- Title: Supporting the goals and ideals of Alzheimer's and Brain Awareness Month.
- Congress: 119
- Bill type: HRES
- Bill number: 562
- Origin chamber: House
- Introduced date: 2025-06-30
- Update date: 2026-04-30T08:06:32Z
- Update date including text: 2026-04-30T08:06:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-30: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-30 - IntroReferral: Submitted in House
- 2025-06-30 - IntroReferral: Submitted in House
- Latest action: 2025-06-30: Submitted in House

## Actions

- 2025-06-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-30 - IntroReferral: Submitted in House
- 2025-06-30 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-30",
    "latestAction": {
      "actionDate": "2025-06-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/562",
    "number": "562",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001300",
        "district": "44",
        "firstName": "Nanette",
        "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
        "lastName": "Barrag\u00e1n",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Supporting the goals and ideals of Alzheimer's and Brain Awareness Month.",
    "type": "HRES",
    "updateDate": "2026-04-30T08:06:32Z",
    "updateDateIncludingText": "2026-04-30T08:06:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-30",
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
      "actionCode": "H11100",
      "actionDate": "2025-06-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-06-30T18:00:40Z",
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
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "FL"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "CA"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "FL"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres562ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 562\nIN THE HOUSE OF REPRESENTATIVES\nJune 30, 2025 Ms. Barrag\u00e1n (for herself, Mr. Buchanan , Ms. S\u00e1nchez , and Mr. Bilirakis ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nSupporting the goals and ideals of Alzheimer\u2019s and Brain Awareness Month.\nThat the House of Representatives\u2014\n**(1)**\nsupports the goals and ideals of Alzheimer\u2019s and Brain Awareness Month; and\n**(2)**\nencourages people in the United States to\u2014\n**(A)**\neducate themselves about Alzheimer\u2019s disease and other forms of dementia;\n**(B)**\nadvocate for Alzheimer\u2019s disease research, care, and support services; and\n**(C)**\noffer their support to individuals living with Alzheimer\u2019s disease and other forms of dementia, their families, and their caregivers.",
      "versionDate": "2025-06-30",
      "versionType": "IH"
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
        "name": "Health",
        "updateDate": "2025-07-11T12:41:23Z"
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
      "date": "2025-06-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres562ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Supporting the goals and ideals of Alzheimer's and Brain Awareness Month.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-01T08:18:23Z"
    },
    {
      "title": "Supporting the goals and ideals of Alzheimer's and Brain Awareness Month.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-01T08:05:37Z"
    }
  ]
}
```
