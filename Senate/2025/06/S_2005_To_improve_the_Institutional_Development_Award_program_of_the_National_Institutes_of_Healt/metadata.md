# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2005?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2005
- Title: IDeA Reauthorization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2005
- Origin chamber: Senate
- Introduced date: 2025-06-10
- Update date: 2025-06-30T13:05:03Z
- Update date including text: 2025-06-30T13:05:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in Senate
- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-06-10: Introduced in Senate

## Actions

- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2005",
    "number": "2005",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "IDeA Reauthorization Act of 2025",
    "type": "S",
    "updateDate": "2025-06-30T13:05:03Z",
    "updateDateIncludingText": "2025-06-30T13:05:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T18:27:54Z",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "WV"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "NH"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2005is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2005\nIN THE SENATE OF THE UNITED STATES\nJune 10, 2025 Mrs. Hyde-Smith (for herself, Mrs. Capito , and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo improve the Institutional Development Award program of the National Institutes of Health.\n#### 1. Short title\nThis Act may be cited as the IDeA Reauthorization Act of 2025 .\n#### 2. Institutional development award program\nSection 461(b)(1) of the Public Health Service Act ( 42 U.S.C. 285k(b)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A), by adding at the end the following: Such program shall be called the Institutional Development Award program or the IDeA program . ;\n**(2)**\nby amending subparagraph (B) to read as follows:\n(B) The entities referred to in subparagraph (A) are entities that conduct biomedical or behavioral research and are located in a State that is at or below the median of all States in aggregate grant funding from the National Institutes of Health, excluding funding under this subsection, received by entities in the State, calculated on a rolling multi-year average, as determined by the Director of NIH (referred to in this paragraph as an IDeA State ). ; and\n**(3)**\nby adding at the end the following:\n(D) The NIH shall submit to Congress, as part of its Federal budget submission, or make available through an annually updated, publicly accessible data source\u2014 (i) a description of the strategy and objectives of the IDeA program; (ii) a description of the awards made under such program in the previous fiscal year, including\u2014 (I) the efforts and accomplishments to more fully integrate the IDeA States in major activities and initiatives of the National Institutes of Health; (II) the percentage of IDeA program reviewers who are from IDeA States; and (III) updates on programs or large collaborator awards involving a partnership of organizations and institutions from IDeA States and non-IDeA States; and (iii) a description of gains in academic research quality and in biomedical science human resource development achieved through the IDeA program over the last 5 fiscal years. .",
      "versionDate": "2025-06-10",
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
        "name": "Health",
        "updateDate": "2025-06-30T13:05:03Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2005is.xml"
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
      "title": "IDeA Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "IDeA Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the Institutional Development Award program of the National Institutes of Health.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T04:18:17Z"
    }
  ]
}
```
