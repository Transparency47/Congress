# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3133?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3133
- Title: Violent Juvenile Offender Accountability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3133
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2026-03-17T11:03:20Z
- Update date including text: 2026-03-17T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3133",
    "number": "3133",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Violent Juvenile Offender Accountability Act of 2025",
    "type": "S",
    "updateDate": "2026-03-17T11:03:20Z",
    "updateDateIncludingText": "2026-03-17T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
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
      "actionDate": "2025-11-06",
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
        "item": [
          {
            "date": "2025-11-06T19:29:45Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-06T19:29:45Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "TX"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "AR"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "TN"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "MT"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3133is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3133\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mrs. Blackburn (for herself, Mr. Cornyn , Mr. Cotton , Mr. Hagerty , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to update the juvenile transfer for criminal prosecution process, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Violent Juvenile Offender Accountability Act of 2025 .\n#### 2. Transfer for criminal prosecution of certain juvenile offenders\nSection 5032 of title 18, United States Code, is amended by adding at the end the following:\nNotwithstanding any other provision in this section, criminal prosecution of a juvenile in the appropriate district court of the United States may be begun without a motion to transfer of the Attorney General if the juvenile is 16 years of age or older and is alleged to have committed\u2014 (1) any crime of homicide under chapter 51; (2) aggravated assault, as described in section 111(b); (3) theft of a motor vehicle under section 2119; (4) robbery under section 1951, to which section 924(c) applies; or (5) aggravated sexual abuse under section 2241, to which section 924(c) applies. .",
      "versionDate": "2025-11-06",
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
        "updateDate": "2025-11-19T13:27:22Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3133is.xml"
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
      "title": "Violent Juvenile Offender Accountability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-17T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Violent Juvenile Offender Accountability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T06:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to update the juvenile transfer for criminal prosecution process, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T06:48:18Z"
    }
  ]
}
```
