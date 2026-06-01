# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3894?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3894
- Title: Respect for Local Communities Act
- Congress: 119
- Bill type: S
- Bill number: 3894
- Origin chamber: Senate
- Introduced date: 2026-02-23
- Update date: 2026-05-19T11:03:45Z
- Update date including text: 2026-05-19T11:03:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-23: Introduced in Senate
- 2026-02-23 - IntroReferral: Introduced in Senate
- 2026-02-23 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-02-23: Introduced in Senate

## Actions

- 2026-02-23 - IntroReferral: Introduced in Senate
- 2026-02-23 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-23",
    "latestAction": {
      "actionDate": "2026-02-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3894",
    "number": "3894",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Respect for Local Communities Act",
    "type": "S",
    "updateDate": "2026-05-19T11:03:45Z",
    "updateDateIncludingText": "2026-05-19T11:03:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-23",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-02-23T20:40:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NH"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "AZ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "AZ"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "VA"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3894is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3894\nIN THE SENATE OF THE UNITED STATES\nFebruary 23, 2026 Mrs. Shaheen (for herself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit the Department of Homeland Security from constructing, acquiring, renovating, or operating any new processing site or detention center without providing a mechanism for public comments regarding such activity, entering into a signed, written agreement with appropriate State and local officials, and providing Congress with advance notice of such activity.\n#### 1. Short title\nThis Act may be cited as the Respect for Local Communities Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate local government officials**\nThe term appropriate local government officials means\u2014\n**(A)**\nthe mayor, county executive, or equivalent elected official of the town, city, county or other local jurisdiction in which a new processing facility or detention center will be located; and\n**(B)**\na majority of the town council, city council, county council, county commission, or equivalent legislative authority in which a new processing facility or detention center will be located.\n**(2) New processing site or detention center**\nThe term new processing site or detention center means any facility operated by, or pursuant to a contract with, U.S. Immigration and Customs Enforcement, including any facility designed under the Detention Reengineering Initiative, that, beginning on or after the date of the enactment of this Act, will be used to temporarily hold persons pending the resolution or completion of immigration removal operations or processes.\n#### 3. Requirements for new ICE processing sites and detention centers\nThe Department of Homeland Security or any other Federal agency may not initiate the construction, acquisition, renovation, or operation of, or otherwise acquire an interest in real property to be used as, a new processing site or detention center for U.S. Immigration and Customs Enforcement until\u2014\n**(1)**\nthe relevant Federal agency issues a public notice in the Federal Register that\u2014\n**(A)**\nis open for public comments for a period lasting at least 30 days;\n**(B)**\ndescribes the scope of the construction, acquisition, renovation, or operation;\n**(C)**\nincludes information regarding such agency's due diligence process, which shall explain how such agency will comply with\u2014\n**(i)**\nFederal guidance and standards related to immigration detention; and\n**(ii)**\napplicable environmental regulations;\n**(D)**\nincludes any other information or documentation relevant to such new processing site or detention center; and\n**(E)**\nincludes an economic impact analysis and an engineering review that addresses the site or center's waste exportation, water usage, and electrical demand;\n**(2)**\nafter the conclusion of the public comment period, the head of the relevant Federal agency\u2014\n**(A)**\nconsiders and responds to significant comments received in accordance with subchapter II of chapter 5 of title 5, United States Code; and\n**(B)**\nenters into a signed, written agreement with appropriate local government officials and the Governor of the State in which such processing site or detention center will be located that authorizes such construction, acquisition, renovation, or operation, as applicable; and\n**(3)**\nat least 30 days has elapsed since the head of the relevant Federal agency submitted a report to the Committee on Homeland Security and Governmental Affairs of the Senate , the Committee on Appropriations of the Senate , the Committee on the Judiciary of the Senate , the Committee on Homeland Security of the House of Representatives , the Committee on Appropriations of the House of Representatives , and the Committee on the Judiciary of the House of Representatives regarding such planned construction, acquisition, renovation, or operation that includes a fully executed copy of the agreement described in paragraph (2).",
      "versionDate": "2026-02-23",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-02-23",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "7652",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Respect for Local Communities Act",
      "type": "HR"
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
        "updateDate": "2026-03-16T17:28:26Z"
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
      "date": "2026-02-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3894is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Respect for Local Communities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T11:03:45Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Respect for Local Communities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the Department of Homeland Security from constructing, acquiring, renovating, or operating any new processing site or detention center without providing a mechanism for public comments regarding such activity, entering into a signed, written agreement with appropriate State and local officials, and providing Congress with advance notice of such activity.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:18:38Z"
    }
  ]
}
```
