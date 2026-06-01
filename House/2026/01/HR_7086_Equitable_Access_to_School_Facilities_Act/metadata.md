# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7086?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7086
- Title: Equitable Access to School Facilities Act
- Congress: 119
- Bill type: HR
- Bill number: 7086
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-05-14T08:08:21Z
- Update date including text: 2026-05-14T08:08:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 15.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 15.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7086",
    "number": "7086",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001133",
        "district": "6",
        "firstName": "Juan",
        "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
        "lastName": "Ciscomani",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Equitable Access to School Facilities Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:21Z",
    "updateDateIncludingText": "2026-05-14T08:08:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 15.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
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
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
        "item": [
          {
            "date": "2026-01-21T19:45:12Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-15T14:01:50Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "GA"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "CA"
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
      "sponsorshipDate": "2026-01-22",
      "state": "HI"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
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
      "sponsorshipDate": "2026-03-26",
      "state": "LA"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "LA"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "AZ"
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
      "sponsorshipDate": "2026-05-13",
      "state": "AR"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7086ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7086\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Ciscomani (for himself and Mr. Bishop ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo support the creation and implementation of State policies, as well as the expansion of existing State policies, for improving the quality and affordability of charter school facilities and to authorize the provision of technical assistance to support the growth and expansion of high-quality charter schools.\n#### 1. Short title\nThis Act may be cited as the Equitable Access to School Facilities Act .\n#### 2. Amendments to State facilities aid program\n##### (a) In general\nSection 4304(k) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7221c(k) ) is amended to read as follows:\n(k) State facilities aid program (1) State entity defined In this subsection, the term State entity has the meaning given the term in section 4303(a). (2) Grants to State entities (A) Grants authorized From the amount reserved under section 4302(b)(1) and remaining after the Secretary makes grants under subsection (a), the Secretary shall award, on a competitive basis, grants to State entities that have the highest-quality applications approved under subparagraph (C), after considering the content of such applications in accordance with subparagraph (D), to pay for the Federal share of the cost of carrying out the activities described in subparagraph (E). (B) Period The Secretary shall award grants under this subsection for periods of not more than 5 years. (C) Application (i) In general A State entity desiring to receive a grant under this subsection shall submit to the Secretary an application in such form as the Secretary may reasonably require and containing the information described in clause (ii). (ii) Contents An application submitted under clause (i) shall contain\u2014 (I) a statement identifying the activities that the State entity proposes to carry out with funds received under this subsection, including a description of how the State entity will determine which charter schools will receive assistance, and how much and what types of assistance such charter schools will receive; (II) a description of the involvement of charter schools in the application\u2019s development and in the design of the proposed activities; (III) a description of whether and how the State entity will partner with an organization as described in subparagraph (G); (IV) a description of how the State entity possesses sufficient expertise to evaluate the likelihood of success of a charter school before providing assistance to such school through the proposed grant; (V) in the case of an application submitted by a State entity described in paragraphs (1), (2), or (3) of section 4303(a), a description of the actions that the entity has taken, or will take, to ensure that charter schools within the State receive the funding they need to have adequate facilities; (VI) a description of whether and how the proposed activities will\u2014 (aa) increase charter schools\u2019 access to State funds or other financing for acquiring or operating facilities (including by reducing gaps to such access between charter schools and other public schools in the same State); (bb) increase charter schools\u2019 access to public buildings; and (cc) increase the access of charter schools in low-income and rural communities to adequate facilities; and (VII) a description of whether the State in which the State entity is located is described in clauses (i), (ii), (iii), or (iv) of subparagraph (D). (iii) No additional information The Secretary may not require any additional information to be included in an application submitted under this subparagraph that is not listed in clause (ii). (D) Priority In making grants under this subsection, the Secretary shall give priority to a State entity located in a State\u2014 (i) that is described in subparagraph (A) or (C) of section 4303(g)(2); (ii) that provides charter schools with access to tax-exempt financing; (iii) with land use policies (including with respect to policies relating to permits and fees) that provide for the same or substantially similar treatment of charter schools as other public schools that are not charter schools; or (iv) that prohibits localities and other instrumentalities of the State from imposing deed restrictions on properties that limit charter school access, including prohibitions or restrictions on charter schools purchasing surplus public property. (E) Use of funds (i) In general A State entity receiving a grant under this subsection shall use such grant to carry out, in the State in which the State entity is located, 1 or more of the following activities: (I) Increasing funding for, or creating financing mechanisms to support, the acquisition, access to leasing, and renovation of facilities by charter schools, which may include partnerships with local educational agencies that provide access to public buildings. (II) Increasing funding for, or creating funding mechanisms to support, charter schools\u2019 ongoing facilities costs. (III) Supporting the creation of alternative ownership models, to plan, develop, and manage facilities for charter schools. (ii) Reserve account (I) State entity not receiving subsection (a) grant In the case of a State entity that is not receiving a grant under subsection (a), such entity may\u2014 (aa) establish and maintain a reserve account described in subsection (f); and (bb) for the purpose of carrying out 1 or more of the activities described in subclauses (I) through (III) of clause (i), deposit an amount of the grant funds received under this subsection (to be determined by the State entity) in such reserve account. (II) State entity receiving subsection (a) grant In the case of a State entity that is receiving a grant under subsection (a), for the purpose of carrying out 1 or more of the activities described in subclauses (I) through (III) of clause (i), such entity may deposit an amount of the grant funds received under this subsection (to be determined by the State entity) in the reserve account established and maintained by the State entity under subsection (f). (iii) Evaluations; technical assistance; dissemination From the amount made available to a State entity through a grant under this subsection for a fiscal year, the State entity may reserve not more than 5 percent to carry out evaluations, to provide technical assistance, and to disseminate information. (iv) Supplement, not supplant Funds made available under this subsection shall be used to supplement, and not supplant, non-Federal funds expended to carry out the activities authorized under this subsection. (F) Federal share The Federal share of the cost of carrying out the activities described in subparagraph (E) shall be not more than an amount equal to 60 percent of the total such cost for the duration of the grant period. (G) Non-Federal share A State entity receiving a grant under this subsection may partner with 1 or more organizations, and such organizations may provide any amount of the non-Federal share of the cost of carrying out the activities described in subparagraph (E). (H) Multiple grants A State may receive more than 1 grant under this subsection, so long as the amount of total funds provided to charter schools increases with each successive grant. .\n##### (b) Applicability\nThe amendment made by subsection (a) shall apply only with respect to a grant awarded under section 4304(k) of the Elementary and Secondary Education Act ( 20 U.S.C. 7221c(k) ) on or after the date of the enactment of this Act.\n#### 3. No Federal interest\nPart C of title IV of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7221 et seq. ) is amended by adding at the end the following:\n4312. No Federal interest No funds made available under this part create a Federal interest (as such term is defined in section 200.1 of title 2, Code of Federal Regulations) for purposes of\u2014 (1) the recording requirement under section 200.316 of such title; or (2) the reporting requirement under section 200.330 of such title. .\n#### 4. Credit enhancement for charter school facilities program\n##### (a) In general\nSection 4304(h)(2)(A) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7221c(h)(2) ) is amended by inserting , for each of the 10 years following the date on which such entity received such grant, after annual report .\n##### (b) Applicability\nThe amendment made by subsection (a) shall apply with respect to an eligible entity that received a grant under section 4304(a) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7221c(a) ) before, on, or after the date of the enactment of this Act.\n#### 5. Grants to support high-quality charter schools\n##### (a) In general\nSection 4303 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7221b ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)(C), by striking and ;\n**(B)**\nin paragraph (2), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby inserting after paragraph (2) the following:\n(3) provide assistance in locating and accessing a facility for purposes of opening, preparing, or expanding charter schools as described in paragraph (1); and (4) provide one-time assistance to any planned or operating charter schools in the State in ensuring that a facility used for a charter school complies with State and local building codes and regulations. ;\n**(2)**\nin subsection (c)(1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking section shall\u2014 and inserting\nsection\u2014 (A) shall\u2014 ;\n**(B)**\nby redesignating subparagraphs (A) though (C) as clauses (i) through (iii), respectively;\n**(C)**\nin clause (i), as so redesignated, by striking 90 percent and inserting 80 percent ;\n**(D)**\nin clause (iii), as so redesignated, by striking the period at the end and inserting ; and ; and\n**(E)**\nby adding at the end the following:\n(B) may reserve not more than 10 percent of such funds for the establishment of a revolving loan fund, which may be used to make loans, under such terms as may be established by the State entity, to\u2014 (i) eligible applicants that have received a subgrant under this section, for the initial operation (during the program period described in subsection (d)(1)(B)) of 1 or more of the charter schools opened or expanded pursuant to a grant under this section; and (ii) eligible applicants to assist such applicants in obtaining, renovating, or rehabilitating facilities for planned or operating charter schools in the State. ; and\n**(3)**\nin subsection (h)(3), by striking necessary renovations and all that follows through school building complies and inserting repairs, renovations, and building out of charter school facilities to ensure that such facilities comply .\n##### (b) Applicability\nThe amendments made by subsection (a) shall apply only with respect to a grant awarded under section 4303 of the Elementary and Secondary Education Act ( 20 U.S.C. 7221b ) on or after the date of the enactment of this Act.",
      "versionDate": "2026-01-15",
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
            "name": "Education programs funding",
            "updateDate": "2026-01-23T18:40:30Z"
          },
          {
            "name": "Educational facilities and institutions",
            "updateDate": "2026-01-23T18:40:38Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-01-23T18:40:20Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-01-23T18:41:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2026-01-20T14:39:59Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7086ih.xml"
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
      "title": "Equitable Access to School Facilities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Equitable Access to School Facilities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To support the creation and implementation of State policies, as well as the expansion of existing State policies, for improving the quality and affordability of charter school facilities and to authorize the provision of technical assistance to support the growth and expansion of high-quality charter schools.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T09:18:42Z"
    }
  ]
}
```
