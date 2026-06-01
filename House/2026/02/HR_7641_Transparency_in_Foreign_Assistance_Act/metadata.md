# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7641?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7641
- Title: Transparency in Foreign Assistance Act
- Congress: 119
- Bill type: HR
- Bill number: 7641
- Origin chamber: House
- Introduced date: 2026-02-23
- Update date: 2026-04-17T17:20:27Z
- Update date including text: 2026-04-17T17:20:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-23: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 44 - 0.
- Latest action: 2026-02-23: Introduced in House

## Actions

- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 44 - 0.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7641",
    "number": "7641",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
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
    "title": "Transparency in Foreign Assistance Act",
    "type": "HR",
    "updateDate": "2026-04-17T17:20:27Z",
    "updateDateIncludingText": "2026-04-17T17:20:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 44 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-23",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-23",
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
        "item": [
          {
            "date": "2026-03-26T16:04:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-23T17:01:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7641ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7641\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 23, 2026 Mr. Lawler (for himself and Ms. Jacobs ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo provide for a pilot program to require congressional notification of additional information for certain foreign assistance programs.\n#### 1. Short title\nThis Act may be cited as the Transparency in Foreign Assistance Act .\n#### 2. Pilot program to require congressional notification of additional information for certain foreign assistance programs\n##### (a) In general\nThe Secretary of State shall direct the Assistant Secretary for the Bureau of African Affairs and the Coordinator for Counterterrorism to carry out a one-year pilot program that requires such officials to submit to the appropriate congressional committees a notification of information, in addition to information required under existing law, for new and existing foreign assistance programs under the authorities of such officials that require funds that are in addition to funds made available for such programs under existing law.\n##### (b) Elements\nThe notification required by subsection (a) shall include, for each program, the following:\n**(1)**\nThe working name of the program.\n**(2)**\nThe country or countries where the program will be implemented.\n**(3)**\nThe mechanism used for the program, such as contract, grant, interagency agreement, bureau transfer.\n**(4)**\nThe total amount of new funding for the program.\n**(5)**\nWhether the program is considered a new program or a continuation or expansion of existing program.\n**(6)**\nThe total amount of funding that will be needed over the life of the program.\n**(7)**\nThe expected period of performance for the program using the requested funds.\n**(8)**\nThe total period of performance of the program up until the time of the request.\n**(9)**\nThe name of the implementing entity or proposed implementing entity of the program, if selected, and other identifying information about the entity, such as whether the entity is a private or public entity or a United States-based or international entity.\n**(10)**\nThe intended objectives of the program.\n**(11)**\nA description of key components or activities of the program.\n**(12)**\nA description of consultations with the chief of mission of the respective country or countries.\n**(13)**\nWhether the program has a significant underspend or overspend of funds based on projected spend rates under the program.\n**(14)**\nWhether a performance improvement plan or other additional administrative oversight has been established for the program.\n##### (c) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Affairs and the Committee on Appropriations of the House of Representatives; and\n**(2)**\nthe Committee on Foreign Relations and the Committee on Appropriations of the Senate.",
      "versionDate": "2026-02-23",
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
        "name": "International Affairs",
        "updateDate": "2026-02-27T16:36:52Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7641ih.xml"
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
      "title": "Transparency in Foreign Assistance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T08:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transparency in Foreign Assistance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T08:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for a pilot program to require congressional notification of additional information for certain foreign assistance programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T08:48:40Z"
    }
  ]
}
```
