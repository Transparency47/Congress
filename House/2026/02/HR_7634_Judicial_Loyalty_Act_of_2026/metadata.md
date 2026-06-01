# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7634?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7634
- Title: Judicial Loyalty Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7634
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-03-11T14:54:29Z
- Update date including text: 2026-03-11T14:54:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-20: Introduced in House

## Actions

- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7634",
    "number": "7634",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "S001212",
        "district": "8",
        "firstName": "Pete",
        "fullName": "Rep. Stauber, Pete [R-MN-8]",
        "lastName": "Stauber",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Judicial Loyalty Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-11T14:54:29Z",
    "updateDateIncludingText": "2026-03-11T14:54:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
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
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-20",
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
          "date": "2026-02-20T16:33:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7634ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7634\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mr. Stauber introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to provide for a limitation on the nationality of persons eligible to serve as judges of the United States.\n#### 1. Short title\nThis Act may be cited as the Judicial Loyalty Act of 2026 .\n#### 2. Limitation on eligibility to serve as a judge of the United States\n##### (a) In general\nChapter 21 of title 28, United States Code, is amended by adding at the end the following:\n464. Limitation on nationality of eligible persons No person shall be eligible to be appointed as a judge of the United States unless that person is a natural born citizen of the United States. .\n##### (b) Clerical amendment\nThe table of sections for such chapter is amended by adding at the end the following:\n464. Limitation on nationality of eligible persons. .\n#### 3. Requirement to resign\nIn the case of any judge of the United States who is a United States citizen and who also is a citizen of a foreign country, if that judge does not officially renounce their foreign citizenship by not later than 60 days after the date of enactment of this Act, that judge may not continue in office.",
      "versionDate": "2026-02-20",
      "versionType": "Introduced in House"
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
        "name": "Law",
        "updateDate": "2026-03-11T14:54:29Z"
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
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7634ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Judicial Loyalty Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T06:38:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Judicial Loyalty Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-10T06:38:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 28, United States Code, to provide for a limitation on the nationality of persons eligible to serve as judges of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-10T06:33:28Z"
    }
  ]
}
```
