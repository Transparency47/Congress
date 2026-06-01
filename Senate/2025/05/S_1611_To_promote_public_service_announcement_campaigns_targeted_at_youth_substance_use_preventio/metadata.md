# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1611?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1611
- Title: Youth Substance Use Prevention and Awareness Act
- Congress: 119
- Bill type: S
- Bill number: 1611
- Origin chamber: Senate
- Introduced date: 2025-05-06
- Update date: 2026-01-22T16:03:02Z
- Update date including text: 2026-01-22T16:03:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-06: Introduced in Senate
- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-06: Introduced in Senate

## Actions

- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1611",
    "number": "1611",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000377",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Kelly, Mark [D-AZ]",
        "lastName": "Kelly",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Youth Substance Use Prevention and Awareness Act",
    "type": "S",
    "updateDate": "2026-01-22T16:03:02Z",
    "updateDateIncludingText": "2026-01-22T16:03:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-06",
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
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T16:22:13Z",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "NC"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1611is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1611\nIN THE SENATE OF THE UNITED STATES\nMay 6, 2025 Mr. Kelly (for himself, Mr. Tillis , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo promote public service announcement campaigns targeted at youth substance use prevention, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Youth Substance Use Prevention and Awareness Act .\n#### 2. Grant use for public service announcement campaigns\n##### (a) Expansion of grant program\nSection 3021(a) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10701(a) ) is amended by adding at the end the following:\n(11) Developing, implementing, or expanding research-based public service announcement campaign programs targeted at youth substance use prevention using age-appropriate material, including\u2014 (A) television, radio, print, outdoor, and digital public service announcements; and (B) public service announcement contests that solicit youth public service announcement submissions. .\n##### (b) Reporting requirements\nThe Attorney General shall publish an annual report on any grants awarded for public service announcement campaigns under paragraph (11) of section 3021(a) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10701(a) ), as added by subsection (a), that includes, which respect to each such public service announcement campaign\u2014\n**(1)**\na description of the grant awarded and the public service announcement campaign funded by the grant;\n**(2)**\nthe research used to inform and develop the public service announcement campaign funded by the grant;\n**(3)**\nany regional or geographic-specific messaging used as part of the public service announcement campaign;\n**(4)**\na description of how the public service announcement campaign funded by the grant supports the other substance use prevention initiatives or strategy of the grantee; and\n**(5)**\nan evaluation of the success of the public service announcement campaign, such as the effectiveness of the campaign at reducing the rate of drug use by youth.",
      "versionDate": "2025-05-06",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6902",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Youth Substance Use Prevention and Awareness Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-22T16:17:47Z"
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
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1611is.xml"
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
      "title": "Youth Substance Use Prevention and Awareness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-16T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Youth Substance Use Prevention and Awareness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-16T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote public service announcement campaigns targeted at youth substance use prevention, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-16T03:18:23Z"
    }
  ]
}
```
