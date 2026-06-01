# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4209?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4209
- Title: TIME for Overdose Justice Act
- Congress: 119
- Bill type: S
- Bill number: 4209
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-04-13T13:33:03Z
- Update date including text: 2026-04-13T13:33:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4209",
    "number": "4209",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "TIME for Overdose Justice Act",
    "type": "S",
    "updateDate": "2026-04-13T13:33:03Z",
    "updateDateIncludingText": "2026-04-13T13:33:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T22:14:21Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4209is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4209\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Mr. Sullivan introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Controlled Substances Act to extend the limitations period for certain offenses resulting in death or serious bodily injury.\n#### 1. Short title\nThis Act may be cited as the Timely Investigation and Maximum Enforcement for Overdose Justice Act or the TIME for Overdose Justice Act .\n#### 2. Limitations\nSection 401(b) of the Controlled Substances Act ( 21 U.S.C. 841(b) ) is amended by adding at the end the following:\n(8) Notwithstanding section 3282 of title 18, United States Code, an indictment may be found or an information instituted at any time without limitation for any violation of subsection (a) described in paragraph (1) of this subsection, or conspiracy to commit a violation of such subsection (a) under section 406, if death or serious bodily injury results from the use of such substance. .",
      "versionDate": "2026-03-25",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-13T13:33:02Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4209is.xml"
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
      "title": "TIME for Overdose Justice Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-09T02:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TIME for Overdose Justice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T02:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Timely Investigation and Maximum Enforcement for Overdose Justice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T02:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Controlled Substances Act to extend the limitations period for certain offenses resulting in death or serious bodily injury.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T02:18:26Z"
    }
  ]
}
```
