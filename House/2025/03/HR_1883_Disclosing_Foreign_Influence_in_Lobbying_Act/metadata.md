# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1883?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1883
- Title: Disclosing Foreign Influence in Lobbying Act
- Congress: 119
- Bill type: HR
- Bill number: 1883
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-05-01T08:08:56Z
- Update date including text: 2026-05-01T08:08:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1883",
    "number": "1883",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001215",
        "district": "1",
        "firstName": "Mariannette",
        "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
        "lastName": "Miller-Meeks",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Disclosing Foreign Influence in Lobbying Act",
    "type": "HR",
    "updateDate": "2026-05-01T08:08:56Z",
    "updateDateIncludingText": "2026-05-01T08:08:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:05:25Z",
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
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1883ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1883\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mrs. Miller-Meeks (for herself and Mr. Krishnamoorthi ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Lobbying Disclosure Act of 1995 to clarify a provision relating to certain contents of registrations under that Act.\n#### 1. Short title\nThis Act may be cited as the Disclosing Foreign Influence in Lobbying Act .\n#### 2. Clarification of contents of registration\nSection 4(b) of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1603(b) ) is amended\u2014\n**(1)**\nin paragraph (6), by striking and at the end; and\n**(2)**\nin paragraph (7), by striking the offense. and inserting the following:\nthe offense; and (8) notwithstanding paragraph (4), the name and address of each government of a foreign country (including any agency or subdivision of a government of a foreign country, such as a regional or municipal unit of government) and foreign political party, other than the client, that participates in the direction, planning, supervision, or control of any lobbying activities of the registrant. .",
      "versionDate": "2025-03-05",
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
        "actionDate": "2025-12-17",
        "actionTime": "10:21:51",
        "text": "Held at the desk."
      },
      "number": "856",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Disclosing Foreign Influence in Lobbying Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Government information and archives",
            "updateDate": "2025-08-07T17:50:27Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-08-07T17:50:27Z"
          },
          {
            "name": "Public participation and lobbying",
            "updateDate": "2025-08-07T17:50:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-13T15:24:14Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1883ih.xml"
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
      "title": "Disclosing Foreign Influence in Lobbying Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disclosing Foreign Influence in Lobbying Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Lobbying Disclosure Act of 1995 to clarify a provision relating to certain contents of registrations under that Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:18:28Z"
    }
  ]
}
```
