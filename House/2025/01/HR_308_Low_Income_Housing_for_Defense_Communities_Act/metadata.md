# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/308?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/308
- Title: Low Income Housing for Defense Communities Act
- Congress: 119
- Bill type: HR
- Bill number: 308
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-08-27T08:05:20Z
- Update date including text: 2025-08-27T08:05:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/308",
    "number": "308",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Low Income Housing for Defense Communities Act",
    "type": "HR",
    "updateDate": "2025-08-27T08:05:20Z",
    "updateDateIncludingText": "2025-08-27T08:05:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:33:25Z",
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
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "WA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NV"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr308ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 308\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Moore of Utah (for himself and Ms. Strickland ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide tax incentives for rental housing for members of the Armed Forces.\n#### 1. Short title; sense of Congress\n##### (a) Short title\nThis Act may be cited as the Low Income Housing for Defense Communities Act .\n##### (b) Sense of Congress\nIt is the sense of Congress that in addition to expanding and strengthening the affordable housing credit for active duty military members through the provisions in the Low Income Housing for Defense Communities Act, further steps should be taken to drive investment into affordable housing projects in the United States and boost overall housing supply for workers and families in the United States, such as the Affordable Housing Credit Improvement Act of 2023.\n#### 2. Tax incentives for rental housing for members of the Armed Forces\n##### (a) Military basic housing allowance not taken into account in applying certain income restrictions on residential rental projects\n**(1) Low-income housing tax credit**\nSection 42(i) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(10) Income determined without regard to military basic housing allowance Payments under section 403 of title 37, United States Code, as a basic pay allowance for housing shall not be taken into account in determining income for purposes of this section. .\n**(2) Tax-exempt bonds for qualified residential rental projects**\n**(A) In general**\nSection 142(d)(2)(B) of such Code, as amended by subparagraph (B), is amended by inserting after clause (i) the following new clause:\n(ii) Income determined without regard to military basis housing allowance Payments under section 403 of title 37, United States Code, as a basic pay allowance for housing shall not be taken into account in determining income for purposes of clause (i). .\n**(B) Repeal of deadwood**\nSection 142(d)(2)(B) of such Code is amended by striking clauses (ii), (iii), and (iv).\n**(3) Effective date**\nThe amendments made by this subsection shall apply to determinations made after the date of the enactment of this Act.\n##### (b) Increase in low-Income housing credit for buildings near certain large military installation\n**(1) In general**\nSection 42(d)(5)(B) of the Internal Revenue Code of 1986 is amended by adding at the end the following new clause:\n(vi) Buildings near certain large military installation (I) In general Any building which is located within 15 miles of a large military installation shall be treated as located in a difficult development area which is designated for purposes of this subparagraph. (II) Large military installation For purposes of this clause, the term large military installation means any military installation with a total plant replacement value (as determined by the Secretary of the Defense) in excess of $2,833,000,000. .\n**(2) Effective date**\nThe amendment made by this subsection shall apply to buildings placed in service after the date of the enactment of this Act.\n**(3) No requirement that buildings be occupied solely by members of the Armed Forces**\nNothing in the amendment made by this subsection shall be applied or interpreted to require that buildings described in section 42(d)(5)(B)(vi) of the Internal Revenue Code of 1986 (as added by this section) be occupied solely by members of the Armed Forces.",
      "versionDate": "2025-01-09",
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
        "updateDate": "2025-02-14T16:45:47Z"
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
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr308ih.xml"
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
      "title": "Low Income Housing for Defense Communities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:03Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Low Income Housing for Defense Communities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide tax incentives for rental housing for members of the Armed Forces.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:30Z"
    }
  ]
}
```
