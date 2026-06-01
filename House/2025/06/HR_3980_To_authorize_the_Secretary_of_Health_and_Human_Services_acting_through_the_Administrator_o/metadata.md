# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3980?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3980
- Title: Streamline Emergency Care Act
- Congress: 119
- Bill type: HR
- Bill number: 3980
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-11-18T09:05:37Z
- Update date including text: 2025-11-18T09:05:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3980",
    "number": "3980",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Streamline Emergency Care Act",
    "type": "HR",
    "updateDate": "2025-11-18T09:05:37Z",
    "updateDateIncludingText": "2025-11-18T09:05:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:08:35Z",
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
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NY"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NC"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3980ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3980\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Lawler (for himself and Mr. Espaillat ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo authorize the Secretary of Health and Human Services, acting through the Administrator of the Health Resources and Services Administration, to award grants for expanding, modernizing, or streamlining emergency department operations.\n#### 1. Short title\nThis Act may be cited as the Streamline Emergency Care Act .\n#### 2. Grants for emergency department operations\n##### (a) Awards\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ), acting through the Administrator of the Health Resources and Services Administration, shall carry out a program of awarding grants to eligible entities for expanding, modernizing, or streamlining emergency department operations.\n##### (b) Eligible entities\nIn this section, the term eligible entity means a health care provider that\u2014\n**(1)**\nis a nonprofit organization; and\n**(2)**\nat the time of applying for a grant under this section, is already operating an emergency department.\n##### (c) Amount\nThe amount of a grant under subsection (a) shall not exceed $500,000.\n##### (d) Use of funds\nA grant received under this section may be used for any of the following:\n**(1)**\nThe hiring and retention of individuals to work in the emergency department.\n**(2)**\nOptimizing and modernizing the capacity of an emergency department, and improving patient flow out of the emergency department, by\u2014\n**(A)**\nrepurposing or renovating hospital spaces;\n**(B)**\nimplementing new processes; or\n**(C)**\npurchasing equipment.\n**(3)**\nTriage and other training to increase the capacity of existing personnel to assist in improving emergency department patient care and flow.\n##### (e) Report\nNot later than the end of the third fiscal year beginning after the date of enactment of this Act, the Secretary shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate a report on the effectiveness and impacts of the grant program under this section.\n##### (f) Authorization of appropriations\nTo carry out this section, there is authorized to be appropriated $20,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-06-12",
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
        "name": "Health",
        "updateDate": "2025-07-07T13:51:08Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3980ih.xml"
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
      "title": "Streamline Emergency Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-24T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Streamline Emergency Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-24T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Health and Human Services, acting through the Administrator of the Health Resources and Services Administration, to award grants for expanding, modernizing, or streamlining emergency department operations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-24T05:48:25Z"
    }
  ]
}
```
