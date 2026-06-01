# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3273?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3273
- Title: American Allies Protection Act
- Congress: 119
- Bill type: S
- Bill number: 3273
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2025-12-19T18:05:03Z
- Update date including text: 2025-12-19T18:05:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3273",
    "number": "3273",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "American Allies Protection Act",
    "type": "S",
    "updateDate": "2025-12-19T18:05:03Z",
    "updateDateIncludingText": "2025-12-19T18:05:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T20:35:56Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3273is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3273\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Budd introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit awarding grants to States that arrest certain foreign officials in cooperation with the International Criminal Court, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Allies Protection Act .\n#### 2. Penalties on state or local enforcement of icc actions\n##### (a) Penalties\nExcept as provided in subsection (b), if any public official, employee, or agent of a State, a territory, or the District of Columbia, or any political subdivision thereof, arrests, detains, or otherwise deprives the liberty of a current or former foreign government official of a member of the North Atlantic Treaty Organization or of a government designated as a Major Non-NATO Ally based solely on a warrant, indictment, summons, or other process issued by the International Criminal Court or cooperates with, or provides assistance to, the International Criminal Court in effectuating such an arrest or detention, with respect to the fiscal year beginning on the first October 1 occurring after the date of enactment of the Act, and each fiscal year thereafter, the Attorney General may not award, renew, or extend a grant to the State, territory, the District of Columbia, or any political subdivision thereof, for a four-year period.\n##### (b) Waiver authority\nThe Attorney General may waive the application of subsection (a) to a grant award if the President certifies to the Committee on the Judiciary , the Committee on Foreign Relations , and the Committee on Armed Services of the Senate and the Committee on the Judiciary , the Committee on Foreign Affairs , and the Committee on Armed Services of the House of Representatives that an act described in subsection (a) is essential to the national security interests of the United States, including a detailed justification for the necessity of the act.",
      "versionDate": "2025-11-20",
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
        "name": "International Affairs",
        "updateDate": "2025-12-19T18:05:03Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3273is.xml"
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
      "title": "American Allies Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Allies Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit awarding grants to States that arrest certain foreign officials in cooperation with the International Criminal Court, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:03:55Z"
    }
  ]
}
```
