# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2139?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2139
- Title: PRIME Act
- Congress: 119
- Bill type: S
- Bill number: 2139
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2025-09-15T18:26:29Z
- Update date including text: 2025-09-15T18:26:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2139",
    "number": "2139",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "PRIME Act",
    "type": "S",
    "updateDate": "2025-09-15T18:26:29Z",
    "updateDateIncludingText": "2025-09-15T18:26:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-06-18T19:27:31Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2139is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2139\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Sheehy introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo provide for expedited procurement for experimental purposes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Procurement Reform for Immediate Military Equipment Act or the PRIME Act .\n#### 2. Modifications to procurement for experimental purposes\nSection 4023 of title 10, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking ordnance, signal, chemical activity, transportation, energy, medical, space flight, telecommunications, and aeronautical supplies, including parts and accessories, and designs thereof, and inserting demonstrations, prototypes, products, supplies, parts, accessories, auxiliary services, and design for defense-related articles ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby inserting or modified after may be made ; and\n**(B)**\nby inserting prototyping, after greater than necessary for ; and\n**(3)**\nby adding at the end the following new subsection:\n(c) Follow-On production contracts or transactions Purchases under this section may allow for follow-on production contracts or transactions without the use of competitive procedures or further justification, even if explicit notification was not provided, if a combatant command submits a written determination that the purchased item successfully completed the experiment and intends to field the item. .",
      "versionDate": "2025-06-18",
      "versionType": "Introduced in Senate"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-15T18:26:29Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2139is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "PRIME Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-02T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PRIME Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Procurement Reform for Immediate Military Equipment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the expedited procurement for experimental purposes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:19:06Z"
    }
  ]
}
```
