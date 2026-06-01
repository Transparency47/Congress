# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/202?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/202
- Title: Censuring Representative Lauren Boebert of Colorado for her recent disparaging and derogatory comments about Representative Al Green of Texas.
- Congress: 119
- Bill type: HRES
- Bill number: 202
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2025-05-07T14:31:48Z
- Update date including text: 2025-05-07T14:31:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-03-10 - IntroReferral: Submitted in House
- 2025-03-10 - IntroReferral: Submitted in House
- Latest action: 2025-03-10: Submitted in House

## Actions

- 2025-03-10 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-03-10 - IntroReferral: Submitted in House
- 2025-03-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/202",
    "number": "202",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "H001085",
        "district": "6",
        "firstName": "Chrissy",
        "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
        "lastName": "Houlahan",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Censuring Representative Lauren Boebert of Colorado for her recent disparaging and derogatory comments about Representative Al Green of Texas.",
    "type": "HRES",
    "updateDate": "2025-05-07T14:31:48Z",
    "updateDateIncludingText": "2025-05-07T14:31:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:07:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres202ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 202\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Ms. Houlahan submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nCensuring Representative Lauren Boebert of Colorado for her recent disparaging and derogatory comments about Representative Al Green of Texas.\nThat\u2014\n**(1)**\nRepresentative Lauren Boebert be censured;\n**(2)**\nRepresentative Lauren Boebert forthwith present herself in the well of the House of Representatives for the pronouncement of censure; and\n**(3)**\n) Representative Lauren Bobert be censured with the public reading of this resolution by the Speaker.",
      "versionDate": "2025-03-10",
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
        "updateDate": "2025-05-07T14:31:48Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres202ih.xml"
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
      "title": "Censuring Representative Lauren Boebert of Colorado for her recent disparaging and derogatory comments about Representative Al Green of Texas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-11T08:18:37Z"
    },
    {
      "title": "Censuring Representative Lauren Boebert of Colorado for her recent disparaging and derogatory comments about Representative Al Green of Texas.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T08:05:26Z"
    }
  ]
}
```
