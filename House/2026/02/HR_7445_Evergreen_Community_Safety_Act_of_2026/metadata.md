# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7445?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7445
- Title: Evergreen Community Safety Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7445
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-03-09T12:09:15Z
- Update date including text: 2026-03-09T12:09:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7445",
    "number": "7445",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000620",
        "district": "7",
        "firstName": "Brittany",
        "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
        "lastName": "Pettersen",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Evergreen Community Safety Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-09T12:09:15Z",
    "updateDateIncludingText": "2026-03-09T12:09:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
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
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:03:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7445ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7445\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Ms. Pettersen introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to provide special rules for the time period for complying court orders or warrants to disclose information for certain providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Evergreen Community Safety Act of 2026 .\n#### 2. Time period for complying with a court order or warrant for certain providers\nSection 2703 of title 18, United States Code, is amended by adding at the end the following:\n(i) Special rules for covered providers (1) In general A warrant or a court order for disclosure issued under this section shall require that a covered provider disclose the contents of a wire or electronic communication, or the records or other information sought not later than 72 hours after the issuance of the warrant or court order. (2) Extension A court may extend the time period under paragraph (1) by periods of not more than 7 days if the information sought is voluminous or complex. (3) Motions to quash or modify The time period for a covered provider to file a motion under subsection (g)(2) is 48 hours. (4) Civil action Notwithstanding any other provision of law, including subsection (e), an individual who is harmed by the failure of a covered provider to comply with a warrant or court order for disclosure in the time period provided by the court may bring a civil action in an appropriate district court of the United States seeking injunctive relief and damages. (5) Definition The term covered provider means a provider of electronic communication service or remote computing service that has 1,000,000 or more users, subscribers, or customers. .",
      "versionDate": "2026-02-09",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-03-09T12:09:15Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7445ih.xml"
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
      "title": "Evergreen Community Safety Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Evergreen Community Safety Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-05T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to provide special rules for the time period for complying court orders or warrants to disclose information for certain providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-05T04:03:29Z"
    }
  ]
}
```
