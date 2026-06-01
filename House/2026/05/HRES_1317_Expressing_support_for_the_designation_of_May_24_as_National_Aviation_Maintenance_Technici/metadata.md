# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1317?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1317
- Title: Expressing support for the designation of May 24 as "National Aviation Maintenance Technician Day" or "National AMT Day" to commemorate the work of aviation maintenance professionals.
- Congress: 119
- Bill type: HRES
- Bill number: 1317
- Origin chamber: House
- Introduced date: 2026-05-21
- Update date: 2026-05-22T10:18:35Z
- Update date including text: 2026-05-22T10:18:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-21: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-05-21 - IntroReferral: Submitted in House
- Latest action: 2026-05-21: Submitted in House

## Actions

- 2026-05-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-05-21 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-21",
    "latestAction": {
      "actionDate": "2026-05-21",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1317",
    "number": "1317",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001221",
        "district": "3",
        "firstName": "Hillary",
        "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
        "lastName": "Scholten",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Expressing support for the designation of May 24 as \"National Aviation Maintenance Technician Day\" or \"National AMT Day\" to commemorate the work of aviation maintenance professionals.",
    "type": "HRES",
    "updateDate": "2026-05-22T10:18:35Z",
    "updateDateIncludingText": "2026-05-22T10:18:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
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
          "date": "2026-05-21T14:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1317ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1317\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2026 Ms. Scholten submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nExpressing support for the designation of May 24 as National Aviation Maintenance Technician Day or National AMT Day to commemorate the work of aviation maintenance professionals.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the contributions of aviation maintenance technicians, who are important airline professionals; and\n**(2)**\nencourages a continued spotlight on the important aviation careers of such technicians, now and in the future.",
      "versionDate": "2026-05-21",
      "versionType": "IH"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1317ih.xml"
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
      "title": "Expressing support for the designation of May 24 as \"National Aviation Maintenance Technician Day\" or \"National AMT Day\" to commemorate the work of aviation maintenance professionals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:35Z"
    },
    {
      "title": "Expressing support for the designation of May 24 as \"National Aviation Maintenance Technician Day\" or \"National AMT Day\" to commemorate the work of aviation maintenance professionals.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T08:07:58Z"
    }
  ]
}
```
