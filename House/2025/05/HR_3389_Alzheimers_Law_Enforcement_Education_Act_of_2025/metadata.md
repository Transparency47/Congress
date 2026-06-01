# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3389?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3389
- Title: Alzheimer’s Law Enforcement Education Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3389
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2026-01-08T09:06:56Z
- Update date including text: 2026-01-08T09:06:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3389",
    "number": "3389",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Alzheimer\u2019s Law Enforcement Education Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-08T09:06:56Z",
    "updateDateIncludingText": "2026-01-08T09:06:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
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
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:00:25Z",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "CA"
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
      "sponsorshipDate": "2025-06-11",
      "state": "NC"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CO"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3389ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3389\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mr. Buchanan (for himself and Ms. Barrag\u00e1n ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo direct the Director of the Office of Community Oriented Policing Services of the Department of Justice to establish a training course relating to Alzheimer\u2019s disease and similar forms of dementia.\n#### 1. Short title\nThis Act may be cited as the Alzheimer\u2019s Law Enforcement Education Act of 2025 .\n#### 2. Training course relating to alzheimer\u2019s disease and similar forms of dementia\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Director of the Office of Community Oriented Policing Services of the Department of Justice, in consultation with the Secretary of Health and Human Services and the Administrator for the Centers for Medicare and Medicaid Services, shall establish a training course relating to Alzheimer\u2019s disease and similar forms of dementia and such training course shall be available online.\n##### (b) Development\nThe training course shall include the following:\n**(1)**\nInstructions on interacting with persons with Alzheimer\u2019s disease or a similar form of dementia.\n**(2)**\nTechniques for recognizing behavioral symptoms and characteristics of Alzheimer\u2019s disease or a similar form of dementia.\n**(3)**\nTechniques for effectively communicating with persons with Alzheimer\u2019s disease or a similar form of dementia.\n**(4)**\nEffective use of alternatives to physical restraints when interacting with persons with Alzheimer\u2019s disease or a similar form of dementia.\n**(5)**\nHow to identify signs of abuse, neglect, or exploitation of persons with Alzheimer\u2019s disease or a similar form of dementia.\n##### (c) Completion\nThe Director shall recommend that applicable State departments and agencies count participation in the course under this section towards the required hours of instruction for continued employment, or for appointment, as a law enforcement officer, correctional officer, or correctional probation officer.",
      "versionDate": "2025-05-14",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-28T12:44:52Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3389ih.xml"
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
      "title": "Alzheimer\u2019s Law Enforcement Education Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Alzheimer\u2019s Law Enforcement Education Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Director of the Office of Community Oriented Policing Services of the Department of Justice to establish a training course relating to Alzheimer's disease and similar forms of dementia.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:39Z"
    }
  ]
}
```
