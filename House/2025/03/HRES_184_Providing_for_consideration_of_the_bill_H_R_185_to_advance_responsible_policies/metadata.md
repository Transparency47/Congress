# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/184?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/184
- Title: Providing for consideration of the bill (H.R. 185) to advance responsible policies.
- Congress: 119
- Bill type: HRES
- Bill number: 184
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-04-06T14:42:57Z
- Update date including text: 2026-04-06T14:42:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Rules.
- 2025-03-03 - Committee: Submitted in House
- Latest action: 2025-03-03: Submitted in House

## Actions

- 2025-03-03 - IntroReferral: Referred to the House Committee on Rules.
- 2025-03-03 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/184",
    "number": "184",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "P000034",
        "district": "6",
        "firstName": "Frank",
        "fullName": "Rep. Pallone, Frank [D-NJ-6]",
        "lastName": "Pallone",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies.",
    "type": "HRES",
    "updateDate": "2026-04-06T14:42:57Z",
    "updateDateIncludingText": "2026-04-06T14:42:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:08:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres184ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 184\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Pallone submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 185) to advance responsible policies.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 185) to advance responsible policies. All points of order against consideration of the bill are waived. The amendment in the nature of a substitute specified in section 3 of this resolution shall be considered as adopted. The bill, as amended, shall be considered as read. All points of order against provisions in the bill, as amended, are waived. The previous question shall be considered as ordered on the bill, as amended, and on any further amendment thereto, to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by the chair and ranking minority member of the Committee on Energy and Commerce or their respective designees; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX shall not apply to the consideration of H.R. 185.\n#### 3.\nThe amendment in the nature of a substitute referred to in the first section of this resolution is an amendment in the nature of a substitute consisting of the text of H.R. 1768 as introduced, modified by an amendment received for printing in the portion of the Congressional Record designated for that purpose in clause 8 of rule XVIII dated at least one day before the consideration of H.R. 185, if submitted by the ranking minority member of the Committee on Energy and Commerce. If more than one such amendment is submitted, then only the last amendment submitted shall be considered as the modification.",
      "versionDate": "2025-03-03",
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
            "updateDate": "2026-04-06T14:42:52Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2026-04-06T14:42:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-05-19T14:14:21Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres184ih.xml"
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
      "updateDate": "2025-03-04T12:48:30Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T09:06:15Z"
    }
  ]
}
```
