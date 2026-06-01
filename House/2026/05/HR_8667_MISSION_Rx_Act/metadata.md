# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8667?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8667
- Title: MISSION Rx Act
- Congress: 119
- Bill type: HR
- Bill number: 8667
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-14T08:08:09Z
- Update date including text: 2026-05-14T08:08:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-07 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-07 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8667",
    "number": "8667",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "MISSION Rx Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:09Z",
    "updateDateIncludingText": "2026-05-14T08:08:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:07:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-07T13:07:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "NY"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "PA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "NH"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "PA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "DC"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "NM"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "IL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8667ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8667\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Vindman (for himself, Mr. Ryan , Ms. Houlahan , Mr. Keating , Ms. Goodlander , Mr. Deluzio , and Mr. Moulton ) introduced the following bill; which was referred to the Committee on Veterans' Affairs , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles 10 and 38, United States Code, to set the maximum cost-sharing amount paid by an eligible covered beneficiary under the TRICARE program and a veteran for such selected drug, as established under the Social Security Act, and the maximum price of a selected drug procured by Federal agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Maximizing Individual Savings for Servicemembers In Obtaining Negotiated Rx Act or the MISSION Rx Act .\n#### 2. Maximum price for a selected drug for the cost-sharing amount paid by an eligible covered beneficiary under TRICARE and a veteran and for Federal procurement\n##### (a) Pharmacy benefits program\nSection 1074g of title 10, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(6), by adding at the end the following new subparagraphs:\n(F) Notwithstanding subparagraphs (A), (B), and (C), during any year a selected drug is covered under the Drug Price Negotiation Program established under section 1191 of the Social Security Act ( 42 U.S.C. 1320f ), the cost-sharing amount under this subsection during a year for such selected drug for an eligible covered beneficiary may not exceed the cost-sharing amount paid by a Medicare beneficiary for such selected drug in that year under part D of title XVIII of that Act ( 42 U.S.C. 1395w\u2013101 et seq. ) pursuant to such Drug Price Negotiation Program. ; and\n**(2)**\nin subsection (i), by adding at the end the following new paragraph:\n(5) The term selected drug has the meaning given such term in section 1192(c) of the Social Security Act ( 42 U.S.C. 1320f\u20131(c) ). .\n##### (b) Copayment for medications\nSection 1722A of title 38, United States Code, is amended by adding at the end the following new subsections:\n(d) Notwithstanding subsections (a) and (b), during any year a selected drug is covered under the Drug Price Negotiation Program established under section 1191 of the Social Security Act ( 42 U.S.C. 1320f ), the copayment amount determined under this section during a year for such selected drug for a veteran may not exceed the copayment amount paid by a Medicare beneficiary for such selected drug in that year under part D of title XVIII of that Act ( 42 U.S.C. 1395w\u2013101 et seq. ) pursuant to such Drug Price Negotiation Program. (e) In this section, the term selected drug has the meaning given such term in section 1192(c) of the Social Security Act ( 42 U.S.C. 1320f\u20131(c) ). .\n##### (c) Limitation on prices of drugs procured by Department and certain other Federal agencies\nSection 8126 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (3), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (4)(C), by striking the period and inserting ; and ; and\n**(C)**\nby adding at the end the following new paragraph:\n(5) with respect to each selected drug of the manufacturer procured by a Federal agency, as described in subsection (b), such master agreement shall be subject to the requirements in subsection (j). .\n**(2)**\nin subsection (g)(1), by striking 1992 and inserting 1992, except with respect to any reference to a provision of such Act in paragraphs (7) and (8) of subsection (h) and in subsection (j) ;\n**(3)**\nin subsection (h)\u2014\n**(A)**\nby redesignating paragraphs (5) and (6) as paragraphs (6) and (8), respectively;\n**(B)**\nby inserting after paragraph (4) the following new paragraph:\n(5) The term maximum fair price has the meaning given such term in section 1191(c)(3) of the Social Security Act ( 42 U.S.C. 1320f(c)(3) ). ; and\n**(C)**\nby inserting after paragraph (6), as redesignated by subparagraph (A), the following new paragraph:\n(7) The term selected drug has the meaning given such term in section 1192(c) of the Social Security Act ( 42 U.S.C. 1320f\u20131(c) ). ; and\n**(4)**\nby adding at the end the following new subsections:\n(j) During any year a selected drug is covered under the Drug Price Negotiation Program established under section 1191 of the Social Security Act ( 42 U.S.C. 1320f ), each manufacturer entering into a master agreement may not set the maximum price for such selected drug included in such master agreement at the time such master agreement is executed at a price exceeding the maximum fair price for such drug as set by such Drug Price Negotiation Program for the duration of such master agreement. .\n##### (d) Application\n**(1) In general**\nThe amendments made in subsection (c) shall apply with respect to each master agreement under section 8126 of title 38, United States Code, covering a selected drug, as defined by such section, that is in effect on the date of the enactment of this Act or enters into force on or after such date.\n**(2) Termination of the Drug Price Negotiation Program**\nUpon termination of the Drug Price Negotiation Program established under section 1191 of the Social Security Act ( 42 U.S.C. 1320f ), each master agreement described in paragraph (1) shall be modified to reflect the drug price maximums as of the date of such modification under existing law for each selected drug, as defined in section 8126 of title 38, United States Code, as amended by subsection (c).\n##### (e) Conforming amendments\nPart E of the Social Security Act ( 42 U.S.C. 1320f et seq. ) is amended\u2014\n**(1)**\nin section 1193(a)(4)(A), by striking 8126(h)(5) and inserting 8126(h) ; and\n**(2)**\nin section 1194(c)(6), by striking 8126(h)(5) and inserting 8126(h) .",
      "versionDate": "2026-05-07",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-05-13T16:15:03Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8667ih.xml"
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
      "title": "MISSION Rx Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T10:08:45Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MISSION Rx Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T10:08:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Maximizing Individual Savings for Servicemembers In Obtaining Negotiated Rx Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T10:08:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles 10 and 38, United States Code, to set the maximum cost-sharing amount paid by an eligible covered beneficiary under the TRICARE program and a veteran for such selected drug, as established under the Social Security Act, and the maximum price of a selected drug procured by Federal agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T10:03:33Z"
    }
  ]
}
```
