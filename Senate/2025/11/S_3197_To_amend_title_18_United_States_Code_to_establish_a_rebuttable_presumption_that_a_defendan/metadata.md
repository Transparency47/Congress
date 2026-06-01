# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3197?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3197
- Title: Flight Risk Reduction Act
- Congress: 119
- Bill type: S
- Bill number: 3197
- Origin chamber: Senate
- Introduced date: 2025-11-19
- Update date: 2026-01-08T14:29:22Z
- Update date including text: 2026-01-08T14:29:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in Senate
- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-11-19: Introduced in Senate

## Actions

- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3197",
    "number": "3197",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Flight Risk Reduction Act",
    "type": "S",
    "updateDate": "2026-01-08T14:29:22Z",
    "updateDateIncludingText": "2026-01-08T14:29:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:51:51Z",
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
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "SC"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "TX"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "TX"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "MO"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "TN"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "FL"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NE"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "IN"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "PA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3197is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3197\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Mr. Lee (for himself, Mr. Graham , Mr. Cornyn , Mr. Cruz , Mr. Hawley , Mr. Tillis , Mrs. Blackburn , Mrs. Moody , Mr. Ricketts , Mr. Banks , Mr. McCormick , and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to establish a rebuttable presumption that a defendant who is not a United States citizen or lawful permanent resident poses a danger to the community and a serious risk of flight, for purposes of determining whether to release or detain the defendant pending trial.\n#### 1. Short title\nThis Act may be cited as the Flight Risk Reduction Act .\n#### 2. Release or detention of a defendant pending trial\n##### (a) Basis for detention hearing\nSection 3142(f)(1) of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) through (E) as clauses (i) through (v), respectively; and adjusting the margins accordingly;\n**(2)**\nin clause (iv), as so redesignated, by striking subparagraphs (A) through (C) of this paragraph each place it appears and inserting clauses (i) through (iii) of this subparagraph ;\n**(3)**\nby striking , in a case that involves\u2014 and inserting the following:\n\u2014 (A) in a case that involves ; and\n**(4)**\nby adding at the end the following:\n(B) if such person is not a citizen or lawful permanent resident of the United States; or .\n##### (b) Detention\nSection 3142(e) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), by striking subsection (f)(1) each place it appears and inserting subsection (f)(1)(A) ; and\n**(2)**\nby adding at the end the following:\n(4) (A) Notwithstanding subsection (d), if the person is not a citizen or lawful permanent resident of the United States, it shall be presumed that no condition or combination of conditions will reasonably assure the appearance of the person as required and the safety of any other person and the community, subject to rebuttal by the person by clear and convincing evidence. (B) Ties to family or employment in the United States shall not be grounds for rebuttal of the presumption under subparagraph (A). .",
      "versionDate": "2025-11-19",
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
        "actionDate": "2025-12-10",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6582",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Flight Risk Reduction Act",
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
        "updateDate": "2025-12-18T15:49:49Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3197is.xml"
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
      "title": "Flight Risk Reduction Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T04:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Flight Risk Reduction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to establish a rebuttable presumption that a defendant who is not a United States citizen or lawful permanent resident poses a danger to the community and a serious risk of flight, for purposes of determining whether to release or detain the defendant pending trial.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T04:18:26Z"
    }
  ]
}
```
