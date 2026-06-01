# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/801?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/801
- Title: Providing for the consideration of the joint resolution (H. J. Res. 12) proposing an amendment to the Constitution of the United States to limit the number of terms that a Member of Congress may serve.
- Congress: 119
- Bill type: HRES
- Bill number: 801
- Origin chamber: House
- Introduced date: 2025-10-10
- Update date: 2025-12-15T16:51:00Z
- Update date including text: 2025-12-15T16:51:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-10: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on Rules.
- 2025-10-10 - IntroReferral: Submitted in House
- 2025-10-10 - IntroReferral: Submitted in House
- Latest action: 2025-10-10: Submitted in House

## Actions

- 2025-10-10 - IntroReferral: Referred to the House Committee on Rules.
- 2025-10-10 - IntroReferral: Submitted in House
- 2025-10-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-10",
    "latestAction": {
      "actionDate": "2025-10-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/801",
    "number": "801",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "L000596",
        "district": "13",
        "firstName": "Anna Paulina",
        "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
        "lastName": "Luna",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Providing for the consideration of the joint resolution (H. J. Res. 12) proposing an amendment to the Constitution of the United States to limit the number of terms that a Member of Congress may serve.",
    "type": "HRES",
    "updateDate": "2025-12-15T16:51:00Z",
    "updateDateIncludingText": "2025-12-15T16:51:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
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
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-10",
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
          "date": "2025-10-10T16:32:50Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres801ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 801\nIN THE HOUSE OF REPRESENTATIVES\nOctober 10, 2025 Mrs. Luna submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for the consideration of the joint resolution (H. J. Res. 12) proposing an amendment to the Constitution of the United States to limit the number of terms that a Member of Congress may serve.\nThat immediately upon adoption of this resolution, without intervention of any point of order, the House shall proceed to the consideration in the House of the joint resolution (H. J. Res. 12) proposing an amendment to the Constitution of the United States to limit the number of terms that a Member of Congress may serve. The resolution shall be considered as read. The previous question shall be considered as ordered on the resolution to adoption without intervening motion or demand for division of the question except one hour of debate equally divided and controlled by the chair and ranking minority member of the Committee on the Judiciary or their respective designees.\n#### 2.\nClause 1(c) of rule XIX shall not apply to the consideration of H. J. Res. 12.",
      "versionDate": "2025-10-10",
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
        "updateDate": "2025-12-15T16:51:00Z"
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
      "date": "2025-10-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres801ih.xml"
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
      "title": "Providing for the consideration of the joint resolution (H. J. Res. 12) proposing an amendment to the Constitution of the United States to limit the number of terms that a Member of Congress may serve.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-11T08:18:17Z"
    },
    {
      "title": "Providing for the consideration of the joint resolution (H. J. Res. 12) proposing an amendment to the Constitution of the United States to limit the number of terms that a Member of Congress may serve.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-11T08:05:32Z"
    }
  ]
}
```
