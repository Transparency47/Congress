# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4099?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4099
- Title: Whistleblower Anti-Gag Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4099
- Origin chamber: Senate
- Introduced date: 2026-03-16
- Update date: 2026-04-01T20:15:21Z
- Update date including text: 2026-04-01T20:15:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in Senate
- 2026-03-16 - IntroReferral: Introduced in Senate
- 2026-03-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-03-16: Introduced in Senate

## Actions

- 2026-03-16 - IntroReferral: Introduced in Senate
- 2026-03-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4099",
    "number": "4099",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Whistleblower Anti-Gag Act of 2026",
    "type": "S",
    "updateDate": "2026-04-01T20:15:21Z",
    "updateDateIncludingText": "2026-04-01T20:15:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-16",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T20:16:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4099is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4099\nIN THE SENATE OF THE UNITED STATES\nMarch 16, 2026 Mr. Grassley introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 5, United States Code, to ensure that Federal employees are fully informed of their whistleblower rights.\n#### 1. Short title\nThis Act may be cited as the Whistleblower Anti-Gag Act of 2026 .\n#### 2. Anti-gag provision\nSection 2302(a)(2)(C)(i) of title 5, United States Code, is amended by inserting or in the case of a nondisclosure policy, form, or agreement described under subsection (b)(13) after (D) .",
      "versionDate": "2026-03-16",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-01T20:15:20Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4099is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to ensure that Federal employees are fully informed of their whistleblower rights.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:38Z"
    },
    {
      "title": "Whistleblower Anti-Gag Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Whistleblower Anti-Gag Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:19Z"
    }
  ]
}
```
