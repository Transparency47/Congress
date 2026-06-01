# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3104?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3104
- Title: Ukrainian Adjustment Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3104
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2026-05-20T08:08:04Z
- Update date including text: 2026-05-20T08:08:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3104",
    "number": "3104",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "K000375",
        "district": "9",
        "firstName": "William",
        "fullName": "Rep. Keating, William R. [D-MA-9]",
        "lastName": "Keating",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Ukrainian Adjustment Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:04Z",
    "updateDateIncludingText": "2026-05-20T08:08:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:05:10Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "PA"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "OH"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "IL"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "TX"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NJ"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NC"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "NY"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "OH"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "FL"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NY"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "CA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "WA"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "PA"
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
      "sponsorshipDate": "2026-02-04",
      "state": "DC"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "LA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "NC"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "NE"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "WI"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "TX"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "NV"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "CO"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "AZ"
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
      "sponsorshipDate": "2026-04-29",
      "state": "NC"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "IN"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3104ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3104\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mr. Keating (for himself, Mr. Fitzpatrick , Ms. Kaptur , and Mr. Quigley ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide for adjustment of status of nationals of Ukraine, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ukrainian Adjustment Act of 2025 .\n#### 2. Adjustment of status for eligible Ukrainian nationals\n##### (a) Streamlined adjustment of status for eligible Ukrainian nationals\n**(1) In general**\nNotwithstanding any other provision of law, the Secretary of Homeland Security shall adjust the status of an eligible Ukrainian national described in subsection (b) to the status of an alien lawfully admitted for permanent residence if the eligible Ukrainian national\u2014\n**(A)**\nsubmits an application for adjustment of status in accordance with procedures established by the Secretary of Homeland Security;\n**(B)**\nsubject to subsection (c), is otherwise admissible to the United States as an immigrant, except that the grounds of inadmissibility under paragraphs (4), (5), and (7)(A) of section 212(a) the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ) shall not apply;\n**(C)**\nhas complied with the vetting requirements under paragraphs (1) and (2) of subsection (d) to the satisfaction of the Secretary of Homeland Security; and\n**(D)**\nthe Secretary of Homeland Security determines that the adjustment of status of the eligible Ukrainian national is not contrary to the national welfare, safety, or security of the United States.\n**(2) Applicability of refugee admissibility requirements**\nThe provisions relating to admissibility for a refugee seeking adjustment of status under section 209(c) of the Immigration and Nationality Act ( 8 U.S.C. 1159(c) ) shall apply to an applicant for adjustment of status under this subsection.\n##### (b) Eligible Ukrainian national\nNotwithstanding any other provision of law, an eligible Ukrainian national for the purpose of this section is a citizen or national of Ukraine (or a person who last habitually resided in Ukraine) who\u2014\n**(1)**\ncompleted security and law enforcement background checks to the satisfaction of the Secretary of Homeland Security and was subsequently\u2014\n**(A)**\nparoled into the United States after February 20, 2014; or\n**(B)**\nparoled into the United States for the purpose of accompanying or following to join as\u2014\n**(i)**\nthe spouse or child (as defined in section 101(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1101(b)(1) )) of an individual described in subparagraph (A); or\n**(ii)**\nthe parent, legal guardian, or primary caregiver of an individual described in subparagraph (A) who is determined to be an unaccompanied child under section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) ) or section 412(d)(2)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1522(d)(2)(B) ); and\n**(2)**\nhas not had such parole terminated by the Secretary of Homeland Security.\n##### (c) Waiver\n**(1) In general**\nWith respect to an applicant for adjustment of status under this section, subject to paragraph (2), the Secretary of Homeland Security may waive any applicable ground of inadmissibility under section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ) (other than paragraphs 2(C) or (3) of such section) for humanitarian purposes, to ensure family unity, or if a waiver is otherwise in the public interest.\n**(2) Limitations**\nThe Secretary of Homeland Security may not waive under this subsection any applicable ground of inadmissibility under section 212(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2) ) that arises due to criminal conduct that was committed\u2014\n**(A)**\non or after February 20, 2014;\n**(B)**\nwithin the United States; and\n**(C)**\nby an applicant for adjustment of status under this section.\n**(3) Rule of construction**\nNothing in this subsection may be construed to limit any other waiver authority.\n##### (d) Interview and vetting requirements\n**(1) In general**\nThe Secretary of Homeland Security shall establish vetting requirements for applicants seeking adjustment of status under this section that are equivalent to the vetting requirements for refugees admitted to the United States through the United States Refugee Admissions Program, including an interview.\n**(2) Rule of construction**\nNothing in this subsection may be construed to limit the authority of the Secretary of Homeland Security to maintain records under any other law.\n##### (e) Protection for battered spouses\n**(1) In general**\nAn alien whose marriage to an eligible Ukrainian national described in paragraph (1)(A) of subsection (b) has been terminated shall be eligible for adjustment of status under this section as an alien described in paragraph (1)(B) of that subsection for not more than 2 years after the date on which such marriage is terminated if there is a demonstrated connection between the termination of the marriage and battering or extreme cruelty perpetrated by the principal applicant.\n**(2) Applicability of other law**\nIn reviewing an application for adjustment of status under this section with respect to spouses and children who have been battered or subjected to extreme cruelty, the Secretary of Homeland Security shall apply section 204(a)(1)(J) of the Immigration and Nationality Act ( 8 U.S.C. 1154(a)(1)(J) ) and section 384 of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1367 ).\n##### (f) Date of approval\nUpon the approval of an application for adjustment of status under this section, the Secretary of Homeland Security shall create a record of the alien\u2019s admission as a lawful permanent resident as of the date on which the alien was inspected and admitted or paroled into the United States.\n##### (g) Prohibition on further authorization of parole\n**(1) In general**\nExcept as provided in paragraph (2), an individual who is a national of Ukraine shall not be authorized for an additional period of parole if such individual\u2014\n**(A)**\nis eligible to apply for adjustment of status under this section; and\n**(B)**\nfails to submit an application for adjustment of status by the later of\u2014\n**(i)**\nthe date that is 1 year after the date on which final guidance described in subsection (h)(2) is published; or\n**(ii)**\nthe date that is 1 year after the date on which such individual becomes eligible to apply for adjustment of status under this section.\n**(2) Exception**\nAn individual described in paragraph (1)(A) may be authorized for an additional period of parole if such individual\u2014\n**(A)**\nwithin the period described in paragraph (1)(B), seeks an extension to file an application for adjustment of status under this section; or\n**(B)**\nhas previously submitted to a vetting equivalent of the vetting required under subsection (d).\n**(3) Deadline for application**\nExcept as provided in paragraph (2), a national of Ukraine who does not submit an application for adjustment of status within the timeline provided in paragraph (1)(B) may not later adjust status under this section.\n##### (h) Implementation\n**(1) Interim guidance**\n**(A) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Homeland Security shall issue guidance implementing this section.\n**(B) Publication**\nNotwithstanding section 553 of title 5, United States Code, such guidance\u2014\n**(i)**\nmay be published on the internet website of the Department of Homeland Security; and\n**(ii)**\nshall be effective on an interim basis immediately upon such publication but may be subject to change and revision after notice and an opportunity for public comment.\n**(2) Final guidance**\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Homeland Security shall finalize guidance implementing this section.\n##### (i) Administrative review\nThe Secretary of Homeland Security shall provide applicants for adjustment of status under this section with the same right to, and procedures for, administrative review as are provided to applicants for adjustment of status under section 245 of the Immigration and Nationality Act ( 8 U.S.C. 1255 ).\n##### (j) Prohibition on fees\nThe Secretary of Homeland Security may not charge a fee to any eligible Ukrainian national in connection with\u2014\n**(1)**\nan application for adjustment of status or employment authorization under this section; or\n**(2)**\nthe issuance of a permanent resident card or an employment authorization document.\n##### (k) Pending applications\nDuring the period beginning on the date on which an alien files a bona fide application for adjustment of status under this section and ending on the date on which the Secretary of Homeland Security makes a final administrative decision regarding such application, any alien and any dependent included in such application who remains in compliance with all application requirements may not be\u2014\n**(1)**\nremoved from the United States unless the Secretary of Homeland Security makes a prima facie determination that the alien is, or has become, ineligible for adjustment of status under this section;\n**(2)**\nconsidered unlawfully present under section 212(a)(9)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(9)(B) ); or\n**(3)**\nconsidered an unauthorized alien (as defined in section 274A(h)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1324a(h)(3) )).\n##### (l) VAWA self petitioners\nSection 101(a)(51) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(51) ) is amended\u2014\n**(1)**\nin subparagraph (F), by striking or ;\n**(2)**\nin subparagraph (G), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(H) section 2(a) of the Ukrainian Adjustment Act of 2025 . .\n##### (m) Exemption from numerical limitations\nAliens granted adjustment of status under this section shall not be subject to the numerical limitations under sections 201, 202, and 203 of the Immigration and Nationality Act ( 8 U.S.C. 1151 , 1152, and 1153).\n##### (n) Rule of construction\nNothing in this section may be construed to preclude an eligible Ukrainian national from applying for or receiving any immigration benefit to which the eligible Ukrainian national is otherwise entitled.",
      "versionDate": "2025-04-30",
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
        "name": "Immigration",
        "updateDate": "2025-05-22T12:57:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-30",
    "originChamber": "House",
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
          "measure-id": "id119hr3104",
          "measure-number": "3104",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-30",
          "originChamber": "HOUSE",
          "update-date": "2026-03-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3104v00",
            "update-date": "2026-03-09"
          },
          "action-date": "2025-04-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Ukrainian Adjustment Act of 2025</strong></p><p>This bill provides a streamlined process for certain Ukrainian nationals (including accompanying spouse and children) who are living in the United States to receive lawful permanent resident status.</p><p>Specifically, the bill permits Ukrainian nationals who have been paroled into the United States after February 20, 2014, to apply for and receive lawful permanent resident status. Additionally, the Department of Homeland Security (DHS) may waive grounds for inadmissibility (excluding certain crimes or security related grounds) for individuals who apply for status adjustment. DHS must establish vetting requirements (including an interview) for applicants that are equivalent to those under the United States Refugee Admissions Program.</p><p>The bill also preserves eligibility for the status adjustment of certain battered spouses whose eligibility for such status stemmed from a marriage that has terminated.</p><p>Finally, the bill requires DHS to issue guidance to implement these requirements and establishes a deadline for eligible individuals to apply for adjustment.</p>"
        },
        "title": "Ukrainian Adjustment Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3104.xml",
    "summary": {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ukrainian Adjustment Act of 2025</strong></p><p>This bill provides a streamlined process for certain Ukrainian nationals (including accompanying spouse and children) who are living in the United States to receive lawful permanent resident status.</p><p>Specifically, the bill permits Ukrainian nationals who have been paroled into the United States after February 20, 2014, to apply for and receive lawful permanent resident status. Additionally, the Department of Homeland Security (DHS) may waive grounds for inadmissibility (excluding certain crimes or security related grounds) for individuals who apply for status adjustment. DHS must establish vetting requirements (including an interview) for applicants that are equivalent to those under the United States Refugee Admissions Program.</p><p>The bill also preserves eligibility for the status adjustment of certain battered spouses whose eligibility for such status stemmed from a marriage that has terminated.</p><p>Finally, the bill requires DHS to issue guidance to implement these requirements and establishes a deadline for eligible individuals to apply for adjustment.</p>",
      "updateDate": "2026-03-09",
      "versionCode": "id119hr3104"
    },
    "title": "Ukrainian Adjustment Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ukrainian Adjustment Act of 2025</strong></p><p>This bill provides a streamlined process for certain Ukrainian nationals (including accompanying spouse and children) who are living in the United States to receive lawful permanent resident status.</p><p>Specifically, the bill permits Ukrainian nationals who have been paroled into the United States after February 20, 2014, to apply for and receive lawful permanent resident status. Additionally, the Department of Homeland Security (DHS) may waive grounds for inadmissibility (excluding certain crimes or security related grounds) for individuals who apply for status adjustment. DHS must establish vetting requirements (including an interview) for applicants that are equivalent to those under the United States Refugee Admissions Program.</p><p>The bill also preserves eligibility for the status adjustment of certain battered spouses whose eligibility for such status stemmed from a marriage that has terminated.</p><p>Finally, the bill requires DHS to issue guidance to implement these requirements and establishes a deadline for eligible individuals to apply for adjustment.</p>",
      "updateDate": "2026-03-09",
      "versionCode": "id119hr3104"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3104ih.xml"
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
      "title": "Ukrainian Adjustment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:53Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ukrainian Adjustment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T06:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for adjustment of status of nationals of Ukraine, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T06:18:42Z"
    }
  ]
}
```
