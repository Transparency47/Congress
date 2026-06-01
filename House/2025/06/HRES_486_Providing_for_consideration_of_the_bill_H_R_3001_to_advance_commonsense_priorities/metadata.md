# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/486?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/486
- Title: Providing for consideration of the bill (H.R. 3001) to advance commonsense priorities.
- Congress: 119
- Bill type: HRES
- Bill number: 486
- Origin chamber: House
- Introduced date: 2025-06-06
- Update date: 2026-01-08T16:37:20Z
- Update date including text: 2026-01-08T16:37:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-06: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Rules.
- 2025-06-06 - IntroReferral: Submitted in House
- 2025-06-06 - IntroReferral: Submitted in House
- 2025-12-10 - Discharge: Motion to Discharge Committee filed by Mr. Fitzpatrick. Petition No: 119-12. (<a href="https://clerk.house.gov/DischargePetition/2025121012">Discharge petition</a> text with signatures.)
- Latest action: 2025-06-06: Submitted in House

## Actions

- 2025-06-06 - IntroReferral: Referred to the House Committee on Rules.
- 2025-06-06 - IntroReferral: Submitted in House
- 2025-06-06 - IntroReferral: Submitted in House
- 2025-12-10 - Discharge: Motion to Discharge Committee filed by Mr. Fitzpatrick. Petition No: 119-12. (<a href="https://clerk.house.gov/DischargePetition/2025121012">Discharge petition</a> text with signatures.)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-06",
    "latestAction": {
      "actionDate": "2025-06-06",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/486",
    "number": "486",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 3001) to advance commonsense priorities.",
    "type": "HRES",
    "updateDate": "2026-01-08T16:37:20Z",
    "updateDateIncludingText": "2026-01-08T16:37:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H17000",
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to Discharge Committee filed by Mr. Fitzpatrick. Petition No: 119-12. (<a href=\"https://clerk.house.gov/DischargePetition/2025121012\">Discharge petition</a> text with signatures.)",
      "type": "Discharge"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-06",
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
      "actionDate": "2025-06-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-06",
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
        "item": {
          "date": "2025-06-06T13:01:10Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres486ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 486\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Mr. Fitzpatrick submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 3001) to advance commonsense priorities.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 3001) to advance commonsense priorities. All points of order against consideration of the bill are waived. The amendment in the nature of a substitute specified in section 3 of this resolution shall be considered as adopted. The bill, as amended, shall be considered as read. All points of order against provisions in the bill, as amended, are waived. The previous question shall be considered as ordered on the bill, as amended, and on any further amendment thereto, to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by Representative Fitzpatrick of Pennsylvania or a designee and an opponent; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX shall not apply to the consideration of H.R. 3001.\n#### 3.\nThe amendment in the nature of a substitute referred to in the first section of this resolution is an amendment in the nature of a substitute received for printing in the portion of the Congressional Record designated for that purpose in clause 8 of rule XVIII dated at least one day before the consideration of H.R. 3001, if submitted by Representative Fitzpatrick of Pennsylvania. If more than one such amendment is submitted, then only the last amendment submitted shall be considered as adopted.",
      "versionDate": "2025-06-06",
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
        "updateDate": "2025-06-18T14:07:03Z"
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
      "date": "2025-06-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres486ih.xml"
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
      "title": "Providing for consideration of the bill (H.R. 3001) to advance commonsense priorities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-07T08:18:25Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 3001) to advance commonsense priorities.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-07T08:06:05Z"
    }
  ]
}
```
