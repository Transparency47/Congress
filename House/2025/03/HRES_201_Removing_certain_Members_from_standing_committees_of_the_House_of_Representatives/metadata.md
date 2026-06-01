# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/201?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/201
- Title: Removing certain Members from standing committees of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 201
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-03-11T08:07:11Z
- Update date including text: 2025-03-11T08:07:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-03-06 - IntroReferral: Submitted in House
- Latest action: 2025-03-06: Submitted in House

## Actions

- 2025-03-06 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-03-06 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/201",
    "number": "201",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "O000175",
        "district": "5",
        "firstName": "Andrew",
        "fullName": "Rep. Ogles, Andrew [R-TN-5]",
        "lastName": "Ogles",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Removing certain Members from standing committees of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-03-11T08:07:11Z",
    "updateDateIncludingText": "2025-03-11T08:07:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Ethics Committee",
          "systemCode": "hsso00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ethics.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:09:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ethics Committee",
      "systemCode": "hsso00",
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
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres201ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 201\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Ogles submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nRemoving certain Members from standing committees of the House of Representatives.\nThat not later than one week following the passage of this resolution, the Sergeant at Arms of the House of Representatives shall provide a determination as to which Members ignored the Speaker\u2019s directive to leave the Well of the House on March 6, 2025, and those individuals shall, upon submission of that list to the Speaker, be removed from any standing committee on which they currently serve for the remainder of the 119th Congress.",
      "versionDate": "2025-03-06",
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
        "updateDate": "2025-03-10T17:59:50Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres201ih.xml"
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
      "title": "Removing certain Members from standing committees of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T09:48:18Z"
    },
    {
      "title": "Removing certain Members from standing committees of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-07T09:06:45Z"
    }
  ]
}
```
