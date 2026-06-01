# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1452?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1452
- Title: Ending the Cycle of Dependency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1452
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-08-05T21:29:38Z
- Update date including text: 2025-08-05T21:29:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-20 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-20 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1452",
    "number": "1452",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001316",
        "district": "7",
        "firstName": "Eric",
        "fullName": "Rep. Burlison, Eric [R-MO-7]",
        "lastName": "Burlison",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Ending the Cycle of Dependency Act of 2025",
    "type": "HR",
    "updateDate": "2025-08-05T21:29:38Z",
    "updateDateIncludingText": "2025-08-05T21:29:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-20",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:37:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-20T20:40:01Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-21T20:37:20Z",
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
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "OK"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert [R-MO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "MO"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1452ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1452\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Burlison (for himself, Mr. Brecheen , and Mr. Onder ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Food and Nutrition Act of 2008 relating to work requirements; to amend title XIX of the Social Security Act to establish work requirements under the Medicaid program.\n#### 1. Short title\nThis Act may be cited as the Ending the Cycle of Dependency Act of 2025 .\n#### 2. Amendments to the Food and Nutrition Act of 2008 relating to work requirements\n##### (a) Work requirements\nSection 6(o) of the Food and Nutrition Act of 2008 (7 U.S.C. 2015(6)(o)) is amended\u2014\n**(1)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (A) by striking clause (ii) and inserting the following:\n(ii) over 60 years of age; ,\n**(B)**\nin subparagraph (C) by inserting under 6 years of age; a after child ,\n**(C)**\nin subparagraph (E) by striking the semicolon at the end and inserting ; or ,\n**(D)**\nby striking subparagraphs (F) and (H).; and\n**(E)**\nby redesignating subparagraph (G) as subparagraph (F), and\n**(2)**\nby striking subparagraph (4).\n##### (b) Conforming amendment\nSection 311 of title II of division C of the Fiscal Responsibility Act of 2023 ( Public Law 118\u20135 ; 137 STAT. 36) is amended by striking subsection (b).\n#### 3. Establishing work requirements under the Medicaid program\n##### (a) In general\nSection 1903(i) of the Social Security Act ( 42 U.S.C. 1396b(i) ) is amended\u2014\n**(1)**\nin paragraph (26), by striking ; or and inserting a semicolon;\n**(2)**\nin paragraph (27), by striking the period at the end and inserting ; or ;\n**(3)**\nby inserting after paragraph (27) the following new paragraph:\n(28) with respect to any amount expended for medical assistance for an applicable individual for a month in a calendar year if such individual did not meet the work requirement under section 1905(kk) for 3 or more preceding months during such calendar year while such individual was an applicable individual and was enrolled in a State plan (or waiver of such plan) under this title. ; and\n**(4)**\nin the flush left matter at the end, by striking and (18) and inserting (18), and (28) .\n##### (b) Work requirement\nSection 1905 of the Social Security Act ( 42 U.S.C. 1396d ) is amended by adding at the end the following new subsection:\n(kk) Work requirement for applicable individuals (1) Work requirement described For purposes of section 1903(i)(28), the work requirement described in this subsection with respect to an applicable individual and a month is that such individual satisfies at least one of the following with respect to such month: (A) The individual works 80 hours or more per month, or has a monthly income that is at least equal to the Federal minimum wage under section 6 of the Fair Labor Standards Act of 1938, multiplied by 80 hours. (B) The individual completes 80 hours or more of community service per month. (C) The individual participates in a work program for at least 80 hours per month. (D) The individual participates in a combination of work, including community service, and a work program for a total of at least 80 hours per month. (2) Definitions In this subsection: (A) Applicable individual The term applicable individual means any individual who is not\u2014 (i) under 19 years of age or age 60 or older; (ii) physically or mentally unfit for employment, as determined and verified by a physician or other medical professional; (iii) pregnant; (iv) the parent or caretaker of a dependent child under the age of 6; (v) the parent or caretaker of an incapacitated person; (vi) complying with work requirements under a different program under Federal law; (vii) participating in a drug or alcohol treatment and rehabilitation program (as defined in section 3(h) of the Food and Nutrition Act of 2008); or (viii) enrolled in an educational program at least half time. (B) Educational program The term educational program means\u2014 (i) an institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965); (ii) a program of career and technical education (as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006); or (iii) any other educational program approved by the Secretary. (C) State Medicaid agency The term State Medicaid agency means the State agency responsible for administering the State Medicaid plan. (D) Work program The term work program has the meaning given such term in section 6(o)(1) of the Food and Nutrition Act of 2008. .\n##### (c) State option To disenroll certain individuals\nSection 1902(a) of the Social Security Act ( 42 U.S.C. 1396a(a) ) is amended by adding at the end of the flush left text following paragraph (87) the following: Notwithstanding any of the preceding provisions of this subsection, at the option of a State, such State may elect to disenroll an applicable individual for a month if, with respect to medical assistance furnished to such individual for such month, no Federal financial participation would be available, pursuant to section 1903(i)(28). .",
      "versionDate": "2025-02-21",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Employment and training programs",
            "updateDate": "2025-07-14T15:21:43Z"
          },
          {
            "name": "Food assistance and relief",
            "updateDate": "2025-07-14T15:22:12Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-14T15:21:54Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-07-14T15:21:31Z"
          },
          {
            "name": "National and community service",
            "updateDate": "2025-07-14T15:21:59Z"
          },
          {
            "name": "Nutrition and diet",
            "updateDate": "2025-07-14T15:22:17Z"
          },
          {
            "name": "Poverty and welfare assistance",
            "updateDate": "2025-07-14T15:22:07Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-14T15:21:47Z"
          },
          {
            "name": "Temporary and part-time employment",
            "updateDate": "2025-07-14T15:21:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-18T13:57:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hr1452",
          "measure-number": "1452",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2025-08-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1452v00",
            "update-date": "2025-08-05"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Ending the Cycle of Dependency Act of 2025</strong></p><p>This bill establishes work requirements for adults ages 19 to 59 under Medicaid. It also extends work requirements to additional individuals under the Supplemental Nutrition Assistance Program (SNAP).</p><p>Specifically, the bill prohibits federal Medicaid payment for adults ages 19 to 59 unless these individuals (1) work at least 80 hours per month or have a monthly income that is at least equal to the federal minimum wage multiplied by 80 hours, (2) participate in a work program for at least 80 hours per month, (3) engage in community service for at least 80 hours per month, or (4) participate in a combination of the aforementioned activities for at least 80 hours per month. States may choose to disenroll individuals from Medicaid if they do not meet these requirements.\u00a0</p><p>The bill excludes certain individuals from these requirements, including those with disabilities, who care for children under the age of six, or who are enrolled in an educational program at least half-time.\u00a0</p><p>The bill also modifies work requirements under SNAP so as to require individuals ages 56 to 60, those with children ages 6 and older, homeless individuals, and certain former foster youth to meet the work requirements for SNAP (these individuals are currently exempt from work requirements). Additionally, states may no longer request to waive work requirements for individuals in areas with high unemployment rates or that lack a sufficient number of available jobs.</p>"
        },
        "title": "Ending the Cycle of Dependency Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1452.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ending the Cycle of Dependency Act of 2025</strong></p><p>This bill establishes work requirements for adults ages 19 to 59 under Medicaid. It also extends work requirements to additional individuals under the Supplemental Nutrition Assistance Program (SNAP).</p><p>Specifically, the bill prohibits federal Medicaid payment for adults ages 19 to 59 unless these individuals (1) work at least 80 hours per month or have a monthly income that is at least equal to the federal minimum wage multiplied by 80 hours, (2) participate in a work program for at least 80 hours per month, (3) engage in community service for at least 80 hours per month, or (4) participate in a combination of the aforementioned activities for at least 80 hours per month. States may choose to disenroll individuals from Medicaid if they do not meet these requirements.\u00a0</p><p>The bill excludes certain individuals from these requirements, including those with disabilities, who care for children under the age of six, or who are enrolled in an educational program at least half-time.\u00a0</p><p>The bill also modifies work requirements under SNAP so as to require individuals ages 56 to 60, those with children ages 6 and older, homeless individuals, and certain former foster youth to meet the work requirements for SNAP (these individuals are currently exempt from work requirements). Additionally, states may no longer request to waive work requirements for individuals in areas with high unemployment rates or that lack a sufficient number of available jobs.</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119hr1452"
    },
    "title": "Ending the Cycle of Dependency Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ending the Cycle of Dependency Act of 2025</strong></p><p>This bill establishes work requirements for adults ages 19 to 59 under Medicaid. It also extends work requirements to additional individuals under the Supplemental Nutrition Assistance Program (SNAP).</p><p>Specifically, the bill prohibits federal Medicaid payment for adults ages 19 to 59 unless these individuals (1) work at least 80 hours per month or have a monthly income that is at least equal to the federal minimum wage multiplied by 80 hours, (2) participate in a work program for at least 80 hours per month, (3) engage in community service for at least 80 hours per month, or (4) participate in a combination of the aforementioned activities for at least 80 hours per month. States may choose to disenroll individuals from Medicaid if they do not meet these requirements.\u00a0</p><p>The bill excludes certain individuals from these requirements, including those with disabilities, who care for children under the age of six, or who are enrolled in an educational program at least half-time.\u00a0</p><p>The bill also modifies work requirements under SNAP so as to require individuals ages 56 to 60, those with children ages 6 and older, homeless individuals, and certain former foster youth to meet the work requirements for SNAP (these individuals are currently exempt from work requirements). Additionally, states may no longer request to waive work requirements for individuals in areas with high unemployment rates or that lack a sufficient number of available jobs.</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119hr1452"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1452ih.xml"
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
      "title": "Ending the Cycle of Dependency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ending the Cycle of Dependency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 relating to work requirements; to amend title XIX of the Social Security Act to establish work requirements under the Medicaid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:37Z"
    }
  ]
}
```
