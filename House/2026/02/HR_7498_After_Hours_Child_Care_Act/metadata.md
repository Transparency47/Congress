# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7498?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7498
- Title: After Hours Child Care Act
- Congress: 119
- Bill type: HR
- Bill number: 7498
- Origin chamber: House
- Introduced date: 2026-02-11
- Update date: 2026-05-16T08:07:35Z
- Update date including text: 2026-05-16T08:07:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-02-11: Introduced in House

## Actions

- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7498",
    "number": "7498",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "H001091",
        "district": "2",
        "firstName": "Ashley",
        "fullName": "Rep. Hinson, Ashley [R-IA-2]",
        "lastName": "Hinson",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "After Hours Child Care Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:35Z",
    "updateDateIncludingText": "2026-05-16T08:07:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-11",
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
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T16:05:30Z",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "OR"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "NH"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "WI"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NY"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "KS"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "IL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "NY"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "VA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NV"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7498ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7498\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2026 Mrs. Hinson (for herself, Ms. Bonamici , Mr. Mackenzie , Mr. Pappas , Ms. Stefanik , and Mr. Pocan ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo establish and expand child care programs for parents who work nontraditional hours, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the After Hours Child Care Act .\n#### 2. Child Care and Development Innovation Fund\n##### (a) Establishment\nThe Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 658P as section 658T, and moving that section 658T to follow section 658S; and\n**(2)**\nby adding at the end the following:\n658U. Child Care and Development Innovation Fund (a) Purpose The purpose of this section is to\u2014 (1) improve child care access for parents working hours outside of traditional 9 to 5 work hours, such as parents working an evening, night, or weekend shift; and (2) address the needs of working parents with young children, so that the parents are able to stay attached to the workforce, attain eligibility for promotions and salary increases, and amass savings. (b) Definitions In this section: (1) Child care program The term child care program means the child care activities of an eligible child care provider. (2) Nontraditional work hours The term nontraditional work hours means work hours at least 25 percent of which\u2014 (A) are before 9 a.m. or after 5 p.m. on a weekday; (B) are on a Saturday or Sunday; or (C) are scheduled within 7 days before required attendance at work for those work hours. (3) Secretary The term Secretary means the Secretary of Health and Human Services. (c) General authority (1) Grants Not later than 90 days after the date of enactment of the After Hours Child Care Act , the Secretary shall establish a pilot program, through which the Secretary shall award grants on a competitive basis to eligible entities to pay for the Federal share of the cost of\u2014 (A) expanding capacity for an existing (as of January 1, 2027) child care program, including such a program of a family child care provider to serve families in which a parent is working nontraditional work hours; (B) entering into an enrollment-based contract with\u2014 (i) an eligible child care provider to serve such families; or (ii) a fiscal intermediary such as a staffed network of family child care providers, child care resource and referral organization, or entity operating a child care facilities fund for the services of multiple eligible child care providers to serve such families; (C) planning activities, including conducting a needs assessment and outreach to existing eligible child care providers (existing on the date of the outreach); (D) establishing an onsite child care program at a workplace to serve such families; (E) expanding capacity for an onsite child care program at a workplace to serve such families; or (F) establishing a child care program, including a program of a family child care provider with the primary goal of serving such families. (2) Duration The Secretary shall award the grant for a period of 5 years. A grant awarded under this section may not be renewed. (3) Amount The Secretary shall award the grant in an amount of not less than $25,000 and not more than $500,000. (d) Eligible entities To be eligible to receive a grant under this section, an entity shall be\u2014 (1) an eligible child care provider; or (2) a partnership of\u2014 (A) an eligible child care provider; and (B) a lead agency, business, child care resource and referral organization, community development financial institution, staffed network of family child care providers, another intermediary with experience supporting child care providers, or another appropriate entity. (e) Application To be eligible to receive a grant under this section, an entity shall submit an application to the Secretary at such time, in such manner, and containing\u2014 (1) a description of the activities to be funded under the grant; (2) a description of the objective for the activities, which may be an objective described in a paragraph of subsection (f), including\u2014 (A) whether the objective is to increase the quantity or quality of a good or service, specified in the description; and (B) information on that quantity or quality of that good or service, on the date of submission of the application; and (3) the population to be served through the activities. (f) Use of funds An entity that receives a grant under this section may use the grant funds for activities that may include\u2014 (1) staffing the child care program involved; (2) improving the child care facility and related equipment; (3) establishing or improving the curriculum of the child care program; (4) assisting eligible child care providers in meeting health and safety requirements, achieving licensure or registration as a child care provider, or improving quality; (5) acquiring other items needed for the child care program; and (6) providing training in the prevention of sudden infant death syndrome and safe sleep practices. (g) Match The non-Federal share of the cost described in subsection (c)(1) shall be 25 percent. (h) Report Not less often than every 2 years, the Secretary shall prepare and submit to Congress a report that includes\u2014 (1) information on the number of children served under this section and the employment status of their parents; (2) general information to demonstrate the impact of activities carried out under grants under this section on child care availability; (3) for each objective referred to in subsection (e)(2) that is described in an application submitted by a grant recipient, a summary of information obtained by\u2014 (A) collecting, from each recipient, information on the quantity or quality of the good or service referred to in subsection (e)(2)(B), as of the last day of the grant period; (B) comparing the information described in subsection (e)(2)(B) with the information described in subparagraph (A), for each such recipient; and (C) summarizing that collected information and those comparisons for all the recipients who described the objective in such an application; and (4) other information relevant to the grants made under this section. (i) Relationship to other requirements None of the requirements of this subchapter, other than section 658T, shall apply to this section. No reference in this subchapter to this subchapter shall be considered to include this section. (j) Reservation of funds The Secretary may reserve up to \u00bc of 1 percent of the amount appropriated under this subchapter to carry out this section for each of the fiscal years 2027 through 2031. .\n##### (b) Conforming amendments\n**(1) Application provisions**\nSection 658E(c)(2) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858c(c)(2) ) is amended\u2014\n**(A)**\nin subparagraph (A)(i)(II), by striking 658P(2) and inserting 658T(2) ; and\n**(B)**\nin subparagraph (K)(i)(IV), by striking 658P(6)(B) and inserting 658T(6)(B) .\n**(2) Report provisions**\nSection 658K(a)(2) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858i(a)(2) ) is amended\u2014\n**(A)**\nin subparagraph (A), by striking 658P(6) and inserting 658T(6) ; and\n**(B)**\nin subparagraph (F), by striking 658P(6)(B) and inserting 658T(6)(B) .",
      "versionDate": "2026-02-11",
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
        "actionDate": "2026-02-11",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3845",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "After Hours Child Care Act",
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
        "name": "Families",
        "updateDate": "2026-02-20T19:30:54Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7498ih.xml"
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
      "title": "After Hours Child Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T05:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "After Hours Child Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish and expand child care programs for parents who work nontraditional hours, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:40Z"
    }
  ]
}
```
