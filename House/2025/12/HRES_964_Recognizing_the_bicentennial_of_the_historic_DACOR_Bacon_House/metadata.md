# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/964?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/964
- Title: Recognizing the bicentennial of the historic DACOR Bacon House.
- Congress: 119
- Bill type: HRES
- Bill number: 964
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2025-12-20T09:05:18Z
- Update date including text: 2025-12-20T09:05:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-18 - IntroReferral: Submitted in House
- 2025-12-18 - IntroReferral: Submitted in House
- Latest action: 2025-12-18: Submitted in House

## Actions

- 2025-12-18 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-18 - IntroReferral: Submitted in House
- 2025-12-18 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/964",
    "number": "964",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001227",
        "district": "4",
        "firstName": "Jennifer",
        "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
        "lastName": "McClellan",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Recognizing the bicentennial of the historic DACOR Bacon House.",
    "type": "HRES",
    "updateDate": "2025-12-20T09:05:18Z",
    "updateDateIncludingText": "2025-12-20T09:05:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:09:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "NE"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres964ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 964\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Ms. McClellan (for herself, Mr. Bacon , and Mr. Beyer ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nRecognizing the bicentennial of the historic DACOR Bacon House.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the historic importance of the DACOR Bacon House to the history of American diplomacy, the Supreme Court, and Congress;\n**(2)**\napplauds the Diplomatic and Consular Officers, Retired (DACOR) organization and DACOR Bacon House Foundation for their decades-long efforts to preserve this unique gem located in the heart of the Nation\u2019s Capital;\n**(3)**\ncongratulates all those who have found meaning and community in the DACOR Bacon House on its bicentennial; and\n**(4)**\nsincerely wishes to see the DACOR Bacon House continue to flourish over the next 200 years.",
      "versionDate": "2025-12-18",
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
        "name": "International Affairs",
        "updateDate": "2025-12-19T20:31:57Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres964ih.xml"
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
      "title": "Recognizing the bicentennial of the historic DACOR Bacon House.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T12:39:53Z"
    },
    {
      "title": "Recognizing the bicentennial of the historic DACOR Bacon House.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T09:07:07Z"
    }
  ]
}
```
