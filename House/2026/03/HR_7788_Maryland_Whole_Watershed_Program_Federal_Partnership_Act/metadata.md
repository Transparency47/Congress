# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7788?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7788
- Title: Maryland Whole Watershed Program Federal Partnership Act
- Congress: 119
- Bill type: HR
- Bill number: 7788
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-04-10T08:06:02Z
- Update date including text: 2026-04-10T08:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-03-04: Introduced in House

## Actions

- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7788",
    "number": "7788",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "E000301",
        "district": "3",
        "firstName": "Sarah",
        "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
        "lastName": "Elfreth",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Maryland Whole Watershed Program Federal Partnership Act",
    "type": "HR",
    "updateDate": "2026-04-10T08:06:02Z",
    "updateDateIncludingText": "2026-04-10T08:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MD"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MD"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MD"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7788ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7788\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Ms. Elfreth (for herself, Mr. Olszewski , Mr. Mfume , and Mr. Raskin ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo authorize the Chesapeake Bay Program Office to serve as a member of certain State watershed programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Maryland Whole Watershed Program Federal Partnership Act .\n#### 2. Chesapeake Bay Program Office authority\n##### (a) In general\nThe Chesapeake Bay Program Office shall serve as an advisory member of the State Management Team for the Maryland Whole Watershed Program and any other substantially similar program in a State.\n##### (b) Authorized activities\nIn carrying out subsection (a), the Chesapeake Bay Program Office is authorized to\u2014\n**(1)**\ncoordinate with State and local governments and Federal agencies; and\n**(2)**\nprovide technical assistance and financial resources for projects carried out in the Chesapeake Bay watershed.\n##### (c) Chesapeake Bay Program Office defined\nIn this section, the term Chesapeake Bay Program Office means the office established and maintained pursuant to section 117(b) of the Federal Water Pollution Control Act ( 33 U.S.C. 1267(b) ).",
      "versionDate": "2026-03-04",
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
        "name": "Environmental Protection",
        "updateDate": "2026-03-27T20:11:46Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7788ih.xml"
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
      "title": "Maryland Whole Watershed Program Federal Partnership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T09:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Maryland Whole Watershed Program Federal Partnership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T09:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Chesapeake Bay Program Office to serve as a member of certain State watershed programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T09:48:21Z"
    }
  ]
}
```
