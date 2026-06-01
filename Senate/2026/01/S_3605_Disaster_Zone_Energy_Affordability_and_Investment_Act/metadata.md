# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3605?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3605
- Title: Disaster Zone Energy Affordability and Investment Act
- Congress: 119
- Bill type: S
- Bill number: 3605
- Origin chamber: Senate
- Introduced date: 2026-01-08
- Update date: 2026-04-29T11:03:33Z
- Update date including text: 2026-04-29T11:03:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in Senate
- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-08: Introduced in Senate

## Actions

- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3605",
    "number": "3605",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Disaster Zone Energy Affordability and Investment Act",
    "type": "S",
    "updateDate": "2026-04-29T11:03:33Z",
    "updateDateIncludingText": "2026-04-29T11:03:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-08",
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
      "actionDate": "2026-01-08",
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
          "date": "2026-01-08T19:28:21Z",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "WA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3605is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3605\nIN THE SENATE OF THE UNITED STATES\nJanuary 8 (legislative day, January 7), 2026 Mr. Graham (for himself and Ms. Cantwell ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow a portion of general business credit carryforwards to be transferred by certain taxpayers affected by federally declared disasters and other incidents.\n#### 1. Short title\nThis Act may be cited as the Disaster Zone Energy Affordability and Investment Act .\n#### 2. Certain carryforwards of general business credit treated as transferrable credits for taxpayers affected by certain disasters\n##### (a) In general\nSection 6418(f)(1)(A) of the Internal Revenue Code of 1986 is amended by adding at the end the following new clause:\n(xiii) so much of the amount of the applicable general business credit carryforwards as does not exceed the eligible expenditures made by the taxpayer during the taxable year. .\n##### (b) Applicable general business credit carryforwards\nSection 6418(f) of such Code is amended by adding at the end the following new paragraph:\n(3) Definitions and rules related to applicable general business credit carryforwards For purposes of paragraph (1)(A)(xiii)\u2014 (A) In general The term applicable general business credit carryforwards means, with respect to any taxable year, the sum of the amounts described in section 38(a)(1) which\u2014 (i) are carried to any taxable year beginning after December 31, 2023, and (ii) attributable to any credit described in clauses (ii) and (ix) of subparagraph (A). (B) Eligible expenditures (i) In general The term eligible expenditures means amounts paid or incurred by the taxpayer\u2014 (I) for the purpose of carrying out a trade or business in a qualified disaster area, and (II) on or before the last day of the second calendar year following the calendar year in which the declaration or determination described in clause (ii) with respect to such qualified disaster area was made. (ii) Qualified disaster area The term qualified disaster area means\u2014 (I) any area with respect to which a major disaster was declared after December 31, 2023, by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act, or (II) any area which is determined by the Governor of a State to be an area affected by a State declared disaster (as defined in section 165(h)(5)(C) of the Internal Revenue Code of 1986 (as added by Public Law 119\u201321 )) if the incident giving rise to the State declared disaster occurred after December 31, 2023. (C) Application to consolidated groups All members of an affiliated group filing a consolidated return shall be treated as one taxpayer. .\n##### (c) Conforming amendment\nSection 6418(f)(1)(C) of such Code is amended by striking The term and inserting Except as provided in paragraph (1)(A)(xiii), the term .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years ending after the date of the enactment of this Act.\n##### (e) Special rule\nNotwithstanding section 6418(g)(1) of the Internal Revenue Code of 1986, the Secretary of the Treasury (or the Secretary's delegate) shall not require registration with respect to the portion of any applicable general business credit carryforwards (as defined in section 6418(f)(3) of such Code, as added by this section) which relates to a taxable year beginning with or before the taxable year that the online registration tool for such registration has been updated to account for the provisions of this section.",
      "versionDate": "2026-01-08",
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
        "actionDate": "2026-02-09",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7450",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Disaster Zone Energy Affordability and Investment Act",
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
        "name": "Taxation",
        "updateDate": "2026-02-04T22:57:55Z"
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
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3605is.xml"
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
      "title": "Disaster Zone Energy Affordability and Investment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow a portion of general business credit carryforwards to be transferred by certain taxpayers affected by federally declared disasters and other incidents.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:49Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Disaster Zone Energy Affordability and Investment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T10:53:15Z"
    }
  ]
}
```
