# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3817?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3817
- Title: Stop Presidential Embezzlement Act
- Congress: 119
- Bill type: S
- Bill number: 3817
- Origin chamber: Senate
- Introduced date: 2026-02-10
- Update date: 2026-03-24T01:42:13Z
- Update date including text: 2026-03-24T01:42:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in Senate
- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-10: Introduced in Senate

## Actions

- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3817",
    "number": "3817",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Stop Presidential Embezzlement Act",
    "type": "S",
    "updateDate": "2026-03-24T01:42:13Z",
    "updateDateIncludingText": "2026-03-24T01:42:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T20:01:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NY"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NM"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3817is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3817\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2026 Mr. Wyden (for himself, Mr. Schumer , Mr. Luj\u00e1n , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to impose a tax on damages received by certain officers of the United States on account of any civil action filed against the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Presidential Embezzlement Act .\n#### 2. Imposition of tax on damages received by the President of the United States on account of civil action filed against the United States\n##### (a) In general\nSubtitle D of the Internal Revenue Code of 1986 is amended by adding at the end the following new chapter:\n50B Certain civil damages received by certain officers of the United States Sec. 5000E. Imposition of tax on damages received on account of civil action filed against the United States. 5000E. Imposition of tax on damages received on account of civil action filed against the United States (a) In general There is hereby imposed on each covered person for any taxable year a tax equal to 100 percent of the qualified civil action amount received by such person during such taxable year. (b) Covered person For purposes of this section\u2014 (1) In general The term covered person means\u2014 (A) any individual who has served in a position described in paragraph (2), and (B) any person related (within the meaning of section 267(b)) to a person described in subparagraph (A). (2) Position described The positions described in this paragraph are the following: (A) President of the United States. (B) Vice President of the United States. (C) Any position at level I of the Executive Schedule under section 5312 of title 5, United States Code. (D) Member of Congress (including any Delegate and Resident Commissioner). (c) Qualified civil action amount For purposes of this section\u2014 (1) In general The term qualified civil action amount means, with respect to any covered person during any taxable year, the aggregate amount of damages received by such person during such taxable year (whether by settlement, verdict, judgment, or otherwise) on account of any civil action\u2014 (A) filed by such person against the United States (or any agency or instrumentality thereof), and (B) with respect to which the filing or settlement of, or issuance of a verdict or judgment for, occurred during the applicable period. (2) Applicable period The term applicable period means, with respect to any covered person, the period of time\u2014 (A) beginning with the date on which the individual described in subsection (b)(1)(A) began serving in a position described in subsection (b)(2)(A), and (B) ending with the date on which such individual ceased to serve in any position described in subsection (b)(2)(A). (d) Special rules (1) Administrative provisions For purposes of subtitle F, any tax imposed by this section shall be treated as a tax imposed by subtitle A. (2) Exclusion from gross income For purposes of chapter 1, the gross income of any covered person for any taxable year shall not include any qualified civil action amount received by such person during such taxable year. .\n##### (b) No deduction from income tax\nSection 275(a)(6) of the Internal Revenue Code of 1986 is amended by inserting 50B, after 50A, .\n##### (c) Clerical amendment\nThe table of chapters for subtitle D of the Internal Revenue Code of 1986 is amended by inserting after the item relating to chapter 50A the following new item:\nChapter 50B\u2014Certain civil damages received by certain officers of the United States .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to amounts received after the date of the enactment of this Act.",
      "versionDate": "2026-02-10",
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
        "actionDate": "2026-02-04",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7381",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Prevent Presidential Profiteering Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-18",
        "text": "Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 360."
      },
      "number": "4125",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Presidential Embezzlement Act",
      "type": "S"
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
        "name": "Taxation",
        "updateDate": "2026-02-27T19:07:08Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3817is.xml"
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
      "title": "Stop Presidential Embezzlement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Presidential Embezzlement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to impose a tax on damages received by certain officers of the United States on account of any civil action filed against the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T04:48:26Z"
    }
  ]
}
```
