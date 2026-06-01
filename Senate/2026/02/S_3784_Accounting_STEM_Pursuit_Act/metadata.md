# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3784?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3784
- Title: Accounting STEM Pursuit Act
- Congress: 119
- Bill type: S
- Bill number: 3784
- Origin chamber: Senate
- Introduced date: 2026-02-05
- Update date: 2026-02-26T14:58:25Z
- Update date including text: 2026-02-26T14:58:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in Senate
- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S511)
- Latest action: 2026-02-05: Introduced in Senate

## Actions

- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S511)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3784",
    "number": "3784",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001035",
        "district": "",
        "firstName": "Susan",
        "fullName": "Sen. Collins, Susan M. [R-ME]",
        "lastName": "Collins",
        "party": "R",
        "state": "ME"
      }
    ],
    "title": "Accounting STEM Pursuit Act",
    "type": "S",
    "updateDate": "2026-02-26T14:58:25Z",
    "updateDateIncludingText": "2026-02-26T14:58:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S511)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-05",
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
          "date": "2026-02-05T17:09:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NV"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-02-09",
      "state": "ME"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3784is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3784\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Ms. Collins (for herself and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Student Support and Academic Enrichment Grant program to promote career awareness in accounting as part of a well-rounded STEM educational experience.\n#### 1. Short title\nThis Act may be cited as the Accounting STEM Pursuit Act .\n#### 2. Accounting as part of a well-rounded educational experience\nSubpart 1 of part A of title IV of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7111 et seq. ) is amended\u2014\n**(1)**\nin section 4104(b)(3)(A)(i), by\u2014\n**(A)**\nstriking or at the end of subclause (VI);\n**(B)**\nredesignating subclause (VII) as subclause (VIII); and\n**(C)**\ninserting after subclause (VI) the following new subclause:\n(VII) accounting education, including accounting career awareness; or ; and\n**(2)**\nin section 4107(a)(3), by\u2014\n**(A)**\nstriking or at the end of subparagraph (I);\n**(B)**\nredesignating subparagraph (J) as subparagraph (K); and\n**(C)**\ninserting after subparagraph (I) the following new subparagraph:\n(J) activities to promote the development, implementation, and strengthening of programs to teach accounting, including increasing access to high-quality accounting courses for students through grade 12 who are members of groups underrepresented in accounting careers; or .",
      "versionDate": "2026-02-05",
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
        "name": "Education",
        "updateDate": "2026-02-26T14:58:25Z"
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
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3784is.xml"
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
      "title": "Accounting STEM Pursuit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-21T04:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Accounting STEM Pursuit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Student Support and Academic Enrichment Grant program to promote career awareness in accounting as part of a well-rounded STEM educational experience.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T04:48:33Z"
    }
  ]
}
```
