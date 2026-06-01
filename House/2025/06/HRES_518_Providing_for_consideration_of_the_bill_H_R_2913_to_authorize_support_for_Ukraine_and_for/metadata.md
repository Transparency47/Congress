# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/518?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/518
- Title: Providing for consideration of the bill (H.R. 2913) to authorize support for Ukraine, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 518
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2026-05-14T08:08:48Z
- Update date including text: 2026-05-14T08:08:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Rules.
- 2025-06-17 - IntroReferral: Submitted in House
- 2025-06-17 - IntroReferral: Submitted in House
- 2025-07-17 - Discharge: Motion to Discharge Committee filed by Mr. Meeks. Petition No: 119-8. (<a href="https://clerk.house.gov/DischargePetition/2025071708">Discharge petition</a> text with signatures.)
- 2026-05-13 - Discharge: Motion to discharge the Committee on Rules filed by Mr. Meeks. Assigned to the Discharge Calendar, Calendar No. 6.
- Latest action: 2025-06-17: Submitted in House

## Actions

- 2025-06-17 - IntroReferral: Referred to the House Committee on Rules.
- 2025-06-17 - IntroReferral: Submitted in House
- 2025-06-17 - IntroReferral: Submitted in House
- 2025-07-17 - Discharge: Motion to Discharge Committee filed by Mr. Meeks. Petition No: 119-8. (<a href="https://clerk.house.gov/DischargePetition/2025071708">Discharge petition</a> text with signatures.)
- 2026-05-13 - Discharge: Motion to discharge the Committee on Rules filed by Mr. Meeks. Assigned to the Discharge Calendar, Calendar No. 6.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/518",
    "number": "518",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001137",
        "district": "5",
        "firstName": "Gregory",
        "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
        "lastName": "Meeks",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 2913) to authorize support for Ukraine, and for other purposes.",
    "type": "HRES",
    "updateDate": "2026-05-14T08:08:48Z",
    "updateDateIncludingText": "2026-05-14T08:08:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12450",
      "actionDate": "2026-05-13",
      "calendarNumber": {
        "calendar": "D00006"
      },
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
      "text": "Motion to discharge the Committee on Rules filed by Mr. Meeks. Assigned to the Discharge Calendar, Calendar No. 6.",
      "type": "Discharge"
    },
    {
      "actionCode": "H17000",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to Discharge Committee filed by Mr. Meeks. Petition No: 119-8. (<a href=\"https://clerk.house.gov/DischargePetition/2025071708\">Discharge petition</a> text with signatures.)",
      "type": "Discharge"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
            "date": "2026-05-13T14:22:14Z",
            "name": "Unknown"
          },
          {
            "date": "2025-06-17T15:02:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres518ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 518\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Meeks (for himself and Mr. Hoyer ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 2913) to authorize support for Ukraine, and for other purposes.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 2913) to authorize support for Ukraine, and for other purposes. All points of order against consideration of the bill are waived. The bill shall be considered as read. All points of order against provisions in the bill are waived. The previous question shall be considered as ordered on the bill and on any amendment thereto to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by the chair and ranking minority member of the Committee on Foreign Affairs or their respective designees; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX and clause 8 of rule XX shall not apply to the consideration of H.R. 2913.\n#### 3.\nThe Clerk shall transmit to the Senate a message that the House has passed H.R. 2913 no later than one week after passage.",
      "versionDate": "2025-06-17",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-07-02T13:17:21Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres518ih.xml"
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
      "title": "Providing for consideration of the bill (H.R. 2913) to authorize support for Ukraine, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-18T08:18:24Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 2913) to authorize support for Ukraine, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-18T08:05:45Z"
    }
  ]
}
```
