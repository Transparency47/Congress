# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1147?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1147
- Title: Defining Male and Female Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1147
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2025-12-05T22:55:06Z
- Update date including text: 2025-12-05T22:55:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1147",
    "number": "1147",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Defining Male and Female Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:55:06Z",
    "updateDateIncludingText": "2025-12-05T22:55:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T17:13:11Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "LA"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "MT"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "MS"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "NE"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1147is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1147\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Marshall (for himself, Mr. Cassidy , Mr. Sheehy , Mrs. Hyde-Smith , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish clear and consistent biological definitions of male and female.\n#### 1. Short title\nThis Act may be cited as the Defining Male and Female Act of 2025 .\n#### 2. Definition of sex , male , female , and related terms\nChapter 1 of title 1, United States Code, is amended by adding at the end the following:\n9. Definition of sex , male , female , and related terms In determining the meaning of any Act of Congress, or of any ruling, regulation, or interpretation of the various departments and Federal agencies of the United States, the term\u2014 (1) boy means a minor human male; (2) father means a male parent; (3) female , when used to refer to a natural person, means a person belonging, at conception, to the sex characterized by a reproductive system with the biological function of producing eggs (ova); (4) gender identity means an identity that reflects an internal and subjective sense of self, disconnected from biological reality and sex and existing on an indeterminate continuum, and, because such an identity does not provide a meaningful basis for identification for purposes of Federal law, the term shall not be recognized by the Federal Government as a replacement for sex; (5) girl means a minor human female; (6) male , when used to refer to a natural person, means a person belonging, at conception, to the biological sex characterized by a reproductive system with the biological function of producing sperm; (7) man , except when used as a generic reference to human beings, means an adult human male; (8) mother means a female parent; (9) sex , when referring to a natural person's individual\u2019s sex, means the person\u2019s immutable biological classification as either male or female, as biologically determined and defined by this section; and (10) woman means an adult human female. .",
      "versionDate": "2025-03-26",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-26",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2378",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Defining Male and Female Act of 2025",
      "type": "HR"
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-05-14T20:53:15Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1147is.xml"
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
      "title": "Defining Male and Female Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T01:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Defining Male and Female Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish clear and consistent biological definitions of male and female.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:28Z"
    }
  ]
}
```
