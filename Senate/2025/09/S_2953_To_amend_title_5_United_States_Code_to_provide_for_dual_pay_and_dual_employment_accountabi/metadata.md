# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2953?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2953
- Title: Dismantling Double Dippers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2953
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2025-12-09T21:01:22Z
- Update date including text: 2025-12-09T21:01:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in Senate
- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-09-30: Introduced in Senate

## Actions

- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2953",
    "number": "2953",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Dismantling Double Dippers Act of 2025",
    "type": "S",
    "updateDate": "2025-12-09T21:01:22Z",
    "updateDateIncludingText": "2025-12-09T21:01:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T19:37:02Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "ID"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2953is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2953\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Ms. Ernst (for herself, Mr. Risch , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 5, United States Code, to provide for dual pay and dual employment accountability.\n#### 1. Short title\nThis Act may be cited as the Dismantling Double Dippers Act of 2025 .\n#### 2. Dual pay and dual employment accountability\n##### (a) In general\nSection 5533 of title 5, United States Code, is amended by adding at the end the following:\n(f) (1) Except as otherwise explicitly provided, an individual may not, while serving as an officer or employee of the United States, directly or indirectly\u2014 (A) hold or perform the duties of more than 1 position in the civil service at the same time; (B) enter into or apply for a contract for the procurement of property or services with any department or agency or instrumentality of the United States; or (C) receive compensation or any other financial benefit under a contract with any department, agency, or instrumentality of the United States. (2) Any individual who knowingly violates this subsection shall\u2014 (A) repay all amounts received in violation of this section, with interest, as determined by the applicable agency; and (B) be referred to the Department of Justice for investigation, and, as appropriate, criminal prosecution. (3) Each agency shall notify the inspector general of the agency or the Inspector General of the Office of Personnel Management of any suspected violation of this section. (g) (1) The Inspector General of the Office of Personnel Management shall annually audit personnel and payroll records to identify violations of this section during the preceding year and submit to Congress, the heads of each agency, and the inspectors general of each agency a report on the audit. (2) Each audit required under paragraph (1) shall\u2014 (A) cross-reference payroll records, time and attendance records, the Office of Personnel Management Enterprise Human Resources Integration System (or any successor system), and other employment verification sources, including Internal Revenue Service data; (B) include a risk-based review of telework and contractor positions where overlapping employment may be concealed; and (C) quantify instances of violations of this section, the amounts recovered, and any disciplinary or enforcement actions taken. .",
      "versionDate": "2025-09-30",
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
        "updateDate": "2025-12-09T21:01:22Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2953is.xml"
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
      "title": "Dismantling Double Dippers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T06:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dismantling Double Dippers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to provide for dual pay and dual employment accountability.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:18:21Z"
    }
  ]
}
```
