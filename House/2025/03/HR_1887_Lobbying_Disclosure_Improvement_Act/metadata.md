# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1887?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1887
- Title: Lobbying Disclosure Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 1887
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2025-12-05T21:42:43Z
- Update date including text: 2025-12-05T21:42:43Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1887",
    "number": "1887",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Lobbying Disclosure Improvement Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:42:43Z",
    "updateDateIncludingText": "2025-12-05T21:42:43Z"
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
          "date": "2025-03-05T15:04:30Z",
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
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1887ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1887\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Neguse (for himself and Mr. Roy ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Lobbying Disclosure Act of 1995 to require certain disclosures by registrants regarding exemptions under the Foreign Agents Registration Act of 1938, as amended.\n#### 1. Short title\nThis Act may be cited as the Lobbying Disclosure Improvement Act .\n#### 2. Registrant disclosure regarding foreign agent registration exemption\nSection 4(b) of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1603(b) ) is amended\u2014\n**(1)**\nin paragraph (6), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (7), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(8) a statement as to whether the registrant is exempt under section 3(h) of the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 613(h) ). .",
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
        "actionDate": "2025-11-03",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 258."
      },
      "number": "865",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Lobbying Disclosure Improvement Act",
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
            "updateDate": "2025-08-07T17:51:03Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-08-07T17:51:03Z"
          },
          {
            "name": "Public participation and lobbying",
            "updateDate": "2025-08-07T17:51:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-13T16:11:13Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1887ih.xml"
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
      "title": "Lobbying Disclosure Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lobbying Disclosure Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Lobbying Disclosure Act of 1995 to require certain disclosures by registrants regarding exemptions under the Foreign Agents Registration Act of 1938, as amended.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:48:33Z"
    }
  ]
}
```
