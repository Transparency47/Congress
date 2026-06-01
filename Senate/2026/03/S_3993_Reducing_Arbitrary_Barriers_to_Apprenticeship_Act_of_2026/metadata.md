# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3993?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3993
- Title: Reducing Arbitrary Barriers to Apprenticeship Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3993
- Origin chamber: Senate
- Introduced date: 2026-03-04
- Update date: 2026-04-30T11:03:20Z
- Update date including text: 2026-04-30T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in Senate
- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2026-03-04: Introduced in Senate

## Actions

- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3993",
    "number": "3993",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Reducing Arbitrary Barriers to Apprenticeship Act of 2026",
    "type": "S",
    "updateDate": "2026-04-30T11:03:20Z",
    "updateDateIncludingText": "2026-04-30T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-04",
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
            "date": "2026-04-29T21:37:34Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-04T22:27:19Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MI"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "ND"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "IL"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "AK"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3993is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3993\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2026 Mr. Sheehy (for himself, Ms. Slotkin , Mr. Cramer , Ms. Duckworth , Mr. Sullivan , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, and title 10, United States Code, to eliminate those provisions relating to veterans educational assistance that disadvantage eligible individuals who choose to pursue programs of apprenticeship or other on-job training instead of a four-year college degree, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reducing Arbitrary Barriers to Apprenticeship Act of 2026 .\n#### 2. Eliminating provisions relating to veterans educational assistance that disadvantage eligible individuals who choose to pursue programs of apprenticeship or other on-job training\n##### (a) Post-9/11 Educational Assistance\n**(1) Ensuring the amount of assistance for full-time program of apprenticeship or other on-job training does not deter individuals interested in such programs and training**\nClause (i) of section 3313(g)(3)(B) of title 38, Unites States Code, is amended by striking a monthly housing stipend equal to\u2014 and all that follows through the period at the end and inserting the following: a monthly housing stipend equal to the monthly amount of the basic allowance for housing payable under section 403 of title 37 for a member with dependents in pay grade E\u20135 residing in the military housing area that encompasses all or the majority portion of the ZIP Code area in which is located the employer at which the individual pursues such program. .\n**(2) Waiver of minimum attendance requirement for receipt of assistance for programs of apprenticeship and other on-job training in construction industry**\nClause (iv) of such section is amended\u2014\n**(A)**\nby striking In any month and inserting (I) Except as provided in subclause (II), in any month ; and\n**(B)**\nby adding at the end the following new subclause:\n(II) Subclause (I) shall not apply to an individual pursuing a program of apprenticeship or other on-job training for an occupation that performs work classified in Sector 23 of the most recent publication of the North American Industry Classification System. .\n##### (b) All-Volunteer Force Educational Assistance Program\n**(1) Ensuring the amount of assistance for full-time program of apprenticeship or other on-job training does not deter individuals interested in such programs and training**\n**(A) In general**\nParagraph (1) of section 3032(c) of such title is amended by striking this chapter is\u2014 and all that follows through the period at the end and inserting the following: this chapter is 100 percent of the monthly educational assistance allowance otherwise payable to such individual under this chapter. .\n**(B) Conforming amendment**\nParagraph (3) of such section is amended by striking at the rate of\u2014 and all that follows through the period at the end and inserting the following: at the rate of 100 percent of a month. .\n**(2) Waiver of minimum attendance requirement for receipt of assistance for programs of apprenticeship and other on-job training in construction industry**\nParagraph (2) of such section is amended\u2014\n**(A)**\nby striking In any month and inserting (A) Except as provided in subparagraph (B), in any month ; and\n**(B)**\nby adding at the end the following new subclause:\n(B) Subparagraph (A) shall not apply to an individual pursuing a program of apprenticeship or other on-job training for an occupation that performs work classified in Sector 23 of the most recent publication of the North American Industry Classification System. .\n##### (c) Educational Assistance for members of the selected reserve\n**(1) Ensuring the amount of assistance for full-time program of apprenticeship or other on-job training does not deter individuals interested in such programs and training**\n**(A) In general**\nParagraph (1) of section 16131(d) of title 10, United States Code, is amended by striking this chapter is\u2014 and all that follows through the period at the end and inserting the following: this chapter is 100 percent of the monthly educational assistance allowance otherwise payable to such person under this chapter. .\n**(B) Conforming amendment**\nParagraph (3) of such section is amended by striking at the rate of\u2014 and all that follows through the period at the end and inserting the following: at the rate of 100 percent of a month. .\n**(2) Waiver of minimum attendance requirement for receipt of assistance for programs of apprenticeship and other on-job training in construction industry**\nParagraph (2) of such section is amended\u2014\n**(A)**\nby striking In any month and inserting (A) Except as provided in subparagraph (B), in any month ; and\n**(B)**\nby adding at the end the following new subclause:\n(B) Subparagraph (A) shall not apply to an individual pursuing a program of apprenticeship or other on-job training for an occupation that performs work classified in Sector 23 of the most recent publication of the North American Industry Classification System. .",
      "versionDate": "2026-03-04",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-24T01:08:14Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3993is.xml"
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
      "title": "Reducing Arbitrary Barriers to Apprenticeship Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reducing Arbitrary Barriers to Apprenticeship Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, and title 10, United States Code, to eliminate those provisions relating to veterans educational assistance that disadvantage eligible individuals who choose to pursue programs of apprenticeship or other on-job training instead of a four-year college degree, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:03:23Z"
    }
  ]
}
```
