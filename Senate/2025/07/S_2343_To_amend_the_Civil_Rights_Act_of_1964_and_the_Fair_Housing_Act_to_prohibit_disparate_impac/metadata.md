# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2343?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2343
- Title: Restoring Equal Opportunity Act
- Congress: 119
- Bill type: S
- Bill number: 2343
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2026-03-25T11:03:19Z
- Update date including text: 2026-03-25T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2343",
    "number": "2343",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
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
    "title": "Restoring Equal Opportunity Act",
    "type": "S",
    "updateDate": "2026-03-25T11:03:19Z",
    "updateDateIncludingText": "2026-03-25T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
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
      "actionDate": "2025-07-17",
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
            "date": "2025-07-17T18:56:49Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-17T18:56:49Z",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2343is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2343\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Lee introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Civil Rights Act of 1964 and the Fair Housing Act to prohibit disparate-impact claims.\n#### 1. Short title\nThis Act may be cited as the Restoring Equal Opportunity Act .\n#### 2. Sense of the Senate\nIt is the sense of the Senate that it is the policy of the United States to eliminate the use of disparate-impact liability in all contexts to the maximum degree possible to avoid violating the Constitution of the United States, Federal civil rights laws, and basic American ideals.\n#### 3. Disparate-impact claims prohibited for employment practices\nSection 703 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e\u20132 ) is amended by striking subsection (k) and inserting the following:\n(k) (1) No person may bring an action or proceeding under this title for a claim alleging an unlawful employment practice based on disparate impact. (2) In this subsection, the term disparate impact , used with respect to an employment practice, means the result of an employment practice that\u2014 (A) is neutral on its face, and does not result from an intention to discriminate in a manner prohibited under this title; but (B) may have a disproportionate effect on certain groups, including protected classes under this title. .\n#### 4. Disparate-impact claims prohibited for housing practices\nSection 807 of the Fair Housing Act ( 42 U.S.C. 3607 ) is amended by adding at the end the following:\n(c) (1) No person may bring an action or proceeding under this title for a claim alleging a discriminatory housing practice based on disparate impact. (2) In this subsection, the term disparate impact , used with respect to a housing practice, means the result of a housing practice that\u2014 (A) is neutral on its face, and does not result from an intention to discriminate in a manner prohibited under this title; but (B) may have a disproportionate effect on certain groups, including protected classes under this title. .\n#### 5. Nullifying regulations\nThe following Presidential approvals of the regulations promulgated under section 602 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d\u20131 ), and the regulations so approved, shall have no force and effect:\n**(1)**\nThe Presidential approval of regulations issued by the Equal Employment Opportunity Commission relating to title VII of the Civil Rights Act of 1964 (31 Fed. Reg. 10269 (July 29, 1966)), as applied to section 42.104(b)(2) of title 28, Code of Federal Regulations, in full.\n**(2)**\nThe Presidential approval of regulations issued by the Department of Justice relating to Regulations To Implement Title VI of the Civil Rights Act of 1964 With Respect to Federal Assistance Administered by the Department of Justice (38 Fed. Reg. 17955 (July 5, 1973)), as applied to the words or effect in both places they appear in section 42.104(b)(3) of title 28, Code of Federal Regulations, and as applied to section 42.104(b)(6)(ii) of title 28, Code of Federal Regulations and section 42.104(c)(2) of title 28, Code of Federal Regulations, in full.",
      "versionDate": "2025-07-17",
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
        "actionDate": "2025-07-16",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4448",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Restoring Equal Opportunity Act",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-05T16:24:09Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2343is.xml"
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
      "title": "Restoring Equal Opportunity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restoring Equal Opportunity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Civil Rights Act of 1964 and the Fair Housing Act to prohibit disparate-impact claims.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:33Z"
    }
  ]
}
```
