# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/132?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/132
- Title: Censuring Representative Robert Garcia of California for inciting violence against a special government employee.
- Congress: 119
- Bill type: HRES
- Bill number: 132
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2025-02-18T16:21:51Z
- Update date including text: 2025-02-18T16:21:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-02-13 - Committee: Submitted in House
- Latest action: 2025-02-13: Submitted in House

## Actions

- 2025-02-13 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-02-13 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/132",
    "number": "132",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Censuring Representative Robert Garcia of California for inciting violence against a special government employee.",
    "type": "HRES",
    "updateDate": "2025-02-18T16:21:51Z",
    "updateDateIncludingText": "2025-02-18T16:21:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionCode": "H12100",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:08:40Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres132ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 132\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Ms. Mace submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nCensuring Representative Robert Garcia of California for inciting violence against a special government employee.\nThat\u2014\n**(1)**\nRepresentative Robert Garcia of California be censured;\n**(2)**\nRepresentative Robert Garcia forthwith present himself in the well of the House of Representatives for the pronouncement of censure; and\n**(3)**\nRepresentative Robert Garcia be censured with the public reading of this resolution by the Speaker.",
      "versionDate": "2025-02-13",
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
        "updateDate": "2025-02-18T16:21:50Z"
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
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres132ih.xml"
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
      "title": "Censuring Representative Robert Garcia of California for inciting violence against a special government employee.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T10:18:17Z"
    },
    {
      "title": "Censuring Representative Robert Garcia of California for inciting violence against a special government employee.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T09:05:59Z"
    }
  ]
}
```
