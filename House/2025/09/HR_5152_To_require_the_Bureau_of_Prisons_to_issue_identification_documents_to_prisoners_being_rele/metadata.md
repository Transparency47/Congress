# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5152?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5152
- Title: BOP Release Card ID Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5152
- Origin chamber: House
- Introduced date: 2025-09-04
- Update date: 2026-02-24T09:05:32Z
- Update date including text: 2026-02-24T09:05:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-04: Introduced in House

## Actions

- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5152",
    "number": "5152",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001212",
        "district": "1",
        "firstName": "Barry",
        "fullName": "Rep. Moore, Barry [R-AL-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "BOP Release Card ID Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-24T09:05:32Z",
    "updateDateIncludingText": "2026-02-24T09:05:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T13:02:15Z",
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
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NJ"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "NE"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "TN"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "NC"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "NJ"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "MS"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "FL"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "LA"
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
      "sponsorshipDate": "2025-09-04",
      "state": "DC"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "GA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "MI"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NJ"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "PA"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "GA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5152ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5152\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 4, 2025 Mr. Moore of Alabama (for himself, Mr. Conaway , Mr. Bacon , Mr. Rose , Mr. Harris of North Carolina , Mr. Van Drew , Mr. Guest , Mr. Rutherford , Mr. Fields , Ms. Norton , Mr. Johnson of Georgia , Mr. Jackson of Illinois , Mr. Thanedar , Ms. Simon , Mrs. Watson Coleman , Ms. Dean of Pennsylvania , and Mrs. McBath ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require the Bureau of Prisons to issue identification documents to prisoners being released from Federal custody, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the BOP Release Card ID Act of 2025 .\n#### 2. Identification documents for prisoners being released\n##### (a) Prisoners being released from Federal custody\nSection 4042 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (e); and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Identification documents (1) Identification documents Not later than 180 days after the date of the enactment of the BOP Release Card ID Act of 2025, the Director shall issue a photo identification release card that meets the minimum standards under section 202(b) of the REAL ID Act of 2005 ( 49 U.S.C. 30301(b) note) to each prisoner who is a citizen of the United States and is being released from custody from a facility of the Bureau of Prisons. (2) Period of validity A photo identification release card shall be valid for not less than 18 months after the date on which the prisoner to whom the card is issued is released from custody. (3) Acceptance of photo identification release card for State IDs (A) In general The Director shall negotiate with each State to establish a system under which a prisoner may use a photo identification release card to obtain identification from the State. (B) Reporting Not later than 1 year after the date of enactment of the BOP Release Card ID Act of 2025, and every year thereafter, the Director shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report on the progress of the Director in negotiating agreements under subparagraph (A). (4) Acceptance of photo identification release card for Federal programs and by Federal agencies A photo identification release card shall be accepted as proof of the identity of the former prisoner to whom the card relates for purposes of\u2014 (A) the old-age, survivors, and disability insurance benefits program established under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ); (B) the Medicaid program established under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ); (C) the Medicare program established under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ); (D) any other program, project, or activity of the Department of Health and Human Services; (E) the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ); (F) any program, project, or activity funded by the temporary assistance for needy families program under part A of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ); (G) any program, project, or activity of the Office of Probation and Pretrial Services of the Administrative Office of the United States Courts; (H) any program, project, or activity of the Court Services and Offender Supervision Agency for the District of Columbia; (I) any program, project, or activity of the Department of Education; (J) any program, project, or activity of the Department of Housing and Urban Development; (K) any program, project, or activity of the Department of Veterans Affairs; and (L) any requirement for an individual to present an identification document to obtain entry into a Federal building. (5) Rule of construction Nothing in this subsection may be construed to satisfy the requirement for the Bureau of Prisons to establish prerelease planning procedures under subsection (a)(6). (6) Definitions In this subsection\u2014 (A) the term Director means the Director of the Bureau of Prisons; and (B) the term State means each of the several States of the United States, the District of Columbia, and any commonwealth or territory of the United States. .\n##### (b) Guidance for States\n**(1) Guidance**\nNot later than one year after the date of the enactment of this Act, the Attorney General shall issue guidance for States regarding the issuance of photo identification release cards for prisoners being released from custody of a correctional facility of the State.\n**(2) State defined**\nIn this subsection, the term State means each of the several States of the United States, the District of Columbia, and any commonwealth or territory of the United States.",
      "versionDate": "2025-09-04",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-23T17:04:26Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5152ih.xml"
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
      "title": "BOP Release Card ID Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BOP Release Card ID Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Bureau of Prisons to issue identification documents to prisoners being released from Federal custody, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:18:25Z"
    }
  ]
}
```
