# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/134?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/134
- Title: Providing for consideration of the bill (H.R. 185) to advance responsible policies.
- Congress: 119
- Bill type: HRES
- Bill number: 134
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-01-22T19:29:21Z
- Update date including text: 2026-01-22T19:29:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Rules.
- 2025-02-13 - Committee: Submitted in House
- Latest action: 2025-02-13: Submitted in House

## Actions

- 2025-02-13 - IntroReferral: Referred to the House Committee on Rules.
- 2025-02-13 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/134",
    "number": "134",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M000312",
        "district": "2",
        "firstName": "James",
        "fullName": "Rep. McGovern, James P. [D-MA-2]",
        "lastName": "McGovern",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies.",
    "type": "HRES",
    "updateDate": "2026-01-22T19:29:21Z",
    "updateDateIncludingText": "2026-01-22T19:29:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-13T14:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres134ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 134\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. McGovern submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 185) to advance responsible policies.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 185) to advance responsible policies. All points of order against consideration of the bill are waived. An amendment in the nature of a substitute received for printing in the portion of the Congressional Record designated for that purpose in clause 8 of rule XVIII dated at least one day before the day of consideration of H.R. 185, if submitted by the ranking minority member of the Committee on Rules, shall be considered as adopted. If more than one such amendment is submitted, then only the last amendment submitted shall be considered as adopted. The bill, as amended, shall be considered as read. All points of order against provisions in the bill, as amended, are waived. The previous question shall be considered as ordered on the bill, as amended, and on any further amendment thereto, to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by the majority leader and minority leader or their respective designees; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX and clause 8 of rule XX shall not apply to the consideration of H.R. 185.\n#### 3.\nThe Clerk shall transmit to the Senate a message that the House has passed H.R. 185 no later than one week after passage.",
      "versionDate": "2025-02-13",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "House of Representatives",
            "updateDate": "2026-01-22T19:29:21Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2026-01-22T19:29:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-18T14:45:06Z"
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
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres134ih.xml"
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
      "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T10:18:18Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T09:06:04Z"
    }
  ]
}
```
