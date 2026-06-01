# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8739?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8739
- Title: Brownfields Revitalization for a Better Tomorrow Act
- Congress: 119
- Bill type: HR
- Bill number: 8739
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-21T20:00:20Z
- Update date including text: 2026-05-21T20:00:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-12 - Committee: Referred to the Subcommittee on Environment.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-05-12: Introduced in House

## Actions

- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-12 - Committee: Referred to the Subcommittee on Environment.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8739",
    "number": "8739",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "G000558",
        "district": "2",
        "firstName": "Brett",
        "fullName": "Rep. Guthrie, Brett [R-KY-2]",
        "lastName": "Guthrie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Brownfields Revitalization for a Better Tomorrow Act",
    "type": "HR",
    "updateDate": "2026-05-21T20:00:20Z",
    "updateDateIncludingText": "2026-05-21T20:00:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Environment Subcommittee",
          "systemCode": "hsif18"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Environment Subcommittee",
          "systemCode": "hsif18"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Environment Subcommittee",
          "systemCode": "hsif18"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T16:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-05-14T15:08:49Z",
                "name": "Reported by"
              },
              {
                "date": "2026-05-14T15:08:31Z",
                "name": "Markup by"
              },
              {
                "date": "2026-05-12T15:08:12Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Environment Subcommittee",
          "systemCode": "hsif18"
        }
      },
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-12T16:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8739ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8739\nIN THE HOUSE OF REPRESENTATIVES\nMay 12, 2026 Mr. Guthrie introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 with respect to brownfields revitalization funding, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Brownfields Revitalization for a Better Tomorrow Act .\n#### 2. Brownfields revitalization funding\n##### (a) Definition of eligible entity\nSection 104(k)(1)(I) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k)(1)(I) ) is amended by inserting or 501(c)(6) after section 501(c)(3) .\n##### (b) Grants and loans for brownfield remediation\nSection 104(k)(3)(A)(ii) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k)(3)(A)(ii) ) is amended by striking $500,000 and all that follows through the period at the end and inserting $1,000,000 for each site to be remediated. .\n##### (c) Multipurpose brownfields grants\nSection 104(k)(4)(B) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k)(4)(B) ) is amended by striking $1,000,000 and inserting $2,000,000 .\n##### (d) General provisions\nSection 104(k)(5) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k)(5) ) is amended\u2014\n**(1)**\nin subparagraph (A), by amending clause (i) to read as follows:\n(i) Brownfield site characterization and assessment A grant under paragraph (2) may be awarded to an eligible entity on a community-wide or site-by-site basis, and shall not exceed, for any individual brownfield site covered by the grant, $500,000. ; and\n**(2)**\nby adding at the end the following:\n(F) Demolition A recipient of a grant or loan under paragraph (2), (3), or (4) may use up to 10 percent of the amounts made available under the grant or loan for demolition activities as needed to carry out the purpose for which the grant or loan was provided, subject to the approval of the Administrator. .\n##### (e) Ranking criteria\nSection 104(k)(6)(C) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k)(6)(C) ) is amended by adding at the end the following:\n(xiii) The extent to which a grant would facilitate the redevelopment and reuse of a brownfield site located in whole or in part on a former military installation. (xiv) The extent to which a grant could facilitate the remediation and reuse of a brownfield site for any activity described in the matter preceding clause (i) of section 41001(6)(A) of the FAST Act (regardless of whether the activity is described in any of clauses (i) through (iv) of such section). .\n##### (f) Implementation of brownfields programs\nSection 104(k)(7) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k)(7) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nby striking The Administrator may provide and inserting the following:\nThe Administrator\u2014 (i) may provide ;\n**(B)**\nby striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(ii) shall provide, on a noncompetitive basis, one grant to a covered entity in each of fiscal years 2028 and 2029, which grant shall be used to provide technical assistance to five covered applicants, selected by the Administrator, for purposes of applying for a grant under this subsection for activities to be carried out in a small community. ; and\n**(2)**\nby adding at the end the following:\n(C) Definitions In this paragraph: (i) Covered applicant The term covered applicant means an eligible entity\u2014 (I) that applied for, but did not receive, a grant under this subsection in the fiscal year immediately preceding the fiscal year for which the Administrator is selecting covered applicants under subparagraph (A)(ii) for activities to be carried out in a small community; and (II) for which the provision of technical assistance under this paragraph would help secure a grant under this subsection. (ii) Covered entity The term covered entity means an eligible entity or nonprofit organization with relevant experience and expertise in applying for and securing Federal assistance that is receiving funding under subparagraph (A)(i). (iii) Small community The term small community has the meaning given such term in section 128(a)(1)(B)(iv). .\n##### (g) Audits\nSection 104(k)(8) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k)(8) ) is amended\u2014\n**(1)**\nby amending subparagraph (A) to read as follows:\n(A) In general Not later than 2 years after the date of enactment of the Brownfields Revitalization for a Better Tomorrow Act , and every 2 years thereafter, the Inspector General of the Environmental Protection Agency shall conduct reviews or audits of the use of\u2014 (i) Federal funds by the Administrator under this subsection; (ii) grants and loans made under this subsection; and (iii) grants made to a State or Indian tribe under section 128(a) and activities carried out using such grants, including grants made to a State or Indian tribe using amounts made available under paragraph (7) of this subsection to carry out section 128(a)(1)(B)(ii)(III). ; and\n**(2)**\nin subparagraph (D), by striking September 30, 2022 and inserting 2 years after the date of enactment of the Brownfields Revitalization for a Better Tomorrow Act, and every 2 years thereafter .\n##### (h) Agreements\nSection 104(k)(10)(B)(iii) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k)(10)(B)(iii) ) is amended\u2014\n**(1)**\nby inserting the eligible entity is located in a small community or disadvantaged area (as those terms are defined in section 128(a)(1)(B)(iv)) or after unless ; and\n**(2)**\nby inserting , in which case the Administrator shall waive the matching share requirement under this clause before ; and .\n##### (i) Authorization of appropriations\nSection 104(k)(13) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k)(13) ) is amended to read as follows:\n(13) Authorization of appropriations (A) In general There is authorized to be appropriated to carry out this subsection $123,500,000 for each of fiscal years 2027 through 2031. (B) Funding for oversight Of the amounts made available under this paragraph for each fiscal year, 0.5 percent shall be available to carry out paragraph (8). .\n#### 3. Reauthorization of funding for certain assistance to States\nSection 128(a) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9628(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by adding at the end the following:\n(C) Brownfields inventory Each State or Indian tribe receiving a grant under this subsection shall maintain, update not less than annually, and make available to the public, by location, an inventory of all brownfield sites within that State on which activities authorized and funded pursuant to that grant have occurred. ; and\n**(2)**\nin paragraph (3), by striking $50,000,000 for each of fiscal years 2019 through 2023 and inserting $46,250,000 for each of fiscal years 2027 through 2031 .\n#### 4. Studies, reports, and guidance\n##### (a) Capitalization of revolving loan funds study\nNot later than September 30, 2028, the Comptroller General shall submit to Congress a report containing a review of revolving loan funds that were capitalized using a grant received under subparagraph (A)(i) of section 104(k)(3) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k)(3) ) during any of fiscal years 2015 through 2025, including information on\u2014\n**(1)**\nthe status and balance of each such revolving loan fund;\n**(2)**\neach loan or grant provided by an eligible entity under subparagraph (B) of such section; and\n**(3)**\nany barriers to the eligible entity providing additional loans or grants under such subparagraph (B).\n##### (b) Report on funding for covered entities and covered applicants\n**(1) In general**\nNot later than September 30, 2030, the Administrator shall submit to Congress a report on\u2014\n**(A)**\nthe effect of providing a grant under subparagraph (A)(ii) of section 104(k)(7)(A) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k)(7)(A) ) (as amended by this Act);\n**(B)**\nthe covered applicants selected by the Administrator under such subparagraph; and\n**(C)**\nthe status of\u2014\n**(i)**\nany applications for a grant under section 104(k) of such Act submitted by a covered applicant that received technical assistance pursuant to such subparagraph (A)(ii); and\n**(ii)**\nany activities for which a grant was provided pursuant to such an application.\n**(2) Updated report**\nNot later than September 30, 2032, the Administrator shall submit to Congress an update to the report submitted under paragraph (1).\n##### (c) Report on loan programs for assessment, remediation, and reuse of brownfield sites\n**(1) In general**\nNot later than two years after the date of enactment of this Act, the Administrator shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Environment and Public Works of the Senate a report containing\u2014\n**(A)**\nan analysis of whether establishing and implementing a loan program for the assessment, remediation, and reuse of brownfield sites, consistent with section 104(k) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k) ), would be feasible and useful, including consideration of\u2014\n**(i)**\nthe demand for larger loans for which the amount of the loan is equal to or greater than the largest loan currently offered by eligible entities under section 104(k)(3)(B) of such Act;\n**(ii)**\nthe extent to which such a program would facilitate the remediation and reuse of brownfield sites at which potential contamination is particularly extensive or complex; and\n**(iii)**\nthe extent to which such a program could facilitate the remediation and reuse of one of more brownfield sites at an earlier date than such activities would otherwise proceed; and\n**(B)**\nif the Administrator finds such a program will be feasible and useful, recommendations for statutory changes needed to authorize such a program.\n**(2) Consultation**\nIn carrying out this subsection, the Administrator shall consult with other Federal agencies, eligible entities, site owners, site developers, and any other entities the Administrator considers appropriate.\n##### (d) National Priorities List deletion study\nThe Comptroller General shall conduct a study with respect to the process for the deletion or partial deletion of sites from the National Priorities List established under section 105 of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9605 ), in order to identify any barriers to such deletion or partial deletion, including a review of the following:\n**(1)**\nThe process of coordination between Federal and State entities with respect to such deletion or partial deletion.\n**(2)**\nAny impediments to timely and efficient deletion or partial deletion of sites.\n**(3)**\nOpportunities to expedite the deletion or partial deletion of sites with respect to which applicable remedial action has been completed.\n##### (e) Guidance for permitting on brownfield sites\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Administrator shall develop guidance to assist Federal agencies in more efficiently issuing Federal authorizations, and conducting environmental reviews for such authorizations, with respect to projects relating to brownfield sites.\n**(2) Considerations**\nIn developing or updating guidance under this subsection, the Administrator shall consider matters related to\u2014\n**(A)**\nthe availability of historic site-specific environmental data;\n**(B)**\npreviously completed environmental reviews required by the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. );\n**(C)**\ndata or information collected as part of assessment or remediation activities under section 104(k) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k) );\n**(D)**\ncommunity engagement and historical experience with previous uses; and\n**(E)**\nany other matters the Administrator determines appropriate.\n**(3) Updates**\nThe Administrator shall update the guidance developed under this subsection periodically.\n##### (f) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Brownfield site**\nThe term brownfield site has the meaning given that term in section 101(39) of the Comprehensive Environmental Response, Compensation, and Liability Act ( 42 U.S.C. 9601(39) ).\n**(3) Federal authorization**\nThe term Federal authorization , with respect to a project\u2014\n**(A)**\nmeans any authorization required under Federal law for the project; and\n**(B)**\nincludes any permits, special use authorizations, certifications, opinions, or other approvals as may be required under Federal law for such project.\n**(4) Remedial action**\nThe term remedial action has the meaning given that term in section 101(24) of the Comprehensive Environmental Response, Compensation, and Liability Act ( 42 U.S.C. 9601(24) ).",
      "versionDate": "2026-05-12",
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
        "name": "Environmental Protection",
        "updateDate": "2026-05-21T20:00:20Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8739ih.xml"
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
      "title": "Brownfields Revitalization for a Better Tomorrow Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T09:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Brownfields Revitalization for a Better Tomorrow Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-13T09:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 with respect to brownfields revitalization funding, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-13T09:03:28Z"
    }
  ]
}
```
