# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1232?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1232
- Title: Amending the Rules of the House of Representatives to permit individuals to wear denim clothing on the floor of the House on the last Wednesday of April of each year.
- Congress: 119
- Bill type: HRES
- Bill number: 1232
- Origin chamber: House
- Introduced date: 2026-04-29
- Update date: 2026-05-15T17:13:29Z
- Update date including text: 2026-05-15T17:13:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Rules.
- 2026-04-29 - IntroReferral: Submitted in House
- Latest action: 2026-04-29: Submitted in House

## Actions

- 2026-04-29 - IntroReferral: Referred to the House Committee on Rules.
- 2026-04-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1232",
    "number": "1232",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001160",
        "district": "4",
        "firstName": "Gwen",
        "fullName": "Rep. Moore, Gwen [D-WI-4]",
        "lastName": "Moore",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Amending the Rules of the House of Representatives to permit individuals to wear denim clothing on the floor of the House on the last Wednesday of April of each year.",
    "type": "HRES",
    "updateDate": "2026-05-15T17:13:29Z",
    "updateDateIncludingText": "2026-05-15T17:13:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-29",
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
      "actionCode": "1025",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
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
          "date": "2026-04-29T13:03:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1232ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1232\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2026 Ms. Moore of Wisconsin submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nAmending the Rules of the House of Representatives to permit individuals to wear denim clothing on the floor of the House on the last Wednesday of April of each year.\n#### 1. Permitting the wearing of denim clothing on the House floor in certain cases\nClause 5 of rule XVII of the Rules of the House of Representatives is amended by inserting A person on the floor of the House may wear denim clothing on the last Wednesday of April of each year. before the last sentence.",
      "versionDate": "2026-04-29",
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
        "updateDate": "2026-05-15T17:13:28Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1232ih.xml"
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
      "title": "Amending the Rules of the House of Representatives to permit individuals to wear denim clothing on the floor of the House on the last Wednesday of April of each year.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T09:48:53Z"
    },
    {
      "title": "Amending the Rules of the House of Representatives to permit individuals to wear denim clothing on the floor of the House on the last Wednesday of April of each year.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T08:06:52Z"
    }
  ]
}
```
