# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1101?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1101
- Title: Censuring Representative Tony Gonzales of Texas.
- Congress: 119
- Bill type: HRES
- Bill number: 1101
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-03-09T15:01:51Z
- Update date including text: 2026-03-09T15:01:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Ethics.
- 2026-03-04 - IntroReferral: Submitted in House
- 2026-03-04 - IntroReferral: Submitted in House
- Latest action: 2026-03-04: Submitted in House

## Actions

- 2026-03-04 - IntroReferral: Referred to the House Committee on Ethics.
- 2026-03-04 - IntroReferral: Submitted in House
- 2026-03-04 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1101",
    "number": "1101",
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
    "title": "Censuring Representative Tony Gonzales of Texas.",
    "type": "HRES",
    "updateDate": "2026-03-09T15:01:51Z",
    "updateDateIncludingText": "2026-03-09T15:01:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
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
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:03:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1101ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1101\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Mrs. Luna submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nCensuring Representative Tony Gonzales of Texas.\nThat\u2014\n**(1)**\nthe House of Representatives hereby censures Representative Tony Gonzales of Texas for conduct that has brought discredit upon the House;\n**(2)**\nRepresentative Tony Gonzales shall present himself in the well of the House for the pronouncement of censure; and\n**(3)**\nthis resolution be entered into the Journal of the House as an expression of the House\u2019s condemnation of the conduct described herein.",
      "versionDate": "2026-03-04",
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
        "updateDate": "2026-03-09T15:01:51Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1101ih.xml"
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
      "title": "Censuring Representative Tony Gonzales of Texas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-05T09:18:25Z"
    },
    {
      "title": "Censuring Representative Tony Gonzales of Texas.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T09:06:32Z"
    }
  ]
}
```
