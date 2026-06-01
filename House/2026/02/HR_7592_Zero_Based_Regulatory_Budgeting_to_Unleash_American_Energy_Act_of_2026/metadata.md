# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7592?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7592
- Title: Zero-Based Regulatory Budgeting to Unleash American Energy Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7592
- Origin chamber: House
- Introduced date: 2026-02-17
- Update date: 2026-03-05T09:06:38Z
- Update date including text: 2026-03-05T09:06:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-17: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-02-17: Introduced in House

## Actions

- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-17",
    "latestAction": {
      "actionDate": "2026-02-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7592",
    "number": "7592",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "G000601",
        "district": "12",
        "firstName": "Craig",
        "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
        "lastName": "Goldman",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Zero-Based Regulatory Budgeting to Unleash American Energy Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-05T09:06:38Z",
    "updateDateIncludingText": "2026-03-05T09:06:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-17",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-17",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-17",
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
          "date": "2026-02-17T16:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-17T16:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "TX"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "TX"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "FL"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "AL"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "NC"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7592ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7592\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 17, 2026 Mr. Goldman of Texas (for himself, Mr. Crenshaw , Mr. Pfluger , Mr. Weber of Texas , Ms. Van Duyne , Mrs. Luna , Mr. Moore of Alabama , and Mr. Harrigan ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require certain agencies to impose extendable sunset dates on certain regulations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Zero-Based Regulatory Budgeting to Unleash American Energy Act of 2026 .\n#### 2. Definitions; statutory identification\nIn this Act:\n**(1) Covered agency**\nThe term covered agency means each of the following:\n**(A)**\nThe Department of Energy.\n**(B)**\nEach of the following offices within the Department of the Interior:\n**(i)**\nThe Bureau of Land Management.\n**(ii)**\nThe Bureau of Ocean Energy Management.\n**(iii)**\nThe Bureau of Safety and Environmental Enforcement.\n**(iv)**\nThe Office of Surface Mining Reclamation and Enforcement.\n**(C)**\nThe Federal Energy Regulatory Commission.\n**(2) Covered regulation**\nThe term covered regulation means\u2014\n**(A)**\nwith respect to the Department of Energy, any regulation promulgated by the Department of Energy under or pursuant to\u2014\n**(i)**\nthe Atomic Energy Act of 1954 ( 42 U.S.C. 2011 et seq. );\n**(ii)**\nthe Energy Independence and Security Act of 2007 ( 42 U.S.C. 17001 et seq. );\n**(iii)**\nthe Energy Policy Act of 1992 ( 42 U.S.C. 13201 et seq. );\n**(iv)**\nthe Energy Policy Act of 2005 ( 42 U.S.C. 15801 et seq. ); or\n**(v)**\npart B of title III of the Energy Policy and Conservation Act ( 42 U.S.C. 6291 et seq. );\n**(B)**\nwith respect to the Bureau of Land Management, any regulation promulgated by the Bureau of Land Management under or pursuant to\u2014\n**(i)**\nthe Energy Policy Act of 2005 ( 42 U.S.C. 15801 et seq. );\n**(ii)**\nthe Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ); or\n**(iii)**\nsections 2319 through 2344 of the Revised Statutes (commonly known as the Mining Law of 1872 ) ( 30 U.S.C. 22 et seq. );\n**(C)**\nwith respect to the Bureau of Ocean Energy Management, any regulation promulgated by the Bureau of Ocean Energy Management under or pursuant to\u2014\n**(i)**\nthe Energy Policy Act of 2005 ( 42 U.S.C. 15801 et seq. ); or\n**(ii)**\nthe Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 et seq. );\n**(D)**\nwith respect to the Bureau of Safety and Environmental Enforcement, any regulation promulgated by the Bureau of Safety and Environmental Enforcement under or pursuant to the Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 et seq. );\n**(E)**\nwith respect to the Office of Surface Mining Reclamation and Enforcement, any regulation promulgated by the Office of Surface Mining Reclamation and Enforcement under or pursuant to the Surface Mining Control and Reclamation Act of 1977 ( 30 U.S.C. 1201 et seq. ); and\n**(F)**\nwith respect to the Federal Energy Regulatory Commission, any regulation promulgated by the Federal Energy Regulatory Commission under or pursuant to\u2014\n**(i)**\nthe Federal Power Act ( 16 U.S.C. 791a et seq. );\n**(ii)**\nthe Natural Gas Act ( 15 U.S.C. 717 et seq. ); or\n**(iii)**\nthe Powerplant and Industrial Fuel Use Act of 1978 ( 42 U.S.C. 8301 et seq. ).\n**(3) Regulation**\nThe term regulation means each part, subpart, or individual provision of a rule (as defined in section 551 of title 5, United States Code) promulgated by a covered agency.\n#### 3. Zero-based regulating\n##### (a) Sunsets required\n**(1) Existing regulations**\nNot later than 90 days after the date of enactment of this Act, the head of each covered agency shall amend each covered regulation in effect on that date to provide that each covered regulation expires not later than the date that is 1 year after the effective date of that amendment.\n**(2) New regulations**\n**(A) In general**\nSubject to subparagraph (B), for each covered regulation promulgated on or after the date of enactment of this Act, the head of the applicable covered agency shall ensure that the covered regulation expires not later than 5 years after the effective date of the covered regulation.\n**(B) Waiver**\nThe head of a covered agency may exempt a covered regulation promulgated by the covered agency on or after the date of enactment of this Act from the requirement under subparagraph (A) if the head of the covered agency\u2014\n**(i)**\ndetermines that the covered regulation has a net deregulatory effect; and\n**(ii)**\nnotifies the Director of the Office of Management and Budget of that determination.\n##### (b) Extension of sunsets\n**(1) In general**\nThe head of a covered agency may only extend an expiration date imposed pursuant to subsection (a)\u2014\n**(A)**\nto a date that is not more than 5 years after the current expiration date; and\n**(B)**\nif, before the current expiration date and except as provided in paragraph (2)(A)\u2014\n**(i)**\nthe head of the covered agency provides an opportunity for public comment on the costs and benefits of the applicable covered regulation, which may include the publication of a request for information with respect to the covered regulation; and\n**(ii)**\nfollowing the completion of the opportunity for public comment under clause (i), the head of the covered agency determines, based on the comments provided in that opportunity, that an extension of the covered regulation is warranted.\n**(2) Effect of amendments**\n**(A) Deregulatory amendments**\nIf the head of a covered agency determines that an amendment to a covered regulation of that covered agency has a net deregulatory effect, the amendment may extend the expiration date for that covered regulation without carrying out the requirements of subparagraph (B) of paragraph (1), subject to the limitation described in subparagraph (A) of that paragraph.\n**(B) Other amendments**\nIf the head of a covered agency does not make the determination described in subparagraph (A) with respect to an amendment to a covered regulation of that covered agency, the existing expiration date of the covered regulation being amended shall apply to that amendment unless the requirements described in paragraph (1)(B) have been met.\n**(3) Continued extensions**\nThe head of a covered agency may extend the expiration date of a covered regulation as many times as the head of the agency determines appropriate, subject to the condition that each extension meets the requirements of this subsection.\n**(4) Savings provision**\nSeeking public comment with respect to a covered regulation under paragraph (1)(B)(i), including through a request for information, shall not automatically extend the applicable expiration date of the covered regulation.\n##### (c) Effect of sunset\nIf the expiration date of a covered regulation is not extended in accordance with subsection (b)\u2014\n**(1)**\nthe covered regulation shall cease to have any effect as of that expiration date;\n**(2)**\nthe applicable covered agency shall not enforce the covered regulation on or after that expiration date; and\n**(3)**\nas soon as practicable after that expiration date, the head of the applicable covered agency shall remove the covered regulation from the Code of Federal Regulations.\n#### 4. Severability\nIf any provision of this Act or the application of such provision to any person or circumstance is held to be unconstitutional, the remainder of this Act, and the application of the provision to any other person or circumstance, shall not be affected.\n#### 5. Administrative provisions\n##### (a) Savings provisions\nNothing in this Act impairs or otherwise affects the authority granted by law to an executive department or agency, or the head of an executive department or agency.\n##### (b) No rights or benefits\nNothing in this Act creates any right or benefit, substantive or procedural, enforceable at law or in equity, by any party against the United States, the departments, agencies, or entities of the United States, the officers, employees, or agents of the United States, or any other person.",
      "versionDate": "2026-02-17",
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
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "2427",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Zero-Based Regulatory Budgeting to Unleash American Energy Act of 2025",
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
        "name": "Energy",
        "updateDate": "2026-02-27T18:31:04Z"
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
      "date": "2026-02-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7592ih.xml"
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
      "title": "Zero-Based Regulatory Budgeting to Unleash American Energy Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T09:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Zero-Based Regulatory Budgeting to Unleash American Energy Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T09:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require certain agencies to impose extendable sunset dates on certain regulations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T09:48:39Z"
    }
  ]
}
```
