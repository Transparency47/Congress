# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8092?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8092
- Title: Native American Housing Assistance and Self-Determination Modernization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8092
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-05-14T08:08:34Z
- Update date including text: 2026-05-14T08:08:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-04-23 - IntroReferral: Sponsor introductory remarks on measure. (CR H3080)
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-04-23 - IntroReferral: Sponsor introductory remarks on measure. (CR H3080)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8092",
    "number": "8092",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "D000634",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Downing, Troy [R-MT-2]",
        "lastName": "Downing",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Native American Housing Assistance and Self-Determination Modernization Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:34Z",
    "updateDateIncludingText": "2026-05-14T08:08:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H3080)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "OR"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "OK"
    },
    {
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "OK"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "MI"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "MO"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "PA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "True",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "KY"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "WI"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "OH"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "IN"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "GA"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "MT"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "NE"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TN"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "SD"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "ND"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "ID"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "WI"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "KS"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MN"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NC"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NM"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "WA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "AZ"
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
      "sponsorshipDate": "2026-03-26",
      "state": "MA"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NM"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "ME"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NM"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "OR"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "IA"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "HI"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "OK"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "CO"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "HI"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NE"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8092ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8092\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Mr. Downing (for himself, Ms. Bynum , Mr. Cole , Mr. Lucas , Mr. Huizenga , Mrs. Wagner , Mr. Meuser , Mr. Haridopolos , Mr. Lawler , Ms. De La Cruz , Mr. Barr , Mr. Steil , Mr. Davidson , Mr. Stutzman , Mr. Loudermilk , Mr. Zinke , Mr. Bacon , Mr. Fleischmann , Mr. Johnson of South Dakota , Mrs. Fedorchak , Mr. Simpson , Mr. Liccardo , Ms. Moore of Wisconsin , Ms. Davids of Kansas , Ms. Craig , Mr. Davis of North Carolina , Mr. Vasquez , Mr. Larsen of Washington , Mr. Stanton , Mr. Keating , Ms. Leger Fernandez , Ms. Pingree , Ms. Stansbury , Mr. Bentz , and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo reauthorize the Native American Housing Assistance and Self-Determination Act of 1996, and for other purposes.\n#### 1. Short title; Table of contents\n##### (a) Short title\nThis Act may be cited as the Native American Housing Assistance and Self-Determination Modernization Act of 2026 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; Table of contents.\nSec. 2. Consolidation of environmental review requirements.\nSec. 3. Authorization of appropriations.\nSec. 4. Student housing assistance.\nSec. 5. Clarification of application of rent rule only to units owned or operated by Indian Tribe or tribally designated housing entity.\nSec. 6. Deadline for action on request for approval regarding exceeding TDC maximum cost for project.\nSec. 7. Homeownership or lease-to-own low-income requirement and income targeting.\nSec. 8. Lease requirements and tenant selection.\nSec. 9. Statutory authority to suspend grant funds in emergencies.\nSec. 10. Reports to Congress.\nSec. 11. 99-year leasehold interest in trust or restricted lands for housing purposes.\nSec. 12. Reauthorization of housing assistance for Native Hawaiians.\nSec. 13. Community-based development organizations and special activities by Indian Tribes.\nSec. 14. Housing counseling certification waiver.\nSec. 15. Eligibility for housing counseling grants.\nSec. 16. Section 184 Indian home loan guarantee program.\nSec. 17. Loan guarantees for Native Hawaiian housing.\nSec. 18. Rental assistance for homeless or at-risk Indian veterans.\nSec. 19. Continuum of care.\nSec. 20. Streamlining reporting requirements.\nSec. 21. Application of Build America, Buy America requirements.\n#### 2. Consolidation of environmental review requirements\nSection 105 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4115 ) is amended\u2014\n**(1)**\nin subsection (c)(2) by adding after other officer of the Tribe the following: , or a tribally designated housing entity official designated by the Tribe, ;\n**(2)**\nin subsection (d)\u2014\n**(A)**\nby redesignating paragraphs (1) through (4) as subparagraphs (A) through (D), respectively;\n**(B)**\nby striking The Secretary may and inserting the following:\n(1) In general The Secretary shall ; and\n**(C)**\nby adding at the end the following:\n(2) Waiver request The Secretary shall act upon a waiver request submitted under this subsection within 60 days after receipt of such request. ; and\n**(3)**\nby adding at the end the following new subsections:\n(e) Consolidation of environmental review requirements For assistance provided under this Act, including under title VIII of this Act, and grants to Indian Tribes issued under title I of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5301 et seq. ), the Indian Tribe or the Director of the Department of Hawaiian Home Lands shall be deemed to be in compliance with the environmental review requirements under this section or section 806 of this Act, title I of the Housing and Community Development Act of 1974, and the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), with regard to such project and to discharge any applicable environmental review requirements that might apply to Federal agencies with respect to the use of additional Federal funding sources for that project, if\u2014 (1) a recipient is using 1 or more sources of Federal funds in addition to grant amounts under this Act or in addition to a grant made to an Indian Tribe under title I of the Housing and Community Development Act of 1974; (2) such other sources of Federal funds do not exceed 49 percent of the Federal share of the project cost; and (3) the recipient\u2019s Indian Tribe or the Director of the Department of Hawaiian Home Lands has assumed all of the responsibilities for environmental review, decision-making, and action pursuant to this section, section 806 of this Act, or title I of the Housing and Community Development Act of 1974. (f) Environmental streamlining For activities assisted under this Act, including title VIII of this Act, or assisted with a grant to an Indian Tribe under title I of the Housing and Community Development Act ( 42 U.S.C. 5301 et seq. ), each of the following apply: (1) General exemption Notwithstanding any other provision of law, activities are exempt from any environmental review requirements where\u2014 (A) similar statutory exemptions apply to comparable activities of other Federal agencies; (B) the activity is an affordable housing activity having a total cost of not more than $250,000; (C) the activity is acquisition of property, including long-term equipment, funded using non-Federal sources; or (D) the activity involves the rehabilitation of a structure and\u2014 (i) the cost of the rehabilitation is less than fifty percent of the market value of the structure before rehabilitation; and (ii) the rehabilitation involves no ground disturbance, footprint change, or historic structure. (2) Radon exemption Notwithstanding any other provision of law, the Secretary may not require recipients (including the Director under title VIII of this Act) and Indian Tribes to consider or test for radon in the environmental review. Nothing in this provision shall be construed to limit the authority of a recipient (including the Director under title VIII of this Act) and an Indian Tribe to consider, test for, and mitigate radon. (3) Lead testing (A) Testing Lead paint testing of target housing that is in a remote area, and that is being rehabilitated, renovated, repaired, or painted in a manner that will repair or disturb building components that are painted or coated, must be conducted via\u2014 (i) paint chip testing, lead-based paint inspection, visual assessment for deteriorated paint, or a lead risk assessment for lead-based paint hazards, as applicable in accordance with section 1012 of the Residential Lead-Based Paint Hazard Reduction Act of 1992; or (ii) visual assessment for deteriorated paint and use of EPA-recognized lead test kits in accordance with sections 402 or 404, as applicable, of the Toxic Substances Control Act ( 15 U.S.C. 2682 , 2684) on each building component that is painted or coated and is to be disturbed. (B) Definitions In this paragraph: (i) Remote area The term Remote Area means as the area of a United States Postal Service ZIP Code that has a level 1 Frontier and Remote Area code as most recently posted on the website of the Department of Agriculture. (ii) Target housing The term Target Housing has the meaning given the term in section 1004(27) of the Residential Lead-Based Paint Hazard Reduction Act of 1992 ( 42 U.S.C. 4851b(27) ) assisted under the Native American Housing Assistance and Self-Determination Act of 1996. (4) Siting of hud projects near explosive and flammable hazards (A) In general Recipients carrying out activities under this Act (including the Director under title VIII of this Act) or Indian Tribe carrying out activities under title I of the Housing and Community Development Act shall be exempt from the Secretary\u2019s acceptable separation distance requirements and mitigation for residential tanks when the tank\u2014 (i) has a capacity of 1,320 gallons or less; (ii) is intended to contain common liquid fuels such as gasoline, fuel oil, kerosene, diesel, liquified petroleum gas (propane), or crude oil; (iii) is sited on land or property that contains a one- to four-family dwelling; (iv) is intended to be used solely by residents of such dwelling; and (v) is intended to be used by residents of such dwelling exclusively for non-commercial, non-industrial purposes. (B) Rule of construction Nothing in this provision shall be construed to limit the authority of a recipient (including the Director under title VIII of this Act) or an Indian Tribe to consider acceptable separation distance or implement mitigation measures. (C) Application The Secretary\u2019s acceptable separation distance requirements between a residential structure assisted with funds under this Act (or assisted with funds under a grant to an Indian Tribe under title 1 of the Housing and Community Development Act) and an above-ground storage tank used to store hazardous substances as defined in subpart C of part 51 of title 24, Code of Federal Regulations, or successor regulation, including mitigation measures, do not apply if the Indian Tribe or recipient (including the Director under title VIII of this Act) determines that\u2014 (i) inapplicability of the requirements is necessary to address the housing needs of the Indian Tribe or recipient (including the Director under title VIII of this Act); (ii) the use of an alternative standard, or the absence of a standard, does not present an unacceptable risk to the health or safety of residents; and (iii) the Indian Tribe or recipient (including the Director under title VIII of this Act) has provided notice and an opportunity for comment to residents of the affected area regarding the inapplicability of the requirements, and has developed a safety and response plan. (5) Streamlining wetland requirements The Secretary may not apply additional requirements involving protection of wetlands in instances where an affected wetland requires a U.S. Army Corps of Engineers General, Regional, or individual permit and the Indian Tribe or recipient (including the Director under title VIII of this Act) complies with permit conditions. .\n#### 3. Authorization of appropriations\nSection 108 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4117 ) is amended, in the first sentence, by striking 2009 through 2013 and inserting 2026 through 2032 .\n#### 4. Student housing assistance\nSection 202(3) of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4132(3) ) is amended by inserting including college housing assistance, after self-sufficiency and other services, .\n#### 5. Clarification of application of rent rule only to units owned or operated by Indian Tribe or tribally designated housing entity\nSection 203(a) of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4133(a) ) is amended\u2014\n**(1)**\nin paragraph (2), by inserting owned or operated by a recipient and after residing in a dwelling unit ; and\n**(2)**\nby adding at the end the following:\n(3) Self-determination Notwithstanding paragraph (2), recipients may establish their own policies governing maximum and minimum rents and homebuyer payments for dwelling units assisted under this Act, provided such policies are written and made publicly available. .\n#### 6. Deadline for action on request for approval regarding exceeding tdc maximum cost for project\n##### (a) Approval\nSection 103 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4113 ) is amended by adding at the end the following new subsection:\n(f) Deadline for action on request To exceed TDC maximum (1) Deadline A request for approval by the Secretary to exceed by more than 10 percent the total development cost maximum cost for a project shall be approved or denied during the 60-day period that begins on the date that the Secretary receives the request. (2) No response by Secretary If the Secretary does not respond to a request in the 60-day period described in paragraph (1), the request shall be deemed approved. .\n##### (b) Definition\nSection 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ) is amended\u2014\n**(1)**\nby redesignating paragraph (22) as paragraph (23); and\n**(2)**\nby inserting after paragraph (21) the following new paragraph:\n(22) Total development cost The term total development cost means, with respect to a housing project, the sum of all costs for the project, including all undertakings necessary for administration, planning, site acquisition, demolition, construction or equipment and financing (including payment of carrying charges), and for otherwise carrying out the development of the project, excluding off-site water and sewer. The total development cost amounts shall be based on a moderately designed house and determined by averaging the current construction costs as listed in not less than two nationally recognized residential construction cost indices. .\n#### 7. Homeownership or lease-to-own low-income requirement and income targeting\nSection 205 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4135 ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nin subparagraph (C), by striking and at the end; and\n**(B)**\nby adding at the end the following:\n(E) notwithstanding any other provision of this paragraph, in the case of rental housing that is made available to a current rental family for conversion to a homebuyer or a lease-purchase unit\u2014 (i) that the current rental family can purchase through a contract of sale, lease-purchase agreement, or any other sales agreement; and (ii) the housing is made available for purchase only by the current rental family, if the rental family was a low-income family at the time of their initial occupancy of such unit; and ; and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby striking The provisions and inserting the following:\n(1) In general The provisions ; and\n**(B)**\nby adding at the end the following:\n(2) Applicability to improvements The provisions of subsection (a)(2) regarding binding commitments for the remaining useful life of property shall not apply to improvements of privately owned homes if the cost of the improvements do not exceed 10 percent of the maximum total development cost for the home. .\n#### 8. Lease requirements and tenant selection\nSection 207 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4137 ) is amended by adding at the end the following:\n(c) Notice of termination The notice period described in subsection (a)(3) shall apply to projects and programs funded in part by amounts authorized under this Act. .\n#### 9. Statutory authority to suspend grant funds in emergencies\nSection 401(a)(4) of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4161(a)(4) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking may take an action described in paragraph (1)(C) and inserting may immediately take an action described in paragraph (1)(C) ; and\n**(2)**\nby striking subparagraph (B) and inserting the following:\n(B) Procedural requirements (i) In general If the Secretary takes an action described in subparagraph (A), the Secretary shall provide notice to the recipient at the time that the Secretary takes that action. (ii) Notice requirements The notice under clause (i) shall inform the recipient that the recipient may request a hearing by not later than 30 days after the date on which the Secretary provides the notice. (iii) Hearing requirements A hearing requested under clause (ii) shall be conducted\u2014 (I) in accordance with subpart A of part 26 of title 24, Code of Federal Regulations (or successor regulations); and (II) to the maximum extent practicable, on an expedited basis. (iv) Failure to conduct a hearing If a hearing requested under clause (ii) is not completed by the date that is 180 days after the date on which the recipient requests the hearing, the action of the Secretary to limit the availability of payments shall no longer be effective. .\n#### 10. Reports to Congress\nSection 407 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4167 ) is amended\u2014\n**(1)**\nin subsection (a), by striking Congress and inserting Committee on Indian Affairs and the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives ; and\n**(2)**\nby adding at the end the following:\n(c) Public availability The report described in subsection (a) shall be made publicly available, including to recipients. .\n#### 11. 99-year leasehold interest in trust or restricted lands for housing purposes\nSection 702 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4211 ) is amended\u2014\n**(1)**\nin the section heading, by striking 50-YEAR and inserting 99-YEAR ;\n**(2)**\nin subsection (b), by striking 50 years and inserting 99 years ; and\n**(3)**\nin subsection (c)(2), by striking 50 years and inserting 99 years .\n#### 12. Reauthorization of housing assistance for Native Hawaiians\nSection 824 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4243 ) is amended by striking for each of fiscal years 2001, 2002, 2003, 2004, and 2005 and inserting each of fiscal years 2026 through 2032. .\n#### 13. Community-based development organizations and special activities by Indian Tribes\nSection 105 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5305 ) is amended by adding at the end the following:\n(i) Indian Tribes, tribally designated housing entities, and Tribal organizations as community-Based development organizations (1) Definitions In this subsection: (A) Tribally designated housing entity The term tribally designated housing entity has the meaning given the term in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ). (B) Tribal organization The term Tribal organization has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). (2) Qualification An Indian Tribe, a tribally designated housing entity, or a Tribal organization shall qualify as a community-based development organization for purposes of carrying out new housing construction under this subsection for a grant made under section 106(a)(1). (j) Special activities by Indian Tribes An Indian Tribe (or a Tribal organization or Tribally designated housing entity designated by such Indian Tribe) receiving a grant under section 106(a)(1) shall be authorized to directly carry out activities described in subsection (a)(15). .\n#### 14. Housing counseling certification waiver\nSubtitle A of title II of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4131 et seq. ) is amended by adding at the end the following new section:\n211. Housing counseling certification waiver Notwithstanding section 106(g)(1) of the Housing and Urban Development Act of 1968 ( 12 U.S.C. 1701x(g)(1) ), Indian Tribes, Tribal organizations, tribally designated housing entities and the Department of Hawaiian Homelands carrying out homeownership counseling or rental housing counseling under section 105(a)(20) of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5305(a)(20) ) and sections 202(3) and 810(b)(2)(A) of the Native American Housing and Self-Determination Act of 1996 ( 25 U.S.C. 4132(3) , 4229(b)(2)(A)), may not be required to comply with any housing counseling certification requirements established by the Secretary. Nothing in this provision shall be construed as limiting such recipients\u2019 ability to obtain a housing counseling certification from the Secretary. .\n#### 15. Eligibility for housing counseling grants\nSection 106(a)(4) of the Housing and Urban Development Act of 1968 ( 12 U.S.C. 1701x(a)(4) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nby striking and and inserting a comma; and\n**(B)**\nby inserting before the period at the end the following: , Indian Tribes, and tribally designated housing entities ;\n**(2)**\nin subparagraph (B), by inserting , Indian Tribes, and tribally designated housing entities after organizations) ;\n**(3)**\nby redesignating subparagraph (F) as subparagraph (G); and\n**(4)**\nby inserting after subparagraph (E) the following:\n(F) Definitions In this paragraph, the terms Indian Tribe and tribally designated housing entity have the meanings given those terms in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ). .\n#### 16. Section 184 Indian home loan guarantee program\n##### (a) In general\nSection 184 of the Housing and Community Development Act of 1992 ( 12 U.S.C. 1715z\u201313a ) is amended\u2014\n**(1)**\nby amending subsection (a) to read as follows:\n(a) Authority To provide access to sources of private financing to Indian families, Indian housing authorities, and Indian Tribes, who otherwise could not acquire housing financing because of the unique legal status of Indian lands and the unique nature of Tribal economies, and to expand homeownership opportunities to Indian families, tribally designated housing entities, Indian housing authorities and Indian Tribes on fee simple lands, the Secretary may guarantee not to exceed 100 percent of the unpaid principal and interest due on any loan eligible under subsection (b) made to an Indian family, tribally designated housing entities, Indian housing authority, or Indian Tribe on trust land and fee simple land. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby amending paragraph (2) to read as follows:\n(2) Eligible housing The loan shall be used to construct, acquire, refinance, or rehabilitate 1- to 4-family dwellings that are standard housing. ;\n**(B)**\nin paragraph (4)\u2014\n**(i)**\nby redesignating subparagraphs (A) through (D) as clauses (i) through (iv), respectively, and adjusting the margins accordingly;\n**(ii)**\nby striking The loan and inserting the following:\n(A) In general The loan ;\n**(iii)**\nin subparagraph (A), as so redesignated, by adding at the end the following:\n(v) Any entity certified as a community development financial institution by the Community Development Financial Institutions Fund established under section 104(a) of the Riegle Community Development and Regulatory Improvement Act of 1994 ( 12 U.S.C. 4703(a) ). ; and\n**(iv)**\nby adding at the end the following:\n(B) Direct guarantee process (i) Authorization The Secretary may authorize qualifying lenders to participate in a direct guarantee process for approving loans under this section. (ii) Indemnification (I) In general If the Secretary determines that a mortgage guaranteed through a direct guarantee process under this subparagraph was not originated in accordance with the requirements established by the Secretary, the Secretary may require the lender approved under this subparagraph to indemnify the Secretary for the loss, irrespective of whether the violation caused the mortgage default. (II) Fraud or misrepresentation If fraud or misrepresentation is involved in a direct guarantee process under this subparagraph, the Secretary may require the originating lender approved under this subparagraph to indemnify the Secretary for the loss regardless of when an insurance claim is paid. (III) Implementation The Secretary may implement any requirement described in this subparagraph by regulation, notice or Dear Lender Letter. (C) Review of mortgagees (i) In general The Secretary may periodically review the mortgagees originating, underwriting, or servicing single family mortgage loans under this section. (ii) Requirements In conducting a review under clause (i), the Secretary\u2014 (I) shall compare the mortgagee with other mortgagees originating or underwriting loan guarantees for Indian housing based on the rates of defaults and claims for guaranteed mortgage loans originated, underwritten, or serviced by that mortgagee; (II) may compare the mortgagee with such other mortgagees based on underwriting quality, geographic area served, or any commonly used factors the Secretary determines necessary for comparing mortgage default risk, provided that the comparison is of factors that the Secretary would expect to affect the default risk of mortgage loans guaranteed by the Secretary; (III) shall implement such comparisons by regulation, notice, or Dear Lender Letter; and (IV) may terminate the approval of a mortgagee to originate, underwrite, or service loan guarantees for housing under this section if the Secretary determines that the mortgage loans originated, underwritten, or serviced by the mortgagee present an unacceptable risk to the Indian Housing Loan Guarantee Fund established under clause (i)\u2014 (aa) based on a comparison of any of the factors set forth in this subparagraph; or (bb) by a determination that the mortgagee engaged in fraud or misrepresentation. ; and\n**(C)**\nin paragraph (5)(A), by inserting before the semicolon at the end the following: except, as determined by the Secretary, when there is a loan modification under subsection (h)(1)(B), the term of the loan shall not exceed 40 years ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking Before and inserting the following:\n(A) In general Except as provided in subparagraph (B), before ; and\n**(ii)**\nby adding at the end the following:\n(B) Exception Subparagraph (A) shall not apply when the Secretary exercises their discretion to delegate direct guarantee endorsement authority to eligible lenders under subsection (b)(4)(B)(i). ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking The Secretary and inserting the following:\n(A) In general Except as provided in subparagraph (B), the Secretary ; and\n**(ii)**\nby adding at the end the following:\n(B) Exceptions When the Secretary exercises its discretion to delegate direct guarantee endorsement authority to eligible lenders under subsection (b)(4)(B)(i)\u2014 (i) subparagraph (A) shall not apply; and (ii) the direct guarantee endorsement lender may issue a certificate under this paragraph as evidence of the guarantee in accordance with requirements established by the Secretary. ; and\n**(C)**\nin paragraph (3), by inserting , or where applicable, the direct guarantee endorsement lender, after Secretary in each place that term appears; and\n**(4)**\nin subsection (l)\u2014\n**(A)**\nby redesignating paragraphs (8) and (9) as paragraphs (9) and (10), respectively; and\n**(B)**\nby inserting after paragraph (7) the following:\n(8) The term tribally designated housing entity has the meaning given the term in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ). .\n##### (b) Loan guarantees for Indian housing\nSection 184(i)(5) of the Housing and Community Development Act of 1992 (12 U.S.C. 1715z\u201313a(i)(5)) is amended\u2014\n**(1)**\nin subparagraph (B), by inserting after the first sentence the following: There are authorized to be appropriated for those costs such sums as may be necessary for each of fiscal years 2026 through 2032. ; and\n**(2)**\nin subparagraph (C), by striking 2008 through 2012 and inserting 2026 through 2032 .\n#### 17. Loan guarantees for Native Hawaiian housing\nSection 184A of the Housing and Community Development Act of 1992 ( 12 U.S.C. 1715z\u201313b ) is amended\u2014\n**(1)**\nin subsection (b), by inserting , and to expand homeownership opportunities to Native Hawaiian families who are eligible to receive a homestead under the Hawaiian Homes Commission Act, 1920 (42 Stat. 108) on fee simple lands in the State of Hawaii after markets ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby amending paragraph (2) to read as follows:\n(2) Eligible housing The loan shall be used to construct, acquire, refinance, or rehabilitate 1- to 4-family dwellings that are standard housing. ;\n**(B)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (B)\u2014\n**(I)**\nby redesignating clause (iv) as clause (v); and\n**(II)**\nby adding after clause (iii) the following:\n(iv) Any other lender that is supervised, approved, regulated, or insured by any agency of the Federal Government, including any entity certified as a community development financial institution by the Community Development Financial Institutions Fund established under section 104(a) of the Riegle Community Development and Regulatory Improvement Act of 1994 ( 12 U.S.C. 4703(a) ). ; and\n**(ii)**\nby adding at the end the following:\n(C) Direct guarantee endorsement and indemnification (i) In general If the Secretary determines that a loan guaranteed under this section was not originated in accordance with the requirements established by the Secretary, the Secretary may require the lender approved under this paragraph to indemnify the Secretary for the loss or potential loss, irrespective of whether the violation caused or will cause the loan default. (ii) Direct guarantee endorsement The Secretary may, dependent on the availability of systems development and staffing resources, delegate to eligible lenders the authority to directly endorse loans under this section. (iii) Fraud or misrepresentation If fraud or misrepresentation is involved in a loan guaranteed under this section, the Secretary may require the originating lender approved under this subparagraph to indemnify the Secretary for the loss regardless of whether there was a payment made by the Secretary under the guarantee. (iv) Implementation The Secretary may implement any requirements described in this subparagraph by regulation, notice, or Dear Lender Letter. (v) Review of lenders (I) In general The Secretary may periodically review the lenders originating, underwriting, or servicing single family mortgage loans under this section. (II) Requirements In conducting a review under paragraph (1), the Secretary\u2014 (aa) shall compare the lender with other lenders originating or underwriting loan guarantees for Indian housing and Native Hawaiian housing based on the rates of defaults and claims for guaranteed loans originated, underwritten, or serviced by that lender; and (bb) may compare the lender with such other lenders based on underwriting quality, geographic area served, or any commonly used factors the Secretary determines necessary for comparing mortgage default risk, provided that the comparison is of factors that the Secretary would expect to affect the default risk of mortgage loans guaranteed by the Secretary. ; and\n**(C)**\nin paragraph (5)(A), by inserting before the semicolon at the end the following: except, as determined by the Secretary, when there is a loan modification under subsection (i)(1)(B), the term of the loan shall not exceed 40 years ;\n**(3)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A), by striking Before and inserting Except as provided in subsection (C), before ;\n**(ii)**\nin subparagraph (B), by striking If and inserting Except as provided under subparagraph (C), before ; and\n**(iii)**\nby adding at the end the following:\n(C) Exception When the Secretary exercises its discretion to delegate direct guarantee endorsement authority pursuant to subsection (c)(4)(C)(ii), subparagraphs (A) and (B) of this paragraph shall not apply. ;\n**(B)**\nby amending paragraph (2) to read as follows:\n(2) Standard for approval (A) Approval Except as provided in subparagraph (B), the Secretary may approve a loan for guarantee under this section and issue a certificate under this subsection only if the Secretary determines that there is a reasonable prospect of repayment of the loan. (B) Exceptions When the Secretary exercises its discretion to delegate direct guarantee endorsement authority pursuant to subsection (c)(4)(C)(ii)\u2014 (i) subparagraph (A) shall not apply; and (ii) the direct guarantee endorsement lender may issue a certificate under this paragraph as evidence of the guarantee in accordance with requirements prescribed by the Secretary. ; and\n**(C)**\nin paragraph (3)(A), by inserting or, where applicable, the direct guarantee endorsement lender, after Secretary ; and\n**(4)**\nin subsection (j)(5)(B), by inserting after the first sentence the following: There are authorized to be appropriated for those costs such sums as may be necessary for each of fiscal years 2026 through 2032. .\n#### 18. Rental assistance for homeless or at-risk indian veterans\nSection 8(o)(19) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(19) ) is amended by adding at the end the following:\n(E) Indian veterans housing rental assistance program (i) Definitions In this subparagraph: (I) Eligible Indian veteran The term eligible Indian veteran means an Indian veteran who is\u2014 (aa) homeless or at risk of homelessness; and (bb) living\u2014 (AA) on or near a reservation; or (BB) in or near any other Indian area. (II) Eligible recipient The term eligible recipient means a recipient eligible to receive a grant under section 101 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4111 ). (III) Indian; Indian area The terms Indian and Indian area have the meanings given those terms in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ). (IV) Indian veteran The term Indian veteran means an Indian who is a veteran. (V) Program The term Program means the Tribal HUD\u2013VASH program carried out under clause (ii). (VI) Tribal organization The term Tribal organization has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). (ii) Program specifications The Secretary may not use less than 5 percent of the amounts made available for rental assistance under this paragraph to carry out a rental assistance and supported housing program, to be known as the Tribal HUD\u2013VASH program , in conjunction with the Secretary of Veterans Affairs, by awarding grants for the benefit of eligible Indian veterans. (iii) Model (I) In general Except as provided in subclause (II), the Secretary shall model the Program on the rental assistance and supported housing program authorized under subparagraph (A) and applicable appropriations Acts, including administration in conjunction with the Secretary of Veterans Affairs. (II) Exceptions (aa) Secretary of housing and urban development After consultation with Indian Tribes, eligible recipients, and any other appropriate Tribal organizations, the Secretary may make necessary and appropriate modifications to facilitate the use of the Program by eligible recipients to serve eligible Indian veterans. (bb) Secretary of veterans affairs After consultation with Indian Tribes, eligible recipients, and any other appropriate Tribal organizations, the Secretary of Veterans Affairs may make necessary and appropriate modifications to facilitate the use of the Program by eligible recipients to serve eligible Indian veterans. (iv) Eligible recipients The Secretary shall make amounts for rental assistance and associated administrative costs under the Program available in the form of grants to eligible recipients. (v) Funding criteria The Secretary shall award grants under the Program based on\u2014 (I) need; (II) administrative capacity; and (III) any other funding criteria established by the Secretary in a notice published in the Federal Register after consulting with the Secretary of Veterans Affairs. (vi) Administration Grants awarded under the Program shall be administered in accordance with the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4101 et seq. ), except that recipients shall\u2014 (I) submit to the Secretary, in a manner prescribed by the Secretary, reports on the utilization of rental assistance provided under the Program; and (II) provide to the Secretary information specified by the Secretary to assess the effectiveness of the Program in serving eligible Indian veterans. (vii) Consultation (I) Grant recipients; Tribal organizations The Secretary, in coordination with the Secretary of Veterans Affairs, shall consult with eligible recipients and any other appropriate Tribal organization on the design of the Program to ensure the effective delivery of rental assistance and supportive services to eligible Indian veterans under the Program. (II) Indian health service The Director of the Indian Health Service shall provide any assistance requested by the Secretary or the Secretary of Veterans Affairs in carrying out the Program. (viii) Waiver (I) In general Except as provided in subclause (II), the Secretary may waive or specify alternative requirements for any provision of law (including regulations) that the Secretary administers in connection with the use of rental assistance made available under the Program if the Secretary finds that the waiver or alternative requirement is necessary for the effective delivery and administration of rental assistance under the Program to eligible Indian veterans. (II) Exception The Secretary may not waive or specify alternative requirements under subclause (I) for any provision of law (including regulations) relating to labor standards or the environment. (ix) Renewal grants The Secretary may\u2014 (I) set aside, from amounts made available for tenant-based rental assistance under this subsection and without regard to the amounts used for new grants under clause (ii), such amounts as may be necessary to award renewal grants to eligible recipients that received a grant under the Program in a previous year; and (II) specify criteria that an eligible recipient must satisfy to receive a renewal grant under subclause (I), including providing data on how the eligible recipient used the amounts of any grant previously received under the Program. (x) Reporting Not later than 1 year after the date of enactment of this subparagraph, and every 5 years thereafter, the Secretary, in coordination with the Secretary of Veterans Affairs and the Director of the Indian Health Service, shall\u2014 (I) conduct a review of the implementation of the Program, including any factors that may have limited its success; and (II) submit a report describing the results of the review under item (aa) to\u2014 (aa) the Committee on Indian Affairs, the Committee on Banking, Housing, and Urban Affairs, the Committee on Veterans\u2019 Affairs, and the Committee on Appropriations of the Senate; and (bb) the Subcommittee on Indian and Insular Affairs of the Committee on Natural Resources, the Committee on Financial Services, the Committee on Veterans\u2019 Affairs, and the Committee on Appropriations of the House of Representatives. (xi) Impact on formula current assisted stock For a given fiscal year\u2019s allocation formula of the Native American Housing Block Grants program, as authorized under title I of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4111 et seq. ), the number of qualifying low-income housing dwelling units under section 302(b)(1) of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4152(b)(1) ) may not be reduced due to the placement of an eligible Indian veteran assisted with amounts provided under the Program within such qualifying units. .\n#### 19. Continuum of care\nTitle IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360 et seq. ) is amended\u2014\n**(1)**\nin section 401 ( 42 U.S.C. 11360 )\u2014\n**(A)**\nby redesignating paragraphs (32) through (35) as paragraphs (33) through (36), respectively; and\n**(B)**\nby inserting after paragraph (31) the following:\n(32) Tribally designated housing entity The term tribally designated housing entity has the meaning given the term in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ). ;\n**(2)**\nin section 423(g) ( 42 U.S.C. 11383(g) ), by inserting Indian Tribe, tribally designated housing entity, after private nonprofit organization, ; and\n**(3)**\nin section 435 ( 42 U.S.C. 11389 )\u2014\n**(A)**\nby striking (as defined in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 )) ;\n**(B)**\nby striking Notwithstanding and inserting the following:\n(a) Eligible entities Notwithstanding ; and\n**(C)**\nby adding at the end the following:\n(b) Civil rights exemptions With respect to grants awarded to carry out eligible activities under this subtitle, title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ) and title VIII of the Civil Rights Act of 1968 ( 42 U.S.C. 3601 et seq. ) shall not apply to applications or awards for projects to be carried out\u2014 (1) on or off reservation or trust lands for awards made to Indian Tribes or tribally designated housing entities; (2) on reservation or trust lands for awards made to eligible entities; or (3) with respect to a project in which amounts provided under this Act will be used specifically to benefit Tribal communities or Tribal members, in formula areas (as such term is defined in section 1000.302 of title 24, Code of Federal Regulations, or any successor regulation) for the Indian Housing Block Grant. (c) Certification Notwithstanding section 106 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12706 ) and section 403 of this Act, with respect to applications for projects to be carried out on reservations or trust land using grants awarded under this subtitle\u2014 (1) the applications shall contain a certification of consistency with an approved Indian housing plan developed under section 102 of the Native American Housing Assistance and Self-Determination Act ( 25 U.S.C. 4112 ); and (2) Indian Tribes and tribally designated housing entities that are recipients of awards for projects on reservations or trust land from such funds shall certify that they are following an approved housing plan developed under section 102 of the Native American Housing Assistance and Self-Determination Act ( 25 U.S.C. 4112 ). (d) Consolidated plan exemption A collaborative applicant for a Continuum of Care whose geographic area includes only reservation or trust land is not required to meet the requirement described in section 402(f)(2). (e) Waiver authority for Tribal participation In administering the amounts made available under this Act, the Secretary may waive, or specify alternative requirements for, any provision of any statute or regulation that the Secretary administers in connection with the obligation by the Secretary or the use by the recipient of these amounts (except for requirements related to labor standards and the environment), if the Secretary finds that good cause exists for the waiver or alternative requirement and such waiver or alternative requirement is necessary to modify any requirements preventing the participation of Indian Tribes or tribally designated housing entity in the Continuum of Care Program, or would expedite or facilitate the use of funds. .\n#### 20. Streamlining reporting requirements\nSection 404 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4164 ) is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (e); and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Consolidated reporting Notwithstanding any other provision of law, the Secretary shall develop policies and procedures that authorize interested Indian Tribes and tribally designated housing entities receiving grant amounts under this Act to submit to the Secretary, at their discretion, one consolidated annual performance report covering all grants the Indian Tribe or tribally designated housing entity receives from other grant programs administered by the Secretary. .\n#### 21. Application of Build America, Buy America requirements\nThe requirements under the Build America, Buy America Act ( 41 U.S.C. 8301 note) and any implementing regulations or guidance shall not apply to any housing activities carried out using any Federal financial assistance provided to Indian tribes, tribally designated housing entities, tribal organizations, and other Tribal entities (including the Department of Hawaiian Home Lands) under any Federal program.",
      "versionDate": "2026-03-26",
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
        "name": "Native Americans",
        "updateDate": "2026-04-09T20:50:30Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8092ih.xml"
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
      "title": "Native American Housing Assistance and Self-Determination Modernization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-07T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Native American Housing Assistance and Self-Determination Modernization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-07T05:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize the Native American Housing Assistance and Self-Determination Act of 1996, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-07T05:48:26Z"
    }
  ]
}
```
