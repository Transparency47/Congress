# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8333?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8333
- Title: YouthBuild for the Future Act
- Congress: 119
- Bill type: HR
- Bill number: 8333
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-05-13T08:06:27Z
- Update date including text: 2026-05-13T08:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-04-16: Introduced in House

## Actions

- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8333",
    "number": "8333",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001081",
        "district": "5",
        "firstName": "Jahana",
        "fullName": "Rep. Hayes, Jahana [D-CT-5]",
        "lastName": "Hayes",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "YouthBuild for the Future Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:27Z",
    "updateDateIncludingText": "2026-05-13T08:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T14:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NC"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "MO"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "IL"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "LA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "IN"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "FL"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "IL"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "GA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NJ"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NJ"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "WI"
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
      "sponsorshipDate": "2026-04-16",
      "state": "DC"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "MI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NJ"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "GA"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "AZ"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "False",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "FL"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "RI"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8333ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8333\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Mrs. Hayes (for herself, Ms. Adams , Mr. Bell , Ms. Budzinski , Mr. Carter of Louisiana , Mr. Carson , Mrs. Cherfilus-McCormick , Ms. Crockett , Mr. Davis of Illinois , Mrs. McBath , Mrs. McIver , Mr. Menendez , Ms. Moore of Wisconsin , Ms. Norton , Ms. Simon , Ms. Tlaib , Mrs. Watson Coleman , and Ms. Williams of Georgia ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo reauthorize the YouthBuild program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the YouthBuild for the Future Act .\n#### 2. YouthBuild program\nSection 171 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3226 ) is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nby amending paragraph (1) to read as follows:\n(1) Reservation; amount of grants (A) Reservation In any fiscal year in which the amount appropriated to carry out this section is greater than $125,000,000, the Secretary shall reserve 20 percent of the portion of such amount that is greater than $125,000,000 for\u2014 (i) grants to applicants that are located in rural areas (as defined by the Secretary); and (ii) grants for programs operated by a tribe, organization, or entity described in section 166(c) or for the benefit of Indians, Alaska Natives, or Native Hawaiians (as the 3 terms are defined in section 166(b)) for the purpose of carrying out YouthBuild programs approved under this section. (B) Amount of grants After making the reservation described in subparagraph (A), the Secretary may use the remaining amount appropriated to carry out this section to make grants to applicants for the purpose of carrying out YouthBuild programs approved under this section. ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), in clause (iv)(II), by striking language ; and\n**(ii)**\nby adding at the end the following:\n(I) Provision of meals and other food assistance that is offered to participants in conjunction with another activity described in this paragraph. (J) Informing participants of their eligibility, and assisting participants in applying, for Federal and State means-tested benefit programs, such as the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ), and assistance provided by the State through the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ). (K) Supportive services for individuals with disabilities to ensure such individuals may fully participate in a YouthBuild program. ; and\n**(C)**\nby adding at the end the following:\n(6) Use of funds for match An entity which receives a grant under this section may use a portion of such grant funds to meet all or a portion of the requirement to provide matching funds under section 121(e) of the National and Community Service Act of 1990 ( 42 U.S.C. 12571(e) ) or any other such requirements under such Act ( 42 U.S.C. 12501 et seq. ), if the funds are used consistent with the requirements described under subsection (e)(3). ;\n**(2)**\nin subsection (e)(1)\u2014\n**(A)**\nin subparagraph (A)(ii), by striking youth offender and inserting youth justice-involved individual ; and\n**(B)**\nin subparagraph (B)(i), by striking are basic skills deficient and inserting have foundational skill needs ;\n**(3)**\nin subsection (f), by adding at the end the following:\n(3) Consultation In establishing expected levels of performance under paragraph (1), the Secretary shall consult, on not less than an annual basis, with entities carrying out YouthBuild programs to ensure such levels of performance account for the workforce development and postsecondary education experiences of youth served by such programs. ;\n**(4)**\nin subsection (g), by adding at the end the following:\n(4) Annual release of Funding Opportunity Announcement The Secretary shall, to the greatest extent practicable, announce new funding opportunities for grants under this section during the same time period each year such grants are announced. (5) State wage data A State receiving grants under this section shall facilitate access for entities carrying out YouthBuild programs in the State to wage data of participants in YouthBuild programs for the purpose of meeting the requirements of this section. Such facilitation shall not reduce any protections afforded by the State which protect the privacy of participant information. ; and\n**(5)**\nby amending subsection (i) to read as follows:\n(i) Authorization of appropriations There are authorized to be appropriated to carry out this section\u2014 (1) $159,500,000 for fiscal year 2027; (2) $167,500,000 for fiscal year 2028; (3) $175,900,000 for fiscal year 2029; (4) $184,700,000 for fiscal year 2030; (5) $193,000,000 for fiscal year 2031; and (6) $203,600,000 for fiscal year 2032. .\n#### 3. YouthBuild employer partnerships\n##### (a) Partnership\nSubtitle D of title I of the Workforce Innovation and Opportunity Act is amended by inserting after section 171 ( 29 U.S.C. 3226 ) the following:\n171A. YouthBuild employer partnerships (a) In general Using funds appropriated under section 172(e), the Secretary shall award grants to eligible consortia for the purposes of developing partnerships, and developing, implementing, and expanding, through those partnerships, employment and training opportunities for participants of YouthBuild programs. (b) Eligible consortia To be eligible to receive a grant under this section, a consortium shall consist of\u2014 (1) an entity carrying out a YouthBuild program; and (2) a public or private employer in the State, region, or local area where such program is located. (c) Application To be eligible to receive a grant under this section, such a consortium shall submit an application at such time, in such form, and containing such information as the Secretary may require, including\u2014 (1) a description of the results of a needs assessment completed by such consortium on the needs of employers in the proposed service area for employees and of participants in the YouthBuild program for employment; (2) a description, listing the members, of any partnerships that the consortium may utilize to carry out employment and training opportunities under this section; (3) based on the results of the needs assessment described under paragraph (1) and the potential partnership described under paragraph (2), a description of the proposed uses of the grant funds by such consortium; and (4) a description of how the consortium will evaluate the effectiveness of the employment and training opportunities the consortium plans to provide under this section. (d) Priority In making grants under this section, the Secretary shall give priority to eligible entities that propose to carry out a partnership with a joint labor-management apprenticeship program. (e) Uses of funds A consortium that receives a grant under this section shall use the funds from such grant to develop a partnership, or to develop, implement, or expand, through those partnerships, employment and training opportunities for participants in the YouthBuild program. Such employment and training opportunities shall be aligned with the characteristics of the labor market in the proposed service area and meet the needs of employers in such area. .\n##### (b) Authorization of appropriations\nSection 172 of the Workforce Innovation and Opportunity Act is amended\u2014\n**(1)**\nby redesignating subsections (e) and (f) as subsections (f) and (g), respectively; and\n**(2)**\nby inserting after subsection (d) the following:\n(e) YouthBuild employer partnership There is authorized to be appropriated $20,000,000 for each of fiscal years 2027 through 2032 to carry out section 171A. .\n##### (c) Table of contents\nThe table of contents in section 1(b) of the Workforce Innovation and Opportunity Act is amended by inserting, after the item relating to section 171, the following:\nSec. 171A. YouthBuild employer partnerships. .",
      "versionDate": "2026-04-16",
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
        "actionDate": "2026-04-16",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4321",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "YouthBuild for the Future Act",
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
        "name": "Labor and Employment",
        "updateDate": "2026-04-24T19:50:50Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8333ih.xml"
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
      "title": "To reauthorize the YouthBuild program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-22T08:01:12Z"
    },
    {
      "title": "YouthBuild for the Future Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "YouthBuild for the Future Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T07:53:23Z"
    }
  ]
}
```
