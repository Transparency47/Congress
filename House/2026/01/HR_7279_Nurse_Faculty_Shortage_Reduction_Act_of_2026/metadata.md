# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7279?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7279
- Title: Nurse Faculty Shortage Reduction Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7279
- Origin chamber: House
- Introduced date: 2026-01-30
- Update date: 2026-05-13T08:06:44Z
- Update date including text: 2026-05-13T08:06:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-30: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-30: Introduced in House

## Actions

- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-30",
    "latestAction": {
      "actionDate": "2026-01-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7279",
    "number": "7279",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
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
    "title": "Nurse Faculty Shortage Reduction Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:44Z",
    "updateDateIncludingText": "2026-05-13T08:06:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-30",
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
          "date": "2026-01-30T15:32:05Z",
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
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "OH"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "IL"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "VA"
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
      "sponsorshipDate": "2026-04-02",
      "state": "PA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "PA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7279ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7279\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 30, 2026 Ms. Bonamici (for herself, Mr. Joyce of Ohio , Ms. Underwood , and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo provide for a wage differential program to support new nursing school faculty members.\n#### 1. Short title\nThis Act may be cited as the Nurse Faculty Shortage Reduction Act of 2026 .\n#### 2. Nurse faculty demonstration program\nSection 846A of the Public Health Service Act ( 42 U.S.C. 297n\u20131 ) is amended\u2014\n**(1)**\nby amending subsection (a) to read as follows:\n(a) In general To increase the number of qualified nursing faculty, the Secretary may\u2014 (1) enter into an agreement with any accredited school of nursing for the establishment and operation of a student loan fund in accordance with subsection (b); and (2) award nurse faculty grants in accordance with subsection (c). ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby redesignating subparagraphs (A) through (D) of paragraph (2) as clauses (i) through (iv), respectively, and adjusting the margins accordingly;\n**(B)**\nby redesignating paragraphs (1) through (5) as subparagraphs (A) through (E), respectively, and adjusting the margins accordingly;\n**(C)**\nin subparagraph (C), as so redesignated, by striking subsection (c) and inserting paragraph (2) ; and\n**(D)**\nby striking (b) Agreements .\u2014Each agreement entered into under subsection (a) shall\u2014 and inserting the following:\n(b) School of nursing student loan fund (1) In general Each agreement entered into under subsection (a)(1) shall\u2014 ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby striking subsection (a) each place it appears and inserting subsection (a)(1) ;\n**(B)**\nin paragraph (3), by redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and adjusting the margins accordingly;\n**(C)**\nin paragraph (6), by redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and adjusting the margins accordingly;\n**(D)**\nby redesignating paragraphs (1) through (6) as subparagraphs (A) through (F), respectively, and adjusting the margins accordingly; and\n**(E)**\nin subparagraph (F)(ii), as so redesignated, by striking subsection (e) and inserting paragraph (4) ;\n**(4)**\nin subsection (e), by striking subsection (c)(6)(B) and inserting paragraph (2)(F)(ii) ;\n**(5)**\nby redesignating subsections (c) through (e) as paragraphs (2) through (4), respectively, and adjusting the margins accordingly; and\n**(6)**\nby adding at the end the following:\n(c) Nurse faculty demonstration program (1) In general The Secretary shall establish and carry out a demonstration program described in subsection (a)(2) under which eligible schools of nursing receive a grant for purposes of supplementing the salaries of eligible nursing faculty members to enhance recruitment and retention of nursing faculty members. (2) Eligible entities To be eligible to receive a grant under this subsection, an entity shall\u2014 (A) be a school of nursing; and (B) submit an application to the Secretary, at such time, in such manner, and containing such information as the Secretary may require, including\u2014 (i) (I) to the extent such information is available to the school of nursing, the salary history of nursing faculty at such school who previously were nurses in clinical practice, for the most recent 3-year period ending on the date of application, adjusted for inflation as appropriate and broken down by credentials, experience, and levels of education of such nurses; or (II) if the information described in subclause (I) is not available, information on the average local salary of nurses in clinical practice, adjusted for inflation as appropriate and broken down by credentials, experience, and levels of education of the individual nurses, in accordance with such requirements as the Secretary may specify; (ii) an attestation of the average nursing faculty salary at the school of nursing during the most recent 3-year period prior to the date of application, adjusted for inflation, as appropriate, broken down by credentials, experience, and levels of education of such faculty members; (iii) the number of nursing faculty member vacancies at the entity at the time of application, and the entity\u2019s projection of such vacancies over the ensuing 5-year period; and (iv) a description of the entity\u2019s plans to identify funding sources to sustainably continue, after the 3-year grant period, the salary available to the eligible nursing faculty member pursuant to the program under this subsection during such grant program and to retain eligible nursing faculty members after the end of the grant period. (3) Awards A grant awarded under this subsection, with respect to supporting eligible nursing faculty members, shall\u2014 (A) be awarded to the school of nursing to supplement the salaries of eligible faculty members at the school of nursing, annually, for up to a 3-year period, in an amount equal to, for each eligible nursing faculty member at the eligible entity during the grant period, the difference between\u2014 (i) the average salary of nurses in clinical practice, as submitted under subclause (I) or (II) of paragraph (2)(B)(i); and (ii) the greater of\u2014 (I) the salary for the eligible nursing faculty member at the school of nursing; or (II) the average nursing faculty salary, as submitted under paragraph (2)(B)(ii) for faculty members with the same or similar credentials and level of education; (B) notwithstanding section 803(a), be used in its entirety to supplement the eligible faculty member\u2019s salary; and (C) be conditioned upon the school of nursing maintaining, for each year in which the award is made as described in subparagraph (A), a salary for such faculty member at a level that is not less than the greater of the amount under subclause (I) or (II) of subparagraph (A)(ii). (4) Priority In awarding grants under this subsection, the Secretary shall ensure the equitable geographic distribution of awards, and shall give priority to applications from schools of nursing that demonstrate\u2014 (A) the greatest need for such grant, which may be based upon the financial circumstances of the school of nursing, the number of eligible nurse faculty members, the planned number of students to be trained or admitted off a wait list; (B) training or partnerships to serve vulnerable patient populations, such as through the location or activity of a school in a health professional shortage area (as defined in section 332); or (C) recruitment and retention of faculty from underrepresented populations. (5) Rule of construction Nothing in this subsection precludes a school of nursing or an eligible nursing faculty member receiving an award under this section from obtaining or receiving any other form of Federal support or funding. (6) Report Not later than 3 years after the date of enactment of the Nurse Faculty Shortage Reduction Act of 2026, the Secretary shall submit to the Committee on Finance and the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Ways and Means and the Committee on Energy and Commerce of the House of Representatives, a report that evaluates the program established under this subsection, including\u2014 (A) the impact of such program on recruitment and retention rates of nursing faculty, as available, and specifically for each faculty member participating in the program; and (B) recommendations and considerations for Congress on continuing the program under this subsection. (7) Definitions In this subsection: (A) Eligible nursing faculty member The term eligible nursing faculty member means a nursing faculty member who\u2014 (i) was hired by a school of nursing within the 2-year period preceding the submission of an application under paragraph (2), or a prospective nursing faculty member; (ii) is currently employed at the school of nursing and who demonstrates the need for such support; (iii) previously worked as a nurse in clinical practice or as a nurse faculty member at another school of nursing; or (iv) may work on a part-time basis as a nursing faculty member, for whom such award amounts described in paragraph (3) shall be prorated relative to the amount of time participating in part-time teaching. (B) Inflation The term inflation means the Consumer Price Index for all urban consumers (all items; U.S. city average). (8) Authorization of appropriations To carry out this subsection, there is authorized to be appropriated $15,000,000 for each of fiscal years 2027 through 2031. .",
      "versionDate": "2026-01-30",
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
        "actionDate": "2026-01-27",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S292-293)"
      },
      "number": "3707",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Nurse Faculty Shortage Reduction Act of 2026",
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
        "name": "Health",
        "updateDate": "2026-02-20T13:42:40Z"
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
      "date": "2026-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7279ih.xml"
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
      "title": "Nurse Faculty Shortage Reduction Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Nurse Faculty Shortage Reduction Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for a wage differential program to support new nursing school faculty members.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:32Z"
    }
  ]
}
```
