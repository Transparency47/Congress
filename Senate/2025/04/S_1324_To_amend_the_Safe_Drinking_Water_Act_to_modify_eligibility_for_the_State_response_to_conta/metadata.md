# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1324?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1324
- Title: A bill to amend the Safe Drinking Water Act to modify eligibility for the State response to contaminants program, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 1324
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2025-12-19T11:56:29Z
- Update date including text: 2025-12-19T11:56:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1324",
    "number": "1324",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "A bill to amend the Safe Drinking Water Act to modify eligibility for the State response to contaminants program, and for other purposes.",
    "type": "S",
    "updateDate": "2025-12-19T11:56:29Z",
    "updateDateIncludingText": "2025-12-19T11:56:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T16:38:12Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "ME"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-08",
      "state": "ME"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "AZ"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NM"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1324is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1324\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mrs. Shaheen (for herself, Ms. Collins , Mr. King , Mr. Kelly , and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Safe Drinking Water Act to modify eligibility for the State response to contaminants program, and for other purposes.\n#### 1. Technical fix for State response to contaminants program\nSection 1459A(j) of the Safe Drinking Water Act (42 U.S.C. 300j\u201319a(j)) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking subsection (c)(2) and inserting clause (i) or (ii) of subparagraph (A) of paragraph (3) or a drinking water well owner described in subparagraph (B) of that paragraph ;\n**(B)**\nby striking contaminant\u2014 and all that follows through to\u2014 in subparagraph (A) in the matter preceding clause (i) and inserting contaminant that is determined by the State\u2014 ;\n**(C)**\nby striking subparagraph (B);\n**(D)**\nby redesignating clauses (i) and (ii) as subparagraphs (A) and (B), respectively, and indenting appropriately;\n**(E)**\nin subparagraph (A) (as so redesignated)\u2014\n**(i)**\nby inserting to before be present ;\n**(ii)**\nby striking serving, and inserting serving a community ; and\n**(iii)**\nby striking for, that community ; and\n**(F)**\nin subparagraph (B) (as so redesignated)\u2014\n**(i)**\nby inserting to before potentially ; and\n**(ii)**\nby striking ; and at the end and inserting a period; and\n**(2)**\nby adding at the end the following:\n(3) Eligibility for assistance or as a beneficiary of assistance For purposes of this subsection, the Administrator may issue a grant to a State\u2014 (A) that is requesting a grant on behalf of\u2014 (i) a community that, under the affordability criteria established by the State under section 1452(d)(3), is determined by the State to be\u2014 (I) a disadvantaged community; or (II) a community that may become a disadvantaged community as a result of carrying out an activity described in paragraph (1); or (ii) a community with a population of fewer than 10,000 individuals that the Administrator determines does not have the capacity to incur debt sufficient to finance an activity described in paragraph (1); or (B) for the benefit of 1 or more owners of drinking water wells that are not public water systems and are not connected to a public water system. .",
      "versionDate": "2025-04-08",
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
        "name": "Environmental Protection",
        "updateDate": "2025-05-28T14:27:51Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1324is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Safe Drinking Water Act to modify eligibility for the State response to contaminants program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:21Z"
    },
    {
      "title": "A bill to amend the Safe Drinking Water Act to modify eligibility for the State response to contaminants program, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T10:56:22Z"
    }
  ]
}
```
