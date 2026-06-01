# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1186?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1186
- Title: Lower Drug Costs for Families Act
- Congress: 119
- Bill type: S
- Bill number: 1186
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2026-01-10T07:01:12Z
- Update date including text: 2026-01-10T07:01:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1186",
    "number": "1186",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Lower Drug Costs for Families Act",
    "type": "S",
    "updateDate": "2026-01-10T07:01:12Z",
    "updateDateIncludingText": "2026-01-10T07:01:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T19:24:24Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MN"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "OR"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "WI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "RI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MN"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CT"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-27",
      "state": "ME"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "VT"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CO"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MI"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "AZ"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1186is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1186\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Ms. Cortez Masto (for herself, Ms. Klobuchar , Mr. Wyden , Ms. Baldwin , Mr. Reed , Ms. Smith , Mr. Blumenthal , Mr. King , Mr. Welch , Mr. Hickenlooper , Ms. Slotkin , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to apply prescription drug inflation rebates to drugs furnished in the commercial market and to change the base year for rebate calculations.\n#### 1. Short title\nThis Act may be cited as the Lower Drug Costs for Families Act .\n#### 2. Application of prescription drug inflation rebates to drugs furnished in the commercial market\n##### (a) Part B drugs\n**(1) Application of prescription drug inflation rebates to drugs furnished in the commercial market**\nSection 1847A(i) of the Social Security Act (42 U.S.C. 1395w\u20133a(i)) is amended\u2014\n**(A)**\nin paragraph (1)(A)(i), by striking units and inserting billing units ;\n**(B)**\nin paragraph (2)(A), by striking for which payment is made under this part and inserting that would be payable under this part if such drug were furnished to an individual enrolled under this part ; and\n**(C)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A)(i), by striking units and inserting billing units ; and\n**(ii)**\nby striking subparagraph (B) and inserting the following:\n(B) Total number of billing units For purposes of subparagraph (A)(i), the total number of billing units with respect to a part B rebatable drug is determined as follows: (i) Determine the total number of units equal to\u2014 (I) the total number of units, as reported under subsection (c)(1)(B) for each National Drug Code of such drug during the calendar quarter that is two calendar quarters prior to the calendar quarter as described in subparagraph (A), minus (II) the total number of units with respect to each National Drug Code of such drug for which payment was made under a State plan under title XIX (or waiver of such plan), as reported by States under section 1927(b)(2)(A) for the rebate period that is the same calendar quarter as described in subclause (I). (ii) Convert the units determined under clause (i) to billing units for the billing and payment code of such drug, using a methodology similar to the methodology used under this section, by dividing the units determined under clause (i) for each National Drug Code of such drug by the billing unit for the billing and payment code of such drug. (iii) Compute the sum of the billing units for each National Drug Code of such drug in clause (ii). .\n**(2) Change of base year for rebate calculation**\nSection 1847A(i) of the Social Security Act (42 U.S.C. 1395w\u20133a(i)) is amended\u2014\n**(A)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (D), by striking July 1, 2021 and inserting July 1, 2016 ; and\n**(ii)**\nin subparagraph (E), by striking January 2021 and inserting January 2016 ; and\n**(B)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking December 1, 2020 and inserting December 31, 2015 ; and\n**(II)**\nby striking January 2021 and inserting January 2016 ;\n**(ii)**\nin subparagraph (B), by striking December 1, 2020 and inserting December 31, 2015 ; and\n**(iii)**\nin subparagraph (C), by striking January 2021 and inserting January 2016 .\n**(3) Effective date**\nThe amendments made by this subsection shall apply with respect to calendar quarters beginning on or after January 1, 2026.\n##### (b) Covered part D drugs\n**(1) Application of prescription drug inflation rebates to drugs furnished in the commercial market**\nSection 1860D\u201314B of the Social Security Act ( 42 U.S.C. 1395w\u2013114b ) is amended\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1)\u2014\n**(I)**\nin subparagraph (A)(i), by striking the total number of units and all that follows through the semicolon and inserting the following: the total number of units that are used to calculate the average manufacturer price of such dosage form and strength with respect to such part D rebatable drug, as reported by the manufacturer of such drug under section 1927 for each month, with respect to such period; ; and\n**(II)**\nby striking subparagraph (B) and inserting the following:\n(B) Excluded units For purposes of subparagraph (A)(i), the Secretary shall exclude from the total number of units for a dosage form and strength with respect to a part D rebatable drug, with respect to an applicable period, the following: (i) Units of each dosage form and strength of such part D rebatable drug for which payment was made under a State plan under title XIX (or waiver of such plan), as reported by States under section 1927(b)(2)(A). (ii) Units of each dosage form and strength of such part D rebatable drug for which a rebate is paid under section 1847A(i). (iii) Beginning with plan year 2026, units of each dosage form and strength of such part D rebatable drug for which the manufacturer provides a discount under the program under section 340B of the Public Health Service Act. ; and\n**(ii)**\nin paragraph (6), by striking information .\u2014The Secretary and all that follows through rebatable covered part D drug dispensed and inserting the following: AMP reports .\u2014The Secretary shall provide for a method and process under which, in the case of a manufacturer of a part D rebatable drug that submits revisions to information submitted under section 1927 by the manufacturer with respect to such drug ; and\n**(B)**\nby striking subsection (d) and inserting the following:\n(d) Information For purposes of carrying out this section, the Secretary shall use information submitted by manufacturers under section 1927(b)(3) and information submitted by States under section 1927(b)(2)(A). .\n**(2) Change of base year for rebate calculation**\nSection 1860D\u201314B of the Social Security Act ( 42 U.S.C. 1395w\u2013114b ) is amended\u2014\n**(A)**\nin subsection (b)(5)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking October 1, 2021 and inserting October 1, 2016 ; and\n**(II)**\nby striking January 2021 and inserting January 2016 ; and\n**(ii)**\nin subparagraph (C), by striking January 2021 and inserting January 2016 ; and\n**(B)**\nin subsection (g)\u2014\n**(i)**\nin paragraph (3)\u2014\n**(I)**\nby striking January 1, 2021 and inserting January 1, 2016 ; and\n**(II)**\nby striking October 1, 2021 and inserting October 1, 2016 ; and\n**(ii)**\nin paragraph (4), by striking January 2021 and inserting January 2016 .\n**(3) Effective date**\nThe amendments made by this subsection shall take apply with respect to applicable periods (as defined in section 1860D\u201314B(g)(7) of the Social Security Act (42 U.S.C. 1395w\u2013114b(g)(7))) beginning on or after October 1, 2025.",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-04-01",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2554",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Drug Costs for Families Act",
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
        "name": "Health",
        "updateDate": "2025-04-11T12:42:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s1186",
          "measure-number": "1186",
          "measure-type": "s",
          "orig-publish-date": "2025-03-27",
          "originChamber": "SENATE",
          "update-date": "2025-04-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1186v00",
            "update-date": "2025-04-18"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Lower Drug Costs for Families Act</b></p> <p>This bill applies certain Medicare prescription drug rebate requirements to prescription drugs that are available under private health insurance.</p> <p>Current law requires drug manufacturers to issue rebates to the Centers for Medicare & Medicaid Services for brand-name drugs without generic equivalents under Medicare that (1) cost $100 or more per year per individual, and (2) for which prices increase faster than inflation. Manufacturers that fail to comply are subject to civil penalties.</p> <p>The bill applies these requirements to prescription drugs that are available in the commercial market under private health insurance. It also indexes rebate calculations to drug prices in 2016 (as opposed to 2021).</p>"
        },
        "title": "Lower Drug Costs for Families Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1186.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Lower Drug Costs for Families Act</b></p> <p>This bill applies certain Medicare prescription drug rebate requirements to prescription drugs that are available under private health insurance.</p> <p>Current law requires drug manufacturers to issue rebates to the Centers for Medicare & Medicaid Services for brand-name drugs without generic equivalents under Medicare that (1) cost $100 or more per year per individual, and (2) for which prices increase faster than inflation. Manufacturers that fail to comply are subject to civil penalties.</p> <p>The bill applies these requirements to prescription drugs that are available in the commercial market under private health insurance. It also indexes rebate calculations to drug prices in 2016 (as opposed to 2021).</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119s1186"
    },
    "title": "Lower Drug Costs for Families Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Lower Drug Costs for Families Act</b></p> <p>This bill applies certain Medicare prescription drug rebate requirements to prescription drugs that are available under private health insurance.</p> <p>Current law requires drug manufacturers to issue rebates to the Centers for Medicare & Medicaid Services for brand-name drugs without generic equivalents under Medicare that (1) cost $100 or more per year per individual, and (2) for which prices increase faster than inflation. Manufacturers that fail to comply are subject to civil penalties.</p> <p>The bill applies these requirements to prescription drugs that are available in the commercial market under private health insurance. It also indexes rebate calculations to drug prices in 2016 (as opposed to 2021).</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119s1186"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1186is.xml"
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
      "title": "Lower Drug Costs for Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Lower Drug Costs for Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to apply prescription drug inflation rebates to drugs furnished in the commercial market and to change the base year for rebate calculations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:33:23Z"
    }
  ]
}
```
