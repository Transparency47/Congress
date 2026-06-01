# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4321?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4321
- Title: YouthBuild for the Future Act
- Congress: 119
- Bill type: S
- Bill number: 4321
- Origin chamber: Senate
- Introduced date: 2026-04-16
- Update date: 2026-05-12T19:29:31Z
- Update date including text: 2026-05-12T19:29:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in Senate
- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-04-16: Introduced in Senate

## Actions

- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4321",
    "number": "4321",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "YouthBuild for the Future Act",
    "type": "S",
    "updateDate": "2026-05-12T19:29:31Z",
    "updateDateIncludingText": "2026-05-12T19:29:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T16:58:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NY"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "VA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "DE"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "OR"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4321is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4321\nIN THE SENATE OF THE UNITED STATES\nApril 16 (legislative day, April 14), 2026 Mr. Markey (for himself, Mrs. Gillibrand , Mr. Kaine , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo reauthorize the YouthBuild program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the YouthBuild for the Future Act .\n#### 2. YouthBuild program\nSection 171 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3226 ) is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nby amending paragraph (1) to read as follows:\n(1) Reservation; amount of grants (A) Reservation In any fiscal year in which the amount appropriated to carry out this section is greater than $125,000,000, the Secretary shall reserve 20 percent of the portion of such amount that is greater than $125,000,000 for\u2014 (i) grants to applicants that are located in rural areas (as defined by the Secretary); and (ii) grants for programs operated by a tribe, organization, or entity described in section 166(c) or for the benefit of Indians, Alaska Natives, or Native Hawaiians (as the 3 terms are defined in section 166(b)) for the purpose of carrying out YouthBuild programs approved under this section. (B) Amount of grants After making the reservation described in subparagraph (A), the Secretary may use the remaining amount appropriated to carry out this section to make grants to applicants for the purpose of carrying out YouthBuild programs approved under this section. ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), in clause (iv)(II), by striking language ; and\n**(ii)**\nby adding at the end the following:\n(I) Provision of meals and other food assistance that is offered to participants in conjunction with another activity described in this paragraph. (J) Informing participants of their eligibility, and assisting participants in applying, for Federal and State means tested benefit programs, such as the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ), and assistance provided by the State through the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ). (K) Supportive services for individuals with disabilities to ensure such individuals may fully participate in a YouthBuild program. ; and\n**(C)**\nby adding at the end the following:\n(6) Use of funds for match An entity which receives a grant under this section may use a portion of such grant funds to meet all or a portion of the requirement to provide matching funds under section 121(e) of the National and Community Service Act of 1990 ( 42 U.S.C. 12571(e) ) or any other such requirements under such Act ( 42 U.S.C. 12501 et seq. ), if the funds are used consistent with the requirements described under subsection (e)(3). ;\n**(2)**\nin subsection (e)(1)\u2014\n**(A)**\nin subparagraph (A)(ii), by striking youth offender and inserting youth justice-involved individual ; and\n**(B)**\nin subparagraph (B)(i), by striking are basic skills deficient and inserting have foundational skill needs ;\n**(3)**\nin subsection (f), by adding at the end the following:\n(3) Consultation In establishing expected levels of performance under paragraph (1), the Secretary shall consult, on not less than an annual basis, with entities carrying out YouthBuild programs to ensure such levels of performance account for the workforce development and postsecondary education experiences of youth served by such programs. ;\n**(4)**\nin subsection (g), by adding at the end the following:\n(4) Annual release of Funding Opportunity Announcement The Secretary shall, to the greatest extent practicable, announce new funding opportunities for grants under this section during the same time period each year such grants are announced. (5) State wage data A State receiving grants under this section shall facilitate access for entities carrying out YouthBuild programs in the State to wage data of participants in YouthBuild programs for the purpose of meeting the requirements of this section. Such facilitation shall not reduce any protections afforded by the State which protect the privacy of participant information. ; and\n**(5)**\nby amending subsection (i) to read as follows:\n(i) Authorization of appropriations There are authorized to be appropriated to carry out this section\u2014 (1) $159,500,000 for fiscal year 2027; (2) $167,500,000 for fiscal year 2028; (3) $175,900,000 for fiscal year 2029; (4) $184,700,000 for fiscal year 2030; (5) $193,000,000 for fiscal year 2031; and (6) $203,600,000 for fiscal year 2032. .\n#### 3. YouthBuild employer partnerships\n##### (a) Partnership\nSubtitle D of title I of the Workforce Innovation and Opportunity Act is amended by inserting after section 171 ( 29 U.S.C. 3226 ) the following:\n171A. YouthBuild employer partnerships (a) In general Using funds appropriated under section 172(e), the Secretary shall award grants to eligible consortia for the purposes of developing partnerships, and developing, implementing, and expanding, through those partnerships, employment and training opportunities for participants of YouthBuild programs. (b) Eligible consortia To be eligible to receive a grant under this section, a consortium shall consist of\u2014 (1) an entity carrying out a YouthBuild program; and (2) a public or private employer in the State, region, or local area where such program is located. (c) Application To be eligible to receive a grant under this section, such a consortium shall submit an application at such time, in such form, and containing such information as the Secretary may require, including\u2014 (1) a description of the results of a needs assessment completed by such consortium on the needs of employers in the proposed service area for employees and of participants in the YouthBuild program for employment; (2) a description, listing the members, of any partnerships that the consortium may utilize to carry out employment and training opportunities under this section; (3) based on the results of the needs assessment described under paragraph (1) and the potential partnership described under paragraph (2), a description of the proposed uses of the grant funds by such consortium; and (4) a description of how the consortium will evaluate the effectiveness of the employment and training opportunities the consortium plans to provide under this section. (d) Priority In making grants under this section, the Secretary shall give priority to eligible entities that propose to carry out a partnership with a joint labor-management apprenticeship program. (e) Uses of funds A consortium that receives a grant under this section shall use the funds from such grant to develop a partnership, or to develop, implement, or expand, through those partnerships, employment and training opportunities for participants in the YouthBuild program. Such employment and training opportunities shall be aligned with the characteristics of the labor market in the proposed service area and meet the needs of employers in such area. .\n##### (b) Authorization of appropriations\nSection 172 of the Workforce Innovation and Opportunity Act is amended\u2014\n**(1)**\nby redesignating subsections (e) and (f) as subsections (f) and (g), respectively; and\n**(2)**\nby inserting after subsection (d) the following:\n(e) YouthBuild employer partnership There is authorized to be appropriated $20,000,000 for each of fiscal years 2027 through 2032 to carry out section 171A. .\n##### (c) Table of contents\nThe table of contents in section 1(b) of the Workforce Innovation and Opportunity Act is amended by inserting, after the item relating to section 171, the following:\nSec. 171A. YouthBuild employer partnerships. .",
      "versionDate": "2026-04-16",
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
        "actionDate": "2026-04-16",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "8333",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "YouthBuild for the Future Act",
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
        "name": "Labor and Employment",
        "updateDate": "2026-05-12T19:29:31Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4321is.xml"
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
      "title": "YouthBuild for the Future Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "YouthBuild for the Future Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the YouthBuild program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:43Z"
    }
  ]
}
```
