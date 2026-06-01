# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1287?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1287
- Title: Recognizing stroke as a national health crisis requiring immediate, coordinated Federal action, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 1287
- Origin chamber: House
- Introduced date: 2026-05-14
- Update date: 2026-05-29T16:07:26Z
- Update date including text: 2026-05-29T16:07:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-14 - IntroReferral: Submitted in House
- Latest action: 2026-05-14: Submitted in House

## Actions

- 2026-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1287",
    "number": "1287",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000606",
        "district": "16",
        "firstName": "George",
        "fullName": "Rep. Latimer, George [D-NY-16]",
        "lastName": "Latimer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Recognizing stroke as a national health crisis requiring immediate, coordinated Federal action, and for other purposes.",
    "type": "HRES",
    "updateDate": "2026-05-29T16:07:26Z",
    "updateDateIncludingText": "2026-05-29T16:07:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-14",
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
      "actionCode": "1025",
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
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
          "date": "2026-05-14T14:06:15Z",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1287ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1287\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2026 Mr. Latimer (for himself and Mrs. Dingell ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRecognizing stroke as a national health crisis requiring immediate, coordinated Federal action, and for other purposes.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes stroke as a national health crisis requiring immediate, coordinated Federal action;\n**(2)**\nsupports the development and implementation of a standardized emergency medical services (EMS) training curriculum for stroke and large vessel occlusion (LVO) recognition;\n**(3)**\nurges States and regional EMS systems to adopt and enforce routing protocols prioritizing direct transport of suspected LVO stroke patients to thrombectomy-capable centers when within recommended transport times;\n**(4)**\nencourages increased Federal and State investment in public stroke education campaigns to promote timely 9\u20131\u20131 activation;\n**(5)**\ncalls for transparency in stroke center capabilities and outcomes to aid EMS routing decisions;\n**(6)**\naffirms the need for equitable access to mechanical thrombectomy and comprehensive stroke care for all Americans, regardless of geographic location; and\n**(7)**\nsupports the goals and ideals of a World Stroke Thrombectomy Day.",
      "versionDate": "2026-05-14",
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
        "updateDate": "2026-05-29T16:07:26Z"
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
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1287ih.xml"
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
      "title": "Recognizing stroke as a national health crisis requiring immediate, coordinated Federal action, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:18:24Z"
    },
    {
      "title": "Recognizing stroke as a national health crisis requiring immediate, coordinated Federal action, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T08:07:47Z"
    }
  ]
}
```
