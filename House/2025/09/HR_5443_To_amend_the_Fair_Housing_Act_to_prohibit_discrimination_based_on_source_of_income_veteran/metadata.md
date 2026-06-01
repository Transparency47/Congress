# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5443?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5443
- Title: Fair Housing Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5443
- Origin chamber: House
- Introduced date: 2025-09-17
- Update date: 2026-03-04T09:06:09Z
- Update date including text: 2026-03-04T09:06:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-17: Introduced in House

## Actions

- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5443",
    "number": "5443",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "P000608",
        "district": "50",
        "firstName": "Scott",
        "fullName": "Rep. Peters, Scott H. [D-CA-50]",
        "lastName": "Peters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Fair Housing Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-04T09:06:09Z",
    "updateDateIncludingText": "2026-03-04T09:06:09Z"
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
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
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
          "date": "2025-09-17T14:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "OR"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "PA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "CA"
    },
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
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "RI"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "VA"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "KY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "DC"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "IL"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "MI"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "MN"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "MI"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "OH"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "IL"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "CA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NC"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MN"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "TX"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5443ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5443\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 17, 2025 Mr. Peters (for himself, Ms. Bonamici , Mr. Evans of Pennsylvania , Mr. Garcia of California , Mr. Gomez , Ms. Jacobs , Mr. Magaziner , Ms. McClellan , Mr. McGarvey , Ms. Norton , Mrs. Ramirez , Mrs. Dingell , Ms. Craig , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Fair Housing Act to prohibit discrimination based on source of income, veteran status, or military status.\n#### 1. Short title\nThis Act may be cited as the Fair Housing Improvement Act of 2025 .\n#### 2. Prohibiting housing discrimination based on source of income, veteran status, or military status\n##### (a) In general\nThe Fair Housing Act ( 42 U.S.C. 3601 et seq. ) is amended\u2014\n**(1)**\nin section 802 ( 42 U.S.C. 3602 ), by adding at the end the following:\n(p) Military status means the status of a person as a member of the uniformed services, as defined in section 101 of title 10, United States Code. (q) Source of income includes\u2014 (1) a housing voucher under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ) and any form of Federal, State, or local housing assistance provided to a person or family or provided to a housing owner on behalf of a person or family, including\u2014 (A) rental vouchers; (B) rental assistance; (C) rental subsidies from nongovernmental organizations; and (D) homeownership subsidies; (2) income received as a monthly benefit under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ), as a supplemental security income benefit under title XVI of the Social Security Act ( 42 U.S.C. 1381 et seq. ), or as a benefit under the Railroad Retirement Act of 1974 ( 45 U.S.C. 231 et seq. ), including any such benefit to which the individual is entitled for which payment is made to a representative payee; (3) income received by court order, including spousal support and child support; (4) any payment from a trust, guardian, conservator, cosigner, or relative; and (5) any other lawful source of income or funds, including savings accounts and investments. (r) Veteran status means the status of a person as a former member of the Armed Forces. ;\n**(2)**\nin section 804 ( 42 U.S.C. 3604 )\u2014\n**(A)**\nby inserting source of income, veteran status, military status, after familial status, each place that term appears; and\n**(B)**\nin subsection (f), by adding at the end the following:\n(10) Nothing in this title shall be construed to prohibit any entity from providing or otherwise making available any services or other assistance to individuals receiving Federal, State or local housing assistance. ;\n**(3)**\nin section 805 ( 42 U.S.C. 3605 )\u2014\n**(A)**\nin subsection (a), by inserting source of income, veteran status, military status, after familial status, ; and\n**(B)**\nin subsection (c), by inserting source of income, veteran status, military status, after handicap, ;\n**(4)**\nin section 806 ( 42 U.S.C. 3606 ), by inserting source of income, veteran status, military status, after familial status, ;\n**(5)**\nin section 808(e)(6) ( 42 U.S.C. 3608(e)(6) ), by inserting source of income, veteran status, military status, after handicap, ; and\n**(6)**\nin section 810(f) ( 42 U.S.C. 3610(f) ), by striking paragraph (4) and inserting the following:\n(4) During the period beginning on the date of enactment of the Fair Housing Improvement Act of 2025 and ending on the date that is 40 months after such date of enactment, each agency certified for purposes of this title on the day before such date of enactment shall, for purposes of this subsection, be considered certified under this subsection with respect to those matters for which the agency was certified on that date. If the Secretary determines in an individual case that an agency has not been able to meet the certification requirements within this 40-month period due to exceptional circumstances, such as the infrequency of legislative sessions in that jurisdiction, the Secretary may extend such period by not more than 6 months. .\n##### (b) Prevention of intimidation in fair housing cases\nSection 901 of the Civil Rights Act of 1968 ( 42 U.S.C. 3631 ) is amended by inserting source of income (as defined in section 802), veteran status (as defined in section 802), military status (as defined in section 802), before or national origin each place that term appears.",
      "versionDate": "2025-09-17",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-09-17",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2827",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fair Housing Improvement Act of 2025",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-11-17T18:24:32Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5443ih.xml"
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
      "title": "Fair Housing Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-30T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Housing Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-30T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Fair Housing Act to prohibit discrimination based on source of income, veteran status, or military status.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-30T04:18:19Z"
    }
  ]
}
```
