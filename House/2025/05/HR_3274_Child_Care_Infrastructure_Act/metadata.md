# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3274?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3274
- Title: Child Care Infrastructure Act
- Congress: 119
- Bill type: HR
- Bill number: 3274
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2026-05-20T08:07:02Z
- Update date including text: 2026-05-20T08:07:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3274",
    "number": "3274",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "C001101",
        "district": "5",
        "firstName": "Katherine",
        "fullName": "Rep. Clark, Katherine M. [D-MA-5]",
        "lastName": "Clark",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Child Care Infrastructure Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:07:02Z",
    "updateDateIncludingText": "2026-05-20T08:07:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:06:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sponsorshipDate": "2025-05-08",
      "state": "OR"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "VA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CO"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "HI"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "DE"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NH"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3274ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3274\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Ms. Clark of Massachusetts (for herself, Ms. Bonamici , Mr. Gomez , Ms. McClellan , Ms. Pettersen , and Ms. Tokuda ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide assistance with respect to child care infrastructure.\n#### 1. Short title\nThis Act may be cited as the Child Care Infrastructure Act .\n#### 2. Infrastructure grants to improve child care safety\n##### (a) In general\nPart A of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ) is amended by inserting after section 418 the following:\n418A. Infrastructure grants to improve child care safety (a) Short title This section may be cited as the Infrastructure Grants To Improve Child Care Safety Act . (b) Needs Assessments (1) Immediate needs assessment (A) In general The Secretary shall conduct an immediate needs assessment of the condition of child care facilities throughout the United States (with priority given to child care programs that receive Federal funds), that\u2014 (i) considers the infrastructure needs, as of the date of the enactment of this section, of a variety of child care centers, including home-based centers; and (ii) considers how the COVID\u201319 pandemic has impacted specific metrics, such as\u2014 (I) capacity; (II) investments in infrastructure changes; (III) the types of infrastructure changes centers need to implement and their associated costs; (IV) the price of tuition; and (V) any changes or anticipated changes in the number and demographic of children attending. (B) Timing The immediate needs assessment should occur simultaneously with the first grant-making cycle under subsection (c). (C) Report Not later than 1 year after the date of the enactment of this section, the Secretary shall submit to the Congress a report containing the result of the needs assessment conducted under subparagraph (A), and make the assessment publicly available. (2) Long-term needs assessment (A) In general The Secretary shall conduct a long-term assessment of the condition of child care facilities throughout the United States (with priority given to child care programs that receive Federal funds). The assessment may be conducted through representative random sampling. (B) Report Not later than 4 years after the date of the enactment of this section, the Secretary shall submit to the Congress a report containing the results of the needs assessment conducted under subparagraph (A), and make the assessment publicly available. (c) Child care facilities grants (1) Grants to States (A) In general The Secretary may award grants to States for the purpose of helping child care providers acquire, construct, renovate, or improve child care facilities, including adapting, reconfiguring, or expanding the facilities. (B) Prioritized facilities The Secretary may not award a grant to a State under subparagraph (A) unless the State involved agrees, with respect to the use of grant funds, to prioritize\u2014 (i) child care facilities primarily serving low-income populations; (ii) child care facilities primarily serving children who have not attained the age of 5 years with a significant percentage of infants and toddlers enrolled; (iii) child care facilities that\u2014 (I) are currently unable to serve young children, had to significantly reduce capacity, or are unable to serve more children, due to factors such as the inadequate condition, quality, or availability of facilities; or (II) are seeking to build capacity and expand the number of children served; (iv) child care facilities that operate under nontraditional hours; and (v) child care facilities located in rural or underserved communities. (C) Duration of grants A grant under this subsection shall be awarded for a period of not more than 5 years. (D) Application To seek a grant under this subsection, a State shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, which information shall\u2014 (i) be disaggregated as the Secretary may require; and (ii) include a plan to use a portion of the grant funds to report back to the Secretary on the impact of using the grant funds to improve child care facilities. (E) Priority In selecting States for grants under this subsection, the Secretary shall prioritize States that\u2014 (i) plan to improve center-based and home-based child care programs, which may include a combination of child care and early Head Start or Head Start programs; (ii) aim to meet specific needs across urban, suburban, or rural areas as determined by the State, such as prioritizing improvements to programs that serve children from families with low incomes or children with disabilities; and (iii) show evidence of collaboration with\u2014 (I) local government officials; (II) other State agencies; (III) nongovernmental organizations, such as\u2014 (aa) organizations within the philanthropic community; (bb) certified community development financial institutions as defined in section 103 of the Community Development Banking and Financial Institutions Act of 1994 ( 12 U.S.C. 4702 ) that have been certified by the Community Development Financial Institutions Fund ( 12 U.S.C. 4703 ); and (cc) organizations that have demonstrated experience in\u2014 (AA) providing technical or financial assistance for the acquisition, construction, renovation, or improvement of child care facilities; (BB) providing technical, financial, or managerial assistance to child care providers; and (CC) securing private sources of capital financing for child care facilities or other low-income community development projects; and (IV) local community organizations, such as\u2014 (aa) child care providers; (bb) community care agencies; (cc) resource and referral agencies; and (dd) unions. (F) Consideration In selecting States for grants under this subsection, the Secretary shall consider\u2014 (i) whether the applicant\u2014 (I) has or is developing a plan to address child care facility needs; and (II) demonstrates the capacity to execute such a plan; and (ii) after the date the report required by subsection (b)(1)(C) is submitted to the Congress, the needs of the applicants based on the results of the assessment. (G) Diversity of awards In awarding grants under this section, the Secretary shall give equal consideration to States with varying capacities under subparagraph (F). (H) Matching requirement (i) In general As a condition for the receipt of a grant under subparagraph (A), a State that is not an Indian tribe shall agree to make available (directly or through donations from public or private entities) contributions with respect to the cost of the activities to be carried out pursuant to subparagraph (A), which may be provided in cash or in kind, in an amount equal to 10 percent of the funds provided through the grant. (ii) Determination of amount contributed Contributions required by clause (i) may include\u2014 (I) amounts provided by the Federal Government, or services assisted or subsidized to any significant extent by the Federal Government; or (II) philanthropic or private-sector funds. (I) Report Not later than 1 year after the last day of the grant period, a State receiving a grant under this paragraph shall submit a report to the Secretary as described in subparagraph (D)\u2014 (i) to determine the effects of the grant in constructing, renovating, or improving child care facilities, including any changes in response to the COVID\u201319 pandemic and any effects on access to and quality of child care; and (ii) to provide such other information as the Secretary may require. (J) Amount limit The annual amount of a grant under this paragraph may not exceed $250,000,000. (2) Grants to intermediary organizations (A) In general The Secretary may award grants to intermediary organizations, such as certified community development financial institutions, tribal organizations, or other organizations with demonstrated experience in child care facilities financing, for the purpose of providing technical assistance, capacity-building, and financial products to develop or finance child care facilities. (B) Application A grant under this paragraph may be made only to intermediary organizations that submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (C) Priority In selecting intermediary organizations for grants under this subsection, the Secretary shall prioritize intermediary organizations that\u2014 (i) demonstrate experience in child care facility financing or related community facility financing; (ii) demonstrate the capacity to assist States and local governments in developing child care facilities and programs; (iii) demonstrate the ability to leverage grant funding to support financing tools to build the capacity of child care providers, such as through credit enhancements; (iv) propose to focus on child care facilities that operate under nontraditional hours; (v) propose to meet a diversity of needs across States and across urban, suburban, and rural areas at varying types of center-based, home-based, and other child care settings, including early care programs located in freestanding buildings or in mixed-use properties; and (vi) propose to focus on child care facilities primarily serving low-income populations and children who have not attained the age of 5 years. (D) Amount limit The amount of a grant under this paragraph may not exceed $15,000,000. (3) Report Not later than the end of fiscal year 2030, the Secretary shall submit to the Congress a report on the effects of the grants provided under this subsection, and make the report publicly accessible. (d) Labor standards for all grants (1) All laborers and mechanics employed by contractors or subcontractors in the performance of construction, renovation, improvement, repair, alteration, adaptation, reconfiguration, or expansion of child care facilities funded in whole or in part under this section shall be paid wages at rates not less than those prevailing on projects of a character similar in the locality as determined by the Secretary of Labor in accordance with subchapter IV of chapter 31 of part A of subtitle II of title 40, United States Code (commonly referred to as the Davis-Bacon Act ). (2) The Secretary shall require that each entity, including grantees and subgrantees, that applies for an infrastructure grant for constructing, renovating, or improving child care facilities, including adapting, reconfiguring, or expanding such facilities, which is funded in whole or in part under this section, shall include in its application written assurance that all laborers and mechanics employed by contractors or subcontractors in the performance of construction, alternation or repair, as part of such project, shall be paid wages in accordance with paragraph (1). The Secretary shall not approve any such funding without first obtaining adequate assurance that required labor standards will be maintained with respect to any such construction work. (3) The Secretary of Labor shall have, with respect to the labor standards specified in paragraph (1), the authority and functions set forth in Reorganization Plan Numbered 14 of 1950 (15 Fed. Reg. 3176; 5 U.S.C. App.) and section 276c of title 40, United States Code. (e) Limitations on authorization of appropriations (1) In general To carry out this section, there is authorized to be appropriated $10,000,000,000 for fiscal year 2026, which shall remain available through fiscal year 2030. (2) Reservations of funds (A) Indian tribes The Secretary shall reserve 3 percent of the total amount made available to carry out this section, for payments to Indian tribes. (B) Territories The Secretary shall reserve 3 percent of the total amount made available to carry out this section, for payments to territories. (3) Grants for intermediary organizations Not less than 10 percent and not more than 15 percent of the total amount made available to carry out this section may be used to carry out subsection (c)(2). (4) Limitation on use of funds for needs assessments Not more than $5,000,000 of the amounts made available to carry out this section may be used to carry out subsection (b). (f) Definition of State In this section, the term State has the meaning provided in section 419, except that it includes the Commonwealth of the Northern Mariana Islands and any Indian tribe. .\n##### (b) Exemption of territory grants from limitation on total payments to the territories\nSection 1108(a)(2) of such Act ( 42 U.S.C. 1308(a)(2) ) is amended by inserting 418A(c), after 413(f), .",
      "versionDate": "2025-05-08",
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
        "name": "Families",
        "updateDate": "2025-05-22T17:47:57Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3274ih.xml"
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
      "title": "Child Care Infrastructure Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-18T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Child Care Infrastructure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Infrastructure Grants To Improve Child Care Safety Act",
      "titleType": "Short Title(s) as Introduced for portions of this bill",
      "titleTypeCode": "106",
      "updateDate": "2025-05-18T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide assistance with respect to child care infrastructure.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-18T04:18:23Z"
    }
  ]
}
```
