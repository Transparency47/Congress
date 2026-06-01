# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8800?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8800
- Title: National Defense Authorization Act for Fiscal Year 2027
- Congress: 119
- Bill type: HR
- Bill number: 8800
- Origin chamber: House
- Introduced date: 2026-05-13
- Update date: 2026-05-15T18:07:44Z
- Update date including text: 2026-05-15T18:07:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-13: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-05-13: Introduced in House

## Actions

- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8800",
    "number": "8800",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000575",
        "district": "3",
        "firstName": "Mike",
        "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
        "lastName": "Rogers",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "National Defense Authorization Act for Fiscal Year 2027",
    "type": "HR",
    "updateDate": "2026-05-15T18:07:44Z",
    "updateDateIncludingText": "2026-05-15T18:07:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T14:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8800ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8800\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2026 Mr. Rogers of Alabama (for himself and Mr. Smith of Washington ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo authorize appropriations for fiscal year 2027 for military activities of the Department of Defense, for military construction, and for defense activities of the Department of Energy, to prescribe military personnel strengths for such fiscal year, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Defense Authorization Act for Fiscal Year 2027 .\nI\nPROCUREMENT\n#### 101. Authorization of appropriations\nFunds are hereby authorized to be appropriated for fiscal year 2027 for procurement for the Army, the Navy and the Marine Corps, the Air Force and the Space Force, and Defense-wide activities, as specified in the funding table in section 4101.\nII\nRESEARCH, DEVELOPMENT, TEST, AND EVALUATION\n#### 201. Authorization of appropriations\nFunds are hereby authorized to be appropriated for fiscal year 2027 for the use of the Department of Defense for research, development, test, and evaluation, as specified in the funding table in section 4201.\nIII\nOperation and Maintenance\n#### 301. Authorization of appropriations\nFunds are hereby authorized to be appropriated for fiscal year 2027 for the use of the Armed Forces and other activities and agencies of the Department of Defense for expenses, not otherwise provided for, for operation and maintenance, as specified in the funding table in section 4301.",
      "versionDate": "2026-05-13",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-05-15T18:07:44Z"
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
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8800ih.xml"
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
      "title": "National Defense Authorization Act for Fiscal Year 2027",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T08:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Defense Authorization Act for Fiscal Year 2027",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T08:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize appropriations for fiscal year 2027 for military activities of the Department of Defense, for military construction, and for defense activities of the Department of Energy, to prescribe military personnel strengths for such fiscal year, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T08:18:27Z"
    }
  ]
}
```
