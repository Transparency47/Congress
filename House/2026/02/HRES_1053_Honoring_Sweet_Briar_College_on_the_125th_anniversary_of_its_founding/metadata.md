# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1053?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1053
- Title: Honoring Sweet Briar College on the 125th anniversary of its founding.
- Congress: 119
- Bill type: HRES
- Bill number: 1053
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-02-18T16:32:41Z
- Update date including text: 2026-02-18T16:32:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-02-10 - IntroReferral: Submitted in House
- 2026-02-10 - IntroReferral: Submitted in House
- Latest action: 2026-02-10: Submitted in House

## Actions

- 2026-02-10 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-02-10 - IntroReferral: Submitted in House
- 2026-02-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1053",
    "number": "1053",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001239",
        "district": "5",
        "firstName": "John",
        "fullName": "Rep. McGuire, John J. [R-VA-5]",
        "lastName": "McGuire",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Honoring Sweet Briar College on the 125th anniversary of its founding.",
    "type": "HRES",
    "updateDate": "2026-02-18T16:32:41Z",
    "updateDateIncludingText": "2026-02-18T16:32:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T15:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1053ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1053\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Mr. McGuire submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nHonoring Sweet Briar College on the 125th anniversary of its founding.\nThat the House of Representatives\u2014\n**(1)**\nhereby commends Sweet Briar College on the occasion of its 125th anniversary;\n**(2)**\nsupports the designation of Sweet Briar College Charter Day in honor of such anniversary;\n**(3)**\nreminds this and future generations of the relevance and importance of Sweet Briar College\u2019s vital mission and its enduring commitments to educating our female leaders of tomorrow; and\n**(4)**\nrecognizes Sweet Briar College\u2019s innumerable contributions to the Commonwealth of Virginia through its commitment to education, its numerous distinguished alumnae, and its enduring mission to maintain a community where women lead, making it undeniably a Category of One.",
      "versionDate": "2026-02-10",
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
        "name": "Education",
        "updateDate": "2026-02-18T16:32:41Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1053ih.xml"
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
      "title": "Honoring Sweet Briar College on the 125th anniversary of its founding.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:33:50Z"
    },
    {
      "title": "Honoring Sweet Briar College on the 125th anniversary of its founding.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T09:06:28Z"
    }
  ]
}
```
