# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5440?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5440
- Title: To amend the Internal Revenue Code of 1986 to establish a tax credit for small businesses to provide diaper changing stations in restrooms.
- Congress: 119
- Bill type: HR
- Bill number: 5440
- Origin chamber: House
- Introduced date: 2025-09-17
- Update date: 2025-10-09T08:06:11Z
- Update date including text: 2025-10-09T08:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-17: Introduced in House

## Actions

- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5440",
    "number": "5440",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001226",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Menendez, Robert [D-NJ-8]",
        "lastName": "Menendez",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to establish a tax credit for small businesses to provide diaper changing stations in restrooms.",
    "type": "HR",
    "updateDate": "2025-10-09T08:06:11Z",
    "updateDateIncludingText": "2025-10-09T08:06:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-09-17T14:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "CA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "CO"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "PA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "OH"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NY"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "MI"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NC"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "CA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "IN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "NY"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5440ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5440\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 17, 2025 Mr. Menendez (for himself, Mr. Gomez , Ms. Pettersen , Mr. Mackenzie , Mr. Landsman , Mr. Goldman of New York , Ms. Tlaib , Mrs. Foushee , Mr. Swalwell , Mr. Kennedy of New York , Mr. Carson , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a tax credit for small businesses to provide diaper changing stations in restrooms.\n#### 1. Diaper changing station restroom credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Diaper changing station restroom credit (a) Allowance of credit For purposes of section 38, in the case of an eligible small business which meets the family bathroom requirement of subsection (e) with respect to a business location of such business, the diaper changing station restroom credit determined under this section for the taxable year is an amount equal to 70 percent of the qualified diaper changing station restroom expenses paid or incurred by the taxpayer during such taxable year with respect to such business location. (b) Limitation (1) In general The credit determined under subsection (a) with respect to any business location of the taxpayer for any taxable year shall not exceed the excess (if any) of\u2014 (A) $10,000, over (B) the aggregate credits determined und subsection (a) with respect to such business location for the 3 preceding taxable years. (2) Business location For purposes of this section\u2014 (A) In general Except as provided in subparagraph (B), the term business location means each building from which the taxpayer conducts a trade or business (other than the trade or business of being an employee). (B) Separate trades or businesses in separate portions of a building In the case of a taxpayer that conducts separate trades or businesses from different portions of a building, each such portion shall be treated as a separate business location for purposes of this section if the taxpayer meets the requirements of subsection (e) applied by taking into account only such portion of such building. (c) Qualified diaper changing station restroom expenses For purposes of this section\u2014 (1) In general The term qualified diaper changing station restroom expenses means, with respect to any business location, amounts paid or incurred by the taxpayer for\u2014 (A) any diaper changing station (which may be accessed free of charge) located in any restroom at such business location (including labor costs and other expenses associated with installation of such station), (B) any diaper dispenser (which may impose a charge and which may dispense hygiene products in addition to diapers) located in any restroom at such business location (including labor costs and other expenses associated with installation of such dispenser), and (C) installation of one or more restrooms which meet the requirements of subsection (e) (or renovation or expansion of one or more existing restrooms into restrooms which meet such requirements). (d) Eligible small business For purposes of this section\u2014 (1) In general The term eligible small business means any taxpayer for any taxable year if\u2014 (A) the business gross receipts of such taxpayer for such taxable year do not exceed $5,000,000, or (B) such taxpayer employs less than 100 full-time equivalent employees for such taxable year (as determined under section 45R(d)(2)). (2) Business gross receipts The term business gross receipts means gross receipts received in the course of any trade or business (other than the trade or business of being an employee). (3) Aggregation rules For purposes of this subsection, all persons treated as a single employer under subsection (a) or (b) of section 52, or subsection (n) or (o) of section 414, shall be treated as one person. (e) Family bathroom requirement The requirements of this subsection are met with respect to any business location if both men and women have access at such location to at least 1 public restroom that is equipped with a diaper changing station (which may be accessed free of charge) and a diaper dispenser (which may impose a charge). (f) Denial of double benefit In the case of any qualified diaper changing station restroom expenses with respect to which credit is allowed under subsection (a)\u2014 (1) no deduction or credit shall be allowed for, or by reason of, any such expense to the extent of the amount of such credit, and (2) the basis of any property shall be reduced by the amount of such credit to the extent that such expenses were taken into account in determining such basis. .\n##### (b) Credit made part of general business credit\nSubsection (b) of section 38 of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) in the case of an eligible small business (as defined in section 45BB), the diaper changing station restroom credit determined under section 45BB. .\n##### (c) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Diaper changing station restroom credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-09-17",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-09-30T23:28:29Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5440ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a tax credit for small businesses to provide diaper changing stations in restrooms.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-30T04:33:13Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to establish a tax credit for small businesses to provide diaper changing stations in restrooms.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T08:06:48Z"
    }
  ]
}
```
