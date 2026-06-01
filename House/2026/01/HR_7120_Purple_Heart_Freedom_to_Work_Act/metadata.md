# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7120?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7120
- Title: Purple Heart Freedom to Work Act
- Congress: 119
- Bill type: HR
- Bill number: 7120
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-04-21T08:06:08Z
- Update date including text: 2026-04-21T08:06:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7120",
    "number": "7120",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S001189",
        "district": "8",
        "firstName": "Austin",
        "fullName": "Rep. Scott, Austin [R-GA-8]",
        "lastName": "Scott",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Purple Heart Freedom to Work Act",
    "type": "HR",
    "updateDate": "2026-04-21T08:06:08Z",
    "updateDateIncludingText": "2026-04-21T08:06:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
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
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:00:40Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "CA"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "OH"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "FL"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "MS"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "NE"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "FL"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "FL"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NC"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NV"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NJ"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "SC"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NC"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "VA"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "TN"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "VA"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "GA"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "TX"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7120ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7120\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Austin Scott of Georgia introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title II of the Social Security Act to establish a disability benefit offset for Purple Heart recipients, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Purple Heart Freedom to Work Act .\n#### 2. Disability benefit offset for Purple Heart recipients\n##### (a) In general\nSection 223(e) of the Social Security Act ( 42 U.S.C. 423(e) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking (1) No benefit and inserting (1)(A) Except as provided in paragraph (2), No benefit ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking (2) No benefit and inserting (B) No benefit ; and\n**(B)**\nby striking paragraph (1) and inserting subparagraph (A) ; and\n**(3)**\nby adding at the end the following:\n(2) (A) Notwithstanding subsection (a)(1) of this section, in any case in which an individual is entitled to a monthly insurance benefit under such subsection based on a disability that is attributable to an injury for which the individual was awarded the Purple Heart, such individual shall be deemed to continue to be entitled to such benefit without regard to the individual\u2019s termination month, except that payment of such benefit for any month shall be subject to the reduction described in subparagraph (B). (B) (i) Any benefit described in subparagraph (A) otherwise payable to an individual described in such subparagraph for a month shall be reduced by $1 for each $4 by which the individual\u2019s earnings derived from services for such month exceeds the amount specified for such month in clause (ii), except that such benefit may not be reduced below $0. (ii) The amount specified in this clause with respect to an individual for a month is the amount of earnings derived from services, applicable to the individual for such month under subsection (d)(4)(A), sufficient to demonstrate the individual\u2019s ability to engage in substantial gainful activity. (C) In the case of a benefit otherwise payable to an individual for a month under section 202 on the basis of the wages and self-employment income of an individual whose benefit is reduced pursuant to subparagraph (B), such benefit shall be reduced for such month by the same proportion as the reduction made pursuant to subparagraph (B). .\n##### (b) Conforming amendments\nSection 223(a)(2) of such Act ( 42 U.S.C. 423(a)(2) ) is amended by striking and section 215(b)(2)(A)(ii) and inserting , section 215(b)(2)(A)(ii), and subsection (e) of this section .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to benefits payable for months beginning after the date that is 6 months after the date of the enactment of this Act.\n#### 3. Application of higher SGA amount for Purple Heart recipients\n##### (a) In general\nSection 223(d)(4)(A) of the Social Security Act ( 42 U.S.C. 423(d)(4)(A) ) is amended by inserting after who is blind the following: or who is entitled to a monthly insurance benefit under subsection (a)(1) based on a disability that is attributable to an injury for which the individual was awarded the Purple Heart .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply with respect to benefits payable for months beginning after the date that is 6 months after the date of the enactment of this Act.",
      "versionDate": "2026-01-15",
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
        "name": "Social Welfare",
        "updateDate": "2026-01-20T14:42:56Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7120ih.xml"
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
      "title": "Purple Heart Freedom to Work Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Purple Heart Freedom to Work Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title II of the Social Security Act to establish a disability benefit offset for Purple Heart recipients, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T09:18:20Z"
    }
  ]
}
```
