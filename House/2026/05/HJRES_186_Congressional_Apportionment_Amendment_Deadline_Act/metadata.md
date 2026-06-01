# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/186?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/186
- Title: Congressional Apportionment Amendment Deadline Act
- Congress: 119
- Bill type: HJRES
- Bill number: 186
- Origin chamber: House
- Introduced date: 2026-05-14
- Update date: 2026-05-29T14:26:39Z
- Update date including text: 2026-05-29T14:26:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-14: Introduced in House

## Actions

- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/186",
    "number": "186",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Congressional Apportionment Amendment Deadline Act",
    "type": "HJRES",
    "updateDate": "2026-05-29T14:26:39Z",
    "updateDateIncludingText": "2026-05-29T14:26:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-14",
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
      "actionDate": "2026-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-14",
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
          "date": "2026-05-14T14:06:00Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres186ih.xml",
      "text": "IA\n119th CONGRESS\n2d Session\nH. J. RES. 186\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2026 Mr. Issa submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nEstablishing a ratification deadline for the Congressional Apportionment Amendment.\n#### 1. Short title\nThis joint resolution may be cited as the Congressional Apportionment Amendment Deadline Act .\n#### 2. Ratification deadline\n##### (a) In general\nNotwithstanding the absence of a ratification deadline at the time of proposal, the Congressional Apportionment Amendment shall be valid to all intents and purposes as part of the Constitution only if it is ratified by the legislatures of three-fourths of the several States not later than December 31, 2026.\n##### (b) Validity after deadline\nAny ratification of such amendment occurring after the date specified in subsection (a) shall not be valid for purposes of adopting the amendment.\n#### 3. Congressional authority\nCongress asserts its authority under Article V of the Constitution of the United States to establish reasonable conditions for the ratification of proposed amendments, including the imposition of a ratification deadline.",
      "versionDate": "2026-05-14",
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
        "updateDate": "2026-05-29T14:26:38Z"
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
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres186ih.xml"
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
      "title": "Congressional Apportionment Amendment Deadline Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T08:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Congressional Apportionment Amendment Deadline Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-15T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Establishing a ratification deadline for the Congressional Apportionment Amendment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:18:36Z"
    }
  ]
}
```
