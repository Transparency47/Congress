# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/978?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/978
- Title: HELPER Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 978
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2026-04-29T11:03:31Z
- Update date including text: 2026-04-29T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/978",
    "number": "978",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "HELPER Act of 2025",
    "type": "S",
    "updateDate": "2026-04-29T11:03:31Z",
    "updateDateIncludingText": "2026-04-29T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
            "date": "2025-03-12T17:17:07Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-12T17:17:07Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "GA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "LA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "GA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "NH"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "NV"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "AZ"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CT"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "AK"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "ID"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "AZ"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "WI"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "PA"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MI"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "AK"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "WV"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "AR"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NM"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "FL"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "OK"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "NH"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s978is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 978\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mrs. Moody (for herself, Mr. Ossoff , Mr. Cassidy , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the National Housing Act to establish a mortgage insurance program for first responders, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Homes for Every Local Protector, Educator, and Responder Act of 2025 or the HELPER Act of 2025 .\n#### 2. FHA mortgage insurance program for mortgages for first responders\nSection 203 of the National Housing Act ( 12 U.S.C. 1709 ) is amended by adding at the end the following:\n(z) FHA mortgage insurance program for mortgages for first responders (1) Definitions In this subsection: (A) First responder The term first responder means an individual who is, as attested by the individual\u2014 (i) (I) employed full-time by a law enforcement agency of the Federal Government, a State, a Tribal government, or a unit of general local government; and (II) in carrying out such full-time employment, sworn to uphold, and make arrests for violations of, Federal, State, county, township, municipal, or Tribal laws, or authorized by law to supervise sentenced criminal offenders or individuals with pending criminal charges; (ii) employed full-time as a firefighter, paramedic, or emergency medical technician by a fire department or emergency medical services responder unit of the Federal Government, a State, a Tribal government, or a unit of general local government; or (iii) employed as a full-time teacher by a State-accredited public school or private school that provides direct services to students in grades pre-kindergarten through 12. (B) First-time homebuyer The term first-time homebuyer has the meaning given the term in section 104 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12704 ). (C) State The term State has the meaning given the term in section 201. (D) Tribal government The term Tribal government means the recognized governing body of any Indian or Alaska Native tribe, band, nation, pueblo, village, community, component band, or component reservation, individually identified (including parenthetically) in the list published most recently pursuant to section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ). (2) Authority The Secretary may, upon application by a mortgagee, insure any mortgage eligible for insurance under this subsection to an eligible mortgagor and, upon such terms and conditions as the Secretary may prescribe, make commitments for the insurance of such mortgages prior to the date of their execution or disbursement. (3) Mortgage terms; mortgage insurance premium (A) Terms (i) In general A mortgage insured under this subsection shall\u2014 (I) be made to an eligible mortgagor; (II) comply with the requirements established under paragraphs (1) through (7) of subsection (b); and (III) be used only to\u2014 (aa) purchase or repair a 1-family residence, including a 1-family dwelling unit in a condominium project, to serve as a principal residence of the mortgagor, as attested by the mortgagor; or (bb) purchase a principal residence of the mortgagor, as attested by the mortgagor, which is\u2014 (AA) a manufactured home to be permanently affixed to a lot that is owned by the mortgagor and titled as real property; or (BB) a manufactured home and a lot to which the home will be permanently affixed that is titled as real property. (ii) No down payment Notwithstanding any provision to the contrary in the matter following subsection (b)(2)(B) with respect to first-time homebuyers\u2014 (I) the Secretary may insure any mortgage that involves an original principal obligation (including allowable charges and fees and the premium pursuant to subparagraph (B) of this paragraph) in an amount not to exceed 100 percent of the appraised value of the property involved; and (II) the mortgagor of a mortgage described in subclause (I) shall not be required to pay any amount, in cash or its equivalent, on account of the property. (B) Mortgage insurance premium (i) Up-front premium The Secretary shall establish and collect an insurance premium in connection with mortgages insured under this subsection that is a percentage of the original insured principal obligation of the mortgage amount, which shall be collected at the time and in the manner provided under subsection (c)(2)(A), except that the premiums collected under this subparagraph\u2014 (I) may be in an amount that exceeds 3 percent of the amount of the original insured principal obligation of the mortgage; and (II) may be adjusted by the Secretary from time to time by increasing or decreasing such percentages as the Secretary considers necessary, based on the performance of mortgages insured under this subsection and market conditions. (ii) Prohibition of monthly premiums A mortgage insured under this subsection shall not be subject to a monthly insurance premium, including a premium under subsection (c)(2)(B). (4) Eligible mortgagors The mortgagor for a mortgage insured under this subsection shall, at the time the mortgage is executed\u2014 (A) be a first-time homebuyer; (B) have completed a program of housing counseling provided through a housing counseling agency approved by the Secretary; (C) as attested by the mortgagor\u2014 (i) be employed as a first responder; (ii) have been\u2014 (I) employed as a first responder for not less than 4 of the 5 years preceding the date on which the mortgagor submitted an application to insure the mortgage under this section; or (II) released from employment as a first responder due to an occupation-connected disability resulting from such duty or employment; (iii) be in good standing as a first responder and not on probation or under investigation for conduct that, if determined to have occurred, is grounds for termination of employment; (iv) in good faith intend to continue as a first responder for not less than 1 year following the date of closing on the mortgage; and (v) have previously never been the mortgagor under a mortgage insured under this subsection; (D) meet such requirements as the Secretary shall establish to ensure that insurance of the mortgage represents an acceptable risk to the Mutual Mortgage Insurance Fund; and (E) meet such underwriting requirements as the Secretary shall establish to meet actuarial objectives identified by the Secretary, which may include avoiding a positive subsidy rate or complying with the capital ratio requirement under section 205(f)(2). (5) Authorization of appropriations There is authorized to be appropriated to carry out the program under this subsection\u2014 (A) $660,000 for fiscal year 2026, to remain available until expended; and (B) $160,000 for each of fiscal years 2027 through 2032, to remain available until expended. (6) Reauthorization required The authority to enter into new commitments to insure mortgages under this subsection shall expire on the date that is 5 years after the date on which the Secretary first makes available insurance for mortgages under this subsection. .",
      "versionDate": "2025-03-12",
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
        "actionDate": "2025-03-14",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "2094",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "HELPER Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-04-04T13:00:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-12",
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
          "measure-id": "id119s978",
          "measure-number": "978",
          "measure-type": "s",
          "orig-publish-date": "2025-03-12",
          "originChamber": "SENATE",
          "update-date": "2026-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s978v00",
            "update-date": "2026-04-17"
          },
          "action-date": "2025-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Homes for Every Local Protector, Educator, and Responder Act of 2025 or the HELPER Act of 2025</strong></p><p>This bill establishes a program administered by the Department of Housing and Urban Development to provide mortgage assistance to law enforcement officers, elementary and secondary school teachers, firefighters, or other first responders. Specifically, these individuals may be eligible for a first-time mortgage on a primary family residence with no down payment. Instead, the mortgage is subject to a one-time, up-front mortgage insurance premium.</p>"
        },
        "title": "HELPER Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s978.xml",
    "summary": {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Homes for Every Local Protector, Educator, and Responder Act of 2025 or the HELPER Act of 2025</strong></p><p>This bill establishes a program administered by the Department of Housing and Urban Development to provide mortgage assistance to law enforcement officers, elementary and secondary school teachers, firefighters, or other first responders. Specifically, these individuals may be eligible for a first-time mortgage on a primary family residence with no down payment. Instead, the mortgage is subject to a one-time, up-front mortgage insurance premium.</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119s978"
    },
    "title": "HELPER Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Homes for Every Local Protector, Educator, and Responder Act of 2025 or the HELPER Act of 2025</strong></p><p>This bill establishes a program administered by the Department of Housing and Urban Development to provide mortgage assistance to law enforcement officers, elementary and secondary school teachers, firefighters, or other first responders. Specifically, these individuals may be eligible for a first-time mortgage on a primary family residence with no down payment. Instead, the mortgage is subject to a one-time, up-front mortgage insurance premium.</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119s978"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s978is.xml"
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
      "title": "HELPER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HELPER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Homes for Every Local Protector, Educator, and Responder Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Housing Act to establish a mortgage insurance program for first responders, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:31Z"
    }
  ]
}
```
