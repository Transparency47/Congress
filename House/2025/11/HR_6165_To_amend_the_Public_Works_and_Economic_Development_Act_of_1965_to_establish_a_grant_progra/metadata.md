# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6165?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6165
- Title: CREATIVE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6165
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-03-25T08:06:08Z
- Update date including text: 2026-03-25T08:06:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-21 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-21 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6165",
    "number": "6165",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "CREATIVE Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-25T08:06:08Z",
    "updateDateIncludingText": "2026-03-25T08:06:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-21",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-21T18:24:32Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-20T15:04:30Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "PA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "OH"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "ME"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "OH"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NJ"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6165ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6165\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Ms. Bonamici (for herself, Mr. Fitzpatrick , Mr. Carey , and Ms. Pingree ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Public Works and Economic Development Act of 1965 to establish a grant program to increase job opportunities for artists and creative professionals, improve the quality and availability of arts facilities and arts-related programming, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Capital, Repairs, and Employment for Art Talent to Improve Visibility Everywhere Act of 2025 or the CREATIVE Act of 2025 .\n#### 2. Grants for keeping artists on the job\nTitle II of the Public Works and Economic Development Act of 1965 ( 42 U.S.C. 3141 et seq. ) is amended by adding at the end the following:\n223. Grants for keeping artists on the job (a) Grants authorized The Secretary shall carry out a program, to be known as the Creative Economy Revitalization and Workforce Development Program , under which the Secretary awards grants to eligible entities, on a competitive basis, as follows: (1) Hiring and production grants The Secretary may award a grant to an eligible entity to hire or compensate professional performers, artists, and related or supporting professional personnel and staff for productions, projects, performances, exhibitions, workshops, or programs. A grant under this paragraph shall be in an amount that is not more than $5,000,000 and shall remain available for expenditure by the eligible entity for a period of 5 years from the date on which the grant is disbursed to such entity. (2) Construction and acquisition grants The Secretary may award a grant to an eligible entity to construct or acquire a facility to house arts productions, projects, performances, exhibitions, workshops, or programs. A grant under this paragraph shall be in an amount that is not more than $3,000,000, shall be accompanied by a commitment from the eligible entity to provide full-time, gainful employment to professional performers, writers, artists, and related or supporting professional personnel upon completion of the grant period and projects fully or partially funded by the grant, and shall remain available for expenditure by the eligible entity for a period of 5 years from the date on which the grant is disbursed to such entity. (3) Maintenance and improvement grants The Secretary may award a grant to an eligible entity to improve, repair, or maintain an existing facility housing arts productions, projects, performances, exhibitions, workshops, or programs. A grant under this paragraph shall be in an amount that is not more than $3,000,000, shall be accompanied by a commitment from the eligible entity to provide gainful employment to professional performers and related or supporting professional personnel during and upon completion of the grant period and projects fully or partially funded by the grant, and shall remain available for expenditure by the eligible entity for a period of 3 years from the date on which the grant is disbursed to such entity. (b) Prohibition on multiple awards An eligible entity may not receive more than 1 grant under subsection (a). (c) Application To be considered for a grant under this section, an eligible entity shall submit an application to the Secretary at such time, in such manner, and accompanied by such information as the Secretary may require. At a minimum each application shall include the following: (1) The type of grant for which the entity is applying from among the grant types described in paragraphs (1) through (3) of subsection (a). (2) A description of the specific purposes for which the entity proposes to use the grant, including, as applicable\u2014 (A) examples of productions, projects, performances, exhibitions, workshops, or programs that may be\u2014 (i) housed at a facility supported by the grant; or (ii) produced by employing professional performers and related or supporting professional personnel artists or staff members supported or employed by the grant; and (B) the perceived benefits that such productions, projects, performances, exhibitions, workshops, or programs provide to professional performers and related or supporting professional personnel, and the communities served by the eligible entity. (3) A description of the level of access to arts facilities and programming in the communities served by the eligible entity and, if applicable, identification of any disparities or gaps in such access. (4) A explanation of how the entity conducted, or intends to conduct, outreach and acquire input from the community in which the grant funds will be used, including input from, low-income individuals, individuals with disabilities, and other under-represented individuals in such community that are underrepresented in the creative sector, as well as arts labor organizations. (5) A description of any input received as a result of the outreach under paragraph (4). (6) A description of the steps the board or other appropriate overseeing body of such eligible entity has taken to ensure that governance of the organization includes representation from individuals described in paragraph (4). (7) A description of\u2014 (A) the level of community need for the activities proposed to be carried out with grant funds; and (B) the extent to which such activities will be supported by additional funds from the community and other sources. (8) If applicable, a comprehensive plan describing how the eligible entity will continue to operate any facility supported by the grant after the grant funds have been expended, including how the eligible entity will continue employing or facilitating employment for professional performers, writers, artists, and related or supporting professional personnel. (9) An attestation that the eligible entity will not abrogate existing collective bargaining agreements for the entire duration of the grant period. (10) An attestation that the eligible entity receiving a grant will abide by the labor standards of professional performers and personnel and guarantee to provide healthy and safe working conditions under section 5(m) of the National Foundation on the Arts and the Humanities Act of 1965 ( 20 U.S.C. 954(m) ). (11) An attestation that the eligible entity receiving a grant will provide or facilitate gainful employment for professional performers and related or supporting professional personnel. (12) Any other information or assurances the Secretary determines appropriate. (d) Priority In awarding grants under this section, the Secretary shall give priority to eligible entities that meet 1 or more of the following criteria (with higher priority given to eligible entities that meet more than 1 such criteria): (1) The eligible entity is located in a community with limited access to high-quality arts productions, projects, performances, exhibitions, or programs, which may be indicated by\u2014 (A) the community having 1 or fewer facilities for hosting arts programming; (B) the presence of an arts facility in the community that is in state of disrepair, a physical state that is not conducive to regularly host arts programming, or in need of infrastructure upgrades necessary for fully accessible workplaces for professional performers and related or supporting professional personnel with disabilities; or (C) the presence of an arts facility in the community that has canceled, paused, or reduced the length of a production season during any of the 3 years preceding the grant application. (2) The eligible entity proposes to use the grant to employ professional performers and related or supporting professional personnel and to expand arts productions, projects, performances, exhibitions, workshops, or programs from linguistically and culturally diverse populations who are considered ethnic, cultural, religious, or linguistic minorities and whose art is underrepresented in popular culture. (3) The eligible entity demonstrates no-fault financial hardship, limited support from State and local government sources, or a level of income insufficient to self-fund the activities for which the grant is sought. (4) The eligible entity proposes to use the grant to employ professional performers and related or supporting professional personnel and to host or produce arts productions, projects, performances, exhibitions, or programs that, if applicable, provide insight and perspective on current or historical events or local or regional economic issues. (5) The eligible entity is not a recipient of another grant under this title and the entity has not previously received a grant under this title. (6) The eligible entity proposes to use the grant to improve access to arts productions, projects, performances, exhibitions, or programs for people with disabilities, or to hire professional performers and other related or supporting professional personnel. (7) The eligible entity is located in a rural community. (8) The eligible entity provides individual artists and groups of artists with the opportunity to display or produce projects, performances, exhibitions, workshops, or programs. (9) The eligible entity proposes to use the grant for a purpose that furthers arts education in the community in which such funds will be used. (e) Supplement, not supplant An eligible entity that receives a grant under this section may use the grant only to supplement, and not to supplant, funds made available from non-Federal sources to carry out the activities supported by such grant. (f) Accountability The Secretary shall regularly review the activities of eligible entities receiving grants under this section to ensure that such entities are using the grant for the purposes for which it was provided and are otherwise in compliance with the requirements of this section. (g) Treatment of unexpended funds Funds received by an eligible entity under subsection (a) that are not expended within the allowable period specified in such subsection shall be returned to Secretary unless the Secretary makes a written determination that the entity may continue to expend the funds after the expiration of such period. (h) Reports (1) In general On an annual basis during each year of the grant period, an eligible entity that receives a grant under this section shall submit to the Secretary a report that includes a description of the following: (A) How the grant funds were used in the year covered by the report. (B) The effects, in the immediate term and over the remaining period of the grant, of the activities supported by the grant with respect to\u2014 (i) increasing access to arts facilities and programming within the community served by the eligible entity; (ii) reducing disparities in access to such facilities and programming in such communities; and (iii) providing or facilitating full-time gainful employment for professional performers and related or supporting professional personnel. (C) To the extent applicable, how the grant has or will be used to\u2014 (i) increase work opportunities for professional performers and related or supporting professional personnel; (ii) improve an existing facility\u2019s ability to host or produce high-quality arts productions, projects, performances, exhibitions, or programs; (iii) contribute to the construction or acquisition of a facility to host or produce high-quality arts productions, projects, performances, exhibitions, or programs, and if acquisition or construction of such facility is complete, how the facility has been able to host or assist in the production of such programming; (iv) support increasing the number of high-quality arts productions, projects, performances, exhibitions, workshops, or programs from linguistically and culturally diverse populations who are considered ethnic, cultural, religious, or linguistic minorities and whose art is underrepresented in popular culture; and (v) improve access to arts productions, projects, performances, exhibitions, or programs for artists with disabilities and other people with disabilities or to improve an eligible entity\u2019s ability to employ professional performers and related or supporting professional personnel with disabilities. (2) Public availability Not later than 180 days after receiving a report under paragraph (1), the Secretary shall make the report available on a publicly accessible website of the Economic Development Administration. (i) Definitions In this section: (1) Arts labor organization The term arts labor organization means an organization which is exempt from tax under section 501(c)(5) of the Internal Revenue Code of 1986. (2) Eligible entity The term eligible entity means\u2014 (A) a local arts agency; (B) a museum; or (C) any other nonprofit arts organization, including literary arts organizations, performing arts organizations, and professional nonprofit theaters, that is described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code. (3) Museum The term museum has the meaning given that term in section 273(1) of the Museum Services Act ( 20 U.S.C. 9172(1) ). (4) Professional nonprofit theater The term professional nonprofit theater means a nonprofit arts organization that is described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code that\u2014 (A) produces live choral, dance, musical, theatrical, operatic, orchestral, symphonic, or variety performances; (B) compensates all professional performers and related or supporting professional personnel at no less than the prevailing minimum compensation under 20 U.S.C. 954(m) ; (C) hosts events that are produced and managed by paid employees and not volunteers; (D) has a minimum of a 3-year history of programming prior to applying for a grant under this section; (E) has not violated any laws enforced by the Department of Labor, Equal Employment Opportunity Commission, National Labor Relations Board, or equivalent State agencies in the 3 years prior to applying for a grant under this section; and (F) is not engaged in a strike, lockout, or other labor dispute at the time of applying for a grant under this section. (5) Rural community The term rural community means a community in an area that is not designated by the Bureau of the Census as an urbanized area or urban cluster. (6) Related or supporting professional personnel The term related or supporting professional personnel means any staff member at an eligible entity that performs specialized work to produce arts productions, projects, performances, exhibitions, or programs at that entity. (7) Secretary The term Secretary means the Secretary of Commerce. (j) Authorization of appropriations (1) In general There are authorized to be appropriated to carry out this section $700,000,000 for each of the fiscal years 2026 through 2030. (2) Reservations From the amount appropriated under paragraph for each fiscal year, the Secretary\u2014 (A) shall reserve up to 25 percent to make grants under this section to eligible entities located in rural communities; and (B) may reserve\u2014 (i) not more than 30 percent to provide Maintenance and Improvement Grants; (ii) not more than 1 percent to provide technical assistance to eligible entities that are receiving grants under this section; and (ii) not more than 0.5 percent to ensure the Economic Development Administration has sufficient personnel to carry out the program under this section. (3) Prohibition None of the funds made available by this Act may be used for any activity that is subject to the reporting requirements set forth in section 203(a) of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 433(a) ). .",
      "versionDate": "2025-11-20",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-12-05T14:10:48Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6165ih.xml"
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
      "title": "CREATIVE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T07:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CREATIVE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Capital, Repairs, and Employment for Art Talent to Improve Visibility Everywhere Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Works and Economic Development Act of 1965 to establish a grant program to increase job opportunities for artists and creative professionals, improve the quality and availability of arts facilities and arts-related programming, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T07:48:27Z"
    }
  ]
}
```
