# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2275?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2275
- Title: SCHOOL Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2275
- Origin chamber: House
- Introduced date: 2025-03-21
- Update date: 2026-04-08T15:06:37Z
- Update date including text: 2026-04-08T15:06:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-21: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-21: Introduced in House

## Actions

- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-21",
    "latestAction": {
      "actionDate": "2025-03-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2275",
    "number": "2275",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "SCHOOL Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-08T15:06:37Z",
    "updateDateIncludingText": "2026-04-08T15:06:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-21",
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
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-21",
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
          "date": "2025-03-21T20:01:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2275ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2275\nIN THE HOUSE OF REPRESENTATIVES\nMarch 21, 2025 Mr. Roy introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo allow Federal funds appropriated for kindergarten through grade 12 education to follow the student.\n#### 1. Short title\nThis Act may be cited as the Support Children Having Open Opportunities for Learning Act of 2025 or the SCHOOL Act of 2025 .\n#### 2. Federal funding under the Elementary and Secondary Education Act of 1965 to follow the student\nTitle VIII of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 et seq. ) is amended by adding at the end the following:\nH Funds to follow the student 8701. Funds to follow the student (a) In general (1) Funds to follow the student Notwithstanding any other provision of law and to the extent permitted under State law, a State educational agency shall allocate grant funds provided under titles I, III, IV, V, and VI, for the purposes of ensuring that funding under such titles follows children, whether learning in person or remotely, to the public school, private school, or home school they attend\u2014 (A) among the local educational agencies in the State based on the number of eligible children enrolled in the public schools operated by each local educational agency; and (B) directly to the eligible children, through education savings accounts, residing in the State who are enrolled in private schools or home schools. (2) Allowable uses of funds Funds allocated under paragraph (1) may be used for, but not limited to\u2014 (A) curriculum and curricular materials; (B) books or other instructional materials; (C) technological educational materials; (D) online educational materials; (E) tutoring or educational classes outside the home; (F) private school tuition; (G) extracurricular activities; (H) testing fees; (I) diagnostic tools; and (J) educational therapies for student with disabilities. (3) Plan (A) In general Each State that carries out allocations described in paragraph (1) shall establish a plan whereby the parent or guardian of each eligible child in the State will annually notify the relevant local educational agency of the public school or private school which the child will attend, or if the child will instead attend home school. (B) Data collection Information collected under this section by the State shall be used for the sole purposes of calculating the allocation of funds and distribution of funds under this section. (b) Definitions In this section: (1) Eligible child The term eligible child means a child aged 5 to 17. (2) Home school The term home school means a home school as defined by the laws of the State in which the eligible child resides. (c) Student enrollment in public schools, private schools, and home schools (1) Identification of eligible children On an annual basis, on a date to be determined by the State educational agency, each local educational agency that receives grant funding in accordance with subsection (a) shall inform the State educational agency of the number of eligible children enrolled in public schools served by the local educational agency and private schools and home schools located in the school district served by the local educational agency in order to provide allocations for each eligible child in equal amounts regardless of where the child attends school in the State. (2) Allocation to local educational agencies and eligible children Based on the identification of eligible children in paragraph (1), the State educational agency shall provide\u2014 (A) to a local educational agency an amount equal to the sum of the amount available for each eligible child in the State multiplied by the number of eligible children identified by the local educational agency under paragraph (1) enrolled in public schools served by the local educational agency; and (B) to an eligible child residing in the State who is enrolled in a private school or home school, through an education savings account, an amount equal to the sum of the amount available for an eligible child in the State. (3) Distribution to public schools Each local educational agency that receives funds under paragraph (2)(A) shall distribute such funds to the public schools served by the local educational agency\u2014 (A) based on the number of eligible children enrolled in such schools; and (B) in a manner that would, in the absence of such Federal funds, supplement the funds made available from non-Federal resources for the education of pupils participating in programs under this Act, and not to supplant such funds (in accordance with the method of determination described in section 1117). (4) Distribution to eligible children Each State that carries out allocations described in paragraph (1) shall distribute amounts to the eligible children residing in that State who enroll in a private school or home school\u2014 (A) through an education savings account, as described in paragraph (2)(B); and (B) in a manner that would, in the absence of such Federal funds, supplement the funds made available from non-Federal resources for the education of pupils participating in programs under this Act, and not to supplant such funds (in accordance with the method of determination described in section 1117). (d) Application of participation of children enrolled in private schools The provisions of section 1116 shall apply to this section. (e) Rule of construction (1) Federally funded school food programs Nothing in this section shall be construed to preclude a child eligible for assistance under the free and reduced price school lunch program established under the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ) from receiving assistance under such program. (2) Prohibition of control over non-public education providers Nothing in this section shall permit, allow, encourage, or authorize Federal or State control over non-public education providers. .\n#### 3. Federal funding under the Individuals with Disabilities Education Act to follow the student\nPart A of the Individuals with Disabilities Education Act ( 20 U.S.C. 1401 et seq. ) is amended by adding at the end the following:\n611. Funds to follow the student (a) In general (1) Funds to follow the student Notwithstanding any other provision of law and to the extent permitted under State law, a State educational agency shall allocate grant funds provided under this Act, for the purposes of ensuring that funding under this Act follows children, whether learning in person or remotely, to the public school, private school, or home school they attend\u2014 (A) among the local educational agencies in the State based on the number of eligible children enrolled in the public schools operated by each local educational agency; and (B) directly to the eligible children, through education savings accounts, residing in that State who are enrolled in private schools or home schools. (2) Allowable uses of funds Funds allocated under paragraph (1) may be used for, but not limited to\u2014 (A) curriculum and curricular materials; (B) books or other instructional materials; (C) technological educational materials; (D) online educational materials; (E) tutoring or educational classes outside the home; (F) private school tuition; (G) extracurricular activities; (H) testing fees; (I) diagnostic tools; and (J) educational therapies for student with disabilities. (3) Plan (A) In general Each State that carries out allocations described in paragraph (1) shall establish a plan whereby the parent or guardian of each eligible child in the State will annually notify the relevant local educational agency of the public school or private school which the child will attend, or if the child will instead attend home school. (B) Data collection Information collected under this section by the State shall be used for the sole purposes of calculating the allocation of funds and distribution of funds under this section. (b) Definitions In this section: (1) Eligible child The term eligible child means a child with a disability who is eligible to receive special education and related services under this Act. (2) Home school The term home school means a home school as defined by the laws of the State in which the eligible child resides. (c) Student enrollment in public schools, private schools, and home schools (1) Identification of eligible children On an annual basis, on a date to be determined by the State educational agency, each local educational agency that receives grant funding in accordance with subsection (a) shall inform the State educational agency of the number of eligible children enrolled in public schools served by the local educational agency and private schools and home schools located in the school district served by the local educational agency in order to provide allocations for each eligible child in equal amounts regardless of where the child attends school in the State. (2) Allocation to local educational agencies and eligible children Based on the identification of eligible children in paragraph (1), the State educational agency shall provide\u2014 (A) to a local educational agency an amount equal to the sum of the amount available for each eligible child in the State multiplied by the number of eligible children identified by the local educational agency under paragraph (1) enrolled in public schools served by the local educational agency; and (B) to an eligible child residing in the State who is enrolled in a private school or home school, through an education savings account, an amount equal to the sum of the amount available for an eligible child in the State. (3) Distribution to public schools Each local educational agency that receives funds under paragraph (2)(A) shall distribute such funds to the public schools served by the local educational agency\u2014 (A) based on the number of eligible children enrolled in such schools; and (B) in a manner that would, in the absence of such Federal funds, supplement the funds made available from non-Federal resources for the education of pupils participating in programs under this Act, and not to supplant such funds. (4) Distribution to eligible children Each State that carries out allocations described in paragraph (1) shall distribute amounts to the eligible children residing in that State who enroll in a private school or home school\u2014 (A) through an education savings account, as described in paragraph (2)(B); and (B) in a manner that would, in the absence of such Federal funds, supplement the funds made available from non-Federal resources for the education of pupils participating in programs under this Act, and not to supplant such funds. (d) Rule of construction (1) Federally funded school lunch programs Nothing in this section shall be construed to preclude a child eligible for assistance under the free and reduced price school lunch program established under the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ) from receiving assistance under such program. (2) Prohibition of control over non-public education providers Nothing in this section shall permit, allow, encourage, or authorize Federal or State control over non-public education providers. .",
      "versionDate": "2025-03-21",
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
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2026-03-05T15:56:09Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-08T15:06:37Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2026-03-05T15:56:09Z"
          },
          {
            "name": "Educational technology and distance education",
            "updateDate": "2026-03-05T15:56:09Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-03-05T15:56:09Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-03-05T15:56:09Z"
          },
          {
            "name": "Special education",
            "updateDate": "2026-03-05T15:56:09Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2026-03-05T15:56:09Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-03-05T15:56:09Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2026-03-05T15:56:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-04-04T12:46:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-21",
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
          "measure-id": "id119hr2275",
          "measure-number": "2275",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-21",
          "originChamber": "HOUSE",
          "update-date": "2025-09-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2275v00",
            "update-date": "2025-09-03"
          },
          "action-date": "2025-03-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Support Children Having Open Opportunities for Learning Act of 2025\u00a0or the SCHOOL Act of </strong><strong>2025</strong></p><p>This bill allows certain federal funds for elementary and secondary education to follow the student to the school that they attend (i.e., public, private, or home school), regardless of whether the student is learning in person or remotely. These funds may be used for educational and instructional materials, tutoring, tuition for private school, and extracurricular activities.</p>"
        },
        "title": "SCHOOL Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2275.xml",
    "summary": {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Support Children Having Open Opportunities for Learning Act of 2025\u00a0or the SCHOOL Act of </strong><strong>2025</strong></p><p>This bill allows certain federal funds for elementary and secondary education to follow the student to the school that they attend (i.e., public, private, or home school), regardless of whether the student is learning in person or remotely. These funds may be used for educational and instructional materials, tutoring, tuition for private school, and extracurricular activities.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hr2275"
    },
    "title": "SCHOOL Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Support Children Having Open Opportunities for Learning Act of 2025\u00a0or the SCHOOL Act of </strong><strong>2025</strong></p><p>This bill allows certain federal funds for elementary and secondary education to follow the student to the school that they attend (i.e., public, private, or home school), regardless of whether the student is learning in person or remotely. These funds may be used for educational and instructional materials, tutoring, tuition for private school, and extracurricular activities.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hr2275"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2275ih.xml"
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
      "title": "SCHOOL Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SCHOOL Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Support Children Having Open Opportunities for Learning Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow Federal funds appropriated for kindergarten through grade 12 education to follow the student.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:42Z"
    }
  ]
}
```
