# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2690?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2690
- Title: Safer Truckers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2690
- Origin chamber: Senate
- Introduced date: 2025-09-03
- Update date: 2026-02-26T12:03:17Z
- Update date including text: 2026-02-26T12:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-03: Introduced in Senate
- 2025-09-03 - IntroReferral: Introduced in Senate
- 2025-09-03 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-09-03: Introduced in Senate

## Actions

- 2025-09-03 - IntroReferral: Introduced in Senate
- 2025-09-03 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2690",
    "number": "2690",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Safer Truckers Act of 2025",
    "type": "S",
    "updateDate": "2026-02-26T12:03:17Z",
    "updateDateIncludingText": "2026-02-26T12:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-03",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-03",
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
            "date": "2025-09-03T15:05:16Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-03T15:05:16Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "MS"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "OK"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "FL"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-10-16",
      "state": "OK"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "PA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2690is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2690\nIN THE SENATE OF THE UNITED STATES\nSeptember 3, 2025 Mrs. Moody introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 49, United States Code, to require that commercial driver\u2019s licenses be restricted to United States citizens, lawful permanent residents, and individuals authorized by U.S. Citizenship and Immigration Services to engage in employment in the United States that includes driving a commercial motor vehicle, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safer Truckers Act of 2025 .\n#### 2. Establishment of residency requirements for CDLs\nSection 31308(1) of title 49, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A), by striking and at the end;\n**(2)**\nin subparagraph (B), by adding and after the semicolon at the end; and\n**(3)**\nby adding at the end the following:\n(C) be a citizen or lawful permanent resident of the United States or authorized by U.S. Citizenship and Immigration Services to engage in employment in the United States that includes driving a commercial motor vehicle; .\n#### 3. Reporting requirements and withholding of amounts for noncompliance\nSection 31311(a) of title 49, United States Code, is amended by adding at the end the following:\n(26) The State may issue a commercial driver\u2019s license to an individual only if the individual is a citizen or lawful permanent resident of the United States or is authorized by U.S. Citizenship and Immigration Services to engage in employment in the United States that includes driving a commercial motor vehicle. (27) Not later than 180 days after the date of enactment of this paragraph, and by December 31 of each year thereafter, the State shall submit to the Secretary a report describing the policies and actions of the State to uphold and enforce the English-language proficiency requirements for drivers of commercial motor vehicles, as described in section 391.11(b)(2) of title 49, Code of Federal Regulations (or a successor regulation). .",
      "versionDate": "2025-09-03",
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
        "actionDate": "2025-11-18",
        "text": "Referred to the Subcommittee on Highways and Transit."
      },
      "number": "6071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Safer Truckers Act of 2025",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-22T14:47:58Z"
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
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2690is.xml"
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
      "title": "Safer Truckers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safer Truckers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-06T07:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 49, United States Code, to require that commercial driver's licenses be restricted to United States citizens, lawful permanent residents, and individuals authorized by U.S. Citizenship and Immigration Services to engage in employment in the United States that includes driving a commercial motor vehicle, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-06T07:33:24Z"
    }
  ]
}
```
