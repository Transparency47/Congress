# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5335?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5335
- Title: PERU Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5335
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-09-26T13:52:38Z
- Update date including text: 2025-09-26T13:52:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5335",
    "number": "5335",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "P000621",
        "district": "9",
        "firstName": "Nellie",
        "fullName": "Rep. Pou, Nellie [D-NJ-9]",
        "lastName": "Pou",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "PERU Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-26T13:52:38Z",
    "updateDateIncludingText": "2025-09-26T13:52:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5335ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5335\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Ms. Pou (for herself and Ms. Salazar ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo include Peru in the list of foreign states whose nationals are eligible for admission into the United States as E\u20131 and E\u20132 nonimmigrants if United States nationals are treated similarly by the Government of Peru.\n#### 1. Short title\nThis Act may be cited as the Promoting Economic Resilience and Unity Act of 2025 or the PERU Act of 2025 .\n#### 2. Nonimmigrant traders and investors\nFor purposes of clauses (i) and (ii) of section 101(a)(15)(E) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(E) ), Peru shall be considered to be a foreign state described in such section if the Government of Peru provides similar nonimmigrant status to nationals of the United States.",
      "versionDate": "2025-09-11",
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
        "name": "Immigration",
        "updateDate": "2025-09-26T13:52:38Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5335ih.xml"
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
      "title": "PERU Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-25T04:43:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PERU Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-25T04:43:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting Economic Resilience and Unity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-25T04:43:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To include Peru in the list of foreign states whose nationals are eligible for admission into the United States as E-1 and E-2 nonimmigrants if United States nationals are treated similarly by the Government of Peru.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-25T04:41:03Z"
    }
  ]
}
```
