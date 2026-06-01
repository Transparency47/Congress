# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4608?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4608
- Title: Francis G. Newlands Memorial Removal Act
- Congress: 119
- Bill type: HR
- Bill number: 4608
- Origin chamber: House
- Introduced date: 2025-07-22
- Update date: 2025-12-05T21:54:02Z
- Update date including text: 2025-12-05T21:54:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-22: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-07-22 - IntroReferral: Sponsor introductory remarks on measure. (CR E706)
- Latest action: 2025-07-22: Introduced in House

## Actions

- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-07-22 - IntroReferral: Sponsor introductory remarks on measure. (CR E706)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4608",
    "number": "4608",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "Francis G. Newlands Memorial Removal Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:54:02Z",
    "updateDateIncludingText": "2025-12-05T21:54:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E706)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T14:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "MD"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4608ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4608\nIN THE HOUSE OF REPRESENTATIVES\nJuly 22, 2025 Ms. Norton (for herself, Mr. Raskin , and Mr. Carson ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of the Interior to remove or permanently conceal the name of Francis Newlands on the grounds of the memorial fountain located at Chevy Chase Circle in the District of Columbia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Francis G. Newlands Memorial Removal Act .\n#### 2. Removal of Plaque and Concrete from Memorial Fountain Grounds\n##### (a) In general\nThe Secretary of the Interior shall\u2014\n**(1)**\nremove the brass plaque bearing the name Senator Francis G. Newlands from the grounds of the memorial fountain;\n**(2)**\nremove from the south end of the memorial fountain\u2019s face, the stone, tablet-like projection bearing the name of Francis Griffith Newlands and a related inscription;\n**(3)**\nremove or permanently conceal the name Newlands carved into the upper face of the memorial fountain\u2019s coping stones; and\n**(4)**\noffer the items removed pursuant to paragraphs (1), (2), and (3) to the descendants of Francis Griffith Newlands for a period of 60 days, and if not claimed within that period, direct the items removed pursuant to paragraphs (1), (2), and (3) to be maintained by the National Park Service as Federal property and accessioned into the Rock Creek Park museum collection.\n##### (b) Memorial fountain\nFor the purposes of this section, the term memorial fountain means the memorial fountain located at Chevy Chase Circle, Connecticut Avenue and Western Avenue NW, in the District of Columbia.",
      "versionDate": "2025-07-22",
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
        "actionDate": "2025-07-22",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "2369",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Francis G. Newlands Memorial Removal Act",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-31T22:15:57Z"
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
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4608ih.xml"
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
      "title": "Francis G. Newlands Memorial Removal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T04:43:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Francis G. Newlands Memorial Removal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:43:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Interior to remove or permanently conceal the name of Francis Newlands on the grounds of the memorial fountain located at Chevy Chase Circle in the District of Columbia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:33:34Z"
    }
  ]
}
```
