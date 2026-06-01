# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1771?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1771
- Title: Larry Henderson Act
- Congress: 119
- Bill type: S
- Bill number: 1771
- Origin chamber: Senate
- Introduced date: 2025-05-14
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in Senate
- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-14: Introduced in Senate

## Actions

- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1771",
    "number": "1771",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Larry Henderson Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-14",
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
      "actionDate": "2025-05-14",
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
          "date": "2025-05-15T00:53:49Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1771is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1771\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2025 Mr. Moreno introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to impose mandatory minimum penalties for assaulting officers and employees of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Larry Henderson Act .\n#### 2. Mandatory minimum penalties for assaulting officers and employees of the United States\nSection 111 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), in the matter preceding subsection (b), by striking only and all that follows through the period at the end and inserting any bodily harm or bodily injury, be fined under this title and imprisoned not less than 20 years. ;\n**(2)**\nby striking subsection (b);\n**(3)**\nby redesignating subsection (c) as subsection (b); and\n**(4)**\nby adding at the end the following:\n(c) Exclusive applicability The provisions of this section shall apply exclusively to any act of assault, resistance, or impediment against any officer or employee of the United States engaged in or on account of the performance of official Federal duties. (d) Effect on State law The provisions of this section shall supersede any and all State laws insofar as they may now or hereafter relate to the assault, resistance, or impediment against any officer or employee of the United States engaged in or on account of the performance of official Federal duties. .\n#### 3. Technical and conforming amendments\nSection 3632(d)(4)(D)(v) of title 18, United States Code, is amended by striking Section 111(b) and inserting Section 111 .\n#### 4. Applicability\nThis Act, and the amendments made by this Act, shall apply to any offense committed on or after the date of enactment of this Act.",
      "versionDate": "2025-05-14",
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
        "updateDate": "2025-05-28T17:30:24Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1771is.xml"
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
      "title": "Larry Henderson Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Larry Henderson Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to impose mandatory minimum penalties for assaulting officers and employees of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:44Z"
    }
  ]
}
```
